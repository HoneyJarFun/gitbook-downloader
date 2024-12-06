import requests
from bs4 import BeautifulSoup, Comment
import json
from urllib.parse import urljoin, urlparse
import re
from slugify import slugify
import os
import logging
from typing import Dict, Optional, List, Set
from dataclasses import dataclass
from datetime import datetime
from markdownify import markdownify as md
import asyncio
import aiohttp
from concurrent.futures import ThreadPoolExecutor
from functools import partial
import time
from contextlib import contextmanager

@contextmanager
def timeout(seconds=0, minutes=0, hours=0):
    """
    Add a signal-based timeout to any function.
    Usage:
    with timeout(seconds=5):
        my_slow_function(...)
    Args:
    - seconds: The time limit, in seconds.
    - minutes: The time limit, in minutes.
    - hours: The time limit, in hours.
    """
    limit = seconds + 60 * minutes + 3600 * hours
    try:
        async def check_timeout():
            await asyncio.sleep(limit)
            raise TimeoutError("timed out after {} seconds".format(limit))
        asyncio.create_task(check_timeout())
        yield
    except TimeoutError as e:
        raise e
    finally:
        asyncio.create_task(check_timeout()).cancel()

@dataclass
class DownloadStatus:
    total_pages: int = 0
    current_page: int = 0
    current_url: str = ""
    status: str = "idle"
    error: Optional[str] = None
    start_time: Optional[float] = None
    pages_scraped: List[str] = None
    output_file: Optional[str] = None
    rate_limit_reset: Optional[int] = None

    def __post_init__(self):
        if self.pages_scraped is None:
            self.pages_scraped = []

    def to_dict(self) -> Dict:
        return {
            "total_pages": self.total_pages,
            "current_page": self.current_page,
            "current_url": self.current_url,
            "status": self.status,
            "error": self.error,
            "elapsed_time": round(datetime.now().timestamp() - self.start_time, 2) if self.start_time else 0,
            "pages_scraped": self.pages_scraped,
            "output_file": self.output_file,
            "rate_limit_reset": self.rate_limit_reset
        }

