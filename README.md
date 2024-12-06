# Gitbook Documentation Downloader

A web application that allows you to download and convert Gitbook documentation into markdown format.

## Features

- Scrape Gitbook documentation sites
- Convert HTML content to markdown format
- View converted content in browser
- Download documentation as a single markdown file
- Handles internal links and navigation
- Preserves document structure

## Installation

1. Clone this repository
2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Start the web server:
```bash
python app.py
```

2. Open your browser and navigate to `http://localhost:5000`

3. Enter the URL of a Gitbook documentation site

4. Choose to either:
   - View the converted content in your browser
   - Download the content as a markdown file

## Technical Details

The application uses:
- Flask for the web interface
- BeautifulSoup4 for HTML parsing
- Requests for fetching web content
- Python-slugify for URL/filename handling

## Note

This tool is designed for Gitbook-based documentation sites. It may not work correctly with other documentation platforms.