class GitbookDownloader:
    def __init__(self, url):
        self.base_url = url.rstrip('/')
        self.status = DownloadStatus()
        self.session = None
        self.output_file = None
        self.visited_urls = set()
        self.delay = 1  # Delay between requests in seconds
        self.max_retries = 3
        self.retry_delay = 2  # Initial retry delay in seconds
        self.pages = []  # Store page titles and content
        self.current_index = 0  # Track page order

    async def download(self):
        """Main download method"""
        try:
            async with aiohttp.ClientSession() as session:
                self.session = session
                self.status.status = 'running'
                
                # Get initial page and parse navigation
                initial_content = await self._fetch_page(self.base_url)
                if not initial_content:
                    raise Exception("Failed to fetch initial page")
                
                nav_links = self._extract_nav_links(initial_content)
                self.status.total_pages = len(nav_links) if nav_links else 1
                
                # Create output file
                timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
                domain = urlparse(self.base_url).netloc
                self.output_file = f'output_{domain}_{timestamp}.md'
                
                # Process each page
                if not nav_links:  # Single page
                    title, content, index = await self._process_page_content(initial_content, self.base_url)
                    if content:
                        self.pages.append({
                            'index': index,
                            'title': title,
                            'content': content,
                            'url': self.base_url
                        })
                        self.status.pages_scraped.append(title)
                else:
                    for i, link in enumerate(nav_links, 1):
                        if link in self.visited_urls:
                            continue
                            
                        self.status.current_page = i
                        self.status.current_url = link
                        
                        try:
                            page_content = await self._fetch_page(link)
                            if page_content:
                                title, content, index = await self._process_page_content(page_content, link)
                                if content:
                                    self.pages.append({
                                        'index': index,
                                        'title': title,
                                        'content': content,
                                        'url': link
                                    })
                                    self.status.pages_scraped.append(title)
                            else:
                                logging.warning(f"Failed to fetch page: {link}")
                        except Exception as e:
                            logging.error(f"Error processing page {link}: {str(e)}")
                            continue  # Skip to next page on error
                            
                        await asyncio.sleep(self.delay)  # Rate limiting delay
                
                # Generate final markdown
                if self.pages:
                    self.status.status = 'generating_markdown'
                    markdown_content = self._generate_markdown()
                    with open(self.output_file, 'w', encoding='utf-8') as f:
                        f.write(markdown_content)
                    self.status.status = 'completed'
                    self.status.output_file = self.output_file
                else:
                    raise Exception("No content was successfully downloaded")
                
                return self.output_file
                
        except Exception as e:
            self.status.status = 'error'
            self.status.error = str(e)
            logging.error(f"Download failed: {str(e)}")
            raise

    async def _fetch_page(self, url):
        """Fetch a page with retry logic"""
        retry_count = 0
        current_delay = self.retry_delay
        
        while retry_count < self.max_retries:
            try:
                async with self.session.get(url) as response:
                    if response.status == 429:  # Rate limit
                        retry_after = response.headers.get('Retry-After', '60')
                        wait_time = int(retry_after)
                        self.status.rate_limit_reset = wait_time
                        logging.warning(f"Rate limited. Waiting {wait_time} seconds")
                        await asyncio.sleep(wait_time)
                        retry_count += 1
                        continue
                        
                    if response.status == 200:
                        return await response.text()
                    else:
                        logging.warning(f"HTTP {response.status} for {url}")
                        return None
                        
            except Exception as e:
                logging.error(f"Error fetching {url}: {str(e)}")
                if retry_count < self.max_retries - 1:
                    await asyncio.sleep(current_delay)
                    current_delay *= 2  # Exponential backoff
                    retry_count += 1
                else:
                    return None
        
        return None

    def _extract_nav_links(self, content):
        """Extract navigation links from page content"""
        try:
            soup = BeautifulSoup(content, 'html.parser')
            nav_links = set()
            
            # Find navigation elements
            nav_elements = soup.find_all(['nav', 'aside'])
            for nav in nav_elements:
                for a in nav.find_all('a', href=True):
                    href = a['href']
                    if href.startswith('/'):
                        full_url = f"{self.base_url}{href}"
                        nav_links.add(full_url)
                    elif href.startswith(self.base_url):
                        nav_links.add(href)
            
            return list(nav_links)
        except Exception as e:
            logging.error(f"Error extracting nav links: {str(e)}")
            return []

    async def _process_page_content(self, content, url):
        """Process page content and convert to markdown"""
        try:
            soup = BeautifulSoup(content, 'html.parser')
            
            # Remove unnecessary elements
            for element in soup.find_all(['script', 'style', 'nav', 'footer', 'header']):
                element.decompose()
            
            # Extract title
            title = soup.find('h1')
            if not title:
                title = soup.find('title')
            if title:
                title = title.get_text().strip()
            else:
                title = urlparse(url).path.split('/')[-1] or "Home"
            
            # Find main content
            main_content = soup.find('main') or soup.find('article') or soup.find('div', class_=['content', 'markdown-body', 'documentation'])
            if not main_content:
                main_content = soup.find('div', {'role': 'main'})
            if not main_content:
                main_content = soup
            
            # Convert to markdown
            markdown = md(str(main_content))
            clean_markdown = self._clean_markdown(markdown)
            
            # Store with index
            index = self.current_index
            self.current_index += 1
            
            return title, clean_markdown, index
            
        except Exception as e:
            logging.error(f"Error processing page content: {str(e)}")
            return None, None, None

    def _clean_markdown(self, markdown_text):
        """Clean up markdown content"""
        try:
            # Remove multiple blank lines
            markdown_text = re.sub(r'\n\s*\n\s*\n', '\n\n', markdown_text)
            
            # Remove HTML comments
            markdown_text = re.sub(r'<!--.*?-->', '', markdown_text, flags=re.DOTALL)
            
            # Fix heading levels (ensure proper hierarchy)
            lines = markdown_text.split('\n')
            cleaned_lines = []
            for line in lines:
                if line.strip().startswith('#'):
                    # Ensure at least one space after #
                    line = re.sub(r'^(#+)(\S)', r'\1 \2', line)
                cleaned_lines.append(line)
            
            markdown_text = '\n'.join(cleaned_lines)
            
            # Fix list formatting
            markdown_text = re.sub(r'^\s*[-*+]\s*', '- ', markdown_text, flags=re.MULTILINE)
            
            return markdown_text.strip()
            
        except Exception as e:
            logging.error(f"Error cleaning markdown: {str(e)}")
            return markdown_text

    def _generate_markdown(self):
        """Generate final markdown document"""
        try:
            parts = []
            
            # Add title and metadata
            parts.append(f"# {urlparse(self.base_url).netloc} Documentation")
            parts.append(f"Downloaded from: {self.base_url}")
            parts.append(f"Downloaded at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            parts.append(f"Total pages: {len(self.pages)}\n")
            
            # Sort pages by index
            sorted_pages = sorted(self.pages, key=lambda x: x.get('index', 0))
            
            # Add table of contents
            parts.append("## Table of Contents")
            for page in sorted_pages:
                parts.append(f"- [{page['title']}](#{slugify(page['title'])})")
            parts.append("")
            
            # Add content sections
            for page in sorted_pages:
                parts.append(f"## {page['title']}")
                parts.append(f"Source: {page['url']}\n")
                parts.append(page['content'])
                parts.append("\n---\n")
            
            return '\n'.join(parts)
            
        except Exception as e:
            logging.error(f"Error generating markdown: {str(e)}")
            return "Error generating markdown document"
