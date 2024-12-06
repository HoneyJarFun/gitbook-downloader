# docs.substreams.dev Documentation
Downloaded from: https://docs.substreams.dev
Downloaded at: 2024-12-07 00:43:26
Total pages: 81

## Table of Contents
- [Filter Instructions | Substreams](#filter-instructions-substreams)
- [Dynamic data sources | Substreams](#dynamic-data-sources-substreams)
- [Development Container Reference | Substreams](#development-container-reference-substreams)
- [Module handler creation | Substreams](#module-handler-creation-substreams)
- [Go | Substreams](#go-substreams)
- [Files | Substreams](#files-substreams)
- [Cosmos | Substreams](#cosmos-substreams)
- [Initialize an Injective Substreams Project | Substreams](#initialize-an-injective-substreams-project-substreams)
- [Substreams:Subgraph | Substreams](#substreams-subgraph-substreams)
- [NFT Trades | Substreams](#nft-trades-substreams)
- [Protobuf Schemas | Substreams](#protobuf-schemas-substreams)
- [EVM Chain-Specific Extensions | Substreams](#evm-chain-specific-extensions-substreams)
- [Reliability Guarantees | Substreams](#reliability-guarantees-substreams)
- [MongoDB | Substreams](#mongodb-substreams)
- [Local Development | Substreams](#local-development-substreams)
- [Deployable Services | Substreams](#deployable-services-substreams)
- [Explore Solana | Substreams](#explore-solana-substreams)
- [Change log | Substreams](#change-log-substreams)
- [Substreams:Stream | Substreams](#substreams-stream-substreams)
- [Local Service | Substreams](#local-service-substreams)
- [FAQ | Substreams](#faq-substreams)
- [PubSub | Substreams](#pubsub-substreams)
- [Making eth_calls | Substreams](#making-eth-calls-substreams)
- [Initialize a MANTRA Substreams Project | Substreams](#initialize-a-mantra-substreams-project-substreams)
- [Exploring Ethereum | Substreams](#exploring-ethereum-substreams)
- [Solana | Substreams](#solana-substreams)
- [Authentication | Substreams](#authentication-substreams)
- [JavaScript | Substreams](#javascript-substreams)
- [Remote Service | Substreams](#remote-service-substreams)
- [Substreams CLI reference | Substreams](#substreams-cli-reference-substreams)
- [Packages | Substreams](#packages-substreams)
- [SQL Sink | Substreams](#sql-sink-substreams)
- [Output | Substreams](#output-substreams)
- [Indexes | Substreams](#indexes-substreams)
- [Dojo DEX USDT Volume Subgraph Example | Substreams](#dojo-dex-usdt-volume-subgraph-example-substreams)
- [Run a Substreams | Substreams](#run-a-substreams-substreams)
- [Develop Substreams | Substreams](#develop-substreams-substreams)
- [Rust | Substreams](#rust-substreams)
- [Retrieve Events of a Smart Contract | Substreams](#retrieve-events-of-a-smart-contract-substreams)
- [How-To Guides | Substreams](#how-to-guides-substreams)
- [Filter Transactions | Substreams](#filter-transactions-substreams)
- [Parameterized Modules | Substreams](#parameterized-modules-substreams)
- [Triggers | Substreams](#triggers-substreams)
- [Key-Value Store | Substreams](#key-value-store-substreams)
- [Publish to The Graph Network | Substreams](#publish-to-the-graph-network-substreams)
- [Prometheus | Substreams](#prometheus-substreams)
- [Consume Substreams | Substreams](#consume-substreams-substreams)
- [Manifest & Modules | Substreams](#manifest-modules-substreams)
- [Deployable Services | Substreams](#deployable-services-substreams)
- [SPL Token Tracker | Substreams](#spl-token-tracker-substreams)
- [Foundational Modules | Substreams](#foundational-modules-substreams)
- [Injective | Substreams](#injective-substreams)
- [Chains and endpoints | Substreams](#chains-and-endpoints-substreams)
- [Manifests Reference | Substreams](#manifests-reference-substreams)
- [Inputs | Substreams](#inputs-substreams)
- [Result struct | Substreams](#result-struct-substreams)
- [GUI Reference | Substreams](#gui-reference-substreams)
- [Filter Transactions | Substreams](#filter-transactions-substreams)
- [Option struct | Substreams](#option-struct-substreams)
- [Rust Dependencies | Substreams](#rust-dependencies-substreams)
- [Keys in stores | Substreams](#keys-in-stores-substreams)
- [Module handlers | Substreams](#module-handlers-substreams)
- [Glossary | Substreams](#glossary-substreams)
- [Architecture | Substreams](#architecture-substreams)
- [DEX Trades | Substreams](#dex-trades-substreams)
- [Test Locally | Substreams](#test-locally-substreams)
- [Simple Substreams Example | Substreams](#simple-substreams-example-substreams)
- [Substreams:SQL | Substreams](#substreams-sql-substreams)
- [Graph Out | Substreams](#graph-out-substreams)
- [Initialize a Solana Substreams Project | Substreams](#initialize-a-solana-substreams-project-substreams)
- [Mapping Blocks | Substreams](#mapping-blocks-substreams)
- [Subgraphs | Substreams](#subgraphs-substreams)
- [Module types | Substreams](#module-types-substreams)
- [Chain-Specific Extensions | Substreams](#chain-specific-extensions-substreams)
- [Initialize a Starknet Substreams Project | Substreams](#initialize-a-starknet-substreams-project-substreams)
- [EVM | Substreams](#evm-substreams)
- [Initialize an EVM Substreams Project | Substreams](#initialize-an-evm-substreams-project-substreams)
- [Aggregation Windows | Substreams](#aggregation-windows-substreams)
- [Install the CLI | Substreams](#install-the-cli-substreams)
- [Other Ways of Consuming | Substreams](#other-ways-of-consuming-substreams)
- [What is Substreams? | Substreams](#what-is-substreams-substreams)

## Filter Instructions | Substreams
Source: https://docs.substreams.dev/tutorials/solana/explore-solana/filter-instructions

[PreviousExplore Solana](/tutorials/solana/explore-solana)[NextFilter Transactions](/tutorials/solana/explore-solana/filter-transactions)

Last updated 9 months ago

---

## Dynamic data sources | Substreams
Source: https://docs.substreams.dev/documentation/develop/manifest-modules/dynamic-data-sources

Using Factory contract is a quite common pattern used by dApps when the main smart contract deploys and manages multiple identical associated contracts, i.e. one smart contract for each Uniswap or Curve swap pool.

When developing traditional subgraphs, you could use [data source templates](https://thegraph.com/docs/en/developing/creating-a-subgraph/#data-source-templates) approach to keep track of such dynamically deployed smart contracts.

Here's how you can achieve that with Substreams.

We'll be using Uniswap V3 example where the Factory creates and deploys its smart contract for each pool.

You start with a simple map module that emits all pool creation events:

Copy
```
- name: map_pools_created
    kind: map
    inputs:
- source: sf.ethereum.type.v2.Block
    output:
      type: proto:uniswap.types.v1.Pools
```
Copy
```
# [substreams::handlers::map]
pub fn map_pools_created(block: Block) -> Result<Pools, Error> {
    Ok(Pools {
        pools: block
            .events::<abi::factory::events::PoolCreated>(&[&UNISWAP_V3_FACTORY])
            .filter_map(|(event, log)| {
                // skipped: extracting pool information from the transaction
                Some(Pool {
                    address,
                    token0,
                    token1,
                    ..Default::default()
                })
            })
            .collect(),
    })
}
```

We can now take that map module output and direct these pool creation events into a Substreams key-value store using a store module:

Copy
```
- name: store_pools_created
    kind: store
    updatePolicy: set
    valueType: proto:uniswap.types.v1.Pool
    inputs:
- map: map_pools_created
```
Copy
```
# [substreams::handlers::store]
pub fn store_pools_created(pools: Pools, store: StoreSetProto<Pool>) {
    for pool in pools.pools {
        let pool_address = &pool.address;
        store.set(pool.log_ordinal, format!("pool:{pool_address}"), &pool);
    }
}
```

Above we are using `pool:{pool_address}` as a key to store the pool information. Eventually, our store will contain all Uniswap pools. Now, in the downstream modules, we can easily retrieve our pool from the store whenever we need it.

Copy
```
- name: map_events
    kind: map
    inputs:
- source: sf.ethereum.type.v2.Block
- store: store_pools_created
    output:
      type: proto:uniswap.types.v1.Events
```
Copy
```
# [substreams::handlers::map]
pub fn map_events(block: Block, pools_store: StoreGetProto<Pool>) -> Result<Events, Error> {
    let mut events = Events::default();
    for trx in block.transactions() {
        for (log, call_view) in trx.logs_with_calls() {
            let pool_address = &Hex(&log.address).to_string();
            let pool = match pools_store.get_last(format!("pool:{pool_address}")) {
                Some(pool) => pool,
                None => { continue; }
            };
            // use the pool information from the store
        }
    }
    Ok(events)
}
```

Here we use `pools_store.get_last()` method to get the pool from the store by its smart contract address. Once we have it, we can use that information to analyze the swap transaction and emit the events.

Alternatively, we could make RPC calls to get the pool details from an RPC node but that would be extremely inefficient considering that we would need to make RPC calls for millions of such events. Using a store will be much faster.

For a real-life application of this pattern see [Uniswap V3 Substreams](https://github.com/streamingfast/substreams-uniswap-v3)

Links
- ----
- [Uniswap-v3 Subgraph and Substreams](https://github.com/streamingfast/substreams-uniswap-v3)
- [Substreams Sink Entity Changes](https://github.com/streamingfast/substreams-sink-entity-changes)

[PreviousKeys in stores](/documentation/develop/manifest-modules/keys-in-stores)[NextAggregation Windows](/documentation/develop/manifest-modules/aggregation-windows)

Last updated 1 year ago

---

## Development Container Reference | Substreams
Source: https://docs.substreams.dev/reference-and-specs/devcontainer-ref

The Substreams Dev Container is a tool to help you build your first project. You can either run it remotely or clone the [substreams-starter repository](https://github.com/streamingfast/substreams-starter?tab=readme-ov-file) to run it locally. Inside the Dev Container, the `substreams init` command sets up a code-generated Substreams project, allowing you to easily build a subgraph or an SQL-based solution for data handling.

## # Prerequisites
- Ensure Docker and VS Code are up-to-date.

## # Navigating the Dev Container

Upon entering the Dev Container, you can either insert your `substreams.yaml` file and run `substreams build` to generate Protobuf files or choose one of the auto-generated paths:
- **Minimal**: Extracts raw data from the block.
- **Non-Minimal**: Extracts filtered data using network-specific cache and Protobufs from the Foundational Modules.

## # Building Your Project

You can configure your Substreams project for querying either through a Subgraph or directly from your SQL database:
- **Subgraph**: Run `substreams codegen subgraph`. This generates a project with a basic `schema.graphql` and `mappings.ts` file. You can customize these to define entities based on the data extracted by Substreams. For more information on configuring a Subgraph sink, see the [Subgraph documentation](https://substreams.streamingfast.io/documentation/consume/subgraph).
- **SQL**: Run `substreams codegen sql` for SQL-based queries. For more information on configuring a SQL sink, refer to the [SQL documentation](https://substreams.streamingfast.io/documentation/consume/sql).

## # Deployment Options

To deploy a Subgraph, you can either run the `graph-node` locally using the `deploy-local` command or deploy to Subgraph Studio by using the `deploy` command from the `package.json` file.

## # Common Errors
- When running locally, make sure to verify that all Docker containers are healthy by running the `dev-status` command.

[PreviousChains and endpoints](/reference-and-specs/chains-and-endpoints)[NextSubstreams CLI reference](/reference-and-specs/command-line-interface)

Last updated 13 days ago

---

## Module handler creation | Substreams
Source: https://docs.substreams.dev/documentation/develop/manifest-modules/writing-module-handlers

Module handler creation overview
- -------------------------------

After generating the ABI and protobuf Rust code, you need to write the handler code. Save the code into the `src` directory and use the filename [`lib.rs`](https://github.com/streamingfast/substreams-template/blob/develop/src/lib.rs).

src/lib.rsCopy
```
mod abi;
mod pb;
use hex_literal::hex;
use pb::erc721;
use substreams::prelude::*;
use substreams::{log, store::StoreAddInt64, Hex};
use substreams_ethereum::{pb::eth::v2 as eth, NULL_ADDRESS};
// Bored Ape Club Contract
const TRACKED_CONTRACT: [u8; 20] = hex!("bc4ca0eda7647a8ab7c2061c2e118a18a936f13d");
substreams_ethereum::init!();
/// Extracts transfers events from the contract
# [substreams::handlers::map]
fn map_transfers(blk: eth::Block) -> Result<erc721::Transfers, substreams::errors::Error> {
    Ok(erc721::Transfers {
        transfers: blk
            .events::<abi::erc721::events::Transfer>(&[&TRACKED_CONTRACT])
            .map(|(transfer, log)| {
                substreams::log::info!("NFT Transfer seen");
                erc721::Transfer {
                    trx_hash: log.receipt.transaction.hash.clone(),
                    from: transfer.from,
                    to: transfer.to,
                    token_id: transfer.token_id.low_u64(),
                    ordinal: log.block_index() as u64,
                }
            })
            .collect(),
    })
}
/// Store the total balance of NFT tokens for the specific TRACKED_CONTRACT by holder
# [substreams::handlers::store]
fn store_transfers(transfers: erc721::Transfers, s: StoreAddInt64) {
    log::info!("NFT holders state builder");
    for transfer in transfers.transfers {
        if transfer.from != NULL_ADDRESS {
            log::info!("Found a transfer out {}", Hex(&transfer.trx_hash));
            s.add(transfer.ordinal, generate_key(&transfer.from), -1);
        }
        if transfer.to != NULL_ADDRESS {
            log::info!("Found a transfer in {}", Hex(&transfer.trx_hash));
            s.add(transfer.ordinal, generate_key(&transfer.to), 1);
        }
    }
}
fn generate_key(holder: &Vec<u8>) -> String {
    return format!("total:{}:{}", Hex(holder), Hex(TRACKED_CONTRACT));
}
```

View the [`lib.rs`](https://github.com/streamingfast/substreams-template/blob/develop/src/lib.rs) file in the repository.

## # **Module handler breakdown**

The logical sections of the [`lib.rs`](https://github.com/streamingfast/substreams-template/blob/develop/src/lib.rs) file are outlined and described in greater detail.

Import the necessary modules.

lib.rs excerptCopy
```
mod abi;
mod pb;
use hex_literal::hex;
use pb::erc721;
use substreams::{log, store, Hex};
use substreams_ethereum::{pb::eth::v2 as eth, NULL_ADDRESS, Event};
```

Store the tracked contract in the example in a `constant`.

lib.rs excerptCopy
```
const TRACKED_CONTRACT: [u8; 20] = hex!("bc4ca0eda7647a8ab7c2061c2e118a18a936f13d");
```

Define the `map` module in the Substreams manifest.

manifest excerptCopy
```
- name: map_transfers
  kind: map
  initialBlock: 12287507
  inputs:
- source: sf.ethereum.type.v2.Block
  output:
    type: proto:eth.erc721.v1.Transfers
```

Notice the: `name: map_transfers`, the module in the manifest name matches the handler function name. Also notice, there is one [`inputs`](/documentation/develop/manifest-modules/inputs) and one [`output`](/documentation/develop/manifest-modules/outputs) definition.

The [`inputs`](/documentation/develop/manifest-modules/inputs) uses the standard Ethereum Block, `sf.ethereum.type.v2.Block,` provided by the [`substreams-ethereum` crate](https://crates.io/crates/substreams-ethereum-core).

The output uses the `type` `proto:eth.erc721.v1.Transfers` which is a custom protobuf definition provided by the generated Rust code.

The function signature produced resembles:

lib.rs excerptCopy
```
# [substreams::handlers::map]
fn map_transfers(blk: eth::Block) -> Result<erc721::Transfers, substreams::errors::Error> {
    ...
}
```
## # **Rust macros**

Did you notice the `#[substreams::handlers::map]` on top of the function? It is a [Rust macro](https://doc.rust-lang.org/book/ch19-06-macros.html) provided by the [`substreams` crate](https://docs.rs/substreams/latest/substreams/).

The macro decorates the handler function as a `map.` Define `store` modules by using the syntax `#[substreams::handlers::store]`.

## # Module handler function

The `map` extracts ERC721 transfers from a `Block` object. The code finds all the `Transfer` `events` emitted by the tracked smart contract. As the events are encountered they are decoded into `Transfer` objects.

lib.rs excerptCopy
```
/// Extracts transfers events from the contract
# [substreams::handlers::map]
fn map_transfers(blk: eth::Block) -> Result<erc721::Transfers, substreams::errors::Error> {
    Ok(erc721::Transfers {
        transfers: blk
            .events::<abi::erc721::events::Transfer>(&[&TRACKED_CONTRACT])
            .map(|(transfer, log)| {
                substreams::log::info!("NFT Transfer seen");
                erc721::Transfer {
                    trx_hash: log.receipt.transaction.hash.clone(),
                    from: transfer.from,
                    to: transfer.to,
                    token_id: transfer.token_id.low_u64(),
                    ordinal: log.block_index() as u64,
                }
            })
            .collect(),
    })
}
```

Define the `store` module in the Substreams manifest.

manifest excerptCopy
```
- name: store_transfers
  kind: store
  initialBlock: 12287507
  updatePolicy: add
  valueType: int64
  inputs:
- map: map_transfers
```
- *Note:** `name: store_transfers` corresponds to the handler function name.

The `inputs` corresponds to the `output` of the `map_transfers` `map` module typed as `proto:eth.erc721.v1.Transfers`. The custom protobuf definition is provided by the generated Rust code.

lib.rs excerptCopy
```
# [substreams::handlers::store]
fn store_transfers(transfers: erc721::Transfers, s: store::StoreAddInt64) {
    ...
}
```
- *Note**: the `store` always receives itself as its own last input.

In the example the `store` module uses an `updatePolicy` set to `add` and a `valueType` set to `int64` yielding a writable `store` typed as `StoreAddInt64`.
- *Note**: **Store types**
- The writable `store` is always the last parameter of a `store` module function.
- The `type` of the writable `store` is determined by the `updatePolicy` and `valueType` of the `store` module.

The goal of the `store` in the example is to track a holder's current NFT `count` for the smart contract provided. The tracking is achieved through the analysis of `Transfers`.

`Transfers` **in detail**
- If the "`from`" address of the `transfer` is the `null` address (`0x0000000000000000000000000000000000000000`) and the "`to`" address is not the `null` address, the "`to`" address is minting a token, which results in the `count` being incremented.
- If the "`from`" address of the `transfer` is not the `null` address and the "`to`" address is the `null` address, the "`from`" address has burned a token, which results in the `count` being decremented.
- If both the "`from`" and the "`to`" address is not the `null` address, the `count` is decremented from the "`from`" address and incremented for the "`to`" address.

## # `store` concepts

There are three important things to consider when writing to a `store`:
- `ordinal`
- `key`
- `value`

### # `ordinal`

`ordinal` represents the order in which the `store` operations are applied.

The `store` handler is called once per `block.`

The `add` operation may be called multiple times during execution, for various reasons such as discovering a relevant event or encountering a call responsible for triggering a method call.
- *Note**: Blockchain execution models are linear. Operations to add must be added linearly and deterministically.

If an `ordinal` is specified, the order of execution is guaranteed. In the example, when the `store` handler is executed by a given set of `inputs`, such as a list of `Transfers`, it emits the same number of `add` calls and `ordinal` values for the execution.

### # `key`

Stores are [key-value stores](https://en.wikipedia.org/wiki/Key%E2%80%93value_database). Care needs to be taken when crafting a `key` to ensure it is unique **and flexible**.

If the `generate_key` function in the example returns the `TRACKED_CONTRACT` address as the `key`, it is not unique among different token holders.

The `generate_key` function returns a unique `key` for holders if it contains only the holder's address.
- *Important**: Issues are expected when attempting to track multiple contracts.

### # `value`

The value being stored. The `type` is dependent on the `store` `type` being used.

lib.rs excerptCopy
```
# [substreams::handlers::store]
fn store_transfers(transfers: erc721::Transfers, s: StoreAddInt64) {
    log::info!("NFT holders state builder");
    for transfer in transfers.transfers {
        if transfer.from != NULL_ADDRESS {
            log::info!("Found a transfer out {}", Hex(&transfer.trx_hash));
            s.add(transfer.ordinal, generate_key(&transfer.from), -1);
        }
        if transfer.to != NULL_ADDRESS {
            log::info!("Found a transfer in {}", Hex(&transfer.trx_hash));
            s.add(transfer.ordinal, generate_key(&transfer.to), 1);
        }
    }
}
fn generate_key(holder: &Vec<u8>) -> String {
    return format!("total:{}:{}", Hex(holder), Hex(TRACKED_CONTRACT));
}
```
## # Summary

Both handler functions have been written.

One handler function for extracting relevant `transfers`, and a second to store the token count per recipient.

Build Substreams to continue the setup process.

Copy
```
cargo build --target wasm32-unknown-unknown --release
```

The next step is to run Substreams with all of the changes made by using the generated code.

[PreviousModule handlers](/documentation/develop/manifest-modules/setting-up-handlers)[NextKeys in stores](/documentation/develop/manifest-modules/keys-in-stores)

Last updated 1 year ago

---

## Go | Substreams
Source: https://docs.substreams.dev/documentation/consume/stream/go

The [Substreams Go Sink library](https://github.com/streamingfast/substreams-sink) allows to you to programmatically stream a Substreams using the Go programming language. The library handles reconnections and provides best practices for error handling.

The [Substreams Sink Examples GitHub repository](https://github.com/streamingfast/substreams-sink-examples) contains an example that you can use as the starting point to build your custom sink logic. After cloning the repository, move to the `go` directory.

## # Run the Program

This example is built in the form of a CLI by using the `cobra` library. You can run the program by running the following command structure:

Copy
```
go run . sink <ENDPOINT> <SPKG> <MODULE_NAME>
```

In the following command, `go run .` is used to execute the `main.go` file. The `mainnet.eth.streamingfast.io:443 https://spkg.io/streamingfast/substreams-eth-block-meta-v0.4.3.spkg db_out` part of the command are useful parameters passed to the Go program (separated by a whitespace).

In the parameters, you pass the Substreams endpoint, the package, and the module to execute.

Copy
```
go run . sink mainnet.eth.streamingfast.io:443 https://github.com/streamingfast/substreams-eth-block-meta/releases/download/v0.5.1/substreams-eth-block-meta-v0.5.1.spkg db_out
```
- *Inspect the Code**

The example contains code comments, which are very useful to understand and adjust the code to your logic needs. Let's inspect the most important parts of the code:

Copy
```
var expectedOutputModuleType = string(new(pbchanges.DatabaseChanges).ProtoReflect().Descriptor().FullName()) // 1.
// ...code omitted...
func main() {
	logging.InstantiateLoggers()
	Run(
		"sinker",
		"Simple Go sinker sinking data to your terminal",
		Command(sinkRunE,
			"sink <endpoint> <manifest> [<output_module>]",
			"Run the sinker code",
			RangeArgs(2, 3),
			Flags(func(flags *pflag.FlagSet) {
				sink.AddFlagsToSet(flags)
			}),
		),
		OnCommandErrorLogAndExit(zlog),
	)
}
```

Create a new sink object from the parameters passed to the program:

Copy
```
func sinkRunE(cmd *cobra.Command, args []string) error {
	endpoint := args[0]
	manifestPath := args[1]
	// Find the output module in the manifest sink.moduleName configuration. If you have no
	// such configuration, you can change the value below and set the module name explicitly.
	outputModuleName := sink.InferOutputModuleFromPackage
	if len(args) == 3 {
		outputModuleName = args[2]
	}
	sinker, err := sink.NewFromViper(
		cmd,
		// Should be the Protobuf full name of the map's module output, we use
		// `substreams-database-changes` imported type. Adjust to your needs.
		//
		// If your Protobuf is defined in your Substreams manifest, you can use `substream protogen`
		// while being in the same folder that contain `buf.gen.yaml` file in the example folder.
		expectedOutputModuleType,
		endpoint,
		manifestPath,
		outputModuleName,
		// This is the block range, in our case defined as Substreams module's start block and up forever
		":",
		zlog,
		tracer,
	)
	cli.NoError(err, "unable to create sinker: %s", err)
	sinker.OnTerminating(func(err error) {
		cli.NoError(err, "unexpected sinker error")
		zlog.Info("sink is terminating")
	})
	// You **must** save the cursor somewhere, saving it to memory while
	// make it last until the process is killed, in which on re-start, the
	// sinker will resume from start block again. You can simply read from
	// a file the string value of the cursor and use `sink.NewCursor(value)`
	// to load it.
	// Blocking call, will return on sinker termination
	sinker.Run(context.Background(), sink.NewBlankCursor(), sink.NewSinkerHandlers(handleBlockScopedData, handleBlockUndoSignal))
	return nil
}
```

It is necessary to handle two kind of Substreams response messages:
- `blockScopedData`: sent by the server whenever a new block is discovered in the blockchain. Contains all the block information that you can decode.
- `blockUndoSignal`: sent every time there is a fork in the blockchain. Because you have probably read incorrect blocks in the `blockScopedData` message, you must rewind back to the latest valid block.

When you run the sinker, you pass two different functions to handle these messages:

Copy
```
sinker.Run(context.Background(), sink.NewBlankCursor(), sink.NewSinkerHandlers(handleBlockScopedData, handleBlockUndoSignal))
```
[PreviousJavaScript](/documentation/consume/stream/javascript)[NextSubstreams:Subgraph](/documentation/consume/subgraph)

Last updated 8 months ago

---

## Files | Substreams
Source: https://docs.substreams.dev/documentation/consume/other-sinks/files

## # Purpose

This documentation exists to assist you in understanding and beginning to use the StreamingFast [`substreams-sink-file`](https://github.com/streamingfast/substreams-sink-files)`s` tool. The Substreams module paired with this tutorial is a basic example of the elements required for sinking blockchain data into files-based storage solutions.

## # Overview

The `substreams-sink-files` tool provides the ability to pipe data extracted from a blockchain to various types of files-based persistence solutions.

For example, you could extract all of the ERC20, ERC721, and ERC1155 transfers from the Ethereum blockchain and persist the data to a files-based store.

Substreams modules are created and prepared specifically for the sink tool. After the sink tool begins running, automated tasks can be set up to have [BigQuery](https://cloud.google.com/bigquery), [Clickhouse](https://clickhouse.com), custom scripts, or other files-based storage solutions, ingest the data. This can only be accomplished indirectly. It's possible to automate further ingestion from files to data stores.

You could use `substreams-sink-files` to sink data in `JSONL` format to a [Google Cloud Storage (GCS)](https://cloud.google.com/storage) bucket and configure a BigQuery Transfer job to run every 15 minutes. The scheduled job ingests the new files found in the GCS bucket where the data, extracted by the Substreams, was written.

## # Accompanying code example

The accompanying Substreams module associated with this documentation is responsible for extracting a handful of data fields from the Block object injected into the Rust-based map module. The sink tool processes the extracted blockchain data line-by-line and outputs the data to the files-based persistence mechanism you've chosen.

The accompanying code example extracts four data points from the Block object and packs them into the `substreams.sink.files.v1` Protobuf's data model. The data is passed to the Protobuf as a single line of plain text.

Binary formats such as [Avro](https://avro.apache.org/) or [Parquet](https://parquet.apache.org/) is possible, however, support is not available. Contributions are welcome to help with support of binary data formats. [Contact the StreamingFast team on Discord](https://discord.gg/mYPcRAzeVN) to learn more and discuss specifics.

Installation
- -----------

## # Install `substreams-sink-files`

Install `substreams-sink-files` by using the pre-built binary release [available in the official GitHub repository](https://github.com/streamingfast/substreams-sink-files/releases).

Extract `substreams-sink-files` into a folder and ensure this folder is referenced globally via your `PATH` environment variable.

## # Accompanying code example

The accompanying code example for this tutorial is available in the `substreams-sink-files` repository. The Substreams project for the tutorial is located in the [docs/tutorial](https://github.com/streamingfast/substreams-sink-files/tree/master/docs/tutorial) directory.

Run the included `make protogen` command to create the required Protobuf files.

Copy
```
make protogen
```

It's a good idea to run the example code using your installation of the `substreams` CLI to make sure everything is set up and working properly.

Verify the setup for the example project by using the `make build` and `substreams run` commands.

Build the Substreams module by using the included `make` command.

Copy
```
make
```

Run the project by using the `substreams run` command.

Copy
```
substreams run -e mainnet.eth.streamingfast.io:443 substreams.yaml jsonl_out --start-block 1000000 --stop-block +1
```

The `substreams run` command will result in output resembling the following:

Copy
```
- ---------- NEW BLOCK #1,000,000 (1000000) ---------------
{
  "@module": "jsonl_out",
  "@block": 1000000,
  "@type": "sf.substreams.sink.files.v1",
  "@data": {
    "lines": [
      "{\"hash\":\"8e38b4dbf6b11fcc3b9dee84fb7986e29ca0a02cecd8977c161ff7333329681e\",\"number\":1000000,\"parent_hash\":\"b4fbadf8ea452b139718e2700dc1135cfc81145031c84b7ab27cd710394f7b38\",\"timestamp\":\"2016-02-13T22:54:13Z\"}"
    ]
  }
}
```

Substreams modifications
- -----------------------

## # Module handler changes for sink

The example code in the [`lib.rs`](https://github.com/streamingfast/substreams-sink-files/blob/master/docs/tutorial/src/lib.rs) Rust source code file contains the `jsonl_out` module handler responsible for extracting the blockchain data. The module handler is responsible for passing the data to the `sf.substreams.sink.files.v1` Protobuf for the sink tool and its processes.

Copy
```
# [substreams::handlers::map]
fn jsonl_out(block: eth::Block) -> Result<Lines, substreams::errors::Error> {
    let header = block.header.as_ref().unwrap();
    Ok(pb::sinkfiles::Lines {
        lines: vec![json!({
            "number": block.number,
            "hash": Hex(&block.hash).to_string(),
            "parent_hash": Hex(&header.parent_hash).to_string(),
            "timestamp": header.timestamp.as_ref().unwrap().to_string()
        })
        .to_string()],
    })
}
```

This module handler uses `JSONL` for the output type, any other plain-text line-based format can be supported, `CSV` for example. The [`json!`](https://docs.rs/serde_json/latest/serde_json/macro.json.html) macro is used to write the block data to the Rust `Vec` type by using the Rust [`vec!`](https://doc.rust-lang.org/std/macro.vec.html) macro.

The example code is intentionally very basic. StreamingFast [provides a more robust and full example](https://github.com/streamingfast/substreams-eth-token-transfers/blob/develop/src/lib.rs#L24) demonstrating how to extract data related to transfers from Ethereum. A crucial aspect of working with Substreams and sinks is a significant amount of data can be extracted from a Block object. The data is extracted and packed into a row. The row is represented by the JSONL or CSV based Protobuf you're responsible for designing for your sink.

The output type for sink is a list of lines. The line content can be any type anything that is formatted as plain text, and line based. For example, a basic string like the transaction's hash, would result in files containing all the hashes for the transactions, one per line.

## # Core steps for Substreams sink modules
- Import sink `.spkg` files, re-generate Protobufs and create and add a mod.rs file.
- Create a map module outputting sf.substreams.sink.files.v1 format. This module extracts the entity to be written, one per block from the block or another module's dependencies. Each line will be in JSON format. You can use the json! macro from the [`serde_json`](https://docs.rs/serde_json/latest/serde_json) crate to assist creating your structure, one per line.
- Add the correct module definition to the Substreams manifest `substreams.yaml`.

Copy
```
imports:
  sink_files: https://github.com/streamingfast/substreams-sink-files/releases/download/v2.1.0/substreams-sink-files-v2.1.0.spkg
binaries:
  default:
    type: wasm/rust-v1
    file: target/wasm32-unknown-unknown/release/substreams.wasm
modules:
- name: jsonl_out
    kind: map
    inputs:
- source: sf.ethereum.type.v2.Block
    output:
      type: proto:sf.substreams.sink.files.v1.Lines
```

Understanding the sink tool
- --------------------------

## # Run and configure the `substreams-sink-files` tool

The command to start and run the `substreams-sink-files` tool for the accompanying Substreams project will resemble:

Copy
```
substreams-sink-files run --encoder=lines --state-store=./output/state.yaml mainnet.eth.streamingfast.io:443 substreams.yaml jsonl_out ./output/files
```

Verify output from tool
- ----------------------

Running the sink tool results in logging information printed to the terminal and directories and files being written to the local system or a cloud provider bucket if configured.

The sink tool will produce output in the terminal resembling the following for a properly configured and working environment and project.

Copy
```
2023-01-09T07:45:02.563-0800 INFO (substreams-sink-files) starting prometheus metrics server {"listen_addr": "localhost:9102"}
2023-01-09T07:45:02.563-0800 INFO (substreams-sink-files) sink to files {"file_output_path": "./localdata/out", "file_working_dir": "./localdata/working", "endpoint": "mainnet.eth.streamingfast.io:443", "encoder": "lines", "manifest_path": "substreams.yaml", "output_module_name": "jsonl_out", "block_range": "", "state_store": "./localdata/working/state.yaml", "blocks_per_file": 10000, "buffer_max_size": 67108864}
2023-01-09T07:45:02.563-0800 INFO (substreams-sink-files) reading substreams manifest {"manifest_path": "substreams.yaml"}
2023-01-09T07:45:02.563-0800 INFO (substreams-sink-files) starting pprof server {"listen_addr": "localhost:6060"}
2023-01-09T07:45:04.041-0800 INFO (pipeline) computed start block {"module_name": "jsonl_out", "start_block": 0}
2023-01-09T07:45:04.042-0800 INFO (substreams-sink-files) ready, waiting for signal to quit
2023-01-09T07:45:04.045-0800 INFO (substreams-sink-files) setting up sink {"block_range": {"start_block": 0, "end_block": "None"}, "cursor": {"Cursor":"","Block":{}}}
2023-01-09T07:45:04.048-0800 INFO (substreams-sink-files) starting new file boundary {"boundary": "[0, 10000)"}
2023-01-09T07:45:04.049-0800 INFO (substreams-sink-files) boundary started {"boundary": "[0, 10000)"}
2023-01-09T07:45:04.049-0800 INFO (substreams-sink-files) starting stats service {"runs_each": "2s"}
2023-01-09T07:45:06.052-0800 INFO (substreams-sink-files) substreams sink stats {"progress_msg_rate": "0.000 msg/s (0 total)", "block_rate": "650.000 blocks/s (1300 total)", "last_block": "#1299 (a0f0f283e0d297dd4bcf4bbff916b1df139d08336ad970e77f26b45f9a521802)"}
```

One bundle of data is created for every 10K blocks during the sink process.

To view the files the `substreams-sink-files` tool generates navigate into the directory you used for the output path. The directory referenced in the example points to the `localdata/out` directory. List the files in the output directory using the standard `ls` command to reveal the files created by the `substreams-sink-files` tool.

Copy
```
...
0000000000-0000010000.jsonl	0000090000-0000100000.jsonl	0000180000-0000190000.jsonl
0000010000-0000020000.jsonl	0000100000-0000110000.jsonl	0000190000-0000200000.jsonl
0000020000-0000030000.jsonl	0000110000-0000120000.jsonl	0000200000-0000210000.jsonl
0000030000-0000040000.jsonl	0000120000-0000130000.jsonl	0000210000-0000220000.jsonl
0000040000-0000050000.jsonl	0000130000-0000140000.jsonl	0000220000-0000230000.jsonl
0000050000-0000060000.jsonl	0000140000-0000150000.jsonl	0000230000-0000240000.jsonl
0000060000-0000070000.jsonl	0000150000-0000160000.jsonl	0000240000-0000250000.jsonl
0000070000-0000080000.jsonl	0000160000-0000170000.jsonl	0000250000-0000260000.jsonl
0000080000-0000090000.jsonl	0000170000-0000180000.jsonl
...
```

The block range spanned by the example is from block 0000000000 to block 0000260000. The blocks contain all the lines received for the full 10K of processed blocks by default. The block range is controlled by using the `--file-block-count` flag.

## # Cursors

When you use Substreams, it sends back a block to a consumer using an opaque cursor. This cursor points to the exact location within the blockchain where the block is. In case your connection terminates or the process restarts, upon re-connection, Substreams sends back the cursor of the last written bundle in the request so that the stream of data can be resumed exactly where it left off and data integrity is maintained.

You will find that the cursor is saved in a file on disk. The location of this file is specified by the flag `--state-store` which points to a local folder. You must ensure that this file is properly saved to a persistent location. If the file is lost, the `substreams-sink-files` tool will restart from the beginning of the chain, redoing all the previous processing.

Therefore, It is crucial that this file is properly persisted and follows your deployment of `substreams-sink-files` to avoid any data loss.

## # High Performance

If you are looking for the fastest performance possible, we suggest that your destination source is able to handle heavy traffic. Also, to speed up things, you can allocate a lot of RAM to the process and increase the flag `--buffer-max-size` to a point where you are able to hold a full batch of N blocks in memory (checking the size of the final file is a good indicator of the size to keep stuff in memory).

A lot of I/O operations is avoid if the buffer can hold everything in memory greatly speeding up the process of writing blocks bundle to its final destination.

## # Cloud-based storage

You can use the `substreams-sink-files` tool to route data to files on your local file system and cloud-based storage solutions. To use a cloud-based solution such as Google Cloud Storage bucket, S3 compatible bucket, or Azure bucket, you need to make sure it is set up properly. Then, instead of referencing a local file in the `substreams-sink-files run` command, use the path to the bucket. The paths resemble `gs://<bucket>/<path>`, `s3://<bucket>/<path>`, and `az://<bucket>/<path>` respectively. Be sure to update the values according to your account and provider.

## # Limitations

When you use the `substreams-sink-files` tool, you will find that it syncs up to the most recent "final" block of the chain. This means it is not real-time. Additionally, the tool writes bundles to disk when it has seen 10,000 blocks. As a result, the latency of the last available bundle can be delayed by around 10,000 blocks. How many blocks per batch can be controlled by changing the flag `--file-block-count`

Conclusion and review
- --------------------

The ability to route data extracted from the blockchain by using Substreams is powerful and useful. Files aren't the only type of sink the data extracted by Substreams can be piped into. Review the core Substreams sinks documentation for [additional information on other types of sinks](/documentation/consume/other-sinks) and sinking strategies.

To use `substreams-sink-files` you need to clone the official repository, install the tooling, generate the required files from the substreams CLI for the example Substreams module and run the sink tool.

You have to ensure the sinking strategy has been defined, the appropriate file types have been targeted, and accounted for, and the module handler code in your Substreams module has been properly updated. You need to start the `substreams-sink-files` tool and use the `run` command being sure to provide all of the required values for the various flags.

[PreviousOther Ways of Consuming](/documentation/consume/other-sinks)[NextKey-Value Store](/documentation/consume/other-sinks/kv)

Last updated 5 months ago

---

## Cosmos | Substreams
Source: https://docs.substreams.dev/tutorials/cosmos

[PreviousDEX Trades](/tutorials/solana/dex-trades)[NextInjective](/tutorials/cosmos/injective)

Last updated 6 months ago

---

## Initialize an Injective Substreams Project | Substreams
Source: https://docs.substreams.dev/documentation/how-to-guides/injective

In this guide, you'll learn how to initialize a Injective-based Substreams project. You’ll learn how to set up a simple project to extract raw data or filter events from a smart contract.

## # Prerequisites
- Docker and VS Code installed and up-to-date.
- Visit the [Getting Started Guide](https://github.com/streamingfast/substreams-starter) to initialize your Dev Container.

## # Step 1: Initialize Your Injective Substreams Project

1. Open your Dev Container and run the following command to initialize your project:
   
   Copy
   ```
   substreams init
   ```
2. You will be given the option to choose between two Injective project options. Select the one that best fits your requirements:
- **Injective-minimal**: Creates a simple Substreams that extracts raw data from the block and generates Rust code.
- **Injective-events**: Creates a Substreams that extracts Injective events using the cached [Injective Foundational Module](https://substreams.dev/packages/injective-common/v0.2.4), filtered by one or more smart contract addresses.

## # Step 2: Visualize the Data

1. Create your account [here](https://thegraph.market/) to generate an authentification token (JWT) and pass it as input to:
   
   Copy
   ```
   substreams auth
   ```
2. Run the following command to visualize and itterate on your filtered data model:
   
   Copy
   ```
   substreams gui
   ```

## # Step 3: Customize your Project

After initialization, you can:
- Modify your Substreams manifest to include additional filters or configurations.
- Implement custom processing logic in Rust based on the filtered data retrieved by the foundational module.

## # Additional Resources

You may find these additional resources helpful for developing your first EVM application.

### # Dev Container Reference

The [Dev Container Reference](/reference-and-specs/devcontainer-ref) helps you navigate the complete container and its common errors.

### # GUI Reference

The [GUI reference](/reference-and-specs/gui) lets you explore all the tools available in the Substreams GUI.

### # Manifests Reference

The [Manifests Reference](/reference-and-specs/manifests) helps you with editing the `substreams.yaml`.

[PreviousInitialize a Starknet Substreams Project](/documentation/how-to-guides/starknet)[NextInitialize a MANTRA Substreams Project](/documentation/how-to-guides/mantra)

Last updated 7 days ago

---

## Substreams:Subgraph | Substreams
Source: https://docs.substreams.dev/documentation/consume/subgraph

[PreviousGo](/documentation/consume/stream/go)[NextGraph Out](/documentation/consume/subgraph/graph-out)

Last updated 5 months ago

---

## NFT Trades | Substreams
Source: https://docs.substreams.dev/tutorials/solana/nft-trades

The NFT Trades project, developed by TopLedger, extracts NFT trades from different Solana exchanges, such as Tensor, MagicEden, or HadeSwap.

## # About TopLedger

[TopLedger](https://topledger.xyz/) is SQL-based data discovery and analytics platform focused on Solana. By using Substreams, TopLedger has been able to extract data from the main Solana dapps, thus providing rich analytics products.

TopLedger is an active contributor to the Substreams community and has developed several useful ready-to-use Substreams.

## # Before You Begin

The NFT Trades Substreams requires medium to advanced Substreams knowledge. If this is the first time you are using Substreams, make sure you:
- Read the [Develop Substreams](/documentation/develop) section, which will teach you the basics of the developing Substreams modules.
- Complete the [Explore Solana](/tutorials/solana/explore-solana) tutorial, which will assist you in understanding the main pieces of the Solana Substreams.

Clone the [TopLedger Solana Programs](https://github.com/Topledger/solana-programs) project and navigate to the `nft-trades` folder, which contains the code of the Substreams.

## # Inspect the Project

The Substreams contains only one module, `map_block`:

Copy
```
modules:
- name: map_block
    kind: map
    inputs:
- source: sf.solana.type.v1.Block
    output:
      type: proto:sf.solana.nft.trades.v1.Output
```

The `Output` object provided as the Substreams output is defined in the `proto/outout.proto` file:

Copy
```
message Output {
  repeated TradeData data = 1;
}
message TradeData {
  required string block_date = 1;
  required int64 block_time = 2;
  required uint64 block_slot = 3;
  required string tx_id = 4;
  required uint64 txn_fee = 5;
  required string mint = 6;
  required double amount = 7;
  required string category = 8;
  required string buyer = 9;
  required string seller = 10;
  required double taker_fee = 11;
  required double maker_fee = 12;
  required double amm_fee = 13;
  required double royalty = 14;
  required string instruction_type = 15;
  required uint32 instruction_index = 16;
  required string outer_program = 17;
  required string inner_program = 18;
  required uint32 inner_instruxtion_index = 19;
  required bool is_inner_instruction = 20;
  required string platform = 21;
  required string currency_mint = 22;
}
```

The `TradeData` object contains information about every trade executed, such as `amount`, `buyer` or `seller`.

Every exchange handles data differently, so there is no unique way to decode the data. Therefore, it is necessary to create a custom *decode* function for every exchange supported by the Substreams. If you navigate to the `nft-trades/dapps` folder, you will find a file for every exchange.

Every `dapp` file has a `parse_trade_instruction` function, which is responsible for decoding the data.

## # Run the Substreams

You can use the Substreams CLI to run the project:

Copy
```
substreams gui -e mainnet.sol.streamingfast.io:443 \
    substreams.yaml map_block -s 200321235 -t +1
```
## # Inspect the Code

The `src/lib.rs` file contains the declaration of the Substreams module, `map_block`. This function is executed for every block of the blockchain.

Copy
```
fn map_block(block: Block) -> Result<Output, substreams::errors::Error> {
    let slot = block.slot;
    let parent_slot = block.parent_slot;
    let timestamp = block.block_time.as_ref().unwrap().timestamp;
    let mut data: Vec<TradeData> = vec![]; // 1.
    for trx in block.transactions_owned() { // 2. 
        let accounts = trx.resolved_accounts_as_strings(); // 3.
        if let Some(transaction) = trx.transaction { // 4.
            let meta = trx.meta.unwrap();
            let pre_balances = meta.pre_balances;
            let post_balances = meta.post_balances;
            let pre_token_balances = meta.pre_token_balances;
            let post_token_balances = meta.post_token_balances;
            let msg = transaction.message.unwrap();
            for (idx, inst) in msg.instructions.into_iter().enumerate() { // 5.
                let program = &accounts[inst.program_id_index as usize]; // 6.
                let trade_data = get_trade_data( // 7.
                    program,
                    inst.data,
                    &inst.accounts,
                    &accounts,
                    &pre_balances,
                    &post_balances,
                    &meta.log_messages,
                    &post_token_balances,
                );
            
                // ...code omitted...
            }
        }
    }
}
```

2. Create an *array* of `TradeData` objects, where the trading data will be stored.
5. Iterate over the transactions of the block.
8. Get accounts of the transaction (the `resolved_accounts()` method contains also accounts stored in the [Address Lookup Tables](https://docs.solana.com/developing/lookup-tables)).
11. *Unwrap transaction*
14. Iterate over the instructions of the transaction.
17. Get the program account. The `instruction.program_id_index` indicates the position of the program account in the accounts array.
20. Pass the data to the `get_trade_data` function. This function verifies if the instruction executed is from one of the NFT exchanges that you want to track. The return type is `Option<TradeData>`. The `Option` will only be populated if the instruction belongs to one of the NFT exchanges.

Because every exchange handles the NFT data differently, there must be a custom decoding function for every exchange. The `dapps` folder of the project contains a file for every exchange, declaring the `parse_trade_instruction` function.

Copy
```
fn get_trade_data(
    dapp_address: &String,
    instruction_data: Vec<u8>,
    account_indices: &Vec<u8>,
    accounts: &Vec<String>,
    pre_balances: &Vec<u64>,
    post_balances: &Vec<u64>,
    log_messages: &Vec<String>,
    post_token_balances: &Vec<TokenBalance>,
) -> Option<TradeData> {
    let input_accounts = prepare_input_accounts(account_indices, accounts); // 1.
    let mut result = None;
    match dapp_address.as_str() { // 2.
        "TSWAPaqyCSx2KABk68Shruf4rp7CxcNi8hAsbdwmHbN" => { // 3. Tensor
            result =
                dapps::dapp_TSWAPaqyCSx2KABk68Shruf4rp7CxcNi8hAsbdwmHbN::parse_trade_instruction( // 4.
                    instruction_data,
                    input_accounts,
                    log_messages,
                );
        }
        "M2mx93ekt1fmXSVkTrUL9xVFHkmME8HTUi5Cyc5aF7K" => { // 4. MagicEden
            result =
                dapps::dapp_M2mx93ekt1fmXSVkTrUL9xVFHkmME8HTUi5Cyc5aF7K::parse_trade_instruction(
                    instruction_data,
                    input_accounts,
                    accounts,
                    log_messages,
                    post_token_balances,
                );
        }
        "hadeK9DLv9eA7ya5KCTqSvSvRZeJC3JgD5a9Y3CNbvu" => { // 5. HadeSwap
            result =
                dapps::dapp_hadeK9DLv9eA7ya5KCTqSvSvRZeJC3JgD5a9Y3CNbvu::parse_trade_instruction(
                    instruction_data,
                    input_accounts,
                    accounts,
                    pre_balances,
                    post_balances,
                )
        }
        "mmm3XBJg5gk8XJxEKBvdgptZz6SgK4tXvn36sodowMc" => { // 6. MMM
            result =
                dapps::dapp_mmm3XBJg5gk8XJxEKBvdgptZz6SgK4tXvn36sodowMc::parse_trade_instruction(
                    instruction_data,
                    input_accounts,
                    accounts,
                    pre_balances,
                    post_balances,
                    log_messages,
                );
        }
        "CJsLwbP1iu5DuUikHEJnLfANgKy6stB2uFgvBBHoyxwz" => {  // 7. Solanart
            result =
                dapps::dapp_CJsLwbP1iu5DuUikHEJnLfANgKy6stB2uFgvBBHoyxwz::parse_trade_instruction(
                    instruction_data,
                    input_accounts,
                    accounts,
                    pre_balances,
                    post_balances,
                    log_messages,
                );
        }
        "SNPRohhBurQwrpwAptw1QYtpFdfEKitr4WSJ125cN1g" => { // 8. Sniper Market
            result =
                dapps::dapp_SNPRohhBurQwrpwAptw1QYtpFdfEKitr4WSJ125cN1g::parse_trade_instruction(
                    instruction_data,
                    input_accounts,
                    accounts,
                    pre_balances,
                    post_balances,
                    log_messages,
                );
        }
        _ => {} // 9.
    }
    return result;
}
```

2. Based on the `account_indices` parameter passed, create an in-order array of accounts.
5. The `dapp_address` parameter passed is the program account. For every NFT program, you handle the decoding differently.
8. For example, the `TSWAPaqyCSx2KABk68Shruf4rp7CxcNi8hAsbdwmHbN` account represents the Tensor exchange.
11. If the program account does not match any of the NFT exchanges, then an empty `Option<TradeData>` object is returned.

[PreviousSPL Token Tracker](/tutorials/solana/token-tracker)[NextDEX Trades](/tutorials/solana/dex-trades)

Last updated 9 months ago

---

## Protobuf Schemas | Substreams
Source: https://docs.substreams.dev/documentation/develop/creating-protobuf-schemas

Protobuf overview
- ----------------

Substreams uses Google Protocol Buffers extensively. Protocol Buffers, also referred to as protobufs, are used as the API for data models specific to the different blockchains. Manifests contain references to the protobufs for your Substreams module.
- *Tip**: Protobufs define the input and output for modules.

Learn more about the details of Google Protocol Buffers in the official documentation provided by Google.
- *Google Protocol Buffer Documentation**

[Learn more about Google Protocol Buffers](https://protobuf.dev/) in the official documentation provided by Google.
- *Google Protocol Buffer Tutorial**

[Explore examples and additional learning material](https://protobuf.dev/programming-guides/proto3/) for Google Protocol Buffers provided by Google.

## # Protobuf definition for Substreams

Define a protobuf model as [`proto:eth.erc721.v1.Transfers`](https://github.com/streamingfast/substreams-template/blob/develop/proto/erc721.proto) representing a list of ERC721 transfers.
- *Note**: The `Transfers` protobuf in the Substreams Template example is located in the proto directory.

eth/erc721/v1/erc721.protoCopy
```
syntax = "proto3";
package eth.erc721.v1;
message Transfers {
  repeated Transfer transfers = 1;
}
message Transfer {
  bytes from = 1;
  bytes to = 2;
  uint64 token_id = 3;
  bytes trx_hash = 4;
  uint64 ordinal = 5;
}
```

[View the `erc721.proto`](https://github.com/streamingfast/substreams-template/blob/develop/proto/erc721.proto) file in the official Substreams Template example repository.

### # Identifying data types

The ERC721 smart contract used in the Substreams Template example contains a `Transfer` event. You can use the event data through a custom protobuf.

The protobuf file serves as the interface between the module handlers and the data being provided by Substreams.
- *Tip**: Protobufs are platform-independent and are defined and used for various blockchains.
- The ERC721 smart contracts used in the Substreams Template example are generic contracts used across many different Ethereum applications.
- The size and scope of the Substreams module dictates the number of and complexity of protobufs.

The Substreams Template example extracts `Transfer` events from the [Bored Ape Yacht Club smart contract](https://etherscan.io/address/0xbc4ca0eda7647a8ab7c2061c2e118a18a936f13d) which is located on the Ethereum blockchain.

Several specific data types exist in the Ethereum smart contract ecosystem, some extending the ERC20 and ERC721 base modules. Complex protobufs are created and refined based on the various data types used across the different blockchains.
- *Tip***:* The use of fully qualified protobuf file paths reduces the risk of naming conflicts when other community members build their Substreams packages.

## # Generating protobufs

The [`substreams` CLI](/reference-and-specs/command-line-interface) is used to generate the associated Rust code for the protobuf.

Notice the `protogen` command and Substreams manifest passed into the [`substreams` CLI](/reference-and-specs/command-line-interface).

Copy
```
substreams protogen ./substreams.yaml --exclude-paths="sf/ethereum,sf/substreams,google"
```

The pairing code is generated and saved into the [`src/pb/eth.erc721.v1.rs`](https://github.com/streamingfast/substreams-template/blob/develop/src/pb/eth.erc721.v1.rs)Rust file.

The [`mod.rs`](https://github.com/streamingfast/substreams-template/blob/develop/src/pb/mod.rs) file located in the `src/pb` directory of the Substreams Template example is responsible for exporting the freshly generated Rust code.

src/pb/mod.rsCopy
```
# [path = "eth.erc721.v1.rs"]
# [allow(dead_code)]
pub mod erc721;
```

View the [`mod.rs`](https://github.com/streamingfast/substreams-template/blob/develop/src/pb/mod.rs) file in the repository.

## # Protobuf and Rust optional fields

Protocol buffers define fields' type by using standard primitive data types, such as integers, booleans, and floats or a complex data type such as `message`, `enum`, `oneof` or `map`. View the [full list](https://developers.google.com/protocol-buffers/docs/proto#scalar) of types in the [Google Protocol Buffers documentation](https://developers.google.com/protocol-buffers/docs/overview).

Any primitive data types in a message generate the corresponding Rust type,[`String`](https://doc.rust-lang.org/std/string/struct.String.html) for `string`, `u64` for `uint64,` and assign the default value of the corresponding Rust type if the field is not present in a message, an empty string for [`String`](https://doc.rust-lang.org/std/string/struct.String.html), 0 for integer types, `false` for `bool`.

Rust generates the corresponding `message` type wrapped by an [`Option`](https://doc.rust-lang.org/rust-by-example/std/option.html) enum type for fields referencing other complex `messages`. The [`None`](https://doc.rust-lang.org/std/option/) variant is used if the field is not present in the message.

The [`Option`](https://doc.rust-lang.org/rust-by-example/std/option.html) [`enum`](https://doc.rust-lang.org/book/ch06-01-defining-an-enum.html) is used to represent the presence through [`Some(x)`](https://doc.rust-lang.org/std/option/) or absence through [`None`](https://doc.rust-lang.org/std/option/) of a value in Rust. [`Option`](https://doc.rust-lang.org/rust-by-example/std/option.html) allows developers to distinguish between a field containing a value versus a field without an assigned a value.
- *Note**: The standard approach to represent nullable data in Rust is to wrap optional values in [`Option<T>`](https://doc.rust-lang.org/rust-by-example/std/option.html).

The Rust [`match`](https://doc.rust-lang.org/rust-by-example/flow_control/match.html) keyword is used to compare the value of an [`Option`](https://doc.rust-lang.org/rust-by-example/std/option.html) to a [`Some`](https://doc.rust-lang.org/std/option/) or [`None`](https://doc.rust-lang.org/std/option/) variant. Handle a type wrapped [`Option`](https://doc.rust-lang.org/rust-by-example/std/option.html) in Rust by using:

Copy
```
match person.Location {
    Some(location) => { /* Value is present, do something */ }
    None => { /* Value is absent, do something */ }
}
```

If you are only interested in finding the presence of a value, use the [`if let`](https://doc.rust-lang.org/rust-by-example/flow_control/if_let.html) statement to handle the [`Some(x)`](https://doc.rust-lang.org/std/option/) arm of the [`match`](https://doc.rust-lang.org/rust-by-example/flow_control/match.html) code.

Copy
```
if let Some(location) = person.location {
    // Value is present, do something
}
```

If a value is present, use the [`.unwrap()`](https://doc.rust-lang.org/rust-by-example/error/option_unwrap.html) call on the [`Option`](https://doc.rust-lang.org/rust-by-example/std/option.html) to obtain the wrapped data. You'll need to account for these types of scenarios if you control the creation of the messages yourself or if the field is documented as always being present.
- *Note**: You need to be **absolutely sure** **the field is always defined**, otherwise Substreams panics and never completes, getting stuck on a block indefinitely.
- **PROST!*** is a tool for generating Rust code from protobuf definitions. [Learn more about `prost`](https://github.com/tokio-rs/prost) in the project's official GitHub repository.

[Learn more about `Option`](https://doc.rust-lang.org/rust-by-example/std/option.html) in the official Rust documentation.

[PreviousAggregation Windows](/documentation/develop/manifest-modules/aggregation-windows)[NextRun a Substreams](/documentation/develop/running-substreams)

Last updated 1 year ago

---

## EVM Chain-Specific Extensions | Substreams
Source: https://docs.substreams.dev/documentation/develop/overview/evm-chain-specific-extensions

[Making eth\_calls](/documentation/develop/overview/evm-chain-specific-extensions/eth-calls)[PreviousChain-Specific Extensions](/documentation/develop/overview)[NextMaking eth\_calls](/documentation/develop/overview/evm-chain-specific-extensions/eth-calls)

Last updated 3 months ago

---

## Reliability Guarantees | Substreams
Source: https://docs.substreams.dev/documentation/consume/reliability-guarantees

When you consume a Substreams package through the CLI (or through any of the different sinks available), you are establishing a gRPC connection with the Substreams provider (i.e. StreamingFast, Pinax...), which streams the data of every block back to your sink.

The Response Format
- ------------------

The response returned by the provider is a [Protobuf object](https://github.com/streamingfast/substreams/blob/831093480ab6bf6970e41f74ea9bc0b04410a028/proto/sf/substreams/rpc/v2/service.proto#L53), which contains the blockchain data plus other relevant information:

Copy
```
message Response {
  oneof message {
    SessionInit session = 1;
    ModulesProgress progress = 2;
    BlockScopedData block_scoped_data = 3;
    BlockUndoSignal block_undo_signal = 4;
    Error fatal_error = 5;
    InitialSnapshotData debug_snapshot_data = 10;
    InitialSnapshotComplete debug_snapshot_complete = 11;
  }
}
```

Data & Cursor
- ------------

One of the most important fields of the response is the `BlockScopedData` object, which contains the actual data of the blockchain, along with other useful fields. Specifically, The `output` field holds the binary data emitted by the Substreams.

Copy
```
message BlockScopedData {
  MapModuleOutput output = 1;
  sf.substreams.v1.Clock clock = 2;
  string cursor = 3;
  uint64 final_block_height = 4;
  repeated MapModuleOutput debug_map_outputs = 10;
  repeated StoreModuleOutput debug_store_outputs = 11;
}
```

In a connection, errors might occur; any of the two parties involved may get disconnected because of a network issue. In theses cases, it is essential to have a mechanism that allows you to consume the data exactly where you left it before the disconnection. This mechanism is usually called a **cursor**. Essentially, a cursor points to the latest piece of data consumed by the user.

In Substreams, the `cursor` field of the response indicates the latest block consumed by the user. The user **must** persist the cursor, so that in the case of a disconnection, the Substreams provider can start streaming data from the latest consumed block.

For example, the SQL sink establishes a gRPC connection with the Substreams provider, and for every block consumed, it persists the number of the block in a table. If a disconnection occurs, the SQL sink establishes a new connection and starts consuming from the latest persisted block. That's why it is very important to persist the cursor!

Forks
- ----

Forks are really common in blockchain. Essentially, a fork occurs when the path of the blockchain diverges (i.e. there are two or more different paths available because different the nodes involved do not agree on the correct path).

The `BlockUndoSignal` object of the response is used to keep track of forks. In Substreams, you are reading real-time data, so if a fork occurs, you may read blocks from the incorrect path. When the blockchain resolves the fork and eventually chooses a path, you will have to *unread* all the incorrect blocks (i.e. discard all the blocks belonging to the incorrect path of the fork). The `BlockUndoSignal` contains the latest valid block of the blockchain and a cursor:

Copy
```
message BlockUndoSignal {
  sf.substreams.v1.BlockRef last_valid_block = 1;
  string last_valid_cursor = 2;
}
```

If you commit cursors in the BlockUndoSignals, you don’t need to mind about disconnections amid forks. It will bring you back exactly where you left off, even if it was mid-ways through a fork.

[PreviousPackages](/documentation/consume/packages)[NextDeployable Services](/documentation/consume/deployable-services)

Last updated 9 months ago

---

## MongoDB | Substreams
Source: https://docs.substreams.dev/documentation/consume/other-sinks/mongodb

It is possible to send Substreams data to MongoDB. See the GitHub repository for an early version of the MongoDB Substreams Sink:
- <https://github.com/streamingfast/substreams-sink-mongodb>
[PreviousKey-Value Store](/documentation/consume/other-sinks/kv)[NextPrometheus](/documentation/consume/other-sinks/prometheus)

Last updated 10 months ago

---

## Local Development | Substreams
Source: https://docs.substreams.dev/tutorials/graph-node/local-development

The Graph Node is the software that indexers run to index subgraphs. When developing a subgraph (or a Substreams-powered subgrpah), it is very convenient to test the subgraph deployment locally. This can be achieved by running the Graph Node software and all its dependencies in a local Docker environment.

Clone the [Substreams Development Environment GitHub respository](https://github.com/streamingfast/substreams-dev-environment), which contains the necessary shell scripts to run a local Graph Node in your computer.

Requirements
- -----------

This tutorial requires you to:
- Have Docker installed.
- Run a Unix-like operating system, so that you can execute bash scripts.

Set up the Environment
- ---------------------

In the [Substreams Development Environment GitHub respository](https://github.com/streamingfast/substreams-dev-environment), move to the `graph-node` folder. The entrypoint to set up the Graph Node local environment is the `start.sh` script, which spins up a Graph Node instance configured for a specific network (e.g. `injective-mainnet`), along with a local IPFS node and a local Postgres database. When using this script, you must pass two parameters: `NETWORK` and `SUBSTREAMS_ENDPOINT`.

Copy
```
./start.sh <NETWORK> <SUBSTREAMS_ENDPOINT>
```

For example, the following command spins up a Graph Node for the `injective-mainnet` network using the `https://mainnet.injective.streamingfast.io:443` Substreams endpoint.

Copy
```
./start.sh injective-mainnet https://mainnet.injective.streamingfast.io:443
```

The script also expects the `SUBSTREAMS_API_TOKEN` environment variable to be configured with your Substreams API authentication token.

Interact With the Graph Node
- ---------------------------

You can interact with the Graph Node using the Graph CLI (`graph`). Some useful command are:
- `graph build --ipfs=http://localhost:5001`: build the subgraph and store the build files in the local IPFS node.
- `graph create <NAME> --node=http://localhost:8020`: create a new subgraph in the local Graph Node.
- `graph remove <NAME> --node=http://localhost:8020`: remove an existing subgraph in the local Graph Node.
- `graph deploy --node http://localhost:8020/ --ipfs http://localhost:5001 <NAME>`: deploy a subgraph to the local Graph Node.
[PreviousSubgraphs](/tutorials/graph-node)[NextPublish to The Graph Network](/tutorials/graph-node/publish-decentralized-network)

Last updated 6 months ago

---

## Deployable Services | Substreams
Source: https://docs.substreams.dev/documentation/consume/deployable-services

The Substreams Deployable Services define a common interface to easily deploy your Substreams to one of the supported sinks, such as SQL or subgraphs. Essentially, it facilitates sending data to a variety of sinks by simply using the Substreams CLI.

## # Hoes Does It Work?

1. Choose what sink you want to use (SQL or subgraphs).
2. Add the `sink` configuration to your manifest.
3. Use the `substreams alpha service` command to deploy, stop or remove your services.

### # Choose a Sink

Depending on your needs, you must choose how you want to consume the data: using a SQL database or a subgraph. Substreams using the SQL sink must have a `db_out` module and those using the subgraph sink must have a `graph_out` module.

### # Add the Sink Configuration

The `sink` configuration in a Substreams manifest defines what sink should be used. To get more information about the Substreams manifest, refer to the [Manifest & Modules page](/documentation/develop/manifest-modules)

Every sink has different configuration fields available, so check out the Manifest Reference for more information. In the following example, a SQL sink is defined:

Copy
```
sink:
  module: db_out
  type: sf.substreams.sink.sql.v1.Service
  config:
    schema: "./schema.sql"
    engine: clickhouse
    postgraphile_frontend:
      enabled: false
    pgweb_frontend:
      enabled: false
    dbt_config:
      enabled: true
      files: "./path/to/folder"
      run_interval_seconds: 300
```
### # Deploy the Service

Use the `substreams alpha service <COMMAND>` command to manage your services. Once your Substreams has the corresponding manifest configuration, you can deploy it by using the `substreams alpha service deploy` command.

You will get a service ID, which is a unique identifier for your service. This will allow you to manage your service and apply actions to it, such a stopping or removing it.

[PreviousReliability Guarantees](/documentation/consume/reliability-guarantees)[NextSubstreams:SQL](/documentation/consume/sql)

Last updated 10 months ago

---

## Explore Solana | Substreams
Source: https://docs.substreams.dev/tutorials/solana/explore-solana

In this tutorial, you will learn the basics of developing Solana Substreams through examples. The Solana Substreams Explorer contains several modules performing basic and advanced aggregations on Solana data.

## # Before You Begin

Before you start coding, there are several dependencies you must install on your computer.

### # The GitHub Repository

The `https://github.com/streamingfast/substreams-explorers` GitHub repository contains all the Substreams Explorers currently available. You can simply clone the repository:

Copy
```
git clone https://github.com/streamingfast/substreams-explorers
```
### # The Substreams CLI

The Substreams CLI allows you to run, package, and visualize your Substreams. Make sure you have the CLI installed by following this [simple tutorial](/documentation/consume/installing-the-cli).

### # Substreams Basics

You should be familiar with the basic Substreams terminology, which includes:
- Manifest & Modules (understanding the difference between a `map` and a `store` module)
- Protobufs
- Packages

Take a look at the *Develop Substreams* section for more information on how to start developing Substreams.

## # The Solana Explorer

The Solana explorer includes several modules showcasing what Solana data you can extract with Substreams (it's easy and fast!). In the following sections, you will find out about the different functions you can use to easily get started with Solana.

[PreviousSolana](/tutorials/solana)[NextFilter Instructions](/tutorials/solana/explore-solana/filter-instructions)

Last updated 8 days ago

---

## Change log | Substreams
Source: https://docs.substreams.dev/reference-and-specs/change-log

Substreams builds upon Firehose.
Keep track of [Firehose releases and Data model updates](https://firehose.streamingfast.io/release-notes/change-logs) in the Firehose documentation.

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

v1.11.1
- ------
- Fix the `gui` breaking when the network field is not set in the spkg
- Fixed `SUBSTREAMS_REGISTRY_TOKEN` environment variable not taking precedence over the `registry-token` file.

v1.11.0
- ------
- Commands `run`, `gui` and `info` now accept the new standard package definition (ex: `ethereum-common@latest`) to reference an spkg file from `https://substreams.dev`.
- Changed `substreams run`: the two positional parameters now align with `gui`: `[package [module_name]]`. The syntax `substreams run <module_name>` is not accepted anymore.
- Added `substreams publish` to `publish` a package on the substreams registry (check on `https://substreams.dev`).
- Added `substreams registry` to `login` and `publish` on the substreams registry (check on `https://substreams.dev`).
- Added `substreams tools extract-wasm` to extract a wasm file from a substreams package.

v1.10.11
- -------
- Add `avalanche-mainnet` to the CLI.

v1.10.10
- -------
- Fix `substreams gui` selecting the wrong module in the 'outputs' view if there is no output the selected output\_module.
- Add the block 'age' printed clock headers in the`substreams run` command.

v1.10.9
- ------
- Add Mantra Mainnet and Testnet to the HardcodedEndpoints map.
- Add Vara Mainnet and Testnet to the HardcodedEndpoints map.
- Fix `substreams gui` command downloading spkg twice which would cause some issues with spkg that are very big.
- Add base58 decoding in the output view for the `substreams gui`

v1.10.8
- ------

## # Server

> **Note** All caches for stores using the updatePolicy `set_sum` (added in substreams v1.7.0) and modules that depend on them will need to be deleted, since they may contain bad data.
- Fix bad data in stores using `set_sum` policy: squashing of store segments incorrectly "summed" some values that should have been "set" if the last event for a key on this segment was a "sum"
- Fix panic in initialization (`metrics sender not set`)

v1.10.7
- ------
- Fix small bug making some requests in development-mode slow to start (when starting close to the module initialBlock with a store that doesn't start on a boundary)
- Fixed `substreams build` creating a buf.gen.yaml file with absolute paths (should be relative)
- Removed `--show-generated-buf-gen` flag to `substreams protogen`
- Bumped neoeinstein-prost version in auto-generated `buf.gen.yaml` file when using `substreams protogen` or `substreams build` (compatible with new substreams-0.6 and prost-0.13)

v1.10.6
- ------
- Fixed `substreams gui` panic (regression appeared in v1.10.3)

v1.10.5
- ------
- Fixed an(other) issue where multiple stores running on the same stage with different initialBlocks will fail to proress (and hang)

v1.10.4
- ------

## # Server
- Fix bug where some invalid cursors may be sent (with 'LIB' being above the block being sent) and add safeguard/loggin if the bug appears again
- Fix panic in the whole tier2 process when stores go above the size limit while being read from "kvops" cached changes

## # CLI
- Add `-o cursor` output type to `substreams run` for debugging purposes

v1.10.3
- ------

## # Server
- Fix "cannot resolve 'old cursor' from files in passthrough mode" error on some requests with an old cursor
- Fix handling of 'special case' substreams module with only "params" as its input: should not skip this execution (used in graph-node for head tracking) -> empty files in module cache with hash `d3b1920483180cbcd2fd10abcabbee431146f4c8` should be deleted for consistency

## # CLI
- Add `substreams tools default-endpoint {network-name}` to help with auto-configuration tools
- Bump `substreams init` protocol version to "1" to be compatible with new codegen endpoint

v1.10.2
- ------
- `substreams gui`: fix panic in some conditions when streaming from block 0

v1.10.1
- ------

## # Server

> **Note** Since a bug that affected substreams with "skipping blocks" was corrected in this release, any previously produced substreams cache should be considered as possibly corrupted and be eventually replaced
- Fix handling of modules that receive both filtered AND unfiltered data as their inputs -> some "repeated entries" could appear where no data should have showed up
- Fix stalling on substreams with both map and store with different initialBlocks on the same stage
- Fix: prevent execution of modules that should be skipped when running live or dev mode (different outputs than when running in batch mode on tier2)

## # Client
- `substreams gui` fixed a panic occuring if the given package path doesn't exist
- `substreams init` must now be called from within your project folder (it no longer downloads file in a subdirectory)
- (since v1.10.0) `substreams gui` no longer accepts "output\_module" as a single argument. It either receives nothing, the package, or the package followed by the output\_module

v1.10.0
- ------

## # Server
- Add `sf.substreams.rpc.v2.EndpointInfo/Info` endpoint (if the infoserver is given as a module, i.e. from firehose-core)
- Add an execution timeout of 3 minutes per block by default (can be overriden in tier1/tier2 Configs) -- this is useful when an external (eth\_call) is stuck on a forked block hash.
- Revert 'initialBlocks' changes from v1.9.1 because a 'changing module hash' causes more trouble.
- Wazero: bump v1.8.0 and activate caching of precompiled wasm modules in `/tmp/wazero` to decrease compilation time
- Metering update: more detailed metering with addition of new metrics (`live_uncompressed_read_bytes`, `live_uncompressed_read_forked_bytes`, `file_uncompressed_read_bytes`, `file_uncompressed_read_forked_bytes`, `file_compressed_read_forked_bytes`, `file_compressed_read_bytes`, `file_uncompressed_write_bytes`, `file_compressed_write_bytes`). *DEPRECATION WARNING*: `bytes_read` and `bytes_written` metrics will be removed in the future, please use the new metrics for metering instead.
- Manifest reader: increase timeout of remote spkg fetch to 5 minutes, up from 30 seconds

## # Client
- Add `substreams auth` command, to authenticate via `thegraph.market` and to get a dev API Key.
- Rename `--discovery-endpoint` into `codegen-endpoint` in `substreams init` command.
- Add `substreams codegen subgraph` command that takes a substreams `module` and an `spkg` and that generates a simple `subgraph` from the `module` output.
- On `substreams init` command, if flag `--state-file` is provided, the state file is used by default for project generation.
- In `substreams init` command, the state file is named using a `Date format` and not using `Unix` anymore.
- Tools->prometheus: added the possibility to override the start-block on an endpoint
- `substreams gui` no longer accepts "output\_module" as a single argument. It either receives nothing, the package, or the package followed by the output\_module

v1.9.3
- -----
- Fixed error handling issue in 'backprocessing' causing high CPU usage in tier1 servers
- Fixed handling of packages referenced by `ipfs://` URL (now simply using /api/v0/cat?arg=...)
- Added `--used-modules-only` flag to `substreams info` to only show modules that are in execution tree for the given output\_module

v1.9.2
- -----

## # Added
- Added support for directly reading spkg file that is compressed with zstd (from http, gs, s3, azure or local)

## # Fixed
- Prevent Noop handler from sending outputs with 'Stalled' step in cursor (which breaks substreams-sink-kv)

v1.9.1
- -----

## # Fixed

Fixed substreams hanging in production-mode on chains with a 'first-streamable-block' higher than 0:
- all initialBlocks will be 'bumped' to the first-streamable-block if it is higher
- this will affect the module hashes: use `substreams info --first-streamable-block=<block_num>` to see how a value will affect your modules
- modules with initialBlocks higher than the first-streamable-block of a chain will be unaffected.

v1.9.0
- -----

## # Important BUG FIX
- Fix a bug introduced in v1.6.0 that could result in corrupted store "state" file if all the "outputs" were already cached for a module in a given segment (rare occurence)
- We recommend clearing your substreams cache after this upgrade and re-processing or validating your data if you use stores.

## # Fixed
- substreams 'tools decode state' now correctly prints the `kvops` when pointing to store output files

## # Added
- Expose a new intrinsic to modules: `skip_empty_output`, which causes the module output to be skipped if it has zero bytes. (Watch out, a protobuf object with all its default values will have zero bytes)
- Improve schedule order (faster time to first block) for substreams with multiple stages when starting mid-chain

v1.8.2
- -----
- `substreams init` (code generation): fix displaying of saved path in filenames

v1.8.1
- -----
- Add a `NoopMode` to the `Tier1` enabling to avoid sending data back to requester while processing live.

v1.8.0
- -----

## # Remote Code Generation

The `substreams init` command now fetches a list of available 'code generators' to "<https://codegen.substreams.dev>". Upon selection of a code generator, it launches an interactive session to gather the information necessary to build your substreams. This allows flexibility and getting anything from "skeleton" of a substreams for a given chain up to a fully built .spkg file with subgraph bindings.

## # Added
- Add 'compressed' boolean field to the 'incoming request' log
- Add a substreams `live back filler`, so a request running close to HEAD in production-mode on tier1 will trigger jobs on tier2 when boundaries are passed by final blocks, backfilling the cache. These jobs will be "unmetered".

## # Fixed
- Fixed Substreams tier1 active worker request metrics that was not decrementing correctly.
- Truncate error messages log lines to 18k characters to prevent them from disappearing through some load balancers.

## # Removed
- Removed local ethereum code generation from `init` command.

v1.7.3
- -----

## # Server-side improvements
- Faster bootstrapping through bstream improvements, now only loads and keeps 200 blocks below LIB to link with merged blocks.
- Fixed delay in serving requests close to chain HEAD when using production-mode

v1.7.2
- -----

## # Improvements on the `use` attribute
- If module with `use` attribute has not `inputs` at all, inputs are replaced by used module inputs
- If module with `use` attribute has no `blockFilter`, it's replaced by used module `blockFilter`
- If `blockFilter` is set to `{}`, it will be considered as `nil` in the spkg, enabling module with `use` attribute to override the `blockFilter` by a `nil` one

v1.7.1
- -----

## # Highlights
- Substreams engine is now able run Rust code that depends on `solana_program` in Solana land to decode and `alloy/ether-rs` in Ethereum land

### # How to use `solana_program` or `alloy`/`ether-rs`

Those libraries when used in a `wasm32-unknown-unknown` context creates in a bunch of [wasmbindgen](https://rustwasm.github.io/wasm-bindgen/) imports in the resulting Substreams Rust code, imports that led to runtime errors because Substreams engine didn't know about those special imports until today.

The Substreams engine is now able to "shims" those `wasmbindgen` imports enabling you to run code that depends libraries like `solana_program` and `alloy/ether-rs` which are known to pull those `wasmbindgen` imports. This is going to work as long as you do not actually call those special imports. Normal usage of those libraries don't accidentally call those methods normally. If they are called, the WASM module will fail at runtime and stall the Substreams module from going forward.

To enable this feature, you need to explicitly opt-in by appending a `+wasm-bindgen-shims` at the end of the binary's type in your Substreams manifest:

Copy
```
binaries:
  default:
    type: wasm/rust-v1
    file: <some_file>
```

to become

Copy
```
binaries:
  default:
    type: wasm/rust-v1+wasm-bindgen-shims
    file: <some_file>
```
## # Others
- substreams.yaml now supports `localPath` attribute under `protobuf.descriptorSets`, so you can pre-build a descriptor set using `buf build --as-file-descriptor-set -o myfile.binpb` and add it directly to your substreams package.
- Substreams clients now enable gzip compression over the network (already supported by servers).
- Substreams binary type can now be optionally composed of runtime extensions by appending a `+<extension>,[<extesions...>]` at the end of the binary type. Extensions are `key[=value]` that are runtime specifics.
  
  > [!NOTE] If you were a library author and parsing generic Substreams manifest(s), you will now need to handle that possibility in the binary type. If you were reading the field without any processing, you don't have to change nothing.
- Fixed a failure in protogen where duplicate files would "appear multiple times" and fail.
- Fixed bug with block rate underflow in `gui`.

v1.7.0
- -----
- Added store with update policy `set_sum` which allows the store to either sum a numerical value, or set it to a new value.
- Re-added Ethereum Sepolia support in `substreams init`.
- Fixed a bug with the new `descriptorSets` feature that wasn't ordered properly to correctly generate Protobuf bindings.

v1.6.2
- -----
- execout: preload only one file instead of two, log if undeleted caches found
- execout: add environment variable SUBSTREAMS\_DISABLE\_PRELOAD\_EXEC\_FILES to disable file preloading

v1.6.1
- -----
- Revert sanity check to support the special case of a substreams with only 'params' as input. This allows a chain-agnostic event to be sent, along with the clock.
- Fix error handling when resolved start-block == stop-block and stop-block is defined as non-zero

v1.6.0
- -----

## # Upgrading

> **Note** Upgrading to v1.6.0 will require changing the tier1 and tier2 versions concurrently, as the internal protocol has changed.

## # Highlights

### # Index Modules and Block Filter
- *Index Modules* and *Block Filter* can now be used to speed up processing and reduce the amount of parsed data.
- When indexes are used along with the `BlockFilter` attribute on a mapper, blocks can be skipped completely: they will not be run in downstreams modules or sent in the output stream, except in live segment or in dev-mode, where an empty 'clock' is still sent.
- See <https://github.com/streamingfast/substreams-foundational-modules> for an example implementation
- Blocks that are skipped will still appear in the metering as "read bytes" (unless a full segment is skipped), but the index stores themselves are not "metered"

### # Scheduling / speed improvements
- The scheduler no longer duplicates work in the first segments of a request with multiple stages.
- Fix all issues with running a substreams where modules have different "initial blocks"
- Maximum Tier1 output speed improved for data that is already processed
- Tier1 'FileWalker' now polls more aggressively on local filesystem to prevent extra seconds of wait time.

## # Fixed
- Fix a bug in the `gui` that would crash when trying to `r`estart the stream.
- fix total read bytes in case data already cache

## # Added
- New environment variable `SUBSTREAMS_WORKERS_RAMPUP_TIME` can specify the initial delay before tier1 will reach the number of tier2 concurrent requests.
- Add 'clock' output to `substreams run` command, useful mostly for performance testing or pre-caching
- (alpha) Introduce the `wasip1/tinygo-v1` binary type.

## # Changed / Removed
- Disabled `otelcol://` tracing protocol, its mere presence affected performance.
- Previous value for `SUBSTREAMS_WORKERS_RAMPUP_TIME` was `4s`, now set to `0`, disabling the mechanism by default.

v1.5.6
- -----

## # Fixes
- Fix bug where substreams tier2 would sometimes write outputs with the wrong tag (leaked from another tier1 request)

## # Remove
- Removed MaxWasmFuel since it is not supported in Wazero

v1.5.5
- -----

## # Fixes
- bump wazero execution to fix issue with certain substreams causing the server process to freeze

## # Changes
- Allow unordered ordinals to be applied from the substreams (automatic ordering before flushing to stores)

## # Add
- add `substreams_tier1_worker_retry_counter` metric to count all worker errors returned by tier2
- add `substreams_tier1_worker_rejected_overloaded_counter` metric to count only worker errors with string "service currently overloaded"
- add `google/protobuf/duration.proto` to system proto files
- Support for buf build urls in substreams manifest. Ex.:

Copy
```
protobuf:
  buf_build:
- buf.build/streamingfast/firehose-cosmos
```

v1.5.4
- -----

## # Fixes
- fix a possible panic() when an request is interrupted during the file loading phase of a squashing operation.
- fix a rare possibility of stalling if only some fullkv stores caches were deleted, but further segments were still present.
- fix stats counters for store operations time

v1.5.3
- -----

Performance, memory leak and bug fixes

## # Server
- fix memory leak on substreams execution (by bumping wazero dependency)
- prevent substreams-tier1 stopping if blocktype auto-detection times out
- allow specifying blocktype directly in Tier1 config to skip auto-detection
- fix missing error handling when writing output data to files. This could result in tier1 request just "hanging" waiting for the file never produced by tier2.
- fix handling of dstore error in tier1 'execout walker' causing stalling issues on S3 or on unexpected storage errors
- increase number of retries on storage when writing states or execouts (5 -> 10)
- prevent slow squashing when loading each segment from full KV store (can happen when a stage contains multiple stores)

## # Gui
- prevent 'gui' command from crashing on 'incomplete' spkgs without moduledocs (when using --skip-package-validation)

v1.5.2
- -----
- Fix a context leak causing tier1 responses to slow down progressively

v1.5.1
- -----
- Fix a panic on tier2 when not using any wasm extension.
- Fix a thread leak on metering GRPC emitter
- Rollback scheduler optimisation: different stages can run concurrently if they are schedulable. This will prevent taking much time to execute when restarting close to HEAD.
- Add `substreams_tier2_active_requests` and `substreams_tier2_request_counter` prometheus metrics
- Fix the `tools tier2call` method to make it work with the new 'generic' tier2 (added necessary flags)

v1.5.0
- -----

## # Operators
- A single substreams-tier2 instance can now serve requests for multiple chains or networks. All network-specific parameters are now passed from Tier1 to Tier2 in the internal ProcessRange request.

> [!IMPORTANT] Since the `tier2` services will now get the network information from the `tier1` request, you must make sure that the file paths and network addresses will be the same for both tiers.

> [!TIP] The cached 'partial' files no longer contain the "trace ID" in their filename, preventing accumulation of "unsquashed" partial store files. The system will delete files under '{modulehash}/state' named in this format`{blocknumber}-{blocknumber}.{hexadecimal}.partial.zst` when it runs into them.

v1.4.0
- -----

## # Client
- Implement a `use` feature, enabling a module to use an existing module by overriding its inputs or initial block. (Inputs should have the same output type than override module's inputs). Check a usage of this new feature on the [substreams-db-graph-converter](https://github.com/streamingfast/substreams-db-graph-converter/) repository.
- Fix panic when using '--header (-H)' flag on `gui` command
- When packing substreams, pick up docs from the README.md or README in the same directory as the manifest, when top-level package.doc is empty
- Added "Total read bytes" summary at the end of 'substreams run' command

## # Server performance in "production-mode"

Some redundant reprocessing has been removed, along with a better usage of caches to reduce reading the blocks multiple times when it can be avoided. Concurrent requests may benefit the other's work to a certain extent (up to 75%)
- All module outputs are now cached. (previously, only the last module was cached, along with the "store snapshots", to allow parallel processing). (this will increase disk usage, there is no automatic removal of old module caches)
- Tier2 will now read back mapper outputs (if they exist) to prevent running them again. Additionally, it will not read back the full blocks if its inputs can be satisfied from existing cached mapper outputs.
- Tier2 will skip processing completely if it's processing the last stage and the `output_module` is a mapper that has already been processed (ex: when multiple requests are indexing the same data at the same time)
- Tier2 will skip processing completely if it's processing a stage that is not the last, but all the stores and outputs have been processed and cached.
- The "partial" store outputs no longer contain the trace ID in the filename, allowing them to be reused. If many requests point to the same modules being squashed, the squasher will detect if another Tier1 has squashed its file and reload the store from the produced full KV.
- Scheduler modification: a stage now waits for the previous stage to have completed the same segment before running, to take advantage of the cached intermediate layers.
- Improved file listing performance for Google Storage backends by 25%

## # Operator concerns
- Tier2 service now supports a maximum concurrent requests limit. Default set to 0 (unlimited).
- Readiness metric for Substreams tier1 app is now named `substreams_tier1` (was mistakenly called `firehose` before).
- Added back readiness metric for Substreams tiere app (named `substreams_tier2`).
- Added metric `substreams_tier1_active_worker_requests` which gives the number of active Substreams worker requests a tier1 app is currently doing against tier2 nodes.
- Added metric `substreams_tier1_worker_request_counter` which gives the total Substreams worker requests a tier1 app made against tier2 nodes.

v1.3.7
- -----
- Fixed `substreams init` generated The Graph GraphQL regarding wrong `Bool` types.
- The `substreams init` command can now be used on Arbitrum Mainnet network.

v1.3.6
- -----

This release brings important server-side improvements regarding performance, especially while processing over historical blocks in production-mode.

## # Backend (through firehose-core)
- Performance: prevent reprocessing jobs when there is only a mapper in production mode and everything is already cached
- Performance: prevent "UpdateStats" from running too often and stalling other operations when running with a high parallel jobs count
- Performance: fixed bug in scheduler ramp-up function sometimes waiting before raising the number of workers
- Added support for authentication using api keys. The env variable can be specified with `--substreams-api-key-envvar` and defaults to `SUBSTREAMS_API_KEY`.
- Added the output module's hash to the "incoming request"
- Added `trace_id` in grpc authentication calls
- Bumped connect-go library to new "connectrpc.com/connect" location
- Enable gRPC reflection API on tier1 substreams service

v1.3.5
- -----

## # Code generation
- Added `substreams init` support for creating a substreams with data from fully-decoded Calls instead of only extracting events.

v1.3.4
- -----

## # Code generation
- Added `substreams init` support for creating a substreams with the "Dynamic DataSources" pattern (ex: a `Factory` contract creating `pool` contracts through the `PoolCreated` event)
- Changed `substreams init` to always add prefixes the tables and entities with the project name
- Fixed `substreams init` support for unnamed params and topics on log events

v1.3.3
- -----
- Fixed `substreams init` generated code when dealing with Ethereum ABI events containing array types.
  
  > [!NOTE] For now, the generated code only works with Postgres, an upcoming revision is going to lift that constraint.

v1.3.2
- -----
- Fixed `store.has_at` Wazero signature which was defined as `has_at(storeIdx: i32, ord: i32, key_ptr: i32, key_len: i32)` but should have been `has_at(storeIdx: i32, ord: i64, key_ptr: i32, key_len: i32)`.
- Fixed the local `substreams alpha service serve` ClickHouse deployment which was failing with a message regarding fork handling.
- Catch more cases of WASM deterministic errors as `InvalidArgument`.
- Added some output-stream info to logs.

v1.3.1
- -----

## # Server
- Fixed error-passing between tier2 and tier1 (tier1 will not retry sending requests that fail deterministicly to tier2)
- Tier1 will now schedule a single job on tier2, quickly ramping up to the requested number of workers after 4 seconds of delay, to catch early exceptions
- "store became too big" is now considered a deterministic error and returns code "InvalidArgument"

v1.3.0
- -----

## # Highlights
- Support new `networks` configuration block in `substreams.yaml` to override modules' *params* and *initial\_block*. Network can be specified at run-time, avoiding the need for separate spkg files for each chain.
- [BREAKING CHANGE] Remove the support for the `deriveFrom` overrides. The `imports`, along with the new `networks` feature, should provide a better mechanism to cover the use cases that `deriveFrom` tried to address.

> These changes are all handled in the substreams CLI, applying the necessary changes to the package before sending the requests. The Substreams server endpoints do not need to be upgraded to support it.

## # Added
- Added `networks` field at the top level of the manifest definition, with `initialBlock` and `params` overrides for each module. See the substreams.yaml.example file in the repository or <https://substreams.streamingfast.io/reference-and-specs/manifests> for more details and example usage.
- The networks `params` and `initialBlock`` overrides for the chosen network are applied to the module directly before being sent to the server. All network configurations are kept when packing an .spkg file.
- Added the `--network` flag for choosing the network on `run`, `gui` and `alpha service deploy` commands. Default behavior is to use the one defined as `network` in the manifest.
- Added the `--endpoint` flag to `substreams alpha service serve` to specify substreams endpoint to connect to
- Added endpoints for Antelope chains
- Command 'substreams info' now shows the params

## # Removed
- Removed the handling of the `DeriveFrom` keyword in manifest, this override feature is going away.
- Removed the `--skip-package-validation`` option only on run/gui/inspect/info

## # Changed
- Added the `--params` flag to `alpha service deploy` to apply per-module parameters to the substreams before pushing it.
- Renamed the `--parameters` flag to `--deployment-params` in `alpha service deploy`, to clarify the intent of those parameters (given to the endpoint, not applied to the substreams modules)
- Small improvement on `substreams gui` command: no longer reads the .spkg multiple times with different behavior during its process.

v1.2.0
- -----

## # Client
- Fixed bug in `substreams init` with numbers in ABI types

## # Backend
- Return the correct GRPC code instead of wrapping it under an "Unknown" error. "Clean shutdown" now returns CodeUnavailable. This is compatible with previous substreams clients like substreams-sql which should retry automatically.
- Upgraded components to manage the new block encapsulation format in merged-blocks and on the wire required for firehose-core v1.0.0

v1.1.22
- ------

## # alpha service deployments
- Fix fuzzy matching when endpoint require auth headers
- Fix panic in "serve" when trying to delete a non-existing deployment
- Add validation check of substreams package before sending deploy request to server

v1.1.21
- ------

## # Changed
- Codegen: substreams-database-change to v1.3, properly generates primary key to support chain reorgs in postgres sink.
- Sink server commands all moved from `substreams alpha sink-*` to `substreams alpha service *`
- Sink server: support for deploying sinks with DBT configuration, so that users can deploy their own DBT models (supported on postgres and clickhouse sinks). Example manifest file segment:
  
  Copy
  ```
  [...]
  sink:
    module: db_out
    type: sf.substreams.sink.sql.v1.Service
    config:
      schema: "./schema.sql"
      wire_protocol_access: true
      postgraphile_frontend:
        enabled: true
      pgweb_frontend:
        enabled: true
      dbt:
        files: "./dbt"
        run_interval_seconds: 60
  ```
  
  where "./dbt" is a folder containing the dbt project.
- Sink server: added REST interface support for clickhouse sinks. Example manifest file segment:
  
  Copy
  ```
  [...]
  sink:
    module: db_out
    type: sf.substreams.sink.sql.v1.Service
    config:
      schema: "./schema.clickhouse.sql"
      wire_protocol_access: true
      engine: clickhouse
      postgraphile_frontend:
        enabled: false
      pgweb_frontend:
        enabled: false
      rest_frontend:
        enabled: true
  ```

## # Fixed
- Fix `substreams info` cli doc field which wasn't printing any doc output

v1.1.20
- ------
- Optimized start of output stream in developer mode when start block is in reversible segment and output module does not have any stores in its dependencies.
- Fixed bug where the first streamable block of a chain was not processed correctly when the start block was set to the default zero value.

v1.1.19
- ------

## # Changed
- Codegen: Now generates separate substreams.{target}.yaml files for sql, clickhouse and graphql sink targets.

## # Added
- Codegen: Added support for clickhouse in schema.sql

## # Fixed
- Fixed metrics for time spent in eth\_calls within modules stats (server and GUI)
- Fixed `undo` json message in 'run' command
- Fixed stream ending immediately in dev mode when start/end blocks are both 0.
- Sink-serve: fix missing output details on docker-compose apply errors
- Codegen: Fixed pluralized entity created for db\_out and graph\_out

v1.1.18
- ------

## # Fixed
- Fixed a regression where start block was not resolved correctly when it was in the reversible segment of the chain, causing the substreams to reprocess a segment in tier 2 instead of linearly in tier 1.

v1.1.17
- ------

## # Fixed
- Missing decrement on metrics `substreams_active_requests`

v1.1.16
- ------

## # Added
- `substreams_active_requests` and `substreams_counter` metrics to `substreams-tier1`

## # Changed
- `evt_block_time` in ms to timestamp in `lib.rs`, proto definition and `schema.sql`

v1.1.15
- ------

## # Highlights
- See those two new features in action in this [tutorial](https://substreams.streamingfast.io/tutorials/from-ethereum-address-to-sql)

## # Added
- Sink configs can now use protobuf annotations (aka Field Options) to determine how the field will be interpreted in substreams.yaml:
- `load_from_file` will put the content of the file directly in the field (string and bytes contents are supported).
- `zip_from_folder` will create a zip archive and put its content in the field (field type must be bytes).
    
    Example protobuf definition:
    
    Copy
    ```
    import "sf/substreams/v1/options.proto";
    message HostedPostgresDatabase {
      bytes schema = 1 [ (sf.substreams.v1.options).load_from_file = true ];
      bytes extra_config_files = 2 [ (sf.substreams.v1.options).zip_from_folder = true ];
    }
    ```
    
    Example manifest file:
    
    Copy
    ```
    [...]
    network: mainnet
    sink:
      module: main:db_out
      type: sf.substreams.sink.sql.v1.Service
      config:
        schema: "./schema.sql"
        wire_protocol_access: true
        postgraphile_frontend:
          enabled: true
        pgweb_frontend:
          enabled: true
    ```
- `substreams info` command now properly displays the content of sink configs, optionally writing the fields that were bundled from files to disk with `--output-sinkconfig-files-path=</some/path>`

## # Changed
- `substreams alpha init` renamed to `substreams init`. It now includes `db_out` module and `schema.sql` to support the substreams-sql-sink directly.
- The override feature has been overhauled. Users may now override an existing substreams by pointing to an override file in `run` or `gui` command. This override manifest will have a `deriveFrom` field which points to the original substreams which is to be overriden. This is useful to port a substreams to one network to another. Example of an override manifest:
  
  Copy
  ```
  deriveFrom: path/to/mainnet-substreams.spkg #this can also be a remote url
  package:
    name: "polygon-substreams"
    version: "100.0.0"
  network: polygon
  initialBlocks:
    module1: 17500000
  params:
    module1: "address=2a75ca72679cf1299936d6104d825c9654489058"
  ```
- The `substreams run` and `substreams gui` commands now determine the endpoint from the 'network' field in the manifest if no value is passed in the `--substreams-endpoint` flag.
- The endpoint for each network can be set by using an environment variable `SUBSTREAMS_ENDPOINTS_CONFIG_<network_name>`, ex: `SUBSTREAMS_ENDPOINTS_CONFIG_MAINNET=my-endpoint:443`
- The `substreams alpha init` has been moved to `substreams init`

## # Fixed
- fixed the `substreams gui` command to correctly compute the stop-block when given a relative value (ex: '-t +10')

v1.1.14
- ------

## # Bug fixes
- Fixed (bumped) substreams protobuf definitions that get embedded in `spkg` to match the new progress messages from v1.1.12.
- Regression fix: fixed a bug where negative start blocks would not be resolved correctly when using `substreams run` or `substreams gui`.
- In the request plan, the process previously panicked when errors related to block number validation occurred. Now the error will be returned to the client.

v1.1.13
- ------

## # Bug fixes
- If the initial block or start block is less than the first block in the chain, the substreams will now start from the first block in the chain. Previously, setting the initial block to a block before the first block in the chain would cause the substreams to hang.
- Fixed a bug where the substreams would fail if the start block was set to a future block. The substreams will now wait for the block to be produced before starting.

v1.1.12
- ------

## # Highlights
- Complete redesign of the progress messages:
- Tier2 internal stats are aggregated on Tier1 and sent out every 500ms (no more bursts)
- No need to collect events on client: a single message now represents the current state
- Message now includes list of running jobs and information about execution stages
- Performance metrics has been added to show which modules are executing slowly and where the time is spent (eth calls, store operations, etc.)

## # Upgrading client and server

> [!IMPORTANT] The client and servers will both need to be upgraded at the same time for the new progress messages to be parsed:
> 
> * The new Substreams servers will *NOT* send the old `modules` field as part of its `progress` message, only the new `running_jobs`, `modules_stats`, `stages`.
> * The new Substreams clients will *NOT* be able to decode the old progress information when connecting to older servers.

However, the actual data (and cursor) will work correctly between versions. Only incompatible progress information will be ignored.

## # CLI

### # Changed
- Bumped `substreams` and `substreams-ethereum` to latest in `substreams alpha init`.
- Improved error message when `<module_name>` is not received, previously this would lead to weird error message, now, if the input is likely a manifest, the error message will be super clear.

### # Fixed
- Fixed compilation errors when tracking some contracts when using `substreams alpha init`.

### # Added
- `substreams info` now takes an optional second parameter `<output-module>` to show how the substreams modules can be divided into stages
- Pack command: added `-c` flag to allow overriding of certain substreams.yaml values by passing in the path of a yaml file. example yaml contents:
  
  Copy
  ```
  package:
    name: my_custom_package_name
  network: arbitrum-one
  initialBlocks:
    module_name_1: 123123123
  params:
    mod1: "custom_parameter"
  ```

## # Backend

### # Removed
- Removed `Config.RequestStats`, stats are now always enabled.

v1.1.11
- ------

## # Fixes
- Added metering of live blocks

v1.1.10
- ------

## # Backend changes
- Fixed/Removed: jobs would hang when config parameter `StateBundleSize` was different from `SubrequestsSize`. The latter has been removed completely: Subrequests size will now always be aligned with bundle size.
- Auth: added support for *continuous authentication* via the grpc auth plugin (allowing cutoff triggered by the auth system).

## # CLI changes
- Fixed params handling in `gui` mode

v1.1.9
- -----

## # Backend changes
- Massive refactoring of the scheduler: prevent excessive splitting of jobs, grouping them into stages when they have the same dependencies. This should reduce the required number of `tier2` workers (2x to 3x, depending on the substreams).
- The `tier1` and `tier2` config have a new configuration `StateStoreDefaultTag`, will be appended to the `StateStoreURL` value to form the final state store URL, ex: `StateStoreURL="/data/states"` and `StateStoreDefaultTag="v2"` will make `/data/states/v2` the default state store location, while allowing users to provide a `X-Sf-Substreams-Cache-Tag` header (gated by auth module) to point to `/data/states/v1`, and so on.
- Authentication plugin `trust` can now specify an exclusive list of `allowed` headers (all lowercase), ex: `trust://?allowed=x-sf-user-id,x-sf-api-key-id,x-real-ip,x-sf-substreams-cache-tag`
- The `tier2` app no longer has customizable auth plugin (or any Modules), `trust` will always be used, so that `tier` can pass down its headers (e.g. `X-Sf-Substreams-Cache-Tag`). The `tier2` instances should not be accessible publicly.

## # GUI changes
- Color theme is now adapted to the terminal background (fixes readability on 'light' background)
- Provided parameters are now shown in the 'Request' tab.

## # CLI changes

### # Added
- `alpha init` command: replace `initialBlock` for generated manifest based on contract creation block.
- `alpha init` prompt Ethereum chain. Added: Mainnet, BNB, Polygon, Goerli, Mumbai.

### # Fixed
- `alpha init` reports better progress specially when performing ABI & creation block retrieval.
- `alpha init` command without contracts fixed Protogen command invocation.

v1.1.8
- -----

## # Backend changes

### # Added
- Max-subrequests can now be overridden by auth header `X-Sf-Substreams-Parallel-Jobs` (note: if your auth plugin is 'trust', make sure that you filter out this header from public access
- Request Stats logging. When enable it will log metrics associated to a Tier1 and Tier2 request
- On request, save "substreams.partial.spkg" file to the state cache for debugging purposes.
- Manifest reader can now read 'partial' spkg files (without protobuf and metadata) with an option.

### # Fixed
- Fixed a bug which caused "live" blocks to be sent while the stream previously received block(s) were historic.

## # CLI changes

### # Fixed
- In GUI, module output now shows fields with default values, i.e. `0`, `""`, `false`

v1.1.7 (<https://github.com/streamingfast/substreams/releases/tag/v1.1.7>)
- -------------------------------------------------------------------------

## # Highlights

Now using `plugin: buf.build/community/neoeinstein-prost-crate:v0.3.1` when generating the Protobuf Rust `mod.rs` which fixes the warning that remote plugins are deprecated.

Previously we were using `remote: buf.build/prost/plugins/crate:v0.3.1-1`. But remote plugins when using <https://buf.build> (which we use to generate the Protobuf) are now deprecated and will cease to function on July 10th, 2023.

The net effect of this is that if you don't update your Substreams CLI to `1.1.7`, on July 10th 2023 and after, the `substreams protogen` will not work anymore.

v1.1.6 (<https://github.com/streamingfast/substreams/releases/tag/v1.1.6>)
- -------------------------------------------------------------------------

## # Backend changes
- `substreams-tier1` and `substreams-tier2` are now standalone **Apps**, to be used as such by server implementations (*firehose-ethereum*, etc.)
- `substreams-tier1` now listens to [Connect](https://buf.build/blog/connect-a-better-grpc) protocol, enabling browser-based substreams clients
- **Authentication** has been overhauled to take advantage of <https://github.com/streamingfast/dauth>, allowing the use of a GRPC-based sidecar or reverse-proxy to provide authentication.
- **Metering** has been overhauled to take advantage of <https://github.com/streamingfast/dmetering> plugins, allowing the use of a GRPC sidecar or logs to expose usage metrics.
- The **tier2 logs** no longer show a `parent_trace_id`: the `trace_id` is now the same as tier1 jobs. Unique tier2 jobs can be distinguished by their `stage` and `segment`, corresponding to the `output_module_name` and `startblock:stopblock`

## # CLI changes
- The `substreams protogen` command now uses this Buf plugin <https://buf.build/community/neoeinstein-prost> to generate the Rust code for your Substreams definitions.
- The `substreams protogen` command no longer generate the `FILE_DESCRIPTOR_SET` constant which generates an unsued warning in Rust. We don't think nobody relied on having the `FILE_DESCRIPTOR_SET` constant generated, but if it's the case, you can provide your own `buf.gen.yaml` that will be used instead of the generated one when doing `substreams protogen`.
- Added `-H` flag on the `substreams run` command, to set HTTP Headers in the Substreams request.

## # Fixed
- Fixed generated `buf.gen.yaml` not being deleted when an error occurs while generating the Rust code.

[v1.1.5](https://github.com/streamingfast/substreams/releases/tag/v1.1.5)
- ------------------------------------------------------------------------

## # Highlights

This release fixes data determinism issues. This comes at a 20% performance cost but is necessary for integration with The Graph ecosystem.

### # Operators
- When upgrading a substreams server to this version, you should delete all existing module caches to benefit from deterministic output

## # Added
- Tier1 now records deterministic failures in wasm, "blacklists" identical requests for 10 minutes (by serving them the same InvalidArgument error) with a forced incremental backoff. This prevents accidental bad actors from hogging tier2 resources when their substreams cannot go passed a certain block.
- Tier1 now sends the ResolvedStartBlock, LinearHandoffBlock and MaxJobWorkers in SessionInit message for the client and gui to show
- Substreams CLI can now read manifests/spkg directly from an IPFS address (subgraph deployment or the spkg itself), using `ipfs://Qm...` notation

## # Fixed
- When talking to an updated server, the gui will not overflow on a negative start block, using the newly available resolvedStartBlock instead.
- When running in development mode with a start-block in the future on a cold cache, you would sometimes get invalid "updates" from the store passed down to your modules that depend on them. It did not impact the caches but caused invalid output.
- The WASM engine was incorrectly reusing memory, preventing deterministic output. It made things go faster, but at the cost of determinism. Memory is now reset between WASM executions on each block.
- The GUI no longer panics when an invalid output-module is given as argument

## # Changed
- Changed default WASM engine from `wasmtime` to `wazero`, use `SUBSTREAMS_WASM_RUNTIME=wasmtime` to revert to prior engine. Note that `wasmtime` will now run a lot slower than before because resetting the memory in `wasmtime` is more expensive than in `wazero`.
- Execution of modules is now done in parallel within a single instance, based on a tree of module dependencies.
- The `substreams gui` and `substreams run` now accept commas inside a `param` value. For example: `substreams run --param=p1=bar,baz,qux --param=p2=foo,baz`. However, you can no longer pass multiple parameters using an ENV variable, or a `.yaml` config file.

[v1.1.4](https://github.com/streamingfast/substreams/releases/tag/v1.1.4)
- ------------------------------------------------------------------------

## # HIGHLIGHTS
- Module hashing changed to fix cache reuse on substreams use imported modules
- Memory leak fixed on rpc-enabled servers
- GUI more responsive

## # Fixed
- BREAKING: The module hashing algorithm wrongfully changed the hash for imported modules, which made it impossible to leverage caches when composing new substreams off of imported ones.
- Operationally, if you want to keep your caches, you will need to copy or move the old hashes to the new ones.
- You can obtain the prior hashes for a given spkg with: `substreams info my.spkg`, using a prior release of the `substreams`
- With a more recent `substreams` release, you can obtain the new hashes with the same command.
- You can then `cp` or `mv` the caches for each module hash.
- You can also ignore this change. This will simply invalidate your cache.
- Fixed a memory leak where "PostJobHooks" were not always called. These are used to hook in rpc calls in Ethereum chain. They are now always called, even if no block has been processed (can be called with `nil` value for the clock)
- Jobs that fail deterministically (during WASM execution) on tier2 will fail faster, without retries from tier1.
- `substreams gui` command now handles params flag (it was ignored)
- Substeams GUI responsiveness improved significantly when handling large payloads

## # Added
- Added Tracing capabilities, using <https://github.com/streamingfast/sf-tracing> . See repository for details on how to enable.

## # Known issues
- If the cached substreams states are missing a 'full-kv' file in its sequence (not a normal scenario), requests will fail with `opening file: not found` <https://github.com/streamingfast/substreams/issues/222>

[v1.1.3](https://github.com/streamingfast/substreams/releases/tag/v1.1.3)
- ------------------------------------------------------------------------

## # Highlights

This release contains fixes for race conditions that happen when multiple request tries to sync the same range using the same `.spkg`. Those fixes will avoid weird state error at the cost of duplicating work in some circumstances. A future refactor of the Substreams engine scheduler will come later to fix those inefficiencies.

Operators, please read the operators section for upgrade instructions.

### # Operators

> **Note** This upgrade procedure is applies if your Substreams deployment topology includes both `tier1` and `tier2` processes. If you have defined somewhere the config value `substreams-tier2: true`, then this applies to you, otherwise, if you can ignore the upgrade procedure.

This release includes a small change in the internal RPC layer between `tier1` processes and `tier2` processes. This change requires an ordered upgrade of the processes to avoid errors.

The components should be deployed in this order:

2. Deploy and roll out `tier1` processes first
5. Deploy and roll out `tier2` processes in second

If you upgrade in the wrong order or if somehow `tier2` processes start using the new protocol without `tier1` being aware, user will end up with backend error(s) saying that some partial file are not found. Those will be resolved only when `tier1` processes have been upgraded successfully.

## # Fixed
- Fixed a race when multiple Substreams request execute on the same `.spkg`, it was causing races between the two executors.
- GUI: fixed an issue which would slow down message consumption when progress page was shown in ascii art "bars" mode
- GUI: fixed the display of blocks per second to represent actual blocks, not messages count

## # Changed
- [`binary`]: Commands `substreams <...>` that fails now correctly return an exit code 1.
- [`library`]: The `manifest.NewReader` signature changed and will now return a `*Reader, error` (previously `*Reader`).

## # Added
- [`library`]: The `manifest.Reader` gained the ability to infer the path if provided with input `""` based on the current working directory.
- [`library`]: The `manifest.Reader` gained the ability to infer the path if provided with input that is a directory.

[v1.1.2](https://github.com/streamingfast/substreams/releases/tag/v1.1.2)
- ------------------------------------------------------------------------

## # Highlights

This release contains bug fixes and speed/scaling improvements around the Substreams engine. It also contains few small enhancements for `substreams gui`.

This release contains an important bug that could have generated corrupted `store` state files. This is important for developers and operators.

### # Sinkers & Developers

The `store` state files will be fully deleted on the Substreams server to start fresh again. The impact for you as a developer is that Substreams that were fully synced will now need to re-generate from initial block the store's state. So you might see long delays before getting a new block data while the Substreams engine is re-computing the `store` states from scratch.

## # Operators

You need to clear the state store and remove all the files that are stored under `substreams-state-store-url` flag. You can also make it point to a brand new folder and delete the old one after the rollout.

## # Fixed
- Fix a bug where not all extra modules would be sent back on debug mode
- Fixed a bug in tier1 that could result in corrupted state files when getting close to chain HEAD
- Fixed some performance and stalling issues when using GCS for blocks
- Fixed storage logs not being shown properly
- GUI: Fixed panic race condition
- GUI: Cosmetic changes

## # Added
- GUI: Added traceID

[v1.1.1](https://github.com/streamingfast/substreams/releases/tag/v1.1.1)
- ------------------------------------------------------------------------

## # Highlights

This release introduces a new RPC protocol and the old one has been removed. The new RPC protocol is in a new Protobuf package `sf.substreams.rpc.v2` and it drastically changes how chain re-orgs are signaled to the user. Here the highlights of this release:
- Getting rid of `undo` payload during re-org
- `substreams gui` Improvements
- Substreams integration testing
- Substreams Protobuf definitions updated

### # Getting rid of `undo` payload during re-org

Previously, the GRPC endpoint `sf.substreams.v1.Stream/Blocks` would send a payload with the corresponding "step", NEW or UNDO.

Unfortunately, this led to some cases where the payload could not be deterministically generated for old blocks that had been forked out, resulting in a stalling request, a failure, or in some worst cases, incomplete data.

The new design, under `sf.substreams.rpc.v2.Stream/Blocks`, takes care of these situations by removing the 'step' component and using these two messages types:
- `sf.substreams.rpc.v2.BlockScopedData` when chain progresses, with the payload
- `sf.substreams.rpc.v2.BlockUndoSignal` during a reorg, with the last valid block number + block hash

The client now has the burden of keeping the necessary means of performing the undo actions (ex: a map of previous values for each block). The BlockScopedData message now includes the `final_block_height` to let you know when this "undo data" can be discarded.

With these changes, a substreams server can even handle a cursor for a block that it has never seen, provided that it is a valid cursor, by signaling the client to revert up to the last known final block, trading efficiency for resilience in these extreme cases.

## # `substreams gui` Improvements
- Added key 'f' shortcut for changing display encoding of bytes value (hex, pruned string, base64)
- Added `jq` search mode (hit `/` twice). Filters the output with the `jq` expression, and applies the search to match all blocks.
- Added search history (with `up`/`down`), similar to `less`.
- Running a search now applies it to all blocks, and highlights the matching ones in the blocks bar (in red).
- Added `O` and `P`, to jump to prev/next block with matching search results.
- Added module search with `m`, to quickly switch from module to module.

### # Substreams integration testing

Added a basic Substreams testing framework that validates module outputs against expected values. The testing framework currently runs on `substreams run` command, where you can specify the following flags:
- `test-file` Points to a file that contains your test specs
- `test-verbose` Enables verbose mode while testing.

The test file, specifies the expected output for a given substreams module at a given block.

### # Substreams Protobuf definitions updated

We changed the Substreams Protobuf definitions making a major overhaul of the RPC communication. This is a **breaking change** for those consuming Substreams through gRPC.

> **Note** The is no breaking changes for Substreams developers regarding your Rust code, Substreams manifest and Substreams package.
- Removed the `Request` and `Response` messages (and related) from `sf.substreams.v1`, they have been moved to `sf.substreams.rpc.v2`. You will need to update your usage if you were consuming Substreams through gRPC.
- The new `Request` excludes fields and usages that were already deprecated, like using multiple `module_outputs`.
- The `Response` now contains a single module output
- In `development` mode, the additional modules output can be inspected under `debug_map_outputs` and `debug_store_outputs`.
- *Separating Tier1 vs Tier2 gRPC protocol (for Substreams server operators)**

Now that the `Blocks` request has been moved from `sf.substreams.v1` to `sf.substreams.rpc.v2`, the communication between a substreams instance acting as tier1 and a tier2 instance that performs the background processing has also been reworked, and put under `sf.substreams.internal.v2.Stream/ProcessRange`. It has also been stripped of parameters that were not used for that level of communication (ex: `cursor`, `logs`...)

## # Fixed
- The `final_blocks_only: true` on the `Request` was not honored on the server. It now correctly sends only blocks that are final/irreversible (according to Firehose rules).
- Prevent substreams panic when requested module has unknown value for "type"

## # Added
- The `substreams run` command now has flag `--final-blocks-only`

[1.0.3](https://github.com/streamingfast/substreams/releases/tag/v1.0.3)
- -----------------------------------------------------------------------

This should be the last release before a breaking change in the API and handling of the reorgs and UNDO messages.

## # Highlights
- Added support for resolving a negative start-block on server
- CHANGED: The `run` command now resolves a start-block=-1 from the head of the chain (as supported by the servers now). Prior to this change, the `-1` value meant the 'initialBlock' of the requested module. The empty string is now used for this purpose,
- GUI: Added support for search, similar to `less`, with `/`.
- GUI: Search and output offset is conserved when switching module/block number in the "Output" tab.
- Library: protobuf message descriptors now exposed in the `manifest/` package. This is something useful to any sink that would need to interpret the protobuf messages inside a Package.
- Added support for resolving a negative start-block on server (also added to run command)
- The `run` and `gui` command no longer resolve a `start-block=-1` to the 'initialBlock' of the requested module. To get this behavior, simply assign an empty string value to the flag `start-block` instead.
- Added support for search within the Substreams gui `output` view. Usage of search within `output` behaves similar to the `less` command, and can be toggled with "/".

[1.0.2](https://github.com/streamingfast/substreams/releases/tag/v1.0.2)
- -----------------------------------------------------------------------
- Release was retracted because it contained the refactoring expected for 1.1.0 by mistake, check <https://github.com/streamingfast/substreams/releases/tag/v1.0.3> instead.

[1.0.1](https://github.com/streamingfast/substreams/releases/tag/v1.0.1)
- -----------------------------------------------------------------------

## # Fixed
- Fixed "undo" messages incorrectly contained too many module outputs (all modules, with some duplicates).
- Fixed status bar message cutoff bug
- Fixed `substreams run` when `manifest` contains unknown attributes
- Fixed bubble tea program error when existing the `run` command

[1.0.0](https://github.com/streamingfast/substreams/releases/tag/v1.0.0)
- -----------------------------------------------------------------------

## # Highlights
- Added command `substreams gui`, providing a terminal-based GUI to inspect the streamed data. Also adds `--replay` support, to save a stream to `replay.log` and load it back in the UI later. You can use it as you would `substreams run`. Feedback welcome.
- Modified command `substreams protogen`, defaulting to generating the `mod.rs` file alongside the rust bindings. Also added `--generate-mod-rs` flag to toggle `mod.rs` generation.
- Added support for module parameterization. Defined in the manifest as:

Copy
```
module:
  name: my_module
  inputs:
    params: string
  ...
params:
  my_module: "0x123123"
  "imported:module": override value from imported module
```

and on the command-line as:
- `substreams run -p module=value -p "module2=other value" ...`

Servers need to be updated for packages to be able to be consumed this way.

This change keeps backwards compatibility. Old Substreams Packages will still work the same, with no changes to module hashes.

## # Added
- Added support for `{version}` template in `--output-file` flag value on `substreams pack`.
- Added fuel limit to wasm execution as a server-side option, preventing wasm process from running forever.
- Added 'Network' and 'Sink{Type, Module, Config}' fields in the manifest and protobuf definition for future bundling of substreams sink definitions within a substreams package.

[0.2.0](https://github.com/streamingfast/substreams/releases/tag/v0.2.0)
- -----------------------------------------------------------------------

## # Highlights
- Improved execution speed and module loading speed by bumping to WASM Time to version 4.0.
- Improved developer experience on the CLI by making the `<manifest>` argument optional.
  
  The CLI when `<manifest>` argument is not provided will now look in the current directory for a `substreams.yaml` file and is going to use it if present. So if you are in your Substreams project and your file is named `substreams.yaml`, you can simply do `substreams pack`, `substreams protogen`, etc.
  
  Moreover, we added to possibility to pass a directory containing a `substreams.yaml` directly so `substreams pack path/to/project` would work as long as `path/to/project` contains a file named `substreams.yaml`.
- Fixed a bug that was preventing production mode to complete properly when using a bounded block range.
- Improved overall stability of the Substreams engine.

### # Operators Notes
- **Breaking** Config values `substreams-stores-save-interval` and `substreams-output-cache-save-interval` have been merged together into `substreams-cache-save-interval` in the `firehose-<chain>` repositories. Refer to chain specific `firehose-<chain>` repository for further details.

## # Added
- The `<manifest>` can point to a directory that contains a `substreams.yaml` file instead of having to point to the file directly.
- The `<manifest>` parameter is now optional in all commands requiring it.

## # Fixed
- Fixed valuetype mismatch for stores
- Fixed production mode not completing when block range was specified
- Fixed tier1 crashing due to missing context canceled check.
- Fixed some code paths where locking could have happened due to incorrect checking of context cancellation.
- Request validation for blockchain's input type is now made only against the requested module it's transitive dependencies.

## # Updated
- Updated WASM Time library to 4.0.0 leading to improved execution speed.

## # Changed
- Remove distinction between `output-save-interval` and `store-save-interval`.
- `substreams init` has been moved under `substreams alpha init` as this is a feature included by mistake in latest release that should not have been displayed in the main list of commands.
- `substreams codegen` has been moved under `substreams alpha codegen` as this is a feature included by mistake in latest release that should not have been displayed in the main list of commands.

[0.1.0](https://github.com/streamingfast/substreams/releases/tag/v0.1.0)
- -----------------------------------------------------------------------

This upcoming release is going to bring significant changes on how Substreams are developed, consumed and speed of execution. Note that there is **no** breaking changes related to your Substreams' Rust code, only breaking changes will be about how Substreams are run and available features/flags.

Here the highlights of elements that will change in next release:
- [Production vs Development Mode](/reference-and-specs/change-log#production-vs-development-mode)
- [Single Output Module](/reference-and-specs/change-log#single-module-output)
- [Output Module must be of type `map`](/reference-and-specs/change-log#output-module-must-be-of-type-map)
- [`InitialSnapshots` is now a `development` mode feature only](/reference-and-specs/change-log#initialsnapshots-is-now-a-development-mode-feature-only)
- [Enhanced Parallel Execution](/reference-and-specs/change-log#enhanced-parallel-execution)

In this rest of this post, we are going to go through each of them in greater details and the implications they have for you. Full changelog is available after.

> **Warning** Operators, refer to [Operators Notes](/reference-and-specs/change-log#operators-notes) section for specific instructions of deploying this new version.

## # Production vs development mode

We introduce an execution mode when running Substreams, either `production` mode or `development` mode. The execution mode impacts how the Substreams get executed, specifically:
- The time to first byte
- The module logs and outputs sent back to the client
- How parallel execution is applied through the requested range

The difference between the modes are:
- In `development` mode, the client will receive all the logs of the executed `modules`. In `production` mode, logs are not available at all.
- In `development` mode, module's are always re-executed from request's start block meaning now that logs will always be visible to the user. In `production` mode, if a module's output is found in cache, module execution is skipped completely and data is returned directly.
- In `development` mode, only backward parallel execution can be effective. In `production` mode, both backward parallel execution and forward parallel execution can be effective. See [Enhanced parallel execution](/reference-and-specs/change-log#enhanced-parallel-execution) section for further details about parallel execution.
- In `development` mode, every module's output is returned back in the response but only root module is displayed by default in `substreams` CLI (configurable via a flag). In `production` mode, only root module's output is returned.
- In `development` mode, you may request specific `store` snapshot that are in the execution tree via the `substreams` CLI `--debug-modules-initial-snapshots` flag. In `production` mode, this feature is not available.

The execution mode is specified at that gRPC request level and is the default mode is `development`. The `substreams` CLI tool being a development tool foremost, we do not expect people to activate production mode (`-p`) when using it outside for maybe testing purposes.

If today's you have `sink` code making the gRPC request yourself and are using that for production consumption, ensure that field `production_mode` in your Substreams request is set to `true`. StreamingFast provided `sink` like [substreams-sink-postgres](https://github.com/streamingfast/substreams-sink-postgres), [substreams-sink-files](https://github.com/streamingfast/substreams-sink-files) and others have already been updated to use `production_mode` by default.

Final note, we recommend to run the production mode against a compiled `.spkg` file that should ideally be released and versioned. This is to ensure stable modules' hashes and leverage cached output properly.

## # Single module output

We now only support 1 output module when running a Substreams, while prior this release, it was possible to have multiple ones.
- Only a single module can now be requested, previous version allowed to request N modules.
- Only `map` module can now be requested, previous version allowed `map` and `store` to be requested.
- `InitialSnapshots` is now forbidden in `production` mode and still allowed in `development` mode.
- In `development` mode, the server sends back output for all executed modules (by default the CLI displays only requested module's output).

> **Note** We added `output_module` to the Substreams request and kept `output_modules` to remain backwards compatible for a while. If an `output_module` is specified we will honor that module. If not we will check `output_modules` to ensure there is only 1 output module. In a future release, we are going to remove `output_modules` altogether.

With the introduction of `development` vs `production` mode, we added a change in behavior to reduce frictions this changes has on debugging. Indeed, in `development` mode, all executed modules's output will be sent be to the user. This includes the requested output module as well as all its dependencies. The `substreams` CLI has been adjusted to show only the output of the requested output module by default. The new `substreams` CLI flag `-debug-modules-output` can be used to control which modules' output is actually displayed by the CLI.

> **Migration Path** If you are currently requesting more than one module, refactor your Substreams code so that a single `map` module aggregates all the required information from your different dependencies in one output.

## # Output module must be of type `map`

It is now forbidden to request a `store` module as the output module of the Substreams request, the requested output module must now be of kind `map`. Different factors have motivated this change:
- Recently we have seen incorrect usage of `store` module. A `store` module was not intended to be used as a persistent long term storage, `store` modules were conceived as a place to aggregate data for later steps in computation. Using it as a persistent storage make the store unmanageable.
- We had always expected users to consume a `map` module which would return data formatted according to a final `sink` spec which will then permanently store the extracted data. We never envisioned `store` to act as long term storage.
- Forward parallel execution does not support a `store` as its last step.

> **Migration Path** If you are currently using a `store` module as your output store. You will need to create a `map` module that will have as input the `deltas` of said `store` module, and return the deltas.

### # Examples

Let's assume a Substreams with these dependencies: `[block] --> [map_pools] --> [store_pools] --> [map_transfers]`
- Running `substreams run substreams.yaml map_transfers` will only print the outputs and logs from the `map_transfers` module.
- Running `substreams run substreams.yaml map_transfers --debug-modules-output=map_pools,map_transfers,store_pools` will print the outputs of those 3 modules.

## # `InitialSnapshots` is now a `development` mode feature only

Now that a `store` cannot be requested as the output module, the `InitialSnapshots` did not make sense anymore to be available. Moreover, we have seen people using it to retrieve the initial state and then continue syncing. While it's a fair use case, we always wanted people to perform the synchronization using the streaming primitive and not by using `store` as long term storage.

However, the `InitialSnapshots` is a useful tool for debugging what a store contains at a given block. So we decided to keep it in `development` mode only where you can request the snapshot of a `store` module when doing your request. In the Substreams' request/response, `initial_store_snapshot_for_modules` has been renamed to `debug_initial_store_snapshot_for_modules`, `snapshot_data` to `debug_snapshot_data` and `snapshot_complete` to `debug_snapshot_complete`.

> **Migration Path** If you were relying on `InitialSnapshots` feature in production. You will need to create a `map` module that will have as input the `deltas` of said `store` module, and then synchronize the full state on the consuming side.

### # Examples

Let's assume a Substreams with these dependencies: `[block] --> [map_pools] --> [store_pools] --> [map_transfers]`
- Running `substreams run substreams.yaml map_transfers -s 1000 -t +5 --debug-modules-initial-snapshot=store_pools` will print all the entries in store\_pools at block 999, then continue with outputs and logs from `map_transfers` in blocks 1000 to 1004.

## # Enhanced parallel execution

There are 2 ways parallel execution can happen either backward or forward.

Backward parallel execution consists of executing in parallel block ranges from the module's start block up to the start block of the request. If the start block of the request matches module's start block, there is no backward parallel execution to perform. Also, this is happening only for dependencies of type `store` which means that if you depends only on other `map` modules, no backward parallel execution happens.

Forward parallel execution consists of executing in parallel block ranges from the start block of the request up to last known final block (a.k.a the irreversible block) or the stop block of the request, depending on which is smaller. Forward parallel execution significantly improves the performance of the Substreams as we execute your module in advanced through the chain history in parallel. What we stream you back is the cached output of your module's execution which means essentially that we stream back to you data written in flat files. This gives a major performance boost because in almost all cases, the data will be already for you to consume.

Forward parallel execution happens only in `production` mode is always disabled when in `development` mode. Moreover, since we read back data from cache, it means that logs of your modules will never be accessible as we do not store them.

Backward parallel execution still occurs in `development` and `production` mode. The diagram below gives details about when parallel execution happen.

You can see that in `production` mode, parallel execution happens before the Substreams request range as well as within the requested range. While in `development` mode, we can see that parallel execution happens only before the Substreams request range, so between module's start block and start block of requested range (backward parallel execution only).

## # Operators Notes

The state output format for `map` and `store` modules has changed internally to be more compact in Protobuf format. When deploying this new version, previous existing state files should be deleted or deployment updated to point to a new store location. The state output store is defined by the flag `--substreams-state-store-url` flag parameter on chain specific binary (i.e. `fireeth`).

## # Library
- Added `production_mode` to Substreams Request
- Added `output_module` to Substreams Request

## # CLI
- Fixed `Ctrl-C` not working directly when in TUI mode.
- Added `Trace ID` printing once available.
- Added command `substreams tools analytics store-stats` to get statistic for a given store.
- Added `--debug-modules-output` (comma-separated module names) (unavailable in `production` mode).
- **Breaking** Renamed flag `--initial-snapshots` to `--debug-modules-initial-snapshots` (comma-separated module names) (unavailable in `production` mode).

[0.0.21](https://github.com/streamingfast/substreams/releases/tag/v0.0.21)
- -------------------------------------------------------------------------
- Moved Rust modules to `github.com/streamingfast/substreams-rs`

## # Library
- Gained significant execution time improvement when saving and loading stores, during the squashing process by leveraging [vtprotobuf](https://github.com/planetscale/vtprotobuf)
- Added XDS support for tier 2s
- Added intrinsic support for type `bigdecimal`, will deprecate `bigfloat`
- Significant improvements in code-coverage and full integration tests.

## # CLI
- Added `substreams tools proxy <package>` subcommand to allow calling substreams with a pre-defined package easily from a web browser using bufbuild/connect-web
- Lowered GRPC client keep alive frequency, to prevent "Too Many Pings" disconnection issue.
- Added a fast failure when attempting to connect to an unreachable substreams endpoint.
- CLI is now able to read `.spkg` from `gs://`, `s3://` and `az://` URLs, the URL format must be supported by our [dstore](https://github.com/streamingfast/dstore) library).
- Command `substreams pack` is now restricted to local manifest file.
- Added command `substreams tools module` to introspect a store state in storage.
- Made changes to allow for `substreams` CLI to run on Windows OS (thanks @robinbernon).
- Added flag `--output-file <template>` to `substreams pack` command to control where the `.skpg` is written, `{manifestDir}` and `{spkgDefaultName}` can be used in the `template` value where `{manifestDir}` resolves to manifest's directory and `{spkgDefaultName}` is the pre-computed default name in the form `<name>-<version>` where `<name>` is the manifest's "package.name" value (`_` values in the name are replaced by `-`) and `<version>` is `package.version` value.
- Fixed relative path not resolved correctly against manifest's location in `protobuf.files` list.
- Fixed relative path not resolved correctly against manifest's location in `binaries` list.
- `substreams protogen <package> --output-path <path>` flag is now relative to `<package>` if `<package>` is a local manifest file ending with `.yaml`.
- Endpoint's port is now validated otherwise when unspecified, it creates an infinite 'Connecting...' message that will never resolves.

[0.0.20](https://github.com/streamingfast/substreams/releases/tag/v0.0.20)
- -------------------------------------------------------------------------

## # CLI
- Fixed error when importing `http/https` `.spkg` files in `imports` section.

[0.0.19](https://github.com/streamingfast/substreams/releases/tag/v0.0.19)
- -------------------------------------------------------------------------
- *New updatePolicy** `append`, allows one to build a store that concatenates values and supports parallelism. This affects the server, the manifest format (additive only), the substreams crate and the generated code therein.

## # Rust API
- Store APIs methods now accept `key` of type `AsRef<str>` which means for example that both `String` an `&str` are accepted as inputs in:
- `StoreSet::set`
- `StoreSet::set_many`
- `StoreSet::set_if_not_exists`
- `StoreSet::set_if_not_exists_many`
- `StoreAddInt64::add`
- `StoreAddInt64::add_many`
- `StoreAddFloat64::add`
- `StoreAddFloat64::add_many`
- `StoreAddBigFloat::add`
- `StoreAddBigFloat::add_many`
- `StoreAddBigInt::add`
- `StoreAddBigInt::add_many`
- `StoreMaxInt64::max`
- `StoreMaxFloat64::max`
- `StoreMaxBigInt::max`
- `StoreMaxBigFloat::max`
- `StoreMinInt64::min`
- `StoreMinFloat64::min`
- `StoreMinBigInt::min`
- `StoreMinBigFloat::min`
- `StoreAppend::append`
- `StoreAppend::append_bytes`
- `StoreGet::get_at`
- `StoreGet::get_last`
- `StoreGet::get_first`
- Low-level state methods now accept `key` of type `AsRef<str>` which means for example that both `String` an `&str` are accepted as inputs in:
- `state::get_at`
- `state::get_last`
- `state::get_first`
- `state::set`
- `state::set_if_not_exists`
- `state::append`
- `state::delete_prefix`
- `state::add_bigint`
- `state::add_int64`
- `state::add_float64`
- `state::add_bigfloat`
- `state::set_min_int64`
- `state::set_min_bigint`
- `state::set_min_float64`
- `state::set_min_bigfloat`
- `state::set_max_int64`
- `state::set_max_bigint`
- `state::set_max_float64`
- `state::set_max_bigfloat`
- Bumped `prost` (and related dependencies) to `^0.11.0`

## # CLI
- Environment variables are now accepted in manifest's `imports` list.
- Environment variables are now accepted in manifest's `protobuf.importPaths` list.
- Fixed relative path not resolved correctly against manifest's location in `imports` list.
- Changed the output modes: `module-*` modes are gone and become the format for `jsonl` and `json`. This means all printed outputs are wrapped to provide the module name, and other metadata.
- Added `--initial-snapshots` (or `-i`) to the `run` command, which will dump the stores specified as output modules.
- Added color for `ui` output mode under a tty.
- Added some request validation on both client and server (validate that output modules are present in the modules graph)

## # Service
- Added support to serve the initial snapshot

[v0.0.13](https://github.com/streamingfast/substreams/releases/tag/v0.0.13)
- --------------------------------------------------------------------------

## # CLI
- Changed `substreams manifest info` -> `substreams info`
- Changed `substreams manifest graph` -> `substreams graph`
- Updated usage

## # Service
- Multiple fixes to boundaries

[v0.0.12](https://github.com/streamingfast/substreams/releases/tag/v0.0.12)
- --------------------------------------------------------------------------

## # `substreams` server
- Various bug fixes around store and parallel execution.

## # `substreams` CLI
- Fix null pointer exception at the end of CLI run in some cases.
- Do log last error when the CLI exit with an error has the error is already printed to the user and it creates a weird behavior.

[v0.0.11](https://github.com/streamingfast/substreams/releases/tag/v0.0.11)
- --------------------------------------------------------------------------

## # `substreams` Docker
- Ensure arguments can be passed to Docker built image.

[v0.0.10-beta](https://github.com/streamingfast/substreams/releases/tag/v0.0.10-beta)
- ------------------------------------------------------------------------------------

## # `substreams` server
- Various bug fixes around store and parallel execution.
- Fixed logs being repeated on module with inputs that was receiving nothing.

[v0.0.9-beta](https://github.com/streamingfast/substreams/releases/tag/v0.0.9-beta)
- ----------------------------------------------------------------------------------

## # `substreams` crate
- Added `substreams::hex` wrapper around hex\_literal::hex macro

## # `substreams` CLI
- Added `substreams run -o ui|json|jsonl|module-json|module-jsonl`.

## # Server
- Fixed a whole bunch of issues, in parallel processing. More stable caching. See chain-specific releases.

[v0.0.8-beta](https://github.com/streamingfast/substreams/releases/tag/v0.0.8-beta)
- ----------------------------------------------------------------------------------
- Fixed `substreams` crate usage from tagged version published on crates.io.

[v0.0.7-beta](https://github.com/streamingfast/substreams/releases/tag/v0.0.7-beta)
- ----------------------------------------------------------------------------------
- Changed `startBlock` to `initialBlock` in substreams.yaml [manifests](https://github.com/streamingfast/substreams/blob/develop/docs/release-notes/docs/reference-and-specs/manifests.md#modules-.initialblock).
- `code:` is now defined in the `binaries` section of the manifest, instead of in each module. A module can select which binary with the `binary:` field on the Module definition.
- Added `substreams inspect ./substreams.yaml` or `inspect some.spkg` to see what's inside. Requires `protoc` to be installed (which you should have anyway).
- Added command `substreams protogen` that writes a temporary `buf.gen.yaml` and generates Rust structs based on the contents of the provided manifest or package.
- Added `substreams::handlers` macros to reduce boilerplate when create substream modules.
  
  `substreams::handlers::map` is used for the handlers corresponding to modules of type `map`. Modules of type `map` should return a `Result` where the error is of type `Error`
  
  Copy
  ```
  /// Map module example
  #[substreams::handlers::map]
  pub fn map_module_func(blk: eth::Block) -> Result<erc721::Transfers, Error> {
       ...
  }
  ```
  
  `substreams::handlers::store` is used for the handlers corresponding to modules of type `store`. Modules of type `store` should have no return value.
  
  Copy
  ```
  /// Map module example
  #[substreams::handlers::store]
  pub fn store_module(transfers: erc721::Transfers, s: store::StoreAddInt64, pairs: store::StoreGet, tokens: store::StoreGet) {
        ...
  }
  ```

[v0.0.6-beta](https://github.com/streamingfast/substreams/releases/tag/v0.0.6-beta)
- ----------------------------------------------------------------------------------
- Implemented [packages (see docs)](https://github.com/streamingfast/substreams/blob/develop/docs/release-notes/docs/reference-and-specs/packages.md).
- Added `substreams::Hex` wrapper type to more easily deal with printing and encoding bytes to hexadecimal string.
- Added `substreams::log::info!(...)` and `substreams::log::debug!(...)` supporting formatting arguments (acts like `println!()` macro).
- Added new field `logs_truncated` that can be used to determined if logs were truncated.
- Augmented logs truncation limit to 128 KiB per module per block.
- Updated `substreams run` to properly report module progress error.
- When a module WASM execution error out, progress with failure logs is now returned before closing the substreams connection.
- The API token is not passed anymore if the connection is using plain text option `--plaintext`.
- The `-c` (or `--compact-output`) can be used to print JSON as a single compact line.
- The `--stop-block` flag on `substream run` can be defined as `+1000` to stream from start block + 1000.

[v0.0.5-beta3](https://github.com/streamingfast/substreams/releases/tag/v0.0.5-beta3)
- ------------------------------------------------------------------------------------
- Added Dockerfile support.

[v0.0.5-beta2](https://github.com/streamingfast/substreams/releases/tag/v0.0.5-beta2)
- ------------------------------------------------------------------------------------

## # Client
- Improved defaults for `--proto-path` and `--proto`, using globs.
- WASM file paths in substreams.yaml manifests now resolve relative to the location of the yaml file.
- Added `substreams manifest package` to create .pb packages to simplify querying using other languages. See the python example.
- Added `substreams manifest graph` to show the Mermaid graph alone.
- Improved mermaid graph layout.
- Removed native Go code support for now.

## # Server
- Always writes store snapshots, each 10,000 blocks.
- A few tools to manage partial snapshots under `substreams tools`

[v0.0.5-beta](https://github.com/streamingfast/substreams/releases/tag/v0.0.5-beta)
- ----------------------------------------------------------------------------------

First chain-agnostic release. THIS IS BETA SOFTWARE. USE AT YOUR OWN RISK. WE PROVIDE NO BACKWARDS COMPATIBILITY GUARANTEES FOR THIS RELEASE.

See <https://github.com/streamingfast/substreams> for usage docs..
- Removed `local` command. See README.md for instructions on how to run locally now. Build `sfeth` from source for now.
- Changed the `remote` command to `run`.
- Changed `run` command's `--substreams-api-key-envvar` flag to `--substreams-api-token-envvar`, and its default value is changed from `SUBSTREAMS_API_KEY` to `SUBSTREAMS_API_TOKEN`. See README.md to learn how to obtain such tokens.

[PreviousGlossary](/reference-and-specs/glossary)[NextFAQ](/reference-and-specs/faq)

Last updated 13 days ago

---

## Substreams:Stream | Substreams
Source: https://docs.substreams.dev/documentation/consume/stream

[PreviousSQL Sink](/documentation/consume/sql/sql-sink)[NextJavaScript](/documentation/consume/stream/javascript)

Last updated 10 months ago

---

## Local Service | Substreams
Source: https://docs.substreams.dev/documentation/consume/sql/deployable-services/local-service

In you want to manage your own infrastructure, you can use still the deployable services, but locally. This essetially means using the `substreams alpha service` command pointing to a local Docker installation. The following tutorial teaches you how to use the Substreams:SQL deployable service locally.

## # Tutorial

In this tutorial, you will:

1. Generate a simple Substreams that extract all events from the Cryptopunks smart contract on Ethereum.
2. Feed your data into a local PostgreSQL database in a Docker-based development environment.
3. Develop and apply SQL transformations with [dbt models](https://docs.getdbt.com/docs/build/models).
4. Go from a local Substreams:SQL environment to a shared remote development environment.
5. Create a production `.spkg` package and test it locally
6. Deploy your `.spkg` to a production environment that fills a PostgreSQL database from your Substreams and applies dbt transformations automatically.

### # Generate a Substreams project from the Cryptopunks ABI
- The cryptopunks address on mainnet is `0xb47e3cd837ddf8e4c57f05d70ab865de6e193bbb`
- Use the `substreams init` command to fetch the ABI from etherscan and scaffold a Substreams project:

Copy
```
substreams init
```

Fill the requested information (name: `cryptopunks`, protocol: `ethereum`, chain: `mainnet`, contract: `b47e3cd837ddf8e4c57f05d70ab865de6e193bbb`)

Copy
```
Project name (lowercase, numbers, undescores): cryptopunks
Protocol: Ethereum
Ethereum chain: Mainnet
✔ Contract address to track: b47e3cd837ddf8e4c57f05d70ab865de6e193bbb
✔ Would you like to track another contract? (Leave empty if not): █
Would you like to track another contract? (Leave empty if not):
Retrieving Ethereum Mainnet contract information (ABI & creation block)
Fetched contract ABI for b47e3cd837ddf8e4c57f05d70ab865de6e193bbb
Fetched initial block 3914495 for b47e3cd837ddf8e4c57f05d70ab865de6e193bbb (lowest 3914495)
Generating ABI Event models for
  Generating ABI Events for Assign (to,punkIndex)
  Generating ABI Events for PunkBidEntered (punkIndex,value,fromAddress)
  Generating ABI Events for PunkBidWithdrawn (punkIndex,value,fromAddress)
  Generating ABI Events for PunkBought (punkIndex,value,fromAddress,toAddress)
  Generating ABI Events for PunkNoLongerForSale (punkIndex)
  Generating ABI Events for PunkOffered (punkIndex,minValue,toAddress)
  Generating ABI Events for PunkTransfer (from,to,punkIndex)
  Generating ABI Events for Transfer (from,to,value)
Writing project files
Generating Protobuf Rust code
Project "cryptopunks" initialized at "/Users/stepd/repos"
Run 'make build' to build the wasm code.
The following substreams.yaml files have been created with different sink targets:
- substreams.yaml: no sink target
- substreams.sql.yaml: PostgreSQL sink
- substreams.clickhouse.yaml: Clickhouse sink
- substreams.subgraph.yaml: Sink into Substreams-based subgraph
```
- See the list of events that have been identified above. By default, each event type is mapped to its own table. This happens in the `map_events()` function inside `src/lib.rs` and the SQL schema is available in `schema.sql`.
- Build the rust code:

Copy
```
make build
```

You should see:

Copy
```
cargo build --target wasm32-unknown-unknown --release
   Compiling proc-macro2 v1.0.69
   Compiling unicode-ident v1.0.12
   Compiling syn v1.0.109
   ...
   Compiling cryptopunks v0.0.1 (/Users/stepd/repos/cryptopunks)
    Finished release [optimized] target(s) in 30.71s
```
### # Start feeding a local database using 'substreams alpha service' and Docker

From another window:

Copy
```
SUBSTREAMS_API_TOKEN=(...) substreams alpha service serve
```

Back to your substreams project:
- Deploy your substreams locally to start putting data in your database:

Copy
```
substreams alpha service deploy substreams.sql.yaml
```
- *Tip:** A new PostgreSQL container will be created at port `5432`. The deployment will fail if there is another Docker container using that port.
- *Tip:** You can also use `substreams service deploy substreams.clickhouse.yaml` to use the Clickhouse engine instead of PostgreSQL. There is no postgraphile or pgweb in that case, you will need a tool like DataGrip to see the data.

You should see:

Copy
```
Deploying... (creating services, please wait)
Deployed substreams sink "7590fdbf":
  Status: STOPPED
Running your deployment inside local docker containersServices:
- 7590fdbf-pgweb: PGWeb service "7590fdbf-pgweb" available at URL: 'http://localhost:8081'
- 7590fdbf-postgraphile: Postgraphile service "7590fdbf-postgraphile" available at URL: 'http://localhost:3000/graphiql' (API at 'http://localhost:3000/graphql')
- 7590fdbf-postgres: PostgreSQL service "7590fdbf-postgres" available at DSN: 'postgres://dev-node:insecure-change-me-in-prod@localhost:5432/substreams?sslmode=disable'
- 7590fdbf-sink: Sink service (no exposed port). Use 'substreams alpha sink-info 7590fdbf' to see last processed block or 'docker logs 7590fdbf-sink' to see the logs.
- 7590fdbf-sinkinfo: Sink info service "7590fdbf-sinkinfo" available at URL: 'http://localhost:8282/sinkinfo'
```
- Look at some SQL data via pgweb at <http://localhost:8081>
- *Tip:** You can run `substreams alpha service pause` if you want to pause the sink from consuming Substreams data while you continue your development. `substreams alpha service resume` will continue the progress.

### # Create a dbt project for transformations
- Initialize the dbt project:

Copy
```
dbt init cryptopunks
```
- *Tip:** Choose 'postgres' as the database.
- Move that project under 'dbt' folder:

Copy
```
mv cryptopunks dbt
```
- Edit the dev credentials under $HOME/.dbt/profiles.yml file:

Copy
```
...
cryptopunks:
  outputs:
    dev:
      type: postgres
      host: localhost
      user: dev-node
      password: insecure-change-me-in-prod
      port: 5432
      dbname: substreams
      schema: public
...
  target: dev

```
- *Tip:** You can see the database credentials again by running `substreams alpha service info`
- Test the dbt connection

Copy
```
dbt debug
```

You should see:

Copy
```
16:04:10  All checks passed!
```
- Remove the example models:

Copy
```
rm -rf models/example
```
- Create a datasource and a basic materialized view:

Copy
```
mkdir models/default
cat <<EOF > models/default/source.yml
version: 2
sources:
- name: cryptopunks
    loaded_at_field: evt_block_time
    tables:
- name: punk_bought
- name: punk_bid_entered
- name: punk_offered
- name: punk_no_longer_for_sale
- name: punk_transfer
- name: punk_bid_withdrawn
- name: transfer
- name: assign
EOF
cat <<EOF > models/default/punks_bought_per_hour.sql
{{ config(materialized='table') }}
select date_trunc('hour', evt_block_time) AS "hour", count(*) from punk_bought  GROUP BY hour order by hour
EOF
```
- Create your views:

Copy
```
dbt run
```
- Check that the `punks_bought_per_hour` has been created.

### # Deploy your Substreams to the "hosted dev" environment

Deployments of type "dev" gives you full read/write access to the database and are a good way of working together on a dataset while developing your dbt models.

Copy
```
substreams alpha service deploy substreams.sql.yaml -e https://deploy.streamingfast.io
```
- *Tip:** Here again, you can use the `substreams.clickhouse.yaml` manifest to use a Clickhouse engine.

You should see this output:

Copy
```
Deployed substreams sink "54546874":
  Status: RUNNING
Deployment *54546874* is *RUNNING*
- Database type is *postgres*
- Owner is *0doqed628575ba7d2bd03*
Indexed blocks: [12287507 - 12326000]
- Sink status is available at 'https://srv.streamingfast.io/54546874/sinkinfo'
Environment is *Development*, which means:
- Read-only direct access to the database is available at 'postgresql://db.srv.streamingfast.io:17622/substreams?sslmode=disable&user=dev-node-ro&password=iv2rqsKsUVH5'
- Read/write direct access to the database is available at 'postgresql://db.srv.streamingfast.io:17622/substreams?sslmode=disable&user=dev-node&password=oTWPmz2Sqssb'
- Read/write access to the database via PGWeb at 'https://srv.streamingfast.io/54546874/pgweb'
Postgraphile is available at these URL:
- GraphiQL (browser): 'https://srv.streamingfast.io/54546874/graphiql'
- GraphQL (apps): 'https://srv.streamingfast.io/54546874/graphql'
See some tutorials at https://substreams.streamingfast.io
```
- *Tip:** You are getting SQL credentials in this output. They can be fetched again by running `substreams alpha service info 46f5e9f6 -e https://deploy.streamingfast.io`.
- *Tip:** The SQL endpoint will be assigned a specific port mapped to your deployment, in this example, port 17622.
- Create another target in your `$HOME/.dbt/profiles.yml` replacing `PORT_NUMBER` and `RW_PASSWORD` with those assigned to you on the previous step:

Copy
```
cryptopunks:
  outputs:
...
    remote:
      type: postgres
      host: db.srv.streamingfast.io
      user: dev-node
      password: {RW_PASSWORD}
      port: {PORT_NUMBER}
      dbname: substreams
      schema: public
```
- You can iterate using `dbt run --target=remote`
- Other devs can work on that data and create dbt models.

### # Pack your production package and test it locally

When your dbt models are ready, you can pack everything (Substreams, [dbt project](https://docs.getdbt.com/docs/build/projects), etc.) inside an `.spkg` file and deploy it as production:
- Add a `dbt_config` section to the `substreams.sql.yaml` (or `substreams.clickhouse.yaml`) file:

Copy
```
    dbt_config:
      enabled: true
      files: "./dbt"
      run_interval_seconds: 180
```
- Start the `substreams alpha service serve` command in another window (if it is not still running from before...)

Copy
```
SUBSTREAMS_API_TOKEN=(...) substreams alpha service serve
```
- Stop the previous deployment completely (only a single deployment can run at the same time on local Docker environment)

Copy
```
substreams alpha service stop
```
- Test your deployment locally, in production mode:

Copy
```
substreams alpha service deploy substreams.sql.yaml --prod # or substreams.clickhouse.yaml
```
- *Tip:** If using Clickhouse, you will need to set `sink.config.rest_frontend.enabled` to `true`: it is currently the only way to consume data in a 'production' deployment.
- See that the database starts correctly and that the tables defined in `dbt` are being created correctly
- When you are happy with the results, verify or bump the `version` field in `substreams.sql.yaml`, you can generate the `cryptopunks-v0.1.0.spkg` file.

Copy
```
substreams pack substreams.sql.yaml # or substreams.clickhouse.yaml
```
### # Deploy your production package to the "hosted prod" environment

Copy
```
substreams alpha service deploy cryptopunks-v0.1.0.spkg -e https://deploy.streamingfast.io --prod
```

The production environment does not allow direct SQL access at the moment, so your apps will need to access the data to either the `postgraphile` frontend (or the `rest` frontend when using Clickhouse)

[PreviousRemote Service](/documentation/consume/sql/deployable-services/remote-service)[NextSQL Sink](/documentation/consume/sql/sql-sink)

Last updated 10 months ago

---

## FAQ | Substreams
Source: https://docs.substreams.dev/reference-and-specs/faq

- *Substreams FAQ overview**
- --------------------------

You can find answers to common Substreams questions in the FAQ documentation. If the answer you're looking for is not included [contact the StreamingFast team](https://discord.gg/mYPcRAzeVN) through Discord to get help.

## # **What is Substreams?**

Substreams is an exceptionally powerful processing engine capable of consuming streams of rich blockchain data. Substreams refines and shapes the data for painless digestion by end-user applications, such as decentralized exchanges.

## # **Do I need Firehose to use Substreams?**

Developers do not need a dedicated installation of Firehose to use Substreams. StreamingFast provides a public Firehose endpoint made available to developers.

## # **Is it possible to use Substreams in my subgraph?**

Yes, Substreams compliments and extend the capabilities and functionalities of subgraphs. Additional information is available in the [Substreams documentation for graph-node and subgraphs](https://substreams.streamingfast.io/reference-and-specs/graph-node-setup).

## # **Is it possible to use Substreams for production deployments?**

Yes. Substreams is [generally available](https://streamingfastio.medium.com/substreams-reach-general-availability-48272f6e942e) and used in production at multiple outlets.

## # **What's in the Substreams name?**

Substreams is the name of the engine, and of the product. It is to be capitalized and kept plural. One can speak of an individual *module* or individual *stream* but in general, when speaking about the engine, you would use the word "*Substreams"*.

## # **What is the** `substreams` **CLI?**

The [`substreams` command line interface (CLI)](/reference-and-specs/command-line-interface) is the main tool developers use to use the Substreams engine. The [`substreams` CLI](/reference-and-specs/command-line-interface) provides a range of features, commands, and flags. Additional information for the [`substreams` CLI](/reference-and-specs/command-line-interface) is available in the Substreams documentation.

## # **How do I get a Substreams authentication token?**

Authentication tokens are required to use Substreams and connect to the public Firehose endpoint. Full [instructions for obtaining a StreamingFast authentication token](https://substreams.streamingfast.io/reference-and-specs/authentication) are available in the Substreams documentation.

## # **My Substreams authentication token isn’t working, what do I do?**

The StreamingFast team is [available on Discord to resolve problems](https://discord.gg/Ugc7KtkA) related to obtaining or by using authentication tokens.

The Substreams documentation also [provides general instructions surrounding authentication](https://substreams.streamingfast.io/reference-and-specs/authentication) tokens.

## # **How do I create a Substreams module?**

Developers create their own Substreams implementations in a variety of ways. Use these [examples](https://github.com/streamingfast/substreams/blob/develop/docs/reference-and-specs/reference-and-specs/examples.md) as a reference and starting point.

The Substreams documentation [provides a Developer's guide](https://substreams.streamingfast.io/developer-guide/overview) to assist you to understand and use Substreams.

## # **What is Substreams used for?**

Substreams and Firehose work together to index and process blockchain data. Substreams is used for transforming rich blockchain data and exposing it to the needs of application developers.

## # **Is Substreams free?**

Yes, Substreams is an open-source project and there are free (albeit rate-limited) endpoints available.

## # **How does a developer reach the information returned from a call to Substreams from a web-based UI?**

Substreams is not meant to be piped to a web UI, it’s a data transformation layer. Substreams reaches Subgraphs, as a data source, and makes GraphQL available for web consumption. Other sinks might expose APIs for web browsers, however, it's not the responsibility of Substreams.

## # Is it possible to listen for new blocks?

Specifying a stop block value of zero (0), the default enables transparent handoff from historical to real-time blocks.

## # **Does StreamingFast have a Discord?**

Yes, [join the StreamingFast Discord](https://discord.gg/Ugc7KtkA).

## # **Is StreamingFast on Twitter?**

Yes, [find StreamingFast on their official Twitter account](https://twitter.com/streamingfastio).

## # **Is StreamingFast on YouTube?**

Yes, [find StreamingFast on their official YouTube account](https://www.youtube.com/c/streamingfast).

## # **Who is dfuse?**

StreamingFast was originally called dfuse. The company changed its name and is in the process of rebranding.

## # What is Sparkle?

Substreams is the successor of [StreamingFast Sparkle](https://github.com/streamingfast/sparkle). Substreams enables greater composability, and provides similar parallelization capabilities. Sparkle is deprecated.

## # **Who is StreamingFast?**

StreamingFast is a protocol infrastructure company providing a massively scalable architecture for streaming blockchain data. StreamingFast is one of the core developers working alongside The Graph Foundation.

## # Why the `wasm32-unknown-unknown` target?

The first unknown is the system you are compiling on, and the second is the system you are targeting.

“Compile on almost any machine, run on almost any machine.”

Additional information [is available in the Github issue for WASM-bindgen](https://github.com/rustwasm/wasm-bindgen/issues/979).

## # Why does the output show "@unknown" instead of "@type" and the decoding failed only showing "@str" and "@bytes"

Check to make sure the module's output type matches the protobuf definition. In some cases, the renamed protobuf package isn't updated in the `substreams.yaml` manifest file's `module.output.type` field, creating an incompatibility.

## # Can I retrieve Mempool data with Substreams?

No, it is currently NOT possible to retrieve Mempool data with Substreams.

[PreviousChange log](/reference-and-specs/change-log)

Last updated 1 year ago

---

## PubSub | Substreams
Source: https://docs.substreams.dev/documentation/consume/other-sinks/pubsub

The PubSub integration allows you to send blockchain data to a [Google PubSub](https://cloud.google.com/pubsub?hl=en) topic by emitting a specific Protobuf object in your Substreams: [sf.substreams.sink.pubsub.v1.Publish](https://github.com/streamingfast/substreams-sink-pubsub/blob/develop/proto/sf/substreams/sink/pubsub/v1/pubsub.proto).

Getting Started
- --------------

If you are new Substreams, refer to the [Develop Substreams](/documentation/develop) section to learn about the main pieces of building a Substreams from scratch.
- Clone the <https://github.com/streamingfast/substreams-sink-pubsub> GitHub repository.
- Install the PubSub CLI. This CLI will help in deploying your Substreams to the PubSub Service.

Copy
```
go install ./cmd/substreams-sink-pubsub
```
- Create a topic in the Google PubSub Service, where the data of your Substreams will be sent.
- Deploy your Substreams by using the PubSub CLI:

Copy
```
substreams-sink-pubsub sink -e <endpoint> --project <project_id> <substreams_manifest> <substreams_module_name> <topic_name> 
```
Copy
```
- `endpoint`: the Substreams provider endpoint that will be used to extract the data (you can find the endpoints available in the [Chains & Endpoints](../../references/chains-and-endpoints.md)) section.
- `project_id`: ID of the Google project.
- `substreams_manifest`: path to the Substreams manifest.
- `substreams_module_name`: name of the Substreams output module. The module must emit `sf.substreams.sink.pubsub.v1.Publish` data.
- `topic_name`: name of the Google topic where the data will be sent.
```

You can find some Substreams examples in the `examples` directory of the repository.

[PreviousPrometheus](/documentation/consume/other-sinks/prometheus)[NextDevelop Substreams](/documentation/develop)

Last updated 9 months ago

---

## Making eth_calls | Substreams
Source: https://docs.substreams.dev/documentation/develop/overview/evm-chain-specific-extensions/eth-calls

[PreviousEVM Chain-Specific Extensions](/documentation/develop/overview/evm-chain-specific-extensions)[NextTest Locally](/documentation/develop/test-locally)

Last updated 10 months ago

---

## Initialize a MANTRA Substreams Project | Substreams
Source: https://docs.substreams.dev/documentation/how-to-guides/mantra

In this guide, you'll learn how to initialize a MANTRA-based Substreams project. You’ll learn how to set up a simple project to extract raw data or filter events from a smart contract.

## # Prerequisites
- Docker and VS Code installed and up-to-date.
- Visit the [Getting Started Guide](https://github.com/streamingfast/substreams-starter) to initialize your Dev Container.

## # Step 1: Initialize Your MANTRA Substreams Project

1. Open your Dev Container and run the following command to initialize your project:
   
   Copy
   ```
   substreams init
   ```
2. You will be given the option to choose between two MANTRA project options. Select the one that best fits your requirements:
- **MANTRA-minimal**: Creates a simple Substreams that extracts raw data from the block and generates Rust code.
- **MANTRA-events**: Creates a Substreams that extracts MANTRA events using the cached [MANTRA Foundational Module](https://substreams.dev/packages/mantra-common/v0.1.0), filtered by one or more smart contract addresses.

## # Step 2: Visualize the Data

1. Create your account [here](https://thegraph.market/) to generate an authentification token (JWT) and pass it as input to:
   
   Copy
   ```
   substreams auth
   ```
2. Run the following command to visualize and itterate on your filtered data model:
   
   Copy
   ```
   substreams gui
   ```

## # Step 3: Customize your Project

After initialization, you can:
- Modify your Substreams manifest to include additional filters or configurations.
- Implement custom processing logic in Rust based on the filtered data retrieved by the foundational module.

## # Additional Resources

You may find these additional resources helpful for developing your first EVM application.

### # Dev Container Reference

The [Dev Container Reference](https://github.com/streamingfast/substreams/blob/develop/docs/references/devcontainer-ref.md) helps you navigate the complete container and its common errors.

### # GUI Reference

The [GUI reference](https://github.com/streamingfast/substreams/blob/develop/docs/references/gui.md) lets you explore all the tools available in the Substreams GUI.

### # Manifests Reference

The [Manifests Reference](https://github.com/streamingfast/substreams/blob/develop/docs/references/manifests.md) helps you with editing the `substreams.yaml`.

[PreviousInitialize an Injective Substreams Project](/documentation/how-to-guides/injective)[NextConsume Substreams](/documentation/consume)

Last updated 3 days ago

---

## Exploring Ethereum | Substreams
Source: https://docs.substreams.dev/tutorials/evm/exploring-ethereum

Getting started with Substreams might feel challenging, but you are not alone! The Substreams Explorers are a set of projects, modules, and code samples that allow you to *explore* and discover the main features of Substreams.
- *Tip**: This tutorial teaches you how to build a Substreams from scratch.

Remember that you can auto-generate your Substreams module by usig the code-generation tools.

As you already know, Substreams supports streaming from several blockchains, and every blockchain holds a different data model. This is why the data structures used change from one blockchain to the other. For example, an Ethereum block is represented by the [`sf.ethereum.type.v2.Block`](https://github.com/streamingfast/firehose-ethereum/blob/develop/proto/sf/ethereum/type/v2/type.proto) Rust struct, while a Near block is represented by [`sf.near.type.v1.Block`](https://github.com/streamingfast/firehose-near/blob/develop/proto/sf/near/type/v1/type.proto).

Before You Begin
- ---------------

Before you start coding, there are several dependencies you must install on your computer.

## # The GitHub Repository

The `https://github.com/streamingfast/substreams-explorers` GitHub repository contains all the Substreams Explorers currently available. You can simply clone the repository:

Copy
```
$ git clone https://github.com/streamingfast/substreams-explorers
```
## # The Substreams CLI

The Substreams CLI allows you to run, package, and visualize your Substreams. Make sure you have the CLI installed by following this [simple tutorial](/documentation/consume/installing-the-cli).

## # Substreams Basics

You should be familiar with the basic Substreams terminology, which includes:
- Modules (understanding the difference between a `map` and a `store` module)
- Protobufs (understanding what they are)

Ethereum Explorer
- ----------------

The Ethereum Explorer consists of several Substreams modules showcasing the most basic operations that you can perform with Substreams on the Ethereum blockchain.

You can find the Ethereum Explorer at <https://github.com/streamingfast/substreams-explorers>

## # Modules

The modules in this repository answer some interesting questions when developing a blockchain application:

### # How Can You Get the Basic Information of a Block?

For every block, the `map_block_meta` module retrieves the most relevant information of the block (number, hash, and parent hash).

### # How Can You Retrieve Transactions By Their From or To Fields?

Given any combination of two parameters (`from` and `to`), the `map_filter_transactions` filters a transaction among all transactions in the blockchain. This involves:

2. Providing the filters (only the `from` fields, only the `to` field, both `from` and `to` fields, or none)
5. Iterating over all the transactions.
8. Filtering the transactions, according to the parameters provided. For example, `from == tx_from`, `from == tx_from and to == tx_to`.

### # How Can You Retrieve All the Events For a Specific Smart Contract?

Given a smart contract address parameter (`contract_address`), the `map_contract_events` module retrieves all the events related to a specific smart contract. This involves:

2. Iterating over all the logs of a block.
5. Filtering the log, where the `address` field is equal to the smart contract address parameter (`address == contract_address`).

In the following sections, you will go through every module, run the corresponding Substreams, and understand every piece of code. Let's go!

## # The Project Structure

2. The `proto` folder contains the Protobuf definitions for the transformations. In this example, there are three Protobuf objects, which are the outputs of the Substreams module mentioned in the previous section: BlockMeta (which represents the information of an Ethereum block), Transaction (which is an abstraction for an Ethereum transaction), and Event (an abstraction for an Ethereum event).
5. The `src` folder contains the source code of the Substreams transformations. Every module has its corresponding Rust file.
8. The `substreams.yml` is the Substreams manifest, which defines relevant information, such as the inputs/outputs of every module or the Protobuf files.

### # The Substreams Manifest

Let's take a closer look at the Substreams manifest (`substreams.yml`):

2. The `protobuf` section specifies the location of the Protobuf files used in the Substreams (i.e. where are the files defining the objects that you are going to use as output). In this example, the files are under the `proto` folder.
5. When you run Substreams, you are really executing a Rust application inside a WASM container. Therefore, Substreams needs to know where is the WASM executable. The `binaries` section specifies the location of the WASM executable.
8. Every module must be defined in the manifest, along with its `kind`, `inputs` and `outputs`. In this example, the `map_block_meta` module is a mapper that takes a raw Ethereum block as input ([`sf.ethereum.type.v2.Block`](https://github.com/streamingfast/firehose-ethereum/blob/develop/proto/sf/ethereum/type/v2/type.proto)) and outputs the `BlockMeta` protobuf. Basically, the `map_block_meta` module returns a reduced version of the Ethereum block.

[PreviousEVM](/tutorials/evm)[NextMapping Blocks](/tutorials/evm/exploring-ethereum/map_block_meta_module)

Last updated 5 months ago

---

## Solana | Substreams
Source: https://docs.substreams.dev/tutorials/solana

[PreviousRetrieve Events of a Smart Contract](/tutorials/evm/exploring-ethereum/map_contract_events_module)[NextExplore Solana](/tutorials/solana/explore-solana)

Last updated 9 months ago

---

## Authentication | Substreams
Source: https://docs.substreams.dev/documentation/consume/authentication

[PreviousInstall the CLI](/documentation/consume/installing-the-cli)[NextPackages](/documentation/consume/packages)

Last updated 3 months ago

---

## JavaScript | Substreams
Source: https://docs.substreams.dev/documentation/consume/stream/javascript

The [Substreams JavaScript library](https://github.com/substreams-js/substreams-js) enables you to run a Substreams, just like you would through the CLI, but using JavaScript.

The library works both on the client-side and on the server-side, but with some small differences. Clone the [Substreams Sink Examples](https://github.com/streamingfast/substreams-sink-examples) repository contains examples several programming language. Then, move to the `javascript` folder.

Depending on your needs, you can use the `node` directory (which contains an example using server-side NodeJS) or the `web` directory (which contains an example using client-side JavaScript).

## # Install the dependencies

The `package.json` contains all the necessary dependencies to run the application.

The NodeJS example uses `@connectrpc/connect-node`, while the Web example uses `@connectrpc/connect-web`.

NodeJSWebCopy
```
{
    "name": "substreams-js-node-example",
    "version": "1.0.0",
    "description": "",
    "main": "index.js",
    "dependencies": {
      "@substreams/core": "^0.1.19",
      "@substreams/manifest": "^0.0.9",
      "@connectrpc/connect-node": "1.3.0",
      "@connectrpc/connect": "1.3.0"
    },
    "type": "module"
  }
```
Copy
```
{
  "name": "substreams-js-web-example",
  "private": true,
  "version": "0.0.0",
  "type": "module",
  "dependencies": {
    "@substreams/core": "^0.1.19",
    "@substreams/manifest": "^0.0.9",
    "@connectrpc/connect-web": "1.4.0",
    "@connectrpc/connect": "1.4.0"
  },
  "scripts": {
    "dev": "vite",
    "build": "vite build",
    "preview": "vite preview"
  },
  "devDependencies": {
    "vite": "^5.1.6"
  }
}
```

You can install the dependencies by running:

Copy
```
npm install
```
## # Run the Application

NodeJSWebCopy
```
node index.js
```

You will start receiving data!

The Web example uses [ViteJS](https://vitejs.dev/) to create a development server that runs the application:

Copy
```
npm run dev
```

Then, you can navigate to `https://localhost:5173`. You will start receiving data!

## # Explore the Application

When you consume a Substreams package, a long-live gRPC connection is established, therefore, disconnections will happen and should be taken as *normal*. The Substreams keeps track of latest block you consumed by sending a **cursor** to your application. You **must** persist the cursor, so that in the case of a disconnection, you can restart the application from the latest consumed block.

NodeJSWeb

The `index.js` file contains the `main()` function, which runs an infite loop and takes care of managing the disconnections.

Copy
```
const TOKEN = process.env.SUBSTREAMS_API_TOKEN // Substreams token. By default it takes the SUBSTREAMS_API_TOKEN environment variable of your system
const ENDPOINT = "https://mainnet.eth.streamingfast.io" // Substreams endpont. In this case, Ethereum mainnet
const SPKG = "https://spkg.io/streamingfast/ethereum-explorer-v0.1.2.spkg" // Substreams package. In this case, taken from the substreams.dev registry
const MODULE = "map_block_meta"
const START_BLOCK = '100000'
const STOP_BLOCK = '+10000'
/*
    Entrypoint of the application.
    Because of the long-running connection, Substreams will disconnect from time to time.
    The application MUST handle disconnections and commit the provided cursor to avoid missing information.
- /
const main = async () => {
    const pkg = await fetchPackage() // Download spkg
    const registry = createRegistry(pkg);
    // Create gRPC connection
    const transport = createConnectTransport({
        baseUrl: ENDPOINT,
        interceptors: [createAuthInterceptor(TOKEN)],
        useBinaryFormat: true,
        jsonOptions: {
            typeRegistry: registry,
        },
    });
    
    // The infite loop handles disconnections. Every time an disconnection error is thrown, the loop will automatically reconnect
    // and start consuming from the latest commited cursor.
    while (true) {
        try {
            await stream(pkg, registry, transport);
        } catch (e) {
            if (!isErrorRetryable(e)) {
              console.log(`A fatal error occurred: ${e}`)
              throw e
            }
            console.log(`A retryable error occurred (${e}), retrying after backoff`)
            console.log(e)
            // Add backoff from a an easy to use library
        }
    }
}
```

The `main.js` file contains the `main()` function, which runs an infite loop and takes care of managing the disconnections.

Copy
```
const TOKEN = "<SUBTREAMS-TOKEN>" // Substreams token. Put here your Substreams API token.
const ENDPOINT = "https://mainnet.eth.streamingfast.io" // Substreams endpont. In this case, Ethereum mainnet
const SPKG = "https://spkg.io/streamingfast/ethereum-explorer-v0.1.2.spkg" // Substreams package. In this case, taken from the substreams.dev registry
const MODULE = "map_block_meta"
const START_BLOCK = '100000'
const STOP_BLOCK = '+10000'
/*
  Entrypoint of the application.
  Because of the long-running connection, Substreams will disconnect from time to time.
  The application MUST handle disconnections and commit the provided cursor to avoid missing information.
- /
const main = async () => {
  const pkg = await fetchPackage(); // Download spkg
  const registry = createRegistry(pkg);
  const transport = createConnectTransport({
      baseUrl: ENDPOINT,
      interceptors: [createAuthInterceptor(TOKEN)],
      useBinaryFormat: true,
      jsonOptions: {
          typeRegistry: registry,
      },
  });
  
  // The infite loop handles disconnections. Every time an disconnection error is thrown, the loop will automatically reconnect
  // and start consuming from the latest commited cursor.
  while (true) {
      try {
          await stream(pkg, registry, transport);
      } catch (e) {
          if (!isErrorRetryable(e)) {
            console.log(`A fatal error occurred: ${e}`)
            throw e
          }
          console.log(`A retryable error occurred (${e}), retrying after backoff`)
          console.log(e)
      }
  }
}
```

The `stream()` function establishes the actual streaming connection by calling the `streamBlocks` function. The response of the function is a `StatefulResponse` object, which contains a progress message (containing useful information about the Substreams execution. The `handleProgressMessage()` function handles this message) and a response message (containing the message sent from the server. The `handleResponseMessage()` function decodes this message).

Copy
```
const stream = async (pkg, registry, transport) => {
  const request = createRequest({
      substreamPackage: pkg,
      outputModule: MODULE,
      productionMode: true,
      startBlockNum: START_BLOCK,
      stopBlockNum: STOP_BLOCK,
      startCursor: getCursor() ?? undefined
  });
  
  // Stream the blocks
  for await (const statefulResponse of streamBlocks(transport, request)) {
       /*
            Decode the response and handle the message.
            There different types of response messages that you can receive. You can read more about the response message in the docs:
            https://substreams.streamingfast.io/documentation/consume/reliability-guarantees#the-response-format
- /
        await handleResponseMessage(statefulResponse.response, registry);
        /*
            Handle the progress message.
            Regardless of the response message, the progress message is always sent, and gives you useful information about the execution of the Substreams.
- /
        handleProgressMessage(statefulResponse.progress, registry);
  }
}
```

There are different kind of response messages that the server can send. The most common are ones `blockScopedData` and `blockUndoSignal`:
- `blockScopedData`: sent by the server whenever a new block is discovered in the blockchain. Contains all the block information that you can decode.
- `blockUndoSignal`: sent every time there is a fork in the blockchain. Because you have probably read incorrect blocks in the `blockScopedData` message, you must rewind back to the latest valid block.

Copy
```
export const handleResponseMessage = async (response, registry) => {
    switch(response.message.case) {
        case "blockScopedData":
            handleBlockScopedDataMessage(response.message.value, registry);
            break;
        case "blockUndoSignal":
            handleBlockUndoSignalMessage(response.message.value);
            break;
    }
}
```
[PreviousSubstreams:Stream](/documentation/consume/stream)[NextGo](/documentation/consume/stream/go)

Last updated 8 months ago

---

## Remote Service | Substreams
Source: https://docs.substreams.dev/documentation/consume/sql/deployable-services/remote-service

Using the StreamingFast SQL remote (hosted) service is the easiest way to get started with Substreams:SQL. The following tutorial teaches you how to deploy a Substreams package from the [Substreams Registry](https://substreams.dev) to StreamingFast remote service.

This tutorial shows you how to deploy Substreams package to the **StreamingFast remote service**. You can also set up a Substreams deployable service environment in your computer, which will allow you to test your deployable services easily.

The Substreams:SQL Tutorial

## # Tutorial

In this short tutorial, you will:
- Deploy the Substreams package to the StreamingFast SQL remote service.
- Explore the SQL database in your browser.

Before you get started, make sure you have:
- The Substreams CLI installed.

The package used in this tutorial is the USDT Ethereum package, which retrieves events from the USDT smart contract on the Ethereum blockchain.

### # Deploying a Substreams Package to the Remote Service

1. You can find the USDT Ethereum package in the Substreams Registry.
2. Deploy the package using the `substreams alpha service deploy` command.

Copy
```
substreams alpha service deploy https://spkg.io/enoldev/substreams-ethereum-usdt-v0.1.0.spkg -e https://deploy.streamingfast.io
```
- The `substreams alpha service deploy` command is used to deploy a package to the remote service.
- In this example, you deploy the USDT Ethereum package (`https://spkg.io/enoldev/substreams-ethereum-usdt-v0.1.0.spkg`).
- The `-e` flag specifies the location of the remote service. In this example, you are using the StreamingFast Remote Service (`https://deploy.streamingfast.io`).

The deployment of the package might take 1-2 minutes.

2. After the deployment is completed, some useful data will be displayed:

Copy
```
Deploying... (creating services, please wait)
Deployed substreams sink "60589e45":
  Status: RUNNING
Deployment *60589e45* is *RUNNING*
- Database type is *postgres*
- Owner is *0qeru2bd28b954a35c12e*
Indexed blocks: [4634748 - 4785000]
- Sink status is available at 'https://srv.streamingfast.io/60589e45/sinkinfo'
Environment is *Development*, which means:
- Read-only direct access to the database is available at 'postgresql://db.srv.streamingfast.io:17441/substreams?sslmode=disable&user=dev-node-ro&password=JWgg68gP33lZ'
- Read/write direct access to the database is available at 'postgresql://db.srv.streamingfast.io:17441/substreams?sslmode=disable&user=dev-node&password=iESYNNa5EihR'
- Read/write access to the database via PGWeb at 'https://srv.streamingfast.io/60589e45/pgweb'
Postgraphile is available at these URL:
- GraphiQL (browser): 'https://srv.streamingfast.io/60589e45/graphiql'
- GraphQL (apps): 'https://srv.streamingfast.io/60589e45/graphql'
Documentation: https://substreams.streamingfast.io
Services:
- pgweb: pod running
- postgraphile: pod running
- postgres: pod running
- sink: pod running
- sinkinfo: pod running
```

2. **Service ID:** the identifier of the deployed service, which you can use to manage the service.
5. **URL of the service status:** use this URL to verify the status of the service.
8. **URL of the PostgreSQL client:** use this client to run SQL queries, update the SQL schema, and manage the SQL database in general.
11. **URL of the GraphQL clent:** use this client to run GraphQL queries.

### # Inspecting the PostgreSQL client

Once the package is deployed, your Substreams starts indexing data. You can access this data through in the form of a PostgreSQL database or a GraphQL API. To access the PostgreSQL client (PGWeb), copy the URL provided.

### # Stopping a Service

If you have not included a stop block in the package manifest, your Substreams will keep indexing the head of the chain, thus consuming bytes from your StreamingFast plan. To stop a service, get the service ID and run the following command:

Copy
```
substreams alpha service stop <SERVICE-ID> -e https://deploy.streamingfast.io
```
[PreviousDeployable Services](/documentation/consume/sql/deployable-services)[NextLocal Service](/documentation/consume/sql/deployable-services/local-service)

Last updated 10 months ago

---

## Substreams CLI reference | Substreams
Source: https://docs.substreams.dev/reference-and-specs/command-line-interface

`substreams` CLI reference overview
- ----------------------------------

The `substreams` command line interface (CLI) is the primary user interface and the main tool for sending requests and receiving data.

The `substreams` CLI exposes many commands to developers enabling a range of features.
- *Note**: When a package is specified, it is optional. If you do use it, you can use:
- Local `substreams.yaml` configuration files
- Local `.spkg` package files
- Remote `.spkg` package URLs
- Local directory containing a `substreams.yaml` file

If you choose to not use it, make sure that you are in a directory that contains a substreams.yaml file. Otherwise, you will get a usage error back.

## # `init`

The `init` command allows you to initialize a Substreams project for several blockchains. It is a conversational-like command: you will be asked several questions and a project with the specicied features will be created for you.

The options included in the `init` command will evolve over time, but every blockchain should, at least, contain one option.

Copy
```
substreams init
```
## # `build`

The `build` command:
- Generates the necessary Protobufs specified in the `substreams.yaml` file.
- Compiles the Rust code.
- Creates a Substreams package file (`.spkg`).

Copy
```
substreams build
```
## # `run`

The `run` command connects to a Substreams endpoint and begins processing data.

run commandCopy
```
substreams run -e mainnet.eth.streamingfast.io:443 \
- t +1 \
   ./substreams.yaml \
   module_name
```

The details of the run command are:
- `-e mainnet.eth.streamingfast.io:443` is the endpoint of the provider running your Substreams.
- `-t +1` or `--stop-block` only requests a single block; the stop block is the manifest's `initialBlock` + 1.
- `substreams.yaml` is the path where you have defined your [Substreams manifest](/reference-and-specs/manifests). You can use a `.spkg` or `substreams.yaml` configuration file.
- `module_name` is the module we want to `run`, referring to the module name [defined in the Substreams manifest](/reference-and-specs/manifests#modules-.name).
- *Tip**: Passing a different `-s` or `--start-block` runs prior modules at a higher speed. Output is provided at the requested start block, keeping snapshots along the way if you want to process it again.

### # Headers

The `-H` option in of the `run` or `gui` command allows you to dynamically pass headers with the gRPC request. This is useful when overriding default parameters in the Substreams execution.
- *X-Sf-Substreams-Parallel-Jobs Header**

The `X-Sf-Substreams-Parallel-Jobs` header sets the number of parallel jobs to use in the Substreams execution. By default, 10 jobs are used.

Copy
```
substreams run -e mainnet.eth.streamingfast.io:443 \
- t +1 \
- H "X-Sf-Substreams-Parallel-Jobs: 20" \
   ./substreams.yaml \
   module_name
```
### # Run example with output

substreams run Copy
```
$ substreams run -e mainnet.eth.streamingfast.io:443 \
    https://github.com/Jannis/gravity-substream/releases/download/v0.0.1/gravity-v0.1.0.spkg \
    gravatar_updates -o json
```

The output of the `gravatar_updates` module starting at block `6200807` will print a message resembling:

run outputCopy
```
{
  "updates": [
    {
      "id": "39",
      "owner": "0xaadcc13071fdf9c73cfbb8d97639ea68aa6fd1d2",
      "displayName": "alex | OpenSea",
      "imageUrl": "https://ucarecdn.com/13a67247-cb89-417a-92d2-50a7d7aa481c/-/crop/382x382/0,0/-/preview/"
    }
  ]
}
...
```
- *Note**: The `-o` or `--output` flag alters the output format.

The available output display options are:
- `ui`, a nicely formatted, UI-driven interface, displaying progress information and execution logs.
- `json`, an indented stream of data, **not** displaying progress information or logs, only data output for blocks proceeding the start block.
- `jsonl`, same as `json` showing every individual output on a single line.

## # `gui`

The `gui` command pops up a terminal-based graphical user interface.

Its parameters are very similar to those of `run`, but provides a UI to navigate the results instead of a stream of data.

### # Replay mode

When you run a `gui` session, a file called `replay.log` gets written with the contents of the streamed data that persists after closing the GUI.

You can reload the data without hitting the server again using `--replay`. The data is immediately reloaded in the GUI, ready for more inspection.

## # `pack` **(DEPRECATED)**
- *(DEPRECATED: use** `build` **instead)**

The `pack` command builds a shippable, importable package from a `substreams.yaml` manifest file.

pack commandCopy
```
$ substreams pack ./substreams.yaml
```

The output of the `pack` command will print a message resembling:

pack outputCopy
```
...
Successfully wrote "your-package-v0.1.0.spkg".
```
## # `info`

The `info` command prints out the contents of a package for inspection. It works on both local and remote `yaml` or `spkg` configuration files.

info commandCopy
```
$ substreams info ./substreams.yaml
```

The output of the `info` command will print a message resembling:

info outputCopy
```
Package name: solana_spl_transfers
Version: v0.5.2
Doc: Solana SPL Token Transfers stream
  Stream SPL token transfers to the nearest human being.
Modules:
- ---
Name: spl_transfers
Initial block: 130000000
Kind: map
Output Type: proto:solana.spl.v1.TokenTransfers
Hash: 2b59e4e840f814f4154a688c2935da9c3b61dc61
Name: transfer_store
Initial block: 130000000
Kind: store
Value Type: proto:solana.spl.v1.TokenTransfers
Update Policy: UPDATE_POLICY_SET
Hash: 11fd70768029bebce3741b051c15191d099d2436
```
## # `graph`

The `graph` command prints out a visual graph of the package in the [mermaid-js format](https://mermaid.js.org/intro/n00b-syntaxReference.html).
- *Tip**: [Mermaid Live Editor](https://mermaid.live/) is the visual editor used by Substreams.

graph commandCopy
```
$ substreams graph ./substreams.yaml
                    [±master ●●]
Mermaid graph:
```mermaid
graph TD;
  spl_transfers[map: spl_transfers]
  sf.solana.type.v1.Block[source: sf.solana.type.v1.Block] --> spl_transfers
  transfer_store[store: transfer_store]
  spl_transfers --> transfer_store
```
```

The `graph` command will result in a graphic resembling:

Mermaid generated graph diagram

## # `inspect`

The `inspect` command reaches deep into the file structure of a `yaml` configuration file or `spkg` package and is used mostly for debugging, or if you're curious\_.\_

inspect commandCopy
```
$ substreams inspect ./substreams.yaml | less
```

The output of the `inspect` command will print a message resembling:

inspect outputCopy
```
proto_files
...
modules {
  modules {
    name: "my_module_name"
...
```
## # `codegen`

The `codegen` command generates a code for a specific sink taking as a Substreams module as input. There are two code generators available: `subgraph` and `sql`.
- Subgraph

Generates a Substreams-powered Subgraph project from the Substreams package found in the current folder.

Copy
```
substreams codegen subgraph
```
- SQL

Generates a SQL-based Substreams project from the Substreams package found in the current folder.

Copy
```
substreams codegen sql
```
## # Help

To view a list of available commands and brief explanations in the `substreams` CLI, run the `substreams` command in a terminal passing the `-h` flag. You can use this help reference at any time.

help optionCopy
```
substreams -h
```
[PreviousDevelopment Container Reference](/reference-and-specs/devcontainer-ref)[NextManifests Reference](/reference-and-specs/manifests)

Last updated 2 months ago

---

## Packages | Substreams
Source: https://docs.substreams.dev/documentation/consume/packages

[PreviousAuthentication](/documentation/consume/authentication)[NextReliability Guarantees](/documentation/consume/reliability-guarantees)

Last updated 7 months ago

---

## SQL Sink | Substreams
Source: https://docs.substreams.dev/documentation/consume/sql/sql-sink

## # Purpose

Learn how to use the StreamingFast [`substreams-sink-sql`](https://github.com/streamingfast/substreams-sink-sql) tool with this documentation. A basic Substreams module example is provided to help you get started. We are going to showcase a Substreams module to extract data from the Ethereum blockchain and route it into a Protobuf for persistence in a SQL database.

The `substreams-sink-sql` today supports two database drivers namely *PostgresSQL* and *Clickhouse*. The tutorial below will focus on Postgres but we will describe how to connect to the other supported drivers.

Installation
- -----------

## # 1. Install `substreams-sink-sql`

Install `substreams-sink-sql` by using the pre-built binary release [available in the official GitHub repository](https://github.com/streamingfast/substreams-sink-sql/releases).

Extract `substreams-sink-sql` into a folder and ensure this folder is referenced globally via your `PATH` environment variable.

## # 2. Set up accompanying code example

Access the accompanying code example for this tutorial in the official `substreams-sink-sql` repository. You will find the Substreams project for the tutorial in the [docs/tutorial](https://github.com/streamingfast/substreams-sink-sql/tree/develop/docs/tutorial) directory.

To create the required Protobuf files, run the included `make protogen` command.

Copy
```
make protogen
```

To ensure proper setup and functionality, use your installation of the [`substreams` CLI](https://substreams.streamingfast.io/reference-and-specs/command-line-interface) to run the example code.

Use the `make build` and `make stream_db_out` commands to verify the setup for the example project. Use the included `make` command to build the Substreams module.

Copy
```
make build
make stream_db_out
```
## # Module handler for sink

The Rust source code file [`lib.rs`](https://github.com/streamingfast/substreams-sink-sql/blob/develop/docs/tutorial/src/lib.rs) contains an example code, the `db_out` module handler, which prepares and returns the module's [`DatabaseChanges`](https://docs.rs/substreams-database-change/latest/substreams_database_change/pb/database/struct.DatabaseChanges.html) output. The `substreams-sink-sql` tool captures the data sent out of the Substreams module and routes it into the appropriate columns and tables in the SQL database.

Copy
```
# [substreams::handlers::map]
fn db_out(block_meta_start: store::Deltas<DeltaProto<BlockMeta>>) -> Result<DatabaseChanges, substreams::errors::Error> {
    let mut database_changes: DatabaseChanges = Default::default();
    transform_block_meta_to_database_changes(&mut database_changes, block_meta_start);
    Ok(database_changes)
}
```

To gain a full understanding of the procedures and steps required for a database sink Substreams module, review the code in [`lib.rs`](https://github.com/streamingfast/substreams-sink-sql/blob/develop/docs/tutorial/src/lib.rs). The complete code includes the addition of a Substreams store module and other helper functions related to the database.
- *DatabaseChanges**

The [`DatabaseChanges`](https://github.com/streamingfast/substreams-sink-database-changes/blob/develop/proto/sf/substreams/sink/database/v1/database.proto#L7) Protobuf definition can be viewed at the following link for a peek into the crates implementation.

When developing your Substreams, the Rust crate [substreams-database-change](https://docs.rs/substreams-database-change/latest/substreams_database_change) can be used to create the required `DatabaseChanges` output type.
- *Note**: An output type of `proto:sf.substreams.sink.database.v1.DatabaseChanges` is required by the map module in the Substreams manifest when working with this sink.

3. Install PostgreSQL
- --------------------

To proceed with this tutorial, you must have a working PostgreSQL installation. Obtain the software by [downloading it from the vendor](https://www.postgresql.org/download/) and [install it by following the instructions](https://www.postgresql.org/docs/current/tutorial-install.html) for your operating system and platform.

If you encounter any issues, [refer to the Troubleshooting Installation page](https://wiki.postgresql.org/wiki/Troubleshooting_Installation) on the official PostgreSQL Wiki for assistance.

4. Create example database
- -------------------------

To store the blockchain data output by the Substreams module, you must create a new database in your PostgreSQL installation. The tutorial provides a schema and the PostgreSQL sink tool that handle the detailed aspects of the database design.

Use the `psql` command in your terminal to launch PostgreSQL.

Upon successful launch, you will see a prompt similar to the following, ready to accept commands for PostgreSQL.

Copy
```
psql (15.1)
Type "help" for help.
default-database-name=#
```

Use the following `SQL` command to create the example database:

Copy
```
CREATE DATABASE "substreams_example";
```

5. Create configuration file
- ---------------------------

Once the database has been created, you must now define the Substreams Sink Config in a Substreams manifest creating a deployable unit.

Let's create a folder `sink` and in it create a file called `substreams.dev.yaml` with the following content:

Copy
```
specVersion: v0.1.0
package:
  name: "<name>"
  version: <version>
imports:
  sql: https://github.com/streamingfast/substreams-sink-sql/releases/download/protodefs-v1.0.1/substreams-sink-sql-protodefs-v1.0.1.spkg
  main: ../substreams.yaml
network: 'mainnet'
sink:
  module: main:db_out
  type: sf.substreams.sink.sql.v1.Service
  config:
    schema: "../schema.sql"
    wire_protocol_access: true
```

The `package.name` and `package.version` are meant to be replaced to fit your project.

The `imports.main` defines your Substreams manifest that you want to sink. The `sink.module` defines which import key (`main` here) and which module's name (`db_out` here).

The `network` field defines which network this deployment should be part of, in our case `mainnet`

The `sink.type` defines the type of the config that we are expecting, in our case it's [sf.substreams.sink.sql.v1.Service](https://buf.build/streamingfast/substreams-sink-sql/docs/main:sf.substreams.sink.sql.v1#sf.substreams.sink.sql.v1.Service) (click on the link to see the message definition).

The `sink.config` is the instantiation of this `sink.type` with the config fully filled. Some config are special because they load from a file or from a folder. For example in our case the `sink.config.schema` is defined with a Protobuf option `load_from_file` which means the content of the `../schema.sql` will actually be inlined in the Substreams manifest.

> The final final can be found at [`sink/substreams.dev.yaml`](https://github.com/streamingfast/substreams-sink-sql/blob/develop/docs/tutorial/sink/substreams.dev.yaml)

6. Run setup command
- -------------------

Use the following command to run the `substreams-sink-sql` tool and set up the database for the tutorial.

Copy
```
substreams-sink-sql setup "psql://dev-node:insecure-change-me-in-prod@127.0.0.1:5432/substreams_example?sslmode=disable" ./sink/substreams.dev.yaml
```

The `"psql://..."` is the DSN (Database Source Name) containing the connection details to your database packed as an URL. The `scheme` (`psql` here) part of the DSN's url defines which driver to use, `psql` is what we are going to use here, see [Drivers](/documentation/consume/sql/sql-sink#drivers) section below to see what other DSN you can use here.

The DSN's URL defines the database IP address, username, and password, which depend on your PostgreSQL installation. Adjust `dev-node` to your own username `insecure-change-me-in-prod` to your password and `127.0.0.1:5432` to where your database can be reached.

## # Drivers

For DSN configuration for the currently supported drivers, see the list below:
- [Clickhouse DSN](https://github.com/streamingfast/substreams-sink-sql#clickhouse)
- [PostgresSQL DSN](https://github.com/streamingfast/substreams-sink-sql#postgresql)

7. Sink data to database
- -----------------------

The `substreams-sink-sql` tool sinks data from the Substreams module to the SQL database. Use the tool's `run` command, followed by the endpoint to reach and your Substreams config file to use:

Copy
```
substreams-sink-sql run "psql://dev-node:insecure-change-me-in-prod@127.0.0.1:5432/substreams_example?sslmode=disable" ./sink/substreams.dev.yaml
```

The endpoint needs to match the blockchain targeted in the Substreams module. The example Substreams module uses the Ethereum blockchain.

Successful output from the `substreams-sink-sql` tool will resemble the following:

Copy
```
2023-01-18T12:32:19.107-0800 INFO (sink-sql) starting prometheus metrics server {"listen_addr": "localhost:9102"}
2023-01-18T12:32:19.107-0800 INFO (sink-sql) sink from psql {"dsn": "psql://dev-node:insecure-change-me-in-prod@127.0.0.1:5432/substreams_example?sslmode=disable", "endpoint": "mainnet.eth.streamingfast.io:443", "manifest_path": "substreams.yaml", "output_module_name": "db_out", "block_range": ""}
2023-01-18T12:32:19.107-0800 INFO (sink-sql) starting pprof server {"listen_addr": "localhost:6060"}
2023-01-18T12:32:19.127-0800 INFO (sink-sql) reading substreams manifest {"manifest_path": "sink/substreams.dev.yaml"}
2023-01-18T12:32:20.283-0800 INFO (pipeline) computed start block {"module_name": "store_block_meta_start", "start_block": 0}
2023-01-18T12:32:20.283-0800 INFO (pipeline) computed start block {"module_name": "db_out", "start_block": 0}
2023-01-18T12:32:20.283-0800 INFO (sink-sql) validating output store {"output_store": "db_out"}
2023-01-18T12:32:20.285-0800 INFO (sink-sql) resolved block range {"start_block": 0, "stop_block": 0}
2023-01-18T12:32:20.287-0800 INFO (sink-sql) ready, waiting for signal to quit
2023-01-18T12:32:20.287-0800 INFO (sink-sql) starting stats service {"runs_each": "2s"}
2023-01-18T12:32:20.288-0800 INFO (sink-sql) no block data buffer provided. since undo steps are possible, using default buffer size {"size": 12}
2023-01-18T12:32:20.288-0800 INFO (sink-sql) starting stats service {"runs_each": "2s"}
2023-01-18T12:32:20.730-0800 INFO (sink-sql) session init {"trace_id": "4605d4adbab0831c7505265a0366744c"}
2023-01-18T12:32:21.041-0800 INFO (sink-sql) flushing table rows {"table_name": "block_data", "row_count": 2}
2023-01-18T12:32:21.206-0800 INFO (sink-sql) flushing table rows {"table_name": "block_data", "row_count": 2}
2023-01-18T12:32:21.319-0800 INFO (sink-sql) flushing table rows {"table_name": "block_data", "row_count": 0}
2023-01-18T12:32:21.418-0800 INFO (sink-sql) flushing table rows {"table_name": "block_data", "row_count": 0}
```
- *Note**: If you have an error looking like `load psql table: retrieving table and schema: pq: SSL is not enabled on the server`, it's because SSL is not enabled to reach you database, add `?sslmode=disable` at the end of the `sink.config.dsn` value to connect without SSL.

You can view the database structure by using the following command, after launching PostgreSQL through the `psql` command.

Copy
```
<default_database_name>=# \c substreams_example
```

The table information is displayed in the terminal resembling the following:

Copy
```
           List of relations
 Schema |    Name    | Type  |  Owner
- -------+------------+-------+----------
 public | block_data | table | postgres
 public | cursors    | table | postgres
(2 rows)
```

You can view the data extracted by Substreams and routed into the database table by using the following command:

Copy
```
substreams_example=# SELECT * FROM "block_data";
```

Output similar to the following is displayed in the terminal:

Copy
```
         id         | version |         at          | number |                               hash                               |                           parent_hash                            |      timestamp
- -------------------+---------+---------------------+--------+------------------------------------------------------------------+------------------------------------------------------------------+----------------------
 day:first:19700101 |         | 1970-01-01 00:00:00 | 0      | d4e56740f876aef8c010b86a40d5f56745a118d0906a34e69aec8c0db1cb8fa3 | 0000000000000000000000000000000000000000000000000000000000000000 | 1970-01-01T00:00:00Z
 month:first:197001 |         | 1970-01-01 00:00:00 | 0      | d4e56740f876aef8c010b86a40d5f56745a118d0906a34e69aec8c0db1cb8fa3 | 0000000000000000000000000000000000000000000000000000000000000000 | 1970-01-01T00:00:00Z
 day:first:20150730 |         | 2015-07-30 00:00:00 | 1      | 88e96d4537bea4d9c05d12549907b32561d3bf31f45aae734cdc119f13406cb6 | d4e56740f876aef8c010b86a40d5f56745a118d0906a34e69aec8c0db1cb8fa3 | 2015-07-30T15:26:28Z
 month:first:201507 |         | 2015-07-01 00:00:00 | 1      | 88e96d4537bea4d9c05d12549907b32561d3bf31f45aae734cdc119f13406cb6 | d4e56740f876aef8c010b86a40d5f56745a118d0906a34e69aec8c0db1cb8fa3 | 2015-07-30T15:26:28Z
 day:first:20150731 |         | 2015-07-31 00:00:00 | 6912   | ab79f822909750f88dfb9dd0350c1ebe98d5495e9c969cdeb6e0ac993b80175b | 8ffd8c04cb89ef45e0e1163639d51d9ed4fa03dd169db90123a1e047361b46fe | 2015-07-31T00:00:01Z
 day:first:20150801 |         | 2015-08-01 00:00:00 | 13775  | 2dcecad4cf2079d18169ca05bc21e7ba0add7132b9382984760f43f2761bd822 | abaabb8f8b7f7fa07668fb38fd5a08da9814cd8ad18a793e54eef6fa9b794ab4 | 2015-08-01T00:00:03Z
 month:first:201508 |         | 2015-08-01 00:00:00 | 13775  | 2dcecad4cf2079d18169ca05bc21e7ba0add7132b9382984760f43f2761bd822 | abaabb8f8b7f7fa07668fb38fd5a08da9814cd8ad18a793e54eef6fa9b794ab4 | 2015-08-01T00:00:03Z
```
## # Cursors

When you use Substreams, it sends back a block to a consumer using an opaque cursor. This cursor points to the exact location within the blockchain where the block is. In case your connection terminates or the process restarts, upon re-connection, Substreams sends back the cursor of the last written bundle in the request so that the stream of data can be resumed exactly where it left off and data integrity is maintained.

You will find that the cursor is saved in the `cursors` table of the `substreams_example` database.

## # Batching

Insertion for historical blocks is performed in batched to increase ingestion speed. The `--flush-interval` flag can be used to change the default value of 1000 blocks. Also, the flag `--live-block-time-delta <duration>` can be used to change the delta at which we start considering blocks to be live, the logic is `isLive = (now() - block.timestamp) < valueOfFlag(live-block-time-delta)`.

Conclusion and review
- --------------------

Routing data extracted from the blockchain using Substreams is a powerful and useful feature. With Substreams, you can route data to various types of sinks, including files and databases such as PostgreSQL. For more information on other types of sinks and sinking strategies, consult the core Substreams sinks documentation at https://substreams.streamingfast.io/developers-guide/substreams-sinks.

[PreviousLocal Service](/documentation/consume/sql/deployable-services/local-service)[NextSubstreams:Stream](/documentation/consume/stream)

Last updated 3 months ago

---

## Output | Substreams
Source: https://docs.substreams.dev/documentation/develop/manifest-modules/outputs

Output overview
- --------------

Substreams `map` modules support a single `output`. The `output` must be a protobuf populated by data acquired inside the `map` module. If the module intends to provide a basic `output` type of a single value, such as a `String` or `bool`, a protobuf is still required. The single value needs to be wrapped in a protobuf for use as the `output` value from a `map` module.
- *Note:** `store` modules **cannot** define an `output`.

An `output` object has a `type` attribute defining the `type` of the `output` for the `map` module. The `output` definition is located in the Substreams manifest, within the module definition.

Copy
```
output:
  type: proto:eth.erc721.v1.Transfers
```
[PreviousInputs](/documentation/develop/manifest-modules/inputs)[NextModule handlers](/documentation/develop/manifest-modules/setting-up-handlers)

Last updated 1 year ago

---

## Indexes | Substreams
Source: https://docs.substreams.dev/documentation/develop/indexes

[PreviousRust Dependencies](/documentation/develop/rust-crates)[NextParameterized Modules](/documentation/develop/parameterized-modules)

Last updated 6 months ago

---

## Dojo DEX USDT Volume Subgraph Example | Substreams
Source: https://docs.substreams.dev/tutorials/cosmos/injective/usdt-exchanges

The [USDT Exchanges Volume Subgraph](https://github.com/streamingfast/injective-subgraph-template) tracks the historical USDT volume for the `INJ-USDT` pair in the Dojo DEX.
- *Tip**: This tutorial teaches you how to build a Substreams from scratch.

Remember that you can auto-generate your Substreams module by usig the code-generation tools.

The subgraph uses the [Substreams triggers](/documentation/consume/subgraph/triggers) to import data from the Injective foundational modules.

## # Before You Begin
- [Install the Substreams CLI](/documentation/consume/installing-the-cli)
- [Get an authentication token](/documentation/consume/authentication)
- [Learn about the basics of the Substreams](/documentation/develop/manifest-modules)
- [Complete the Block Stats Substreams tutorial](/tutorials/cosmos/injective/block-stats)
- [Complete the Foundational Modules tutorial](/tutorials/cosmos/injective/foundational)

## # Inspect the Project

The `subgraph.yaml` file defines the configuration of the data sources (i.e. where the subgraph should get the data from).

Copy
```
specVersion: 1.0.0
indexerHints:
  prune: auto
schema:
  file: ./schema.graphql # 1.
dataSources:
- kind: substreams
    name: Events
    network: injective-mainnet # 2.
    source:
      package:
        moduleName: wasm_events # 3.
        file: wasm-events-v0.1.0.spkg # 4.
    mapping: # 5.
      apiVersion: 0.0.7
      kind: substreams/graph-entities
      file: ./src/mapping.ts
      handler: handleEvents
```

2. Path to the GraphQL schema, which defines the entities of the subgraph.
5. Network where data should be indexed. In this case, `injective-mainnet`.
8. Substreams module imported in the subgraph. This module extracts all the events with `type = wasm`.
11. Substreams package (`.spkg`) that contains the `wasm_events` module.
14. Definition of mappings. The `handleEvents` function will receive the data from the `wasm_events` Substreams module to be processed by the subgraph.

## # Inspect the Schema

The `schema.graphql` schema defines only one entity, `USDTExchangeVolume`, which holds the historical amount of the USDT exchanged in the Dojo DEX for the `INJ-USDT` pair.

Copy
```
type USDTExchangeVolume @entity {
  id: ID!
  amount: String!
}
```

The `amount` field is updated every time that a new exchange happens in the DEX.

## # Inspect the Code

The `handleEvents` function in the `mappings.ts` file receives the filtered events of the Substreams (those with `type = wasm`). The logic of the code finds out the USDT amount exchanged in the swap and updates the `USDTExchangeVolume` entity, adding up the amount.

Copy
```
export function handleEvents(bytes: Uint8Array): void { // 1.
    const eventList: EventList = Protobuf.decode<EventList>(bytes, EventList.decode); // 2.
    const events = eventList.events;
    log.info("Protobuf decoded, length: {}", [events.length.toString()]);
    let entity = USDTExchangeVolume.load(ID); // 3.
    if (entity == null) {
        log.info("Entity not found, creating one...", []);
        entity = new USDTExchangeVolume(ID);
        entity.amount = '0';
    }
    for (let i = 0; i < events.length; i++) { // 4.
        const event = events[i].event;
        if (event == null || event.type != "wasm") { // should be filtered by substreams
            continue;
        }
        let contract_addr = "";
        let action = "";
        let ask_asset = "";
        let ask_amount = "";
        let offer_asset = "";
        let offer_amount = "";
        for (let i = 0; i < event.attributes.length; ++i) { // 5.
            const attr = event.attributes[i];
            if (attr.key == '_contract_addr') {
                    contract_addr = attr.value;
            } else if (attr.key == '_action') {
                    action = attr.value;
            } else if (attr.key == 'ask_asset') {
                    ask_asset = attr.value;
            } else if (attr.key == 'ask_amount' || attr.key == 'return_amount') {
                    ask_amount = attr.value;
            } else if (attr.key == 'offer_asset') {
                    offer_asset = attr.value;
            } else if (attr.key == 'offer_amount') {
                    offer_amount = attr.value;
            }
        }
        if (contract_addr != DOJO_addr) { // 6.
            continue;
        }
        let exchangeAmountStr = "";
        if (ask_asset == USDT_addr && ask_amount != "") {
            exchangeAmountStr = ask_amount;
        } 
        if (offer_asset == USDT_addr && offer_amount != "") {
            exchangeAmountStr = ask_amount;
        }
        if (exchangeAmountStr == "") {
            continue;
        }
        const exchangeAmount = BigInt.fromString(exchangeAmountStr);
        const entityAmount = BigInt.fromString(entity.amount);
        const sumResult = entityAmount.plus(exchangeAmount); // 7.
        entity.amount = sumResult.toString();
        entity.save();
        log.debug("Entity saved: {}", [entity.amount]);
    }
}
```

2. Definition of the `handleEvents` function. As a parameter, it receives an array of bytes, representing the events consumed from the Substreams.
5. Decode the byte array into the `EventList` Protobuf object, which is the output of the Substreams.
8. Load the `USDTExchangeVolume` subgraph entity, which will store the historical volume. If it is the first trade, then the entity will not exist, and it must be created.
11. Iterate over the events and verify that the event type is `wasm` (`type == wasm`). This should be already filtered by the Substreams, but it is also nice to re-check it.
14. Iterate over the attributes of every event, finding out the neccesary information (contract address, action, ask amount, offer amount...).
17. Verify that the contract where the event is executed corresponds to the `INJ-USDT` pair in the Dojo DEX.
20. Update the entity.

## # Deploy to a Local Graph Node

You can test your Substreams-powered Subgraph by deploying to a local Graph Node set-up. Take a look at the the [Graph Node Local Development tutorial](/tutorials/graph-node/local-development), which provides information on how to spin up a local environment for Graph Node.

First, clone the [Substreams Development Environment GitHub respository](https://github.com/streamingfast/substreams-dev-environment) and move to the `graph-node` folder. Execute the `start.sh` command with the Injective information (make sure you have Docker running in your computer).

Copy
```
./start.sh injective-mainnet https://mainnet.injective.streamingfast.io:443
```

The previous command will spin up a local IPFS node, a local Postgres database and a local Graph Node instance. Now, you can create a new subgraph in the Graph Node:

Copy
```
graph create usdt-exchange-volume --node=http://localhost:8020
```

Then, you can deploy:

Copy
```
graph deploy --node http://localhost:8020/ --ipfs http://localhost:5001 usdt-exchange-volume
```

The subgraph will start indexing in the Graph Node, and you check out the different logs emitted by the subgraph.

[PreviousFoundational Modules](/tutorials/cosmos/injective/foundational)[NextSubgraphs](/tutorials/graph-node)

Last updated 5 months ago

---

## Run a Substreams | Substreams
Source: https://docs.substreams.dev/documentation/develop/running-substreams

[PreviousProtobuf Schemas](/documentation/develop/creating-protobuf-schemas)[NextRust Dependencies](/documentation/develop/rust-crates)

Last updated 9 months ago

---

## Develop Substreams | Substreams
Source: https://docs.substreams.dev/documentation/develop

[PreviousPubSub](/documentation/consume/other-sinks/pubsub)[NextManifest & Modules](/documentation/develop/manifest-modules)

Last updated 10 months ago

---

## Rust | Substreams
Source: https://docs.substreams.dev/tutorials/rust

Currently, the only programming language supported to build Substreams is Rust, although more might be added in the future.

If you have experience with typed programming languages, such as Go or Java, you should be able to understand and learn Rust pretty easily. However, there some features and standards that are specific to the Rust programming language.

The Substreams team recommends following the official [Rust by Example tutorial](https://doc.rust-lang.org/rust-by-example/), which pretty much includes everything you should know about Rust. At the same time, the following sections cover some features and standards that are important when developing Substreams.

[PreviousPublish to The Graph Network](/tutorials/graph-node/publish-decentralized-network)[NextOption struct](/tutorials/rust/option)

Last updated 1 year ago

---

## Retrieve Events of a Smart Contract | Substreams
Source: https://docs.substreams.dev/tutorials/evm/exploring-ethereum/map_contract_events_module

Given a smart contract address passed as a parameter, this module returns the logs attached to the contract.
- *Tip**: This tutorial teaches you how to build a Substreams from scratch.

Remember that you can auto-generate your Substreams module by usig the code-generation tools.

Running the Substreams
- ---------------------

First, generate the Protobuf modules and build the Rust code:

Copy
```
make protogen
```
Copy
```
make build
```

Now, you can run the Substreams. The logs retrieved correspond to the `0xbc4ca0eda7647a8ab7c2061c2e118a18a936f13d` (BoredApeYachtClub smart contract). To avoid iterating over the full blockchain, the following command starts at block `17717995` and finished at block `17718004`. Therefore, only the BoredApeYachtClub smart contract logs that happened within this block range are printed.

Copy
```
substreams run -e mainnet.eth.streamingfast.io:443 substreams.yaml map_contract_events --start-block 17717995 --stop-block +10
```

The output of the command should be similar to:

Copy
```
...output omitted...
- ---------- BLOCK #17,717,995 (bfecb26963a2cd77700754612185e0074fc9589d2d73abb90e362fe9e7969451) ---------------
- ---------- BLOCK #17,717,996 (7bf431a4f9df67e1d7e385d9a6cba41c658e66a77f0eb926163a7bbf6619ce20) ---------------
- ---------- BLOCK #17,717,997 (fa5a57231348f1f138cb71207f0cdcc4a0a267e2688aa63ebff14265b8dae275) ---------------
{
  "@module": "map_contract_events",
  "@block": 17717997,
  "@type": "eth.event.v1.Events",
  "@data": {
    "events": [
      {
        "address": "bc4ca0eda7647a8ab7c2061c2e118a18a936f13d",
        "topics": [
          "8c5be1e5ebec7d5bd14f71427d1e84f3dd0314c0f7b2291e5b200ac8c7c3b925",
          "000000000000000000000000e2a83b15fc300d8457eb9e176f98d92a8ff40a49",
          "0000000000000000000000000000000000000000000000000000000000000000",
          "00000000000000000000000000000000000000000000000000000000000026a7"
        ],
        "txHash": "f18291982e955f3c2112de58c1d0a08b79449fb473e58b173de7e0e189d34939"
      },
      {
        "address": "bc4ca0eda7647a8ab7c2061c2e118a18a936f13d",
        "topics": [
          "ddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef",
          "000000000000000000000000e2a83b15fc300d8457eb9e176f98d92a8ff40a49",
          "000000000000000000000000c67db0df922238979da0fd00d46016e8ae14cecb",
          "00000000000000000000000000000000000000000000000000000000000026a7"
        ],
        "txHash": "f18291982e955f3c2112de58c1d0a08b79449fb473e58b173de7e0e189d34939"
      }
    ]
  }
}
- ---------- BLOCK #17,717,998 (372ff635821a434c81759b3b23e8dac59393fc27a7ebb88b561c1e5da3c4643a) ---------------
- ---------- BLOCK #17,717,999 (43f0878e119836cc789ecaf12c3280b82dc49567600cc44f6a042149e2a03779) ---------------
- ---------- BLOCK #17,718,000 (439efaf9cc0059890a09d34b4cb5a3fe4b61e8ef96ee67673c060d58ff951d4f) ---------------
- ---------- BLOCK #17,718,001 (c97ca5fd26db28128b0ec2483645348bbfe998e9a6e19e3a442221198254c9ea) ---------------
- ---------- BLOCK #17,718,002 (9398569e46a954378b16e0e7ce95e49d0f21e6119ed0e3ab84f1c91f16c0c30e) ---------------
- ---------- BLOCK #17,718,003 (80bcd4c1131c35a413c32903ffa52a14f8c8fe712492a8f6a0feddbb03b10bba) ---------------
- ---------- BLOCK #17,718,004 (d27309ac29fe47f09fa4987a318818c325403863a53eec6a3676c2c2f8c069d9) ---------------
all done
```

The smart contract address is passed as a parameter defined in the Substreams manifest (`substreams.yml`):

Copy
```
params:
  map_contract_events: "0xbc4ca0eda7647a8ab7c2061c2e118a18a936f13d"
```

Inspecting the Code
- ------------------

Declaration of the module in the manifest (`substreams.yml`):

Copy
```
- name: map_contract_events
    kind: map
    inputs:
- params: string
- source: sf.ethereum.type.v2.Block
    output:
      type: proto:eth.event.v1.Events
```

The module expects two inputs: the parameter as a string, and a raw Ethereum block. The output is the `Events` object defined in the Protobuf.

The corresponding Rust function declaration, which matches the name of the module, `map_contract_events`:

Copy
```
fn map_contract_events(contract_address: String, blk: Block) -> Result<Events, Error> {
    verify_parameter(&contract_address)?; // Verify address
    let events: Vec<Event> = blk
        .logs() // 1.
        .filter(|log| log.address().to_vec() == Hex::decode(&contract_address).expect("already validated")) // 2.
        .map(|log| Event { // 3.
            address: Hex::encode(log.address()),
            topics: log.topics().into_iter().map(Hex::encode).collect(),
            tx_hash: Hex::encode(&log.receipt.transaction.hash),
        })
        .collect(); // 4.
    Ok(Events { events })
}
```

In this example, you do not need to parse the parameters, as `contract_address` is the only string passed and you can use it directly. However, it is necessary to verify that the parameter is a valid Ethereum; this verification is performed by the `verify_parameter` function.

Then, you iterate over the events of the contract:

2. The `.logs()` function iterates over the logs of successful transactions within the block.
5. For every log of a successful transaction, you verify if its `address` matches the smart contract address (i.e. you verify if the log was actually emitted by the smart contract). For the comparison, both `log.address()` and `contract_address` are converted to `Vec<u8>`.
8. Every filtered log (i.e. every log that belongs to the smart contract) is mapped to a `pb::eth::event::v1::Event` struct, which was specified in the Protobuf definition.
11. Finally, you collect all the events in a vector.

[PreviousFilter Transactions](/tutorials/evm/exploring-ethereum/map_filter_transactions_module)[NextSolana](/tutorials/solana)

Last updated 5 months ago

---

## How-To Guides | Substreams
Source: https://docs.substreams.dev/documentation/how-to-guides

[Initialize an EVM Substreams Project](/documentation/how-to-guides/evm)[Initialize a Solana Substreams Project](/documentation/how-to-guides/solana)[Initialize a Starknet Substreams Project](/documentation/how-to-guides/starknet)[Initialize an Injective Substreams Project](/documentation/how-to-guides/injective)[Initialize a MANTRA Substreams Project](/documentation/how-to-guides/mantra)[PreviousWhat is Substreams?](/)[NextInitialize an EVM Substreams Project](/documentation/how-to-guides/evm)

Last updated 2 months ago

---

## Filter Transactions | Substreams
Source: https://docs.substreams.dev/tutorials/evm/exploring-ethereum/map_filter_transactions_module

This module iterates over all the blockchain transactions and filters them by some of their fields (the `from` and `to` fields). For example, if you want to retrieve all the transactions initiated by the address `0xb6692f7ae54e89da0269c1bfd685ccdfd41d2bf7`, you set the filter `from = 0xb6692f7ae54e89da0269c1bfd685ccdfd41d2bf7`.
- *Tip**: This tutorial teaches you how to build a Substreams from scratch.

Remember that you can auto-generate your Substreams module by usig the code-generation tools.

Running the Substreams
- ---------------------

First, generate the Protobuf modules and build the Rust code:

Copy
```
make protogen
```
Copy
```
make build
```

Now, you can run the Substreams:

Copy
```
substreams run -e mainnet.eth.streamingfast.io:443 substreams.yaml map_filter_transactions --start-block 17712038 --stop-block +3
```

The output of the command should be similar to:

Copy
```
...output omitted...
- ---------- BLOCK #17,712,038 (b96fc7e71c0daf69b19211c45fbb5c201f4356fb2b5607500b7d88d298599f5b) ---------------
{
  "@module": "map_filter_transactions",
  "@block": 17712038,
  "@type": "eth.transaction.v1.Transactions",
  "@data": {
    "transactions": [
      {
        "from": "b6692f7ae54e89da0269c1bfd685ccdfd41d2bf7",
        "to": "dac17f958d2ee523a2206206994597c13d831ec7",
        "hash": "933b74565234ac9ca8389f7a49fad80099abf1be77e4bef5af69ade30127f30e"
      },
...output omitted...
      {
        "from": "4c8e30406f5dbedfaa18cb6b9d0484cd5390490a",
        "to": "dac17f958d2ee523a2206206994597c13d831ec7",
        "hash": "558031630b43c8c61e36d742a779f967f3f0102fa290111f6f6f9c2acaadf3ea"
      }
    ]
  }
}
- ---------- BLOCK #17,712,039 (1385f853d28b16ad7ebc5d51b6f2ef6d43df4b57bd4c6fe4ef8ccb6f266d8b91) ---------------
{
  "@module": "map_filter_transactions",
  "@block": 17712039,
  "@type": "eth.transaction.v1.Transactions",
  "@data": {
    "transactions": [
      {
        "from": "75e89d5979e4f6fba9f97c104c2f0afb3f1dcb88",
        "to": "dac17f958d2ee523a2206206994597c13d831ec7",
        "hash": "43e0e1b6315c4cc1608d876f98c9bbf09f2a25404aabaeac045b5cc852df0e85"
      },
      
...output omitted...
      {
        "from": "e41febca31f997718d2ddf6b21b9710c5c7a3425",
        "to": "dac17f958d2ee523a2206206994597c13d831ec7",
        "hash": "45c03fcbefcce9920806dcd7d638cef262ad405f8beae383fbc2695ad4bc9b1b"
      }
    ]
  }
}
- ---------- BLOCK #17,712,040 (31ad07fed936990d3c75314589b15cbdec91e4cc53a984a43de622b314c38d0b) ---------------
{
  "@module": "map_filter_transactions",
  "@block": 17712040,
  "@type": "eth.transaction.v1.Transactions",
  "@data": {
    "transactions": [
      {
        "from": "48c04ed5691981c42154c6167398f95e8f38a7ff",
        "to": "dac17f958d2ee523a2206206994597c13d831ec7",
        "hash": "137799eea9fa8ae410c913e16ebc5cc8a01352a638f3ce6f3f29a283ad918987"
      },
...output omitted...
      {
        "from": "f89d7b9c864f589bbf53a82105107622b35eaa40",
        "to": "dac17f958d2ee523a2206206994597c13d831ec7",
        "hash": "0544143b459969c9ed36741533fba70d6ea7069f156d2019d5362c06bf8d887f"
      }
    ]
  }
}
all done
```

In the previous command, you are filtering all the transactions from blocks `17712038` to `17712040`, where `to = 0xdac17f958d2ee523a2206206994597c13d831ec7` (the USDT smart contract address). The filters are specified in the `params` section of the Substreams manifest (`substreams.yml`):

Copy
```
map_filter_transactions: "to=0xdAC17F958D2ee523a2206206994597C13D831ec7"
```

Applying Filters
- ---------------

The filters are specified as a query-encoded string (`param1=value1&param2=value2&param3=value3`). In this example, only two parameters are supported, `from` and `to`, which you can use to create filters, such as:

Copy
```
map_filter_transactions: "from=0x89e51fa8ca5d66cd220baed62ed01e8951aa7c40&to=0xdAC17F958D2ee523a2206206994597C13D831ec7"
```

Retrieve all transactions where `from=0x89e51fa8ca5d66cd220baed62ed01e8951aa7c40` and `to=0xdAC17F958D2ee523a2206206994597C13D831ec7`.

Copy
```
map_filter_transactions: "from=0x89e51fa8ca5d66cd220baed62ed01e8951aa7c40"
```

Retrieve all transactions where `from=0x89e51fa8ca5d66cd220baed62ed01e8951aa7c40`.

Copy
```
map_filter_transactions: ""
```

Retrieve all transactions. Without applying any filter.

Inspecting the Code
- ------------------

Declaration of the module in the manifest (`substreams.yml`):

Copy
```
- name: map_filter_transactions
    kind: map
    inputs:
- params: string
- source: sf.ethereum.type.v2.Block
    output:
      type: proto:eth.transaction.v1.Transactions
```

The module expects two inputs: the parameters string, which contains the filters, plus a raw Ethereum block. The output is the `Transactions` object declared in the Protobuf.

Now, let's take a look at the actual Rust code:

Copy
```
# [derive(Deserialize)]
struct TransactionFilterParams {
    to: Option<String>,
    from: Option<String>,
}
# [substreams::handlers::map]
fn map_filter_transactions(params: String, blk: Block) -> Result<Transactions, Vec<substreams::errors::Error>> {
    let filters = parse_filters_from_params(params)?;
    let transactions: Vec<Transaction> = blk
        .transactions()
        .filter(|trans| apply_filter(&trans, &filters))
        .map(|trans| Transaction {
            from: Hex::encode(&trans.from),
            to: Hex::encode(&trans.to),
            hash: Hex::encode(&trans.hash),
        })
        .collect();
    Ok(Transactions { transactions })
}
```

The function name, `map_filter_transactions` matches the name given in the Substreams manifest. Two parameters are passed: `params: String, blk: Block`. For Substreams, the parameter specified in the manifest is a simple String. The query-encoded format is just an abstraction that you must parse. The `parse_filters_from_params` parses the string and creates a `TransactionFilterParams` struct.

Copy
```
let filters = parse_filters_from_params(params)?;
```
Copy
```
fn parse_filters_from_params(params: String) -> Result<TransactionFilterParams, Vec<substreams::errors::Error>> {
    let parsed_result = serde_qs::from_str(&params);
    if parsed_result.is_err() {
        return Err(Vec::from([anyhow!("Unexpected error while parsing parameters")]));
    }
    let filters = parsed_result.unwrap();
    verify_filters(&filters)?;
    Ok(filters)
}
```

The `serde_qs::from_str(&params)` from the [Serde QS Rust library](https://docs.rs/serde_qs/latest/serde_qs/) parses the parameters and returns the filters struct. Then, you call the `verify_filters(&filters)?` function, which ensures that the filters provided are valid Ethereum addresses. If there are errors while parsing the parameters, they are collected in a `substreams::errors::Error` vector and returned.

Back in the main function, if the parameters parsing is correct, you start filtering the transactions:

Copy
```
    let filters = parse_filters_from_params(params)?;
    // At this point, the filters are correct. If not, a Vec<substreams::errors::Error> object is returned.
    let transactions: Vec<Transaction> = blk
        .transactions() // 1.
        .filter(|trans| apply_filter(&trans, &filters)) // 2.
        .map(|trans| Transaction { // 3.
            from: Hex::encode(&trans.from),
            to: Hex::encode(&trans.to),
            hash: Hex::encode(&trans.hash),
        })
        .collect(); // 4.
```

2. The `transactions()` method iterates over all the **successful** transactions of the block.
5. Then, for every successful transaction, the previously parsed filters are applied.
8. Every transaction that complies with the filters provided is mapped into a `pb::eth::transaction::v1::Transaction` struct. This struct is part of the Protobuf declarations and is part of the output of the Substreams module.
11. Finally, all the transactions are collected into a vector of type `pb::eth::transaction::v1::Transaction`.

[PreviousMapping Blocks](/tutorials/evm/exploring-ethereum/map_block_meta_module)[NextRetrieve Events of a Smart Contract](/tutorials/evm/exploring-ethereum/map_contract_events_module)

Last updated 5 months ago

---

## Parameterized Modules | Substreams
Source: https://docs.substreams.dev/documentation/develop/parameterized-modules

Substreams allows you to pass parameters to your modules by specifying them in the manifest.

## # Parameterization of a Factory contract

It's quite common for a smart contract to be deployed on different networks or even by different dApps within the same network. Uniswap Factory smart contract is a good example of that.

When running Substreams for a dApp, you need to know the smart contract deployment address and for obvious reasons, this address will be different for each deployment.

Instead of hard-coding the address in the Substreams binary, you can customize it without having to rebuild or even repackage the Substreams package. The consumer can then just provide the address as a parameter.

First, you need to add the `params` field as an input. Note that it's always a string and it's always the first input for the module:

Copy
```
modules:
- name: map_pools_created
    kind: map
    inputs:
- params: string
- source: sf.ethereum.type.v2.Block
    output:
      type: proto:uniswap.types.v1.Pools
params:
  map_params: 1f98431c8ad98523631ae4a59f267346ea31f984
```

You can specify the default value directly in the manifest. In this case, we use `0x1f98431c8ad98523631ae4a59f267346ea31f984` - the deployment address for UniswapV3 contract on Ethereum Mainnet.

Handling the parameter in the module is easy. The module handler receives it as a first input parameter and you can use it to filter transactions instead of the hard-coded value:

Copy
```
# [substreams::handlers::map]
pub fn map_pools_created(params: String, block: Block) -> Result<Pools, Error> {
    let factory_address = Hex::decode(params).unwrap();
    Ok(Pools {
        pools: block
            .events::<abi::factory::events::PoolCreated>(&[&factory_address])
            .filter_map(|(event, log)| {
                // skipped: extracting pool information from the transaction
                Some(Pool {
                    address,
                    token0,
                    token1,
                    ..Default::default()
                })
            })
            .collect(),
    })
}
```

To pass the parameter to the module using `substreams` CLI you can use `-p` key:

Copy
```
substreams gui -e $SUBSTREAMS_ENDPOINT map_pools_created -t +1000 -p map_pools_created="1f98431c8ad98523631ae4a59f267346ea31f984"`
```
### # Documenting parameters

It's always a good idea to document what the params represent and how they are structured, so the consumers of your modules know how to properly parameterize them. You can use `doc` field for the module definition in the manifest.

Copy
```
modules:
- name: map_pools_created
    kind: map
    inputs:
- source: sf.ethereum.type.v2.Block
- params: string
    output:
      type: proto:uniswap.types.v1.Pools
    doc: |
      Params contains Uniswap factory smart contract address without `0x` prefix, i.e. 1f98431c8ad98523631ae4a59f267346ea31f984 for Ethereum Mainnet
```
## # Advanced parameters

Sometimes you may need to use multiple parameters for a module. To pass multiple parameters, you can encode them as a URL-encoded query string, i.e. `param1=value1&param2=value2`.

Suppose you want to track transfers to/from a certain address exceeding a certain amount of ETH. Your module manifest could look like this:

Copy
```
modules:
- name: map_whale_transfers
    kind: map
    inputs:
- params: string
- source: sf.ethereum.type.v2.Block
    output:
      type: proto:Transfers
params:
  map_params: address=aaa..aaa&amount=100
```

Our module gets a params string with two parameters: `address` and `amount`.

In your module handler, you can decode your parameters using one of the URL decoding crates such as `serde_qs`, `serde_urlencoded` or your own helper functions. Here's an example using `serde_qs`:

Copy
```
# [derive(Debug, Deserialize)]
struct Params {
    address: String,
    amount: u64,
}
# [substreams::handlers::map]
pub fn map_whale_transfers(params: String, block: Block) -> Result<Transfers, Error> {
    let query: Params = serde_qs::from_str(params.as_str()).unwrap();
    log::info!("Tracking transfers for address: {} of more than {} ETH", query.address, query.amount);
    // filter transfers by address and amount
}
```

Sometimes parameters can be optional, i.e. you want to track all transfers rather than a specific address. Decoding will look like this in that case:

Copy
```
# [derive(Debug, Deserialize)]
struct QueryParams {
    address: Option<String>,
    amount: u64,
}
# [substreams::handlers::map]
pub fn map_whale_transfers(params: String, block: Block) -> Result<Transfers, Error> {
    let query: QueryParams = serde_qs::from_str(params.as_str()).unwrap();
    if query.address.is_none() {
      log::info!("Tracking all of more than {} ETH", query.amount);
    }
    else {
      log::info!("Tracking transfers for address: {} of more than {} ETH", query.address, query.amount);
    }
}
```

You can even pass a vector of addresses to track multiple specific whales in our example:

Copy
```
# [derive(Debug, Deserialize)]
struct QueryParams {
    address: Vec<String>,
    amount: u64,
}
# [substreams::handlers::map]
pub fn map_whale_transfers(params: String, block: Block) -> Result<Transfers, Error> {
    let query: QueryParams = serde_qs::from_str(params.as_str()).unwrap();
    log::info!("Tracking transfers for addresses: {:?} of more than {} ETH", query.address, query.amount);
}
```

Depending on the crate you use to decode params string, you can pass them to Substreams CLI like this for example:

Copy
```
substreams gui map_whale_transfers -p map_whale_transfers="address[]=aaa..aaa&address[]=bbb..bbb&amount=100"
```
## # Parameters Per Network

It also possible to specify parameters per network. For example, consider that you want to specify a specific parameter for Ethereum and a different one for Solana.

The syntax to specify the parameters per network in your manifest uses the top-level `networks` block.

Copy
```
...
networks:
    <NETWORK-NAME>:
        params: 
            <MODULE-NAME>: “value”
...
```

For example, if you want to specify a parameter for the `my-module` module on Ethereum Mainnet:

Copy
```
...
networks:
    mainnet:
        params: 
            my-module: “value”
...
```
[PreviousIndexes](/documentation/develop/indexes)[NextChain-Specific Extensions](/documentation/develop/overview)

Last updated 3 months ago

---

## Triggers | Substreams
Source: https://docs.substreams.dev/documentation/consume/subgraph/triggers

- *Substreams triggers allow you to embed Substreams data directly in your subgraph**. Essentially, you **import the Protobufs emitted by your Substreams module** and you receive the data in the handler of your subgraph.

You can find all the information related to triggers in [The Graph documentation](https://thegraph.com/docs/en/sps/triggers/).

[PreviousGraph Out](/documentation/consume/subgraph/graph-out)[NextOther Ways of Consuming](/documentation/consume/other-sinks)

Last updated 1 month ago

---

## Key-Value Store | Substreams
Source: https://docs.substreams.dev/documentation/consume/other-sinks/kv

Purpose
- ------

This documentation will assist you in using [`substreams-sink-kv`](https://github.com/streamingfast/substreams-sink-kv) to write data from your existing substreams into a key-value store and serve it back through Connect-Web/GRPC.

Overview
- -------

`substreams-sink-kv` works by reading the output of specially-designed substreams module (usually called `kv_out`) that produces data in a protobuf-encoded structure called `sf.substreams.sink.kv.v1.KVOperations`.

The data is written to a key-value store. Currently supported KV store are Badger, BigTable and TiKV.

A Connect-Web interface makes the data available directly from the `substreams-sink-kv` process. Alternatively, you can consume the data directly from your key-value store.

Requirements
- -----------
- An existing substreams (including `substreams.yaml` and Rust code) that you want to instrument for `substreams-sink-kv`.
- A key-value store where you want to send your data (a badger local file can be used for development)
- Knowledge about Substreams development (start [here](https://substreams.streamingfast.io/getting-started/quickstart))
- Rust installation and compiler

Installation
- -----------
- Install [substreams-sink-kv CLI](https://github.com/streamingfast/substreams-sink-kv/releases)
- Install [substreams CLI](https://substreams.streamingfast.io/getting-started/installing-the-cli)
- Install [grpcurl](https://github.com/fullstorydev/grpcurl/releases) to easily read the data back from the KV store

Instrumenting your Substreams
- ----------------------------

## # Assumptions

The following instructions will assume that you are instrumenting [substreams-eth-block-meta](https://github.com/streamingfast/substreams-eth-block-meta), which contains:
- A store `store_block_meta_end` defined like [this](https://github.com/streamingfast/substreams-eth-block-meta/blob/v0.4.0/substreams.yaml#L29-L34):

Copy
```
# substreams.yaml
...
- name: store_block_meta_end
    kind: store
    updatePolicy: set
    valueType: proto:eth.block_meta.v1.BlockMeta
    inputs:
- source: sf.ethereum.type.v2.Block
```
- a `eth.block_meta.v1.BlockMeta` protobuf structure like [this](https://github.com/streamingfast/substreams-eth-block-meta/blob/v0.4.0/proto/block_meta.proto#L7-L12):

Copy
```
message BlockMeta {
  uint64 number = 1;
  bytes hash = 2;
  bytes parent_hash = 3;
  google.protobuf.Timestamp timestamp = 4;
}
```
> **Note** The [substreams-eth-block-meta](https://github.com/streamingfast/substreams-eth-block-meta) is already instrumented for sink-kv, the proposed changes here are a simplified version of what has been implemented. Please adjust the proposed code to your own substreams.

## # Import the Cargo module

2. Add the `substreams-sink-kv` crate to your `Cargo.toml`:

Copy
```
# Cargo.toml
[dependencies]
substreams-sink-kv = "0.1.1"
# ...

```

2. Add `map` module implementation function named `kv_out` to your `src/lib.rs`:

Copy
```
# substreams.yaml
...
- name: kv_out
    kind: map
    inputs:
- store: store_block_meta_end
        mode: deltas
    output:
      type: proto:sf.substreams.sink.kv.v1.KVOperations
```

2. Add a `kv_out` public function to your `src/lib.rs`:

Copy
```
// src/lib.rs
# [path = "kv_out.rs"]
mod kv;
use substreams_sink_kv::pb::kv::KvOperations;
# [substreams::handlers::map]
pub fn kv_out(
    deltas: store::Deltas<DeltaProto<BlockMeta>>,
) -> Result<KvOperations, Error> {
    // Create an empty 'KvOperations' structure
    let mut kv_ops: KvOperations = Default::default();
    // Call a function that will push key-value operations from the deltas
    kv::process_deltas(&mut kv_ops, deltas);
    // Here, we could add more operations to the kv_ops
    // ...
    Ok(kv_ops)
}
```

2. Add the `kv::process_deltas` transformation function referenced in the last snippet:

Copy
```
// src/kv_out.rs
use substreams::proto;
use substreams::store::{self, DeltaProto};
use substreams_sink_kv::pb::kv::KvOperations;
use crate::pb::block_meta::BlockMeta;
pub fn process_deltas(ops: &mut KvOperations, deltas: store::Deltas<DeltaProto<BlockMeta>>) {
    use substreams::pb::substreams::store_delta::Operation;
    for delta in deltas.deltas {
        match delta.operation {
            // KV Operations do not distinguish between Create and Update.
            Operation::Create | Operation::Update => {
                let val = proto::encode(&delta.new_value).unwrap();
                ops.push_new(delta.key, val, delta.ordinal);
            }
            Operation::Delete => ops.push_delete(&delta.key, delta.ordinal),
            x => panic!("unsupported opeation {:?}", x),
        }
    }
}
```

Test your substreams
- -------------------

2. Compile your changes in your rust code:

Copy
```
cargo build --release --target=wasm32-unknown-unknown
```

2. Run with `substreams` command directly:

Copy
```
substreams run -e mainnet.eth.streamingfast.io:443 substreams.yaml kv_out --start-block 1000000 --stop-block +1
```
> **Note** To connect to a public StreamingFast substreams endpoint, you will need an authentication token, follow this [guide](https://substreams.streamingfast.io/reference-and-specs/authentication) to obtain one.

2. Run with `substreams-sink-kv`:

Copy
```
substreams-sink-kv \
  run \
  "badger3://$(pwd)/badger_data.db" \
  mainnet.eth.streamingfast.io:443 \
  manifest.yaml \
  kv_out
```

You should see output similar to this one:

Copy
```
2023-01-12T10:08:31.803-0500 INFO (sink-kv) starting prometheus metrics server {"listen_addr": "localhost:9102"}
2023-01-12T10:08:31.803-0500 INFO (sink-kv) sink to kv {"dsn": "badger3:///Users/stepd/repos/substreams-sink-kv/badger_data.db", "endpoint": "mainnet.eth.streamingfast.io:443", "manifest_path": "https://github.com/streamingfast/substreams-eth-block-meta/releases/download/v0.4.0/substreams-eth-block-meta-v0.4.0.spkg", "output_module_name": "kv_out", "block_range": ""}
2023-01-12T10:08:31.803-0500 INFO (sink-kv) starting pprof server {"listen_addr": "localhost:6060"}
2023-01-12T10:08:31.826-0500 INFO (sink-kv) reading substreams manifest {"manifest_path": "https://github.com/streamingfast/substreams-eth-block-meta/releases/download/v0.4.0/substreams-eth-block-meta-v0.4.0.spkg"}
2023-01-12T10:08:32.186-0500 INFO (sink-kv) validating output store {"output_store": "kv_out"}
2023-01-12T10:08:32.186-0500 INFO (sink-kv) resolved block range {"start_block": 0, "stop_block": 0}
2023-01-12T10:08:32.186-0500 INFO (sink-kv) starting to listen on {"addr": "localhost:8000"}
2023-01-12T10:08:32.186-0500 INFO (sink-kv) starting stats service {"runs_each": "2s"}
2023-01-12T10:08:32.186-0500 INFO (sink-kv) no block data buffer provided. since undo steps are possible, using default buffer size {"size": 12}
2023-01-12T10:08:32.186-0500 INFO (sink-kv) starting stats service {"runs_each": "2s"}
2023-01-12T10:08:32.186-0500 INFO (sink-kv) ready, waiting for signal to quit
2023-01-12T10:08:32.186-0500 INFO (sink-kv) launching server {"listen_addr": "localhost:8000"}
2023-01-12T10:08:32.187-0500 INFO (sink-kv) serving plaintext {"listen_addr": "localhost:8000"}
2023-01-12T10:08:32.278-0500 INFO (sink-kv) session init {"trace_id": "a3c59bd7992c433402b70f9541565d2d"}
2023-01-12T10:08:34.186-0500 INFO (sink-kv) substreams sink stats {"db_flush_rate": "10.500 flush/s (21 total)", "data_msg_rate": "0.000 msg/s (0 total)", "progress_msg_rate": "0.000 msg/s (0 total)", "block_rate": "0.000 blocks/s (0 total)", "flushed_entries": 0, "last_block": "None"}
2023-01-12T10:08:34.186-0500 INFO (sink-kv) substreams sink stats {"progress_msg_rate": "16551.500 msg/s (33103 total)", "block_rate": "10941.500 blocks/s (21883 total)", "last_block": "#291883 (66d03f819dde948b297c8d582889246d7ba11a5b947335497f8716a7b608f78e)"}
```
> **Note** This writes the data to a local folder "./badger\_data.db/" in Badger format. You can `rm -rf ./badger_data.db` between your tests to cleanup all existing data.

2. Look at the stored data

You can scan the whole dataset using the 'Scan' command:

Copy
```
grpcurl --plaintext -d '{"begin": "", "limit":100}' localhost:8000 sf.substreams.sink.kv.v1.Kv/Scan
```

You can look at data by key prefix:

Copy
```
grpcurl --plaintext   -d '{"prefix": "day:first:201511", "limit":31}' localhost:8000 sf.substreams.sink.kv.v1.Kv/GetByPrefix
```

Consume the key-value data from a web-page using Connect-Web
- -----------------------------------------------------------

The [Connect-Web](https://connect.build/docs/web/getting-started) library allows you to quickly bootstrap a web-based client for your key-value store.

## # Requirements
- [NodeJS](https://nodejs.dev/download)
- [npm](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm)
- [buf CLI](https://docs.buf.build/installation)

## # Start from our example for `substreams-eth-block-meta`

You can checkout and run our connect-web-example like this:

Copy
```
git clone git@github.com:streamingfast/substreams-sink-kv
cd substreams-sink-kv/connect-web-example
npm install
npm run dev
```

Then, enter a key in the text box. The app currently only decodes `eth.block_meta.v1.BlockMeta`, so you will likely receive the corresponding value encoded in hex string.

To decode the value of your own data structures, add your `.proto` files under `proto/` and generate Rust bindings like this:

Copy
```
npm run buf:generate
```

You should see this output:

Copy
```
> connect-web-example@0.0.0 buf:generate
> buf generate ../proto/substreams/sink/kv/v1 && buf generate ./proto
```

Then, modify the code from `src/App.tsx` to decode your custom type, from this:

Copy
```
    import { BlockMeta } from "../gen/block_meta_pb";
    ...
    const blkmeta = BlockMeta.fromBinary(response.value);
    output = JSON.stringify(blkmeta, (key, value) => {
        if (key === "hash") {
            return "0x" + bufferToHex(blkmeta.hash);
        }
        if (key === "parentHash") {
            return "0x" + bufferToHex(blkmeta.parentHash);
        }
        return value;
    }, 2);
```

to this:

Copy
```
    import { MyData } from "../gen/my_data_pb";
    ...
    const decoded = MyData.fromBinary(response.value);
    output = JSON.stringify(decoded, null, 2);
```
## # Bootstrap your own application

If you want to start with an empty application, you can follow [these instructions](https://github.com/streamingfast/substreams-sink-kv/tree/main/connect-web-example/README.md)

Sending to a production key-value store
- --------------------------------------

Until now, we've used the **badger** database as a store, for simplicity. However, `substreams-sink-kv` also supports **TiKV** and **bigtable**.
- `tikv://pd0,pd1,pd2:2379?prefix=namespace_prefix`
- `bigkv://project.instance/namespace-prefix?createTables=true`

See [kvdb](https://github.com/streamingfast/kvdb) for more details.

Conclusion and review
- --------------------

The ability to route data extracted from the blockchain by using Substreams is powerful and useful. Key-value stores aren't the only type of sink the data extracted by Substreams can be piped into. Review the core Substreams sinks documentation for [additional information on other types of sinks](https://substreams.streamingfast.io/developers-guide/substreams-sinks) and sinking strategies.

[PreviousFiles](/documentation/consume/other-sinks/files)[NextMongoDB](/documentation/consume/other-sinks/mongodb)

Last updated 10 months ago

---

## Publish to The Graph Network | Substreams
Source: https://docs.substreams.dev/tutorials/graph-node/publish-decentralized-network

[PreviousLocal Development](/tutorials/graph-node/local-development)[NextRust](/tutorials/rust)

Last updated 6 months ago

---

## Prometheus | Substreams
Source: https://docs.substreams.dev/documentation/consume/other-sinks/prometheus

[PreviousMongoDB](/documentation/consume/other-sinks/mongodb)[NextPubSub](/documentation/consume/other-sinks/pubsub)

Last updated 10 months ago

---

## Consume Substreams | Substreams
Source: https://docs.substreams.dev/documentation/consume

[PreviousInitialize a MANTRA Substreams Project](/documentation/how-to-guides/mantra)[NextInstall the CLI](/documentation/consume/installing-the-cli)

Last updated 10 months ago

---

## Manifest & Modules | Substreams
Source: https://docs.substreams.dev/documentation/develop/manifest-modules

## # Modules and Manifests

In Substreams, manifests and modules are concepts tighly related because they are fundamental to understand how Substreams works.

In simple terms, a Substreams module is a Rust function that receives an input and returns an output. For example, the following Rust function receives an Ethereum block and returns a custom object containing fields such as block number, hash or parent hash.

Copy
```
fn get_my_block(blk: Block) -> Result<MyBlock, substreams::errors::Error> {
    let header = blk.header.as_ref().unwrap();
    Ok(MyBlock {
        number: blk.number,
        hash: Hex::encode(&blk.hash),
        parent_hash: Hex::encode(&header.parent_hash),
    })
}
```

And also in simple terms, a Substreams manifest (`substreams.yaml`) is a configuration file (a YAML file) for your Substreams, which defines the different modules (functions) for your Substreams, among other configurations. For example, the following manifest receives a raw Ethereum block as input (`sf.ethereum.type.v2.Block`) and outputs a custom object (`eth.example.MyBlock`).

Copy
```
modules:
- name: map_block
    kind: map
    initialBlock: 12287507
    inputs:
- source: sf.ethereum.type.v2.Block
    output:
      type: proto:eth.example.MyBlock
```

Among other things, the manifest allows you to define:
- How many modules your Substreams uses, along with their corresponding inputs and outputs.
- The schema(s) (i.e. the data model) your Substreams uses.
- How you will consume the data emitted by your Substreams (SQL, Webhooks...).

## # Module Chaining

Modules were built with composability in mind, so it is possible to chain them. Given two modules, `module1` and `module2`, you can set the output of `module1` to be the input of `module2`, creating a chain of interconnected Substreams modules. Let's take a look at the following example:

Copy
```
modules:
- name: map_events
    kind: map
    initialBlock: 4634748
    inputs:
- source: sf.ethereum.type.v2.Block
    output:
      type: proto:contract.v1.Events
- name: db_out
    kind: map
    initialBlock: 4634748
    inputs:
- map: map_events
    output:
      type: proto:sf.substreams.sink.database.v1.DatabaseChanges
```

There are two modules defined: `map_events` and `graph_out`.
- The `map_events` module receives a `sf.ethereum.type.v2.Block` object (a raw Ethereum block) as a parameter and outputs a custom `contract.v1.Events` object.
- The `db_out` module receives `map_events`'s output as an input, and outputs another custom object, `sf.substreams.sink.database.v1.DatabaseChanges`.

Technically, modules have one or more inputs, which can be in the form of a `map` or `store`, or a `Block` or `Clock` object received from the blockchain's data source. Every time a new `Block` is processed, all of the modules are executed as a directed acyclic graph (DAG).

## # Module Kinds

There are two types of modules: `map` and `store`. `map` modules are used for stateless transformations and `store` modules are used for stateful transformations.

Substreams executes the Rust function associated with module for every block on the blockchain, but there will be times when you will have to save data between blocks. `store` modules allow you to save in-memory data.

### # `map` modules

`map` modules are used for data extraction, filtering, and transformation. They should be used when direct extraction is needed avoiding the need to reuse them later in the DAG.

To optimize performance, you should use a single `map` module instead of multiple `map` modules to extract single events or functions. It is more efficient to perform the maximum amount of extraction in a single top-level `map` module and then pass the data to other Substreams modules for consumption. This is the recommended, simplest approach for both backend and consumer development experiences.

Functional `map` modules have several important use cases and facts to consider, including:
- Extracting model data from an event or function's inputs.
- Reading data from a block and transforming it into a custom protobuf structure.
- Filtering out events or functions for any given number of contracts.

### # `store` modules

`store` modules are used for the aggregation of values and to persist state that temporarily exists across a block.
- *Important:** Stores should not be used for temporary, free-form data persistence.

Unbounded `store` modules are discouraged. `store` modules shouldn't be used as an infinite bucket to dump data into.

Notable facts and use cases for working `store` modules include:
- `store` modules should only be used when reading data from another downstream Substreams module.
- `store` modules cannot be output as a stream, except in development mode.
- `store` modules are used to implement the Dynamic Data Sources pattern from Subgraphs, keeping track of contracts created to filter the next block with that information.
- Downstream of the Substreams output, do not use `store` modules to query anything from them. Instead, use a sink to shape the data for proper querying.

## # Defining Modules

Modules are defined as a YAML list under the `modules` section of the manifest. In the following example, a `map_events` module is defined:

Copy
```
modules:
- name: map_events
    kind: map
    initialBlock: 4634748
    inputs:
- source: sf.ethereum.type.v2.Block
    output:
      type: proto:contract.v1.Events
```

Then, you create the corresponding Rust function under the `src/lib.rs` file.

Copy
```
# [substreams::handlers::map]
fn map_events(blk: eth::Block) -> Result<contract::Events, substreams::errors::Error> {
...output omitted...
}
```
[PreviousDevelop Substreams](/documentation/develop)[NextModule types](/documentation/develop/manifest-modules/types)

Last updated 10 months ago

---

## Deployable Services | Substreams
Source: https://docs.substreams.dev/documentation/consume/sql/deployable-services

[Remote Service](/documentation/consume/sql/deployable-services/remote-service)[Local Service](/documentation/consume/sql/deployable-services/local-service)[PreviousSubstreams:SQL](/documentation/consume/sql)[NextRemote Service](/documentation/consume/sql/deployable-services/remote-service)

Last updated 4 months ago

---

## SPL Token Tracker | Substreams
Source: https://docs.substreams.dev/tutorials/solana/token-tracker

The Solana Token Tracker Substreams allows you to extract transfers from Solana Token Programs. You can simply provide the address of the token you want to track as an input to the Substreams.

## # Before You Begin

The Solana Token Tracker Substreams requires medium to advanced Substreams knowledge. If this is the first time you are using Substreams, make sure you:
- Read the [Develop Substreams](/documentation/develop) section, which will teach you the basics of the developing Substreams modules.
- Complete the [Explore Solana](/tutorials/solana/explore-solana) tutorial, which will assist you in understanding the main pieces of the Solana Substreams.

If you already have the required knowledge, clone the [Solana Token Tracker GitHub repository](https://github.com/streamingfast/solana-token-tracker). You will go through the code in the following steps.

## # Inspect the Project

The Substreams has only one module: `map_solana_token_events`, as you can check in the Substreams manifest (`substreams.yaml`):

Copy
```
modules:
- name: map_solana_token_events 
    kind: map
    initialBlock: 158558168
    inputs:
- params: string
- source: sf.solana.type.v1.Block
    output:
      type: proto:solana_token_tracker.types.v1.Output
params:
  map_solana_token_events: "token_contract=EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v&token_decimals=6"
```

The module receives two inputs (defined in the `intputs` section of the YAML):
- A string containing a couple of parameters: this parameter is defined in the `params` section of the YAML, and defines the token that you want to extract data from: `token_contract=EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v&token_decimals=6` `token_contract=EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v` is the address of the USDC contract in Solana mainnet and `token_decimals=6` is the number of decimals used the USDC token.
- A raw Solana block.

You can update the `token_contract` parameter to track any token of your choice. You can also use the `-p` option in the Substreams GUI to dynamically override the parameters of the Substreams.

## # Run the Substreams

You can run the Substreams by using the Substreams CLI. As specified in the manifest by default, the USDC data will be retrieved.

Copy
```
substreams gui ./substreams.yaml map_solana_token_events -e mainnet.sol.streamingfast.io:443  --start-block 158558168 --stop-block +1
```

You can also override the parameters of the manifest by using the `-p` option of the CLI. For example, if you want to track the transfer of the USDT token (`Es9vMFrzaCERmJfrF4H2FYD4KCoNkY11McCe8BenwNYB`):

Copy
```
substreams gui ./substreams.yaml map_solana_token_events -e mainnet.sol.streamingfast.io:443  --start-block 158558168 --stop-block +1 -p map_solana_token_events="token_contract=Es9vMFrzaCERmJfrF4H2FYD4KCoNkY11McCe8BenwNYB&token_decimals=6"
```
## # Inspect the Code
- Open the `lib.rs` file, which contains the code for the `map_solana_token_events` module. The function receives two parameters: the raw Solana block object and the parameters provided in the Substreams manifest.
- The `parse_parameters` function converts the parameters string passed to the module and converts it into a `TokenParams` object. This object contains two fields: `token_contract` (representing the address of the token to track) and `token_decimals` (representing the number of decimals used in the token).

Copy
```
pub fn map_solana_token_events(params: String, block: Block) -> Result<Output, Error> {
    let parameters = parse_parameters(params)?;
    // ...
}
```
- Then, you iterate over all the transactions

Copy
```
pub fn map_solana_token_events(params: String, block: Block) -> Result<Output, Error> {
    let parameters = parse_parameters(params)?;
    let mut output = Output::default(); // 1.
    let timestamp = block.block_time.as_ref().unwrap().timestamp;
    for confirmed_trx in block.transactions_owned() { // 2.
        let accounts = confirmed_trx.resolved_accounts_as_strings(); // 3.
        if let Some(trx) = confirmed_trx.transaction { // 4.
            let trx_hash = bs58::encode(&trx.signatures[0]).into_string();
            let msg = trx.message.unwrap(); // 5.
            let meta = confirmed_trx.meta.as_ref().unwrap(); // 6.
            for (i, compiled_instruction) in msg.instructions.iter().enumerate() { // 7.
                utils::process_compiled_instruction( // 8.
                    &mut output,
                    timestamp,
                    &trx_hash,
                    meta,
                    i as u32,
                    compiled_instruction,
                    &accounts,
                    &parameters
                );
            }
        }
    }
    Ok(output) // 9.
}
```

2. Create an `Output` object, which is the container of all the events extracted.
5. Iterate over the confirmed transactions of the block.
8. Get the accounts of the transaction. The `resolved_accounts()` method contains also accounts stored in the [Address Lookup Tables](https://docs.solana.com/developing/lookup-tables).
11. *Unwrap* the transaction if it is available.
14. *Unwrap* the transaction message.
17. *Unwrap* the transaction metadata.
20. Iterave over the instructions contained within the transaction.
23. For every instruction, call the `process_compiled_instruction(...)` function to process the instruction further.
- The `process_compiled_instruction(...)` function is defined in the `util.rs` file.

Copy
```
pub fn process_compiled_instruction(
    output: &mut Output,
    timestamp: i64,
    trx_hash: &String,
    meta: &TransactionStatusMeta,
    inst_index: u32,
    inst: &CompiledInstruction,
    accounts: &Vec<String>,
    parameters: &TokenParams
) {
    let instruction_program_account = &accounts[inst.program_id_index as usize]; // 1.
    if instruction_program_account == constants::TOKEN_PROGRAM { // 2.
        match process_token_instruction(trx_hash, timestamp, &inst.data, &inst.accounts, meta, accounts, output, parameters) {
            Err(err) => {
                panic!(
                    "trx_hash {} top level transaction without inner instructions: {}",
                    trx_hash, err
                );
            }
            Ok(()) => {}
        }
    }
    process_inner_instructions(output, inst_index, meta, accounts, trx_hash, timestamp, parameters); // 3.
}
```

2. The `instruction.program_id_index` indicates the position of the program account in the accounts array. For example, if `program_index_id = 5`, it means that the program account will be at position number 5 in the `accounts` array.
5. If the instruction account is the Token Program Account (i.e. `TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA`), this means that the instruction executed in the transaction has been produced by the Token Program. Therefore, you process the instruction further by calling the `process_token_instruction(...)` function to extract token-related information, such as transfers or mints.
8. Every top-level instruction holds inner instructions. If the top-level instruction is not from the Token Program, you check if any Inner Instruction is from the Token Program by calling the `process_inner_instructions(...)` function.
- A top-level instruction could hold a Token Program instruction within its inner instructions. The `process_inner_instructions(...)` checks if there are Token Program among the inner instructions of every top-level instruction.

Copy
```
pub fn process_inner_instructions(
    output: &mut Output,
    instruction_index: u32,
    meta: &TransactionStatusMeta,
    accounts: &Vec<String>,
    trx_hash: &String,
    timestamp: i64,
    parameters: &TokenParams,
) {
    meta.inner_instructions // 1.
        .iter()
        .filter(|inst| inst.index == instruction_index) // 2.
        .for_each(|inst| { // 3.
            inst.instructions
                .iter() // 4.
                .filter(|&inner_instruction| { // 5.
                    let instruction_program_account = &accounts[inner_instruction.program_id_index as usize];
                    instruction_program_account == constants::TOKEN_PROGRAM
                })
                .for_each(|inner_instruction| {
                    match process_token_instruction( // 6.
                        trx_hash,
                        timestamp,
                        &inner_instruction.data,
                        &inner_instruction.accounts,
                        meta,
                        accounts,
                        output,
                        parameters
                    ) {
                        Err(err) => {
                            panic!("trx_hash {} filtering inner instructions: {}", trx_hash, err)
                        }
                        Ok(()) => {}
                    }
                })
        });
}
```

2. The `TransactionStatusMeta` object holds an array with the inner instructions of the transaction (an array of `InnerTransactions` objects).
5. Because the inner instructions are at the transaction level (contained within the `TransactionStatusMeta`), you keep only the inner transactions belonging to the current top-level instruction. For this purpose, an index variable (`instruction_index`) is passed as a parameter. Essentially, you are matching every top-level instruction with its corresponding `InnerTransactions` object. The filtering should only keep **one** `InnerTransactions` object, as every top-level instruction should only have one `InnerTransactions` object.
8. The `InnerTransactions` object is a just wrapper for the array of inner transactions. For every `InnerTransactions` object filtered (which should be **only one**), you actually extract the inner instructions.
11. You iterate over the array of inner instructions.
14. You only keep Token Program inner instructions.
17. You process every Token Program inner instruction found further by calling the `process_token_instruction(...)`.

Once you have identified all the Token Program instructions, the `proces_token_instruction(...)` function extracts transfer or mint data from these instructions. To easily extract data from a Token Program instruction, the Substreams relies on the `substreams-solana-program-instructions` Rust crate, which provides useful helper functions.

Copy
```
fn process_token_instruction(
    trx_hash: &String,
    timestamp: i64,
    data: &Vec<u8>,
    inst_accounts: &Vec<u8>,
    meta: &TransactionStatusMeta,
    accounts: &Vec<String>,
    output: &mut Output,
    parameters: &TokenParams,
) -> Result<(),Error> {
    match TokenInstruction::unpack(&data) { // 1.
        Err(err) => { // 2.
            substreams::log::info!("unpacking token instruction {:?}", err);
            return Err(anyhow::anyhow!("unpacking token instruction: {}", err));
        }
        Ok(instruction) => match instruction { // 3.
            TokenInstruction::Transfer { amount: amt }  => { // 4.
                let authority = &accounts[inst_accounts[2] as usize];
                if is_token_transfer(&meta.pre_token_balances, &authority, &parameters.token_contract) { // 5.
                    let source = &accounts[inst_accounts[0] as usize];
                    let destination = &accounts[inst_accounts[1] as usize];
                    output.transfers.push(Transfer { // 6.
                        trx_hash: trx_hash.to_owned(),
                        timestamp,
                        from: source.to_owned(),
                        to: destination.to_owned(),
                        amount: amount_to_decimals(amt as f64, parameters.token_decimals as f64),
                    });
                    return Ok(());
                }
            }
            // ...code omitted...
        }
    }
}
```

2. The `TokenInstruction::unpack(...)` function decodes the instruction and allows you to identify the action executed: `Transfer`, `TransferChecked`, `Mint`, or `Burn`.
5. Controlled way to handle errors from the `unpack(...)` function.
8. If there are no errors, then you can handle every action (`Transfer`, `Mint`...) differently.
11. Handle the `Transfer` instruction.
14. Call the `is_token_transfer(...)` to verify if the transfer is from the specified in the parameters of the Substreams module. Note that you pass `parameters.token_contract` as a parameter to the function.
17. Create a new `Transfer` object from the Protobuf with the corresponding data. This object is added to the `Output` object and will be emitted as the output of the Substreams.

The code for other actions (`Mint`, `Burn`...) is analogous to the code of the `Transfer` instructions.

[PreviousFilter Transactions](/tutorials/solana/explore-solana/filter-transactions)[NextNFT Trades](/tutorials/solana/nft-trades)

Last updated 9 months ago

---

## Foundational Modules | Substreams
Source: https://docs.substreams.dev/tutorials/cosmos/injective/foundational

The [Injective Foundational Substreams](https://github.com/streamingfast/substreams-foundational-modules/injective-common) contains Substreams modules, which retrieve fundammental data on the Injective blockchain.

You can use the Injective Foundational Modules as the input for your Substreams or subgraph.

The Foundational Modules are the base of the code generation tools provided by the Substreams CLI.

## # Before You Begin
- [Install the Substreams CLI](/documentation/consume/installing-the-cli)
- [Get an authentication token](/documentation/consume/authentication)
- [Learn about the basics of the Substreams](/documentation/develop/manifest-modules)
- [Go through the Block Stats Substreams tutorial](/tutorials/cosmos/injective/block-stats)

Clone the [Foundational Substreams GitHub repository](https://github.com/streamingfast/substreams-foundational-modules), move to the `injective-common` folder, and open it in an IDE of your choice (for example, VSCode).

## # The Foundational Modules

First, take a look at the Substreams manifest (`substreams.yaml`), which contains the declaration of all the Injective Foundational Modules.

Copy
```
...output omitted...
modules:
- name: all_transactions # 1.
    kind: map
    initialBlock: 0
    inputs:
- source: sf.cosmos.type.v2.Block
    output:
      type: proto:sf.substreams.cosmos.v1.TransactionList
- name: all_events # 2.
    kind: map
    initialBlock: 0
    inputs:
- source: sf.cosmos.type.v2.Block
    output:
      type: proto:sf.substreams.cosmos.v1.EventList
- name: index_events # 3.
    kind: blockIndex
    inputs:
- map: all_events
    output:
      type: proto:sf.substreams.index.v1.Keys
    doc: |
      `index_events` sets the keys corresponding to every event 'type' 
      ex: `coin_received`, `message` or `injective.peggy.v1.EventDepositClaim`
- name: filtered_events # 4.
    kind: map
    blockFilter:
      module: index_events
      query:
        params: true
    inputs:
- params: string
- map: all_events
    output:
      type: proto:sf.substreams.cosmos.v1.EventList
    doc: |
      `filtered_events` reads from `all_events` and applies a filter on the event types, only outputing the events that match the filter. 
      The only operator that you should need to use this filter is the logical or `||`, because each event can only match one type.
```

2. The `all_transactions` module provides access to all the transactions of the Injective blockchain. It receives a raw Injective block object as input (`sf.cosmos.type.v2.Block`), and outputs a list of transactions object (`sf.substreams.cosmos.v1.TransactionList`).
5. The `all_events` module provides access to all the events in the Injective blockchain. It receives a raw Injective block as input (`sf.cosmos.type.v2.Block`), and outputs a list of events object (`sf.substreams.cosmos.v1.EventList`).
8. The `index_events` module uses the `all_events` module to create a cache where events are sorted based on their `type` field. This cache helps in the performance of the module. You can read more about *index modules* in the [correspoding documentation](https://github.com/streamingfast/substreams/blob/develop/docs/new/develop/indexes/README.md).
11. The `filtered_events` allows you to use the `index_events` module (i.e. using the cache of events), to filter only the event types you are interested in. The string parameter passed as input is used to specify which events you want to consume.

## # Use The Foundational Modules

All this module are pre-programmed and ready to use in your Substreams or your subgraphs.

### # Use in a Substreams

Using another module as input for your Substreams is very easy: you just have to declare it in the manifest.

For example, the following declaration of the `my_test_module` module receives the `all_transactions` module as input:

Copy
```
- name: my_test_module
  kind: map
  inputs:
- map: all_transactions
  output:
    type: proto:sf.test.MyOutputObject
```

Then, in the Rust handler declaration, you can simply receive the output object of the `all_transactions` module:

Copy
```
# [substreams::handlers::map]
fn my_test_module(transactions: TransactionList) -> Result<MyOutputObject, Error> {
    // Your code here
}
```
### # Use in a Subgraph

You can easily import a Substreams module into a subgraph by defining it in the subgraph manifest (`subgraph.yaml`):

Copy
```
specVersion: 1.0.0
indexerHints:
  prune: auto
schema:
  file: ./schema.graphql
dataSources:
- kind: substreams
    name: Events
    network: injective-mainnet
    source:
      package:
        file: injective-foundational-v0.1.0.spkg # 1.
        moduleName: all_events # 2.
    mapping:
      apiVersion: 0.0.7
      kind: substreams/graph-entities
      file: ./src/mapping.ts # 3.
      handler: handleEvents # 4.
```

2. Define the Substreams package (`.spkg`) containing the module of your choice.
5. Define the module that you want to use (which must be contained in the package).
8. Define the file where you will create the handler.
11. Define the handler name.

Then, in the `mappings.ts` file you can create the `handleEvents` function.

Copy
```
export function handleEvents(bytes: Uint8Array): void { // 1.
    const eventList: EventList = Protobuf.decode<EventList>(bytes, EventList.decode); // 2.
    const events = eventList.events;
    // Your code here
}
```

2. Definition of the function, which receives the raw bytes of the Substreams.
5. Decode the bytes into the `EventList` Protobuf object, which is the output of the Substreams.

You can check out a full example in the [USDT Exchange Volume tutorial](/tutorials/cosmos/injective/usdt-exchanges)

[PreviousSimple Substreams Example](/tutorials/cosmos/injective/block-stats)[NextDojo DEX USDT Volume Subgraph Example](/tutorials/cosmos/injective/usdt-exchanges)

Last updated 5 months ago

---

## Injective | Substreams
Source: https://docs.substreams.dev/tutorials/cosmos/injective

[Simple Substreams Example](/tutorials/cosmos/injective/block-stats)[Foundational Modules](/tutorials/cosmos/injective/foundational)[Dojo DEX USDT Volume Subgraph Example](/tutorials/cosmos/injective/usdt-exchanges)[PreviousCosmos](/tutorials/cosmos)[NextSimple Substreams Example](/tutorials/cosmos/injective/block-stats)

Last updated 6 months ago

---

## Chains and endpoints | Substreams
Source: https://docs.substreams.dev/reference-and-specs/chains-and-endpoints

[PreviousResult struct](/tutorials/rust/result)[NextDevelopment Container Reference](/reference-and-specs/devcontainer-ref)

Last updated 7 days ago

---

## Manifests Reference | Substreams
Source: https://docs.substreams.dev/reference-and-specs/manifests

- *Tip**: When writing and checking your `substreams.yaml` file, it may help to check your manifest against our [JSON schema](https://json-schema.org/) to ensure there are no problems. JSON schemas can be used in [Jetbrains](https://www.jetbrains.com/help/idea/json.html#ws_json_schema_add_custom) and [VSCode](https://marketplace.visualstudio.com/items?itemName=redhat.vscode-yaml). Our manifest schema can be seen [here](https://github.com/streamingfast/substreams/blob/develop/docs/schemas/manifest-schema.json).

Manifests overview
- -----------------

The manifest is the high-level outline for a Substreams module. The manifest file is used for defining properties specific to the current Substreams module and identifying the dependencies between the `inputs` and `outputs` of modules.

This reference documentation **provides a guide for all fields and values** used in a Substreams manifest.

## # `specVersion`

Excerpt pulled from the example Substreams manifest.

manifest excerptCopy
```
specVersion: v0.1.0
```

Use `v0.1.0` for the `specVersion` field.

## # `package`

Excerpt pulled from the example Substreams manifest.

manifest excerptCopy
```
package:
  name: module_name_for_project
  version: v0.5.0
  doc: |
    Documentation heading for the package.
    More detailed documentation for the package.
```
### # `package.name`

The `package.name` field is used to identify the package.

The `package.name` field infers the filename when the [`pack`](https://substreams.streamingfast.io/reference-and-specs/command-line-interface#pack) command is run by using `substreams.yaml` as a flag for the Substreams package.

The content of the `name` field must match the regular expression: `^([a-zA-Z][a-zA-Z0-9_]{0,63})$`. For consistency, use the `snake_case` naming convention.

The regular expression ruleset translates to the following:
- 64 characters maximum
- Separate words by using `_`
- Starts by using `a-z` or `A-Z` and can contain numbers thereafter

### # `package.version`

The `package.version` field identifies the package for the Substreams module.
- *Note**: The`package.version` **must respect** [Semantic Versioning, version 2.0](https://semver.org/)

### # package.url

The `package.url` field identifies and helps users discover the source of the Substreams package.

### # package.doc

The `package.doc` field is the documentation string of the package. The first line is used by the different UIs as a short-form description.

This field should be written in Markdown format.

## # `imports`

The `imports` section allow you to import third-party Substreams packages. It adds local references to modules in those packages, and pull in the WASM code, Protobuf and modules into the current Package.

Relying on imports rather than copying source code from third-party packages allows you to leverage server-side caches, and lower your costs.

Example:

Copy
```
imports:
  sol: https://spkg.io/streamingfast/solana-explorer-v0.2.0.spkg
  # or:
  ethereum: substreams-ethereum-v1.0.0.spkg
  token: ../eth-token/substreams.yaml
...
modules:
...
    inputs:
- map: sol:map_block_without_votes
# replacing:
#    inputs:
#      - source: sf.solana.type.v1.Block
```

Note the `:` separator that signifies to use the imported namespace, as defined under `imports`.

The filename can be absolute or relative or a remote path prefixed by `http://` or `https://`. It can also be an IPFS reference.

## # `protobuf`

The `protobuf` section points to the Google Protocol Buffer (protobuf) definitions used by the Rust modules in the Substreams module.

Copy
```
protobuf:
  files:
- google/protobuf/timestamp.proto
- pcs/v1/pcs.proto
- pcs/v1/database.proto
  importPaths:
- ./proto
- ../../external-proto
```

The Substreams packager loads files in any of the listed `importPaths`.
- *Note**: The `imports` section of the manifest also affects which `.proto` files are used in the final Substreams package.

Protobufs and modules are packaged together to help Substreams clients decode the incoming streams. Protobufs are not sent to the Substreams server in network requests.

[Learn more about Google Protocol Buffers](https://protobuf.dev/) in the official documentation provided by Google.

## # `binaries`

The `binaries` field specifies the WASM binary code to use when executing modules.

The `modules[].binary` field uses a default value of `default`.

Copy
```
binaries:
  default:
    type: wasm/rust-v1
    file: ./target/wasm32-unknown-unknown/release/my_package.wasm
  other:
    type: wasm/rust-v1
    file: ./snapshot_of_my_package.wasm
```
- *Important***:* Defining the `default` binary is required when creating a Substreams manifest.

See the [`binary`](/reference-and-specs/manifests#module-binary) field under `modules` to see its use.

### # `binaries[name].type`

The type of code and implied virtual machine for execution. There is **only one virtual machine available** that uses a value of: `wasm/rust-v1`.

### # `binaries[name].file`

The `binaries[name].file` field references a locally compiled [WASM module](https://webassembly.github.io/spec/core/syntax/modules.html). Paths for the `binaries[name].file` field are absolute or relative to the manifest's directory. The **standard location** of the compiled WASM module is the **root directory** of the Substreams module.
- *Tip**: The WASM file referenced by the `binary` field is picked up and packaged into an `.spkg` when invoking the [`pack`](https://substreams.streamingfast.io/reference-and-specs/command-line-interface#pack) and [`run`](https://substreams.streamingfast.io/reference-and-specs/command-line-interface#run) commands through the [`substreams` CLI](/reference-and-specs/command-line-interface).

## # network

The `network` field specifies the blockchain where the Substreams will be executed.

Copy
```
network: solana
```

or

Copy
```
network: ethereum
```
## # image

The `image` field specifies the icon displayed for the Substreams package, which is used in the [Substreams Regsitry](https://substreams.dev). The path is relative to the folder where the manifest is.

Copy
```
image: ./ethereum-icon.png
```
## # sink

The `sink` field specifies the sink you want to use to consume your data (for example, a database or a subgraph).

### # Sink `module`

Specifies the name of the module that emits the data to the sink. For example, `db_out` or `graph_out`.

### # Sink `type`

Specifies the service used to consume the data. For example, `sf.substreams.sink.subgraph.v1.Service` for subgraphs, or `sf.substreams.sink.sql.v1.Service` for databases.

### # Sink `config`

Specifies the configuration specific to every sink. This field is different for every sink.
- *Database Config**

Copy
```
sink:
  module: db_out
  type: sf.substreams.sink.sql.v1.Service
  config:
    schema: "./schema.sql"
    engine: clickhouse
    postgraphile_frontend:
      enabled: false
    pgweb_frontend:
      enabled: false
    dbt_config:
      enabled: true
      files: "./path/to/folder"
      run_interval_seconds: 300
```
- `schema`: SQL file specifying the schema.
- `engine`: `postgres` or `clickhouse`.
- `postgraphile_frontend.enabled`: enables or disables the Postgraphile portal.
- `pgweb_frontend.enabled`: enables or disables the PGWeb portal.
- `dbt_config`: specifies the configuration of dbt engine.
- `enabled`: enables or disabled the dbt engine.
- `files`: path to the dbt models.
- `run_interval_seconds`: execution intervals in seconds.
- *Subgraph Config**

Copy
```
sink:
  module: graph_out
  type: sf.substreams.sink.subgraph.v1.Service
  config:
    schema: "./schema.graphql"
    subgraph_yaml: "./subgraph.yaml"
```
- `schema`: path to the GraphQL schema.
- `subgraph_yaml`: path to the Subgraph manifest.

## # `modules`

This example shows one map module, named `events_extractor` and one store module, named `totals` :

substreams.yamlCopy
```
- name: events_extractor
    kind: map
    initialBlock: 5000000
    binary: default  # Implicit
    inputs:
- source: sf.ethereum.type.v2.Block
- store: myimport:prices
    output:
      type: proto:my.types.v1.Events
    doc:
      This module extracts events
      
      Use in such and such situations
- name: totals
    kind: store
    updatePolicy: add
    valueType: int64
    inputs:
- source: sf.ethereum.type.v2.Block
- map: events_extractor
```
### # Module `name`

The identifier for the module, prefixed by a letter, followed by a maximum of 64 characters of `[a-zA-Z0-9_]`. The [same rules applied to the `package.name`](/reference-and-specs/manifests#package.name) field applies to the module `name`, including the convention to use `snake_case` names.

The module `name` is the reference identifier used on the command line for the `substreams` [`run`](https://substreams.streamingfast.io/reference-and-specs/command-line-interface#run) command. The module `name` is also used in the [`inputs`](/reference-and-specs/manifests#modules-.inputs) defined in the Substreams manifest.

The module `name` also corresponds to the **name of the Rust function** invoked on the compiled WASM code upon execution. The module `name` is the same `#[substreams::handlers::map]` as defined in the Rust code. Maps and stores both work in the same fashion.
- *Important***:* When importing another package, all module names are prefixed by the package's name and a colon. Prefixing ensures there are no name clashes across multiple imported packages and almost any name can be safely used for a module `name`.

### # Module `initialBlock`

The initial block for the module is where Substreams begins processing data for a module. The runtime never processes blocks prior to the one for any given module.

If all the inputs have the same `initialBlock`, the field can be omitted and its value is inferred by its dependent [`inputs`](/reference-and-specs/manifests#modules-.inputs).

`initialBlock` becomes **mandatory** **when inputs have different values**.

### # Module `kind`

There are two module types for `modules[].kind`:
- `map`
- `store`

### # Module `updatePolicy`

Specifies the merge strategy for two contiguous partial stores produced by parallelized operations.

The values for `modules[].updatePolicy` are defined using specific rules stating:
- `set`, the last key wins the merge strategy
- `set_if_not_exists`, the first key wins the merge strategy
- `append`, concatenates two keys' values
- `add`, sum the two keys' values
- `min`, min between two keys' values
- `max`, max between two keys' values
- `set_sum`, either `set` the value or `sum` the two keys' values

### # Module `valueType`

Tip: The module `updatePolicy` field is only available for modules of `kind: store`.

Specifies the data type of all keys in the `store`, and determines what WASM imports are available to the module and are able to write to the `store`.

The values for `modules[].valueTypes` can use various types including:
- `bigfloat`
- `bigint`
- `int64`
- `bytes`
- `string`
- `proto:path.to.custom.protobuf.Model`

Tip: The module `valueType` field is only available for modules of `kind: store`.

### # Module `binary`

An identifier referring to the [`binaries`](/reference-and-specs/manifests#binaries) section of the Substreams manifest.

The `modules[].binary` field overrides which binary is used from the `binaries` declaration section. This means multiple WASM files can be bundled in the Package.

Copy
```
modules:
- name: hello
    binary: other
  ...
```

The default value for `binary` is `default`. Therefore, a `default` binary must be defined under [`binaries`](/reference-and-specs/manifests#binaries).

### # Module `inputs`

substreams.yamlCopy
```
inputs:
- params: string
- source: sf.ethereum.type.v2.Block
- store: my_store
      mode: deltas
- store: my_store # defaults to mode: get
- map: my_map
```

The `inputs` field is a **list of input structures**. One of three keys is required for every object.

The key types for `inputs` include:
- `source`
- `store,` used to define `mode` keys
- `map`
- `params`

You can find more details about inputs in the [Developer Guide's section about Modules](https://github.com/streamingfast/substreams/blob/develop/docs/new/developers-guide/modules/types.md).

### # Module `output`

substreams.yamlCopy
```
output:
    type: proto:eth.erc721.v1.Transfers
```

The value for `type` is always prefixed using `proto:` followed by a definition specified in the protobuf definitions, and referenced in the `protobuf` section of the Substreams manifest.
- *Tip**: The module `output` field is only available for modules of `kind: map`.

### # Module `doc`

This field should contain Markdown documentation of the module. Use it to describe how to use the params, or what to expect from the module.

## # `params`

The `params` mapping changes the default values for modules' parameterizable inputs.

Copy
```
modules:
  ...
params:
  module_name: "default value"
  "imported:module": "overridden value"
```

You can override those values with the `-p` parameter of `substreams run`.

When rolling out your consuming code -- in this example, Python -- you can use something like:

Copy
```
my_mod = [mod for mod in pkg.modules.modules if mod.name == "store_pools"][0]
my_mod.inputs[0].params.value = "myvalue"
```

which would be inserted just before starting the stream.

Params that are defined under `networks` do not need to be repeated here (their value will be overwritten)

## # `network`

The `network` field specifies the default network to be used with this Substreams. It will help the client choose an endpoint if necessary, and will be used as the default value when applying the values defined under `networks`.

## # `networks`

The `networks` allows specifying per-network `params` and `initialBlock` for each module:

Copy
```
networks:
  mainnet:
    initialBlock:
      mod1: 200
      lib:mod1: 400
    params:
      mod2: "addr=0x1234"
  sepolia:
    [...]
```

You can override values for modules imported from other .spkg.

Every local module specified under `networks` must have a value for **each network**

[PreviousSubstreams CLI reference](/reference-and-specs/command-line-interface)[NextGUI Reference](/reference-and-specs/gui)

Last updated 2 months ago

---

## Inputs | Substreams
Source: https://docs.substreams.dev/documentation/develop/manifest-modules/inputs

`inputs` overview
- ----------------

Modules receive `inputs` of three types:
- `source`
- `map`
- `store`
- `params`

Input type `source`
- ------------------

An `inputs` of type `source` represents a chain-specific, Firehose-provisioned protobuf object. Learn more about the supported protocols and their corresponding message types in the [Chains and inputs documentation](/reference-and-specs/chains-and-endpoints).
- *Note**: The different blockchains reference different `Block` objects. For example, Solana references its `Block` object as `sf.solana.type.v1.Block`. Ethereum-based Substreams modules specify `sf.ethereum.type.v2.Block.`

The `source` `inputs` type \_\_ is defined in the Substreams manifest. It is important to specify the correct `Block` object for the chain.

Copy
```
modules:
- name: my_mod
  inputs:
- source: sf.ethereum.type.v2.Block
```
### # `Clock` object

The `sf.substreams.v1.Clock` object is another source type available on any of the supported chains.

The `sf.substreams.v1.Clock` represents:
- `Block` `number`
- `Block` `ID`
- `Block` `timestamp`

Input type `params`
- ------------------

An `inputs` of type `params` represents a parameterizable module input. Those parameters can be specified either:
- in the `params` section of the manifest,
- on the command-line (using `substreams run -p` for instance),
- by tweaking the protobuf objects directly when consuming from your favorite language

See the [Manifest's `params` manifest section of the Reference & specs](/reference-and-specs/manifests#params) for more details.

Input type `map`
- ---------------

An input of type `map` represents the output of another `map` module. It defines a parent-child relationship between modules.

The object's type is defined in the [`output.type`](/reference-and-specs/manifests#modules-.output) attribute of the `map` module.
- *Important**: The graph built by input dependencies is a Directed Acyclic Graph, which means there can be no circular dependencies.

Define the `map` input type in the manifest and choose a name for the `map` reflecting the logic contained within it.

manifest excerptCopy
```
  inputs:
- map: my_map
```

Learn more about `maps` in the Modules section.

Input type `store`
- -----------------

A `store inputs` type represents the state of another `store` used by the Substreams module being created.

The developer defines the `store` `inputs` type in the Substreams manifest and gives the `store` a descriptive name that reflects the logic contained within it, similar to a `map`.

Store modules are set to `get` mode by default:

manifest excerptCopy
```
  inputs:
- store: my_store # defaults to mode: get
```

Alternatively, set `stores` to `deltas` mode by using:

manifest excerptCopy
```
  inputs:
- store: my_delta_store
      mode: deltas
```
## # Store access `mode`

Substreams uses two types of `mode` for modules:
- `get`
- `delta`

## # Store constraints
- A `store` can only receive `inputs` as read-only.
- A `store` cannot depend on itself.

## # `get` mode

`get` mode provides a key-value store readily queryable and guaranteed to be in sync with the block being processed.
- *Tip**: `get` `mode` is the default mode for modules.

## # `delta` mode

`delta` `mode` modules are [protobuf objects](https://github.com/streamingfast/substreams/blob/develop/pb/sf/substreams/v1/substreams.proto#L124) containing all the changes occurring in the `store` module available in the same block.

`delta` mode enables you to loop through keys and decode values mutated in the module.

### # `store` `deltas`

The protobuf model for `StoreDeltas` is defined by using:

Copy
```
message StoreDeltas {
  repeated StoreDelta deltas = 1;
}
message StoreDelta {
  enum Operation {
    UNSET = 0;
    CREATE = 1;
    UPDATE = 2;
    DELETE = 3;
  }
  Operation operation = 1;
  uint64 ordinal = 2;
  string key = 3;
  bytes old_value = 4;
  bytes new_value = 5;
}
```
[PreviousModule types](/documentation/develop/manifest-modules/types)[NextOutput](/documentation/develop/manifest-modules/outputs)

Last updated 1 year ago

---

## Result struct | Substreams
Source: https://docs.substreams.dev/tutorials/rust/result

In Rust, the `Result<T, E>` struct is used to abstract both a successful response (if it exists) and an error (if it occurs). Let's better understand through an example.

Basic Usage
- ----------

Consider that you have a function `divide(num1, num2)`, which executes the division between two numbers. As you already know, dividing by 0 is undefined, and generates an error in Rust. You can use `Result` to return a controlled error.

Copy
```
fn divide(num1: u32, num2: u32) -> Result<u32, String> {
    if num2 == 0 {
        return Err(String::from("You can't divide by 0"));
    }
    return Ok(num1 / num2);
}
fn main() {
    let result = divide(6, 0);
    if result.is_ok() {
        println!("This is the happy path: {}", result.unwrap())
    } else {
        println!("This is the error: {}", result.err().unwrap())
    }
}
```

Let's inspect the `divide` function:

Copy
```
fn divide(num1: u32, num2: u32) -> Result<u32, String> { // 1.
    if num2 == 0 {
        return Err(String::from("You can't divide by 0")); // 2.
    }
    return Ok(num1 / num2); // 3.
}
```

2. Declaration of the function. Two unsigned numbers of 32-bit length are passed as parameters. The return type is `Result<u32, String>`: the first type (`u32`) is for the successful response, and the second type (`String`) is for the error response.
5. If dividing by 0, you return an error String.
8. If not, you return the result of the division (`u32`).

The `Result<T, E>` is really an enum that can take two values: `Ok(T)` (success) and `Err(E)` (error).

In the previous code, when you return `Err(String)`, the success part is automatically empty. At the same time, when you return `Ok(u32)`, the error part is empty.

Now, let's see how you can interact with this result.

Copy
```
fn main() {
    let result = divide(6, 0); // 1.
    if result.is_ok() { // 2.
        println!("This is the happy path: {}", result.unwrap())
    } else { // 3.
        println!("This is the error: {}", result.err().unwrap())
    }
}
```

2. You invoke the function and store the `Result<T,E>` enum in a variable.
5. If the result *is ok* (i.e. the happy path has been returned), you can take its value by using the `result.unwrap()` method.
8. If the error has been returned, you can return the error string by using the `result.err().unwrap()` method.

The output of the program for `divide(6,2)` (happy path) is:

Copy
```
This is the happy path: 3
```

The output of the program for `divide(6,0)` (error) is:

Copy
```
This is the error: You can't divide by 0
```

The Shortcut
- -----------

Checking with an `if` condition whether the result contains an error is a valid approach. However, Rust includes a shortcut to improve this.

In the previous example, consider that you want to invoke the `divide` function from another function that performs other computations.

Copy
```
fn divide(num1: u32, num2: u32) -> Result<u32, String> {
    if num2 == 0 {
        return Err(String::from("You can't divide by 0"));
    }
    return Ok(num1 / num2);
}
fn computations() -> Result<u32, String> {
    let result = divide(6, 0); // Performing the division
    if result.is_err() { // If the division returns an error, then you return an error.
        return Err(result.err().unwrap());
    }
    let division_result = result.unwrap();
    return Ok(division_result + 5);
}
fn main() {
    let result = computations();
    if result.is_ok() {
        println!("This is the happy path: {}", result.unwrap())
    } else {
        println!("This is the error: {}", result.err().unwrap())
    }
}
```

Now, the Rust program adds `5` to the result of the division, checking that the division is correct first. Although this approach is correct, Rust provides a `?` symbol that simplifies the logic:

Copy
```
fn divide(num1: u32, num2: u32) -> Result<u32, String> {
    if num2 == 0 {
        return Err(String::from("You can't divide by 0"));
    }
    return Ok(num1 / num2);
}
fn computations() -> Result<u32, String> {
    let division_result = divide(6, 0)?;
    return Ok(division_result + 5);
}
fn main() {
    let result = computations();
    if result.is_ok() {
        println!("This is the happy path: {}", result.unwrap())
    } else {
        println!("This is the error: {}", result.err().unwrap())
    }
}
```

The `?` symbol after a `Result` enum does two things:

2. If successful, it unwraps the result (in this case, a `u32` number), and stores it in a variable `let division_result = divide(6, 0)?;`
5. If an error occurs, it returns the error directly. In this example, the error type of the `divide` and the `computations` function is the same (a `String`).

In Substreams
- ------------

The `Result` enum is used in Substreams to return the data (or the errors) of a module. For example, if you take the `map_filter_transactions` module from the [Ethereum Explorer tutorial](https://github.com/streamingfast/substreams/blob/develop/tutorials/ethereum/exploring-ethereum/map_filter_transactions_module/README.md):

Copy
```
[...]
# [substreams::handlers::map]
fn map_filter_transactions(params: String, blk: Block) -> Result<Transactions, Vec<substreams::errors::Error>> {
    let filters = parse_filters_from_params(params)?;
    let transactions: Vec<Transaction> = blk
        .transactions()
        .filter(|trans| apply_filter(&trans, &filters))
        .map(|trans| Transaction {
            from: Hex::encode(&trans.from),
            to: Hex::encode(&trans.to),
            hash: Hex::encode(&trans.hash),
        })
        .collect();
    Ok(Transactions { transactions })
}
[...]
```

This module returns a `Result<Transactions, Vec<substreams::errors::Error>>` enum. If successful, it returns the transactions filtered; in the case of an error, it returns the `substreams::errors::Error` error, which is a Substreams wrapper for a generic [anyhow Rust error](https://docs.rs/anyhow/latest/anyhow/).

[PreviousOption struct](/tutorials/rust/option)[NextChains and endpoints](/reference-and-specs/chains-and-endpoints)

Last updated 10 months ago

---

## GUI Reference | Substreams
Source: https://docs.substreams.dev/reference-and-specs/gui

[PreviousManifests Reference](/reference-and-specs/manifests)[NextGlossary](/reference-and-specs/glossary)

Last updated 1 year ago

---

## Filter Transactions | Substreams
Source: https://docs.substreams.dev/tutorials/solana/explore-solana/filter-transactions

[PreviousFilter Instructions](/tutorials/solana/explore-solana/filter-instructions)[NextSPL Token Tracker](/tutorials/solana/token-tracker)

Last updated 9 months ago

---

## Option struct | Substreams
Source: https://docs.substreams.dev/tutorials/rust/option

The Problem
- ----------

Consider that you want to implement a function that returns a username, given the corresponding user identifier. The signature of the function could be as follows:

Copy
```
fn get_username_by_id(id: u32) -> String {
    // function body
}
```

In a success case, you pass the user identifier as a parameter and the function returns the corresponding username. However, **what happens if the function does not have a username for the given identifier?** A possible solution is to return an empty string:
- If the function **is able to retrieve the data**, then the string returned is the username.
- If the function **is NOT able to retrieve the data**, then the string returned is the empty string (`''`).

Although this is a valid approach, it creates hidden logic that is not visible unless you deep dive into the function code.

The Solution
- -----------

Rust provides a better way of dealing with these situations by using the `Option<T>` enum. This enum has two possible values: `Some(T)` (used when the returned value is present) and `None` (used when the returned value is not present). Therefore, the previous function can be refactored to:

Copy
```
fn get_username_by_id(id: u32) -> Option<String> {
    // function body
}
```

Now, the function works as follows:
- If the function **is able to retrieve the data**, then a `Some` value containing the string is returned.
- If the function **is NOT able to retrieve the data**, then a `None` value is returned.

Let's complete the body of the function:

Copy
```
fn get_username_by_id(id: u32) -> Option<String> { // 1.
    match(id) {
        1 => Some(String::from("Susan")), // 2.
        2 => Some(String::from("John")), // 3.
        _ => None // 4.
    }
}
```

2. Given a user identifier, return the corresponding username if it exists.
5. If `id == 1`, then a `Some` struct containing the string is returned.
8. If `id == 2`, then a `Some` struct containing the string is returned.
11. If `id` does not match with any of the provided identifiers, then a `None` struct is returned.

Using Options
- ------------

The `Option<T>` struct contains two helper methods to check if the returned type is `Some` or `None`: the `.is_some()` and `.is_none()` methods. Let's see how to use these methods:

Copy
```
fn get_username_by_id(id: u32) -> Option<String> {
    match(id) {
        1 => Some(String::from("Susan")),
        2 => Some(String::from("John")),
        _ => None
    }
}
fn main() {
    let user1 = get_username_by_id(1); // 1.
    let user10 = get_username_by_id(10); // 2.
    if (user1.is_some()) { // 3.
        println!("User with id = 1 holds username {}", user1.unwrap())
    }
    if (user10.is_none()) { // 4.
        println!("User with id = 10 does not exist")
    }
}
```

2. Get the user with `id == 1`.
5. Get the user with `id == 10`.
8. If the function returned a name for `id == 1`, then `user1.is_some()` returns `true`.
11. If the function did NOT return a name for `id == 10`, then `user1.is_none()` returns `true`.

You can also use [pattern matching](https://doc.rust-lang.org/book/ch18-03-pattern-syntax.html) instead of the helper methods:

Copy
```
fn get_username_by_id(id: u32) -> Option<String> {
    match(id) {
        1 => Some(String::from("Susan")),
        2 => Some(String::from("John")),
        _ => None
    }
}
fn main() {
    let user1 = get_username_by_id(1);
    let user10 = get_username_by_id(10);
    
    match (&user1) {
        Some(name) => println!("User with id = 1 holds username {}", &user1.unwrap()),
        None => println!("No user with id = 1 found")
    }
    
    match (&user10) {
        Some(name) => println!("User with id = 10 holds username {}", &user10.unwrap()),
        None => println!("No user with id = 10 found")
    }
}
```
[PreviousRust](/tutorials/rust)[NextResult struct](/tutorials/rust/result)

Last updated 10 months ago

---

## Rust Dependencies | Substreams
Source: https://docs.substreams.dev/documentation/develop/rust-crates

Rust crates overview
- -------------------

The official [`substreams` crate](https://crates.io/crates/substreams) helps developers create module handlers.
- Use the [`substreams-ethereum` crate](https://crates.io/crates/substreams-ethereum) for Ethereum and other Ethereum-compatible chains.
- Use the [`substreams-solana` crate](https://crates.io/crates/substreams-solana) for the Solana blockchain.
- Use the [`substreams-antelope` crate](https://github.com/pinax-network/substreams-antelope) for the Antelope blockchain (by [Pinax Network](https://pinax.network/))
- *Note**: If a crate is not available for Substreams, you can use the `spkg` release for the chain, which includes the `Block` protobuf model, and generate the Rust structs yourself.

## # Third-party libraries

Any third-party library capable of compiling `wasm32` can be used for execution in Substreams services.

Some libraries include kernel syscalls or other operations unavailable in the Substreams execution environment and cannot be compiled to WASM. The internal functionality of third-party libraries is an essential consideration for Substreams development.

Helpful information people found through the use of third-party libraries and Substreams together include:
- [`tiny_keccak`](https://docs.rs/tiny-keccak): an implementation of Keccak-derived functions specified in FIPS-202, SP800-185, and KangarooTwelve.

## # Git Versions

[Specifying dependencies from Git repositories](https://doc.rust-lang.org/cargo/reference/specifying-dependencies.html#specifying-dependencies-from-git-repositories) is possible in Rust, but it is **NOT recommended** by the Substreams team, as they are not fully tested and can bring bugs to your Substreams project.

The Substreams team recommends using the templates provided in the [Examples section](https://github.com/streamingfast/substreams/blob/develop/docs/new/develop/examples.md) as a starting point to develop your Substreams application.

## # Logs

The `substreams` crate allows you to log data in the Substreams execution for debugging purposes. The `std::println(...)` function of Rust won't work in Substreams.

Use the `substreams::log::pritnln(...)` function in your Rust code to log data during the execution.

Copy
```
# [substreams::handlers::map]
fn all_transactions_without_votes(blk: Block) -> Result<Transactions, substreams::errors::Error> {
    let transactions: Vec<ConfirmedTransaction> = blk.transactions.into_iter().collect();
    substreams::log::println(format!("Number of transactions:{}", transactions.len()));
    Ok(Transactions { transactions })
}
```
[PreviousRun a Substreams](/documentation/develop/running-substreams)[NextIndexes](/documentation/develop/indexes)

Last updated 3 months ago

---

## Keys in stores | Substreams
Source: https://docs.substreams.dev/documentation/develop/manifest-modules/keys-in-stores

We use store modules to aggregate the data in the underlying key-value storage. It is important to have a system for organizing your keys to be able to efficiently retrieve, filter and free them when needed.

In most cases, you will encode data into your keys into segmented parts, adding a prefix as namespace for example `user` and `<address>` joined together using a separator. Segments in a key are conventionally joined with `:` as a separator.

Here are some examples,
- `Pool:{pool_address}:volumeUSD` - `{pool_address}` pool total traded USD volume
- `Token:{token_addr}:volume` - total `{token_addr}` token volume traded
- `UniswapDayData:{day_id}:volumeUSD` - `{day_id}` daily USD trade volume
- `PoolDayData:{day_id}:{pool_address}:{token_addr}:volumeToken1` - total `{day_id}` daily volume of `{token_addr}` token that went through a `{pool_address}` pool in token1 equivalent

In the example of a counter store below, we increment transaction counters for different metrics that we could use in the downstream modules:

Copy
```
# [substreams::handlers::store]
pub fn store_total_tx_counts(clock: Clock, events: Events, output: StoreAddBigInt) {
    let timestamp_seconds = clock.timestamp.unwrap().seconds;
    let day_id = timestamp_seconds / 86400;
    let hour_id = timestamp_seconds / 3600;
    let prev_day_id = day_id - 1;
    let prev_hour_id = hour_id - 1;
    for event in events.pool_events {
        let pool_address = &event.pool_address;
        let token0_addr = &event.token0;
        let token1_addr = &event.token1;
        output.add_many(
            event.log_ordinal,
            &vec![
                format!("pool:{pool_address}"),
                format!("token:{token0_addr}"),
                format!("token:{token1_addr}"),
                format!("UniswapDayData:{day_id}"),
                format!("PoolDayData:{day_id}:{pool_address}"),
                format!("PoolHourData:{hour_id}:{pool_address}"),
                format!("TokenDayData:{day_id}:{token0_addr}"),
                format!("TokenDayData:{day_id}:{token1_addr}"),
                format!("TokenHourData:{hour_id}:{token0_addr}"),
                format!("TokenHourData:{hour_id}:{token1_addr}"),
            ],
            &BigInt::from(1 as i32),
        );
    }
}
```

In the downstream modules consuming this store, you can query the store by key in `get` mode. Or, an even more powerful approach would be to filter needed store deltas by segments. `key` module of the `substreams` crates offers several helper functions. Using these functions you can extract the first/last/nth segment from a key:

Copy
```
for delta in deltas.into_iter() {
    let kind = key::first_segment(delta.get_key());
    let address = key::segment_at(delta.get_key(), 1);
    // Do something for this kind and address
}
```

`key` module also provides corresponding `try_` methods that don't panic:
- `first_segment` & `try_first_segment`
- `last_segment` & `try_last_segment`
- `segment_at` & `try_segment_at`

For a full example see [Uniswap V3 Substreams](https://github.com/streamingfast/substreams-uniswap-v3/blob/ca90fe3908a76905b43e05f0522e1e9338d88972/src/lib.rs#L1139-L1163)

Links
- ----
- [Uniswap-v3 Subgraph and Substreams](https://github.com/streamingfast/substreams-uniswap-v3)
- [Key module documentation](https://docs.rs/substreams/latest/substreams/key/index.html)

[PreviousModule handler creation](/documentation/develop/manifest-modules/writing-module-handlers)[NextDynamic data sources](/documentation/develop/manifest-modules/dynamic-data-sources)

Last updated 1 year ago

---

## Module handlers | Substreams
Source: https://docs.substreams.dev/documentation/develop/manifest-modules/setting-up-handlers

Module handlers overview
- -----------------------

To begin creating the custom module handlers initialize a new Rust project by using the `cargo` `init` command.

Copy
```
# Creates a empty Rust project suitable for WASM compilation
cargo init --lib
```

Update the generated [`Cargo.toml`](https://github.com/streamingfast/substreams-template/blob/develop/Cargo.toml) file by using:

Cargo.tomlCopy
```
[package]
name = "substreams-template"
version = "0.1.0"
description = "Substream template demo project"
edition = "2021"
repository = "https://github.com/streamingfast/substreams-template"
[lib]
name = "substreams"
crate-type = ["cdylib"]
[dependencies]
ethabi = "17"
hex-literal = "0.3.4"
prost = "0.11"
# Use latest from https://crates.io/crates/substreams
substreams = "0.5"
# Use latest from https://crates.io/crates/substreams-ethereum
substreams-ethereum = "0.9"
# Required so ethabi > ethereum-types build correctly under wasm32-unknown-unknown
[target.wasm32-unknown-unknown.dependencies]
getrandom = { version = "0.2", features = ["custom"] }
[build-dependencies]
anyhow = "1"
substreams-ethereum = "0.8"
[profile.release]
lto = true
opt-level = 's'
strip = "debuginfo"
```

View the [`Cargo.toml`](https://github.com/streamingfast/substreams-template/blob/develop/Cargo.toml) file in the repository.

You compile the Rust code into [WebAssembly (WASM)](https://webassembly.org/), a binary instruction format that runs in a virtual machine. The compilation process generates a .so file.

## # `Cargo.toml` **configuration file breakdown**

Build the Rust dynamic system library after the `package` by using:

Cargo.toml excerptCopy
```
...
[lib]
crate-type = ["cdylib"]
```

The next definition in the [`Cargo.toml`](https://github.com/streamingfast/substreams-template/blob/develop/Cargo.toml) configuration file is for `dependencies`.
- *Note**: Module handlers compile down to a WASM module. Explicitly specify the target`asm32-unknown-unknown` by using `[target.wasm32-unknown-unknown.dependencies]`.

### # `ethabi`

The [`ethabi` crate](https://crates.io/crates/ethabi) is used to decode events from the application binary interface (ABI) and is required for `substreams-ethereum` ABI capabilities.

### # `hex-literal`

The [`hex-literal` crate](https://crates.io/crates/hex-literal) is used to define bytes from hexadecimal string literals at compile time.

### # `substreams`

The [`substreams` crate](https://docs.rs/substreams/latest/substreams/) offers all the basic building blocks for the module handlers.

### # `substreams-ethereum`

The [`substreams-ethereum` crate](https://crates.io/crates/substreams-ethereum-core) offers all the Ethereum constructs including blocks, transactions, eth, and useful ABI decoding capabilities.

Because code is being built by WASM output it's necessary to configure Rust to match the correct architecture. Create and add a [`rust-toolchain.toml`](https://github.com/streamingfast/substreams-template/blob/develop/rust-toolchain.toml) configuration file at the root of your Substreams directory.

## # Rust toolchain

rust-toolchain.tomlCopy
```
[toolchain]
channel = "1.65"
components = [ "rustfmt" ]
targets = [ "wasm32-unknown-unknown" ]
```

View the [`rust-toolchain.toml`](https://github.com/streamingfast/substreams-template/blob/develop/rust-toolchain.toml) file in the repository.

Build the code by using:

Copy
```
cargo build --target wasm32-unknown-unknown --release
```
## # **Rust build target**

When running `cargo build` the target is set to `wasm32-unknown-unknown`, which is important because it specifies the goal is to generate compiled WASM code.

To avoid having to specify the target `wasm32-unknown-unknown` for every `cargo` command, create a `config.toml` configuration file in the `.cargo` directory at the root of the Substreams project. The `config.toml` configuration file allows the target to be set automatically for all `cargo` commands.

The content for the `config.toml` configuration file is:

.cargo/config.tomlCopy
```
[build]
target = "wasm32-unknown-unknown"
```

The `config.toml` configuration file updates the default `cargo build` command to `cargo build --target wasm32-unknown-unknown` eliminating the need to specify the target manually every time you build.

## # ABI generation

The [`substreams-ethereum` crate](https://crates.io/crates/substreams-ethereum) offers an [`Abigen`](https://docs.rs/substreams-ethereum-abigen/latest/substreams_ethereum_abigen/build/struct.Abigen.html) API to generate Rust types from a smart contract's ABI.

Place the contract's [ABI JSON file](https://github.com/streamingfast/substreams/blob/develop/docs/.gitbook/assets/erc721.json) in the Substreams project in the `abi` directory.

## # **Rust build script**

Before building a package, Cargo compiles a build script into an executable if it has not already been built. The build script runs as part of the build process responsible for performing a variety of tasks.

To cause Cargo to compile and run a script before building a package, place a file called `build.rs` in the root of the package.

Create a [`build.rs`](https://github.com/streamingfast/substreams-template/blob/develop/build.rs) build script file in the root of the Substreams project by using:

build.rsCopy
```
use anyhow::{Ok, Result};
use substreams_ethereum::Abigen;
fn main() -> Result<(), anyhow::Error> {
    Abigen::new("ERC721", "abi/erc721.json")?
        .generate()?
        .write_to_file("src/abi/erc721.rs")?;
    Ok(())
}
```

View the [`build.rs`](https://github.com/streamingfast/substreams-template/blob/develop/build.rs) file in the repository.

Run the build script to generate the ABI directory and files.

Copy
```
cargo build --target wasm32-unknown-unknown --release
```

Create a [`mod.rs`](https://github.com/streamingfast/substreams-template/blob/develop/src/abi/mod.rs) export file in the ABI directory, which is created by the Rust build process. The [`mod.rs`](https://github.com/streamingfast/substreams-template/blob/develop/src/abi/mod.rs) export file is responsible for exporting the generated Rust code.

src/abi/mod.rsCopy
```
pub mod erc721;
```

View the [`mod.rs`](https://github.com/streamingfast/substreams-template/blob/develop/src/abi/mod.rs) file in the repository.

You're now ready to [write the module handlers](/documentation/develop/manifest-modules/writing-module-handlers).

[PreviousOutput](/documentation/develop/manifest-modules/outputs)[NextModule handler creation](/documentation/develop/manifest-modules/writing-module-handlers)

Last updated 1 year ago

---

## Glossary | Substreams
Source: https://docs.substreams.dev/reference-and-specs/glossary

Substreams
- ---------

[Substreams](https://substreams.streamingfast.io/) is a powerful indexing technology, which allows you to:

1. Extract data from several blockchains (Ethereum, Polygon, BNB, Solana...).
2. Apply custom transformations to the data.
3. Send the data to a place of your choice (for example, a Postgres database or a file).

Firehose
- -------

[Firehose](https://firehose.streamingfast.io/) is the extraction layer of Substreams (i.e. step number one of the previous glossary entry). Although Firehose is a different project, it is tightly related to Substreams.

CLI
- --

`CLI`, which stands for command-line interface, is a text-based interface that allows you to input commands to interact with a computer. The [Substreams CLI](https://substreams.streamingfast.io/getting-started/installing-the-cli) allows you to deploy and manage your Substreams.

Module
- -----

[Modules](https://substreams.streamingfast.io/developers-guide/modules) are small pieces of Rust code running in a WebAssembly (WASM) virtual machine. Modules have one or more inputs and an output. For example, a module could receive an Ethereum block as input and emit a list of transfers for that block as output.

There are two types of modules: `map` and `store`.

map Module
- ---------

`map` modules receive an input and emit an output (i.e. they perform a transformation).

store Module
- -----------

`store` modules write to key-value stores and are stateful. They are useful in combination with `map` modules to keep track of past data.

Directed Acyclic Graph (DAG)
- ---------------------------

[DAGs](https://en.wikipedia.org/wiki/Directed_acyclic_graph) are data structures used in many computational models. In Substreams, DAGs are used to define module data flows.

A DAG is a one-direction, acyclic graph. They are used in a variety of software, such as Git or IPFS.

Composability
- ------------

Modules make Substreams really *composable*. Being composable means that Substreams can be independent, but they can also work together to create powerful streams.

For example, consider that you have two *map modules*: one emitting `Transfer` objects and another one emitting `AccountInformation` objects. You could create another module that receives the previous two modules as input and merges the information from both.

That is why Substreams is so powerful!

Protocol Buffers (Protobuf)
- --------------------------

[Protocol Buffers](https://protobuf.dev/) is a serializing format used to define module inputs and outputs in Substreams. For example, a manifest might define a module called `map_tranfers` with an input object, `Transfer` (representing an Ethereum transaction), and an output object `MyTransfer` (representing a reduced version of an Ethereum transaction).

Manifest
- -------

The [Substreams manifest](https://substreams.streamingfast.io/developers-guide/creating-your-manifest) (called `substreams.yaml`) is a YAML file where you define all the configurations needed. For example, the modules of your Substreams (along with their inputs and outputs), or the Protobuf definitions used.

WebAssembly (WASM)
- -----------------

[WebAssembly (WASM)](https://webassembly.org/) is a binary-code format used to run a Substreams. The Rust code used to define your Substreams transformations is packed into a WASM module, which you can use as an independent executable.

Block
- ----

The `Block` Protobuf object contains all the blockchain information for a specific block number. EVM-compatible chains share the same [Block](https://github.com/streamingfast/firehose-ethereum/blob/develop/proto/sf/ethereum/type/v2/type.proto) object, but non-EVM-compatible chains must use [their corresponding Block Protobuf definition](https://substreams.streamingfast.io/reference-and-specs/chains-and-endpoints).

![](https://docs.substreams.dev/~gitbook/image?url=https%3A%2F%2F2510971185-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FerQrzMtqELZRGAdugCR2%252Fuploads%252Fgit-blob-9efe1db24a42c1502b9603986b43c45611e9535f%252Fchains-endpoints.png%3Falt%3Dmedia&width=768&dpr=4&quality=100&sign=149b0eec&sv=2)

SPKG (.spkg)
- -----------

[SPKG files](https://substreams.streamingfast.io/reference-and-specs/packages) contain Substreams definitions. You can create an `.spkg` file from a Substreams manifest using the `substreams pack` command. Then, you can use this file to share or run the Substreams independently. The `.spkg` file contains everything needed to run a Substreams: Rust code, Protobuf definitions and the manifest.

GUI
- --

The CLI includes two commands to run a Substreams: `run` and `gui`. The `substreams run` command prints the output of the execution linearly for every block, while the `substreams gui` allows you to easily jump to the output of a specific block.

![](https://docs.substreams.dev/~gitbook/image?url=https%3A%2F%2F2510971185-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FerQrzMtqELZRGAdugCR2%252Fuploads%252Fgit-blob-0d2568c3115982809987a77f2c99e50edf61b83a%252Fgui.png%3Falt%3Dmedia&width=768&dpr=4&quality=100&sign=bed4e007&sv=2)

Subgraph
- -------

[Subgraphs](https://thegraph.com/docs/en/developing/creating-a-subgraph/) are another indexing mechanism developed by The Graph. In Subgraphs, data is indexed and available through a GraphQL endpoint.

One of the main differences between Subgraphs and Substreams is that Subgraphs rely on *polling*, while Substreams relies on *streaming*.

Triggers
- -------

In Subgraphs, you define *triggers* to index your data. These triggers are events that happen in the blockchain (for example, `AccountCreated`). Subgraphs listen for those events, and index the data accordingly.

Sink
- ---

Substreams allows you to extract blockchain data and apply transformations to it. After that, you should choose **a place to send your transform data, which is called** ***sink***. A sink can be a [SQL database](https://substreams.streamingfast.io/developers-guide/sink-targets/substreams-sink-sql), [a file](https://substreams.streamingfast.io/developers-guide/sink-targets/substreams-sink-files) or a [custom solution of your choice](https://substreams.streamingfast.io/developers-guide/sink-targets/custom-sink-js).

Deployable Unit
- --------------

A deployable unit is a Substreams manifest or package (spkg) that contains all the information about how to run it from sink service. In the manifest, it corresponds to the `network` and `sink` fields. See [Working with deployable units](https://substreams.streamingfast.io/developers-guide/sink-deployable-units)

Substreams-powered Subgraph
- --------------------------

When a Subgraph acts as a sink for your Substreams, you call it a [Substreams-powered Subgraph](https://thegraph.com/docs/en/cookbook/substreams-powered-subgraphs/).

The Subgraph Sink is one of the *official sinks* supported by Substreams, and can help you index your Subgraph way faster!

Parallel execution
- -----------------

[Parallel execution](https://substreams.streamingfast.io/developers-guide/parallel-execution) is the process of a Substreams module's code executing multiple segments of blockchain data simultaneously in a forward or backward direction.

Workers
- ------

Workers are the fundamental unit of parallelizing in Substreams. Workers are computer processes that run in parallel to speed up the Substreams computations.

[PreviousGUI Reference](/reference-and-specs/gui)[NextChange log](/reference-and-specs/change-log)

Last updated 1 year ago

---

## Architecture | Substreams
Source: https://docs.substreams.dev/documentation/develop/architecture

Parallel execution is the process of a Substreams module's code executing multiple segments of blockchain data simultaneously in a forward or backward direction. Substreams modules can be executed in parallel, rapidly producing data for consumption in end-user applications. Parallel execution enables Substreams' highly efficient blockchain data processing capabilities.

Parallel execution occurs when a requested module's start block is further back in the blockchain's history than the requested start block. For example, if a module starts at block 12,000,000 and a user requests data at block 15,000,000, parallel execution is used. This applies to both the development and production modes of Substreams operation.

Parallel execution addresses the problem of the slow single linear execution of a module. Instead of running a module in a linear fashion, one block after the other without leveraging full computing power, N number of workers are executed over a different segment of the chain. It means data can be pushed back to the user N times faster than cases using a single worker.

The server will define an execution schedule and take the module's dependencies into consideration. The server's execution schedule is a list of pairs of (`module, range`), where range contains `N` blocks. This is a configurable value set to 25K blocks, on the server.

The single map\_transfer module will fulfill a request from 0 - 75,000. The server's execution plan returns the results of `[(map_transfer, 0 -> 24,999), (map_transfer, 25,000 -> 49,999), (map_transfer, 50,000 -> 74,999)]`.

The three pairs will be simultaneously executed by the server handling caching of the output of the store. For stores, an additional step will combine the store keys across multiple segments producing a unified and linear view of the store's state.

Assuming a chain has 16,000,000 blocks, which translates to 640 segments of 25K blocks. The server currently has a limited amount of concurrency. In theory, 640 concurrent workers could be spawned. In practice, the number of concurrent workers depends on the capabilities of the service provider. For the production endpoint, StreamingFast sets the concurrency to 15 to ensure fair usage of resources for the free service.

Production versus development mode for parallel execution
- --------------------------------------------------------

The amount of parallel execution for the two modes is illustrated in the diagram. Production mode results in more parallel processing than development mode for the requested range. In contrast, development mode consists of more linear processing. Another important note is, forward parallel execution only occurs in production mode.

![](https://docs.substreams.dev/~gitbook/image?url=https%3A%2F%2Fgithub.com%2Fstreamingfast%2Fsubstreams%2Fraw%2Fdevelop%2Fdocs%2Fassets%2Fsubstreams_processing.png&width=768&dpr=4&quality=100&sign=5177a62&sv=2)

Substreams production versus development mode for parallel execution diagram

Backward and forward parallel execution steps
- --------------------------------------------

The two steps involved during parallel execution are **backward execution and forward execution**.

Backward parallel execution consists of executing in parallel block ranges, from the module's initial block, up to the start block of the request. If the start block of the request matches the module's initial block no backward execution is performed.

Forward parallel execution consists of executing in parallel block ranges from the start block of the request up to the last known final block, also called an irreversible block, or the stop block of the request depending on which is smaller. Forward parallel execution significantly improves the performance of Substreams.

Backward parallel execution will occur in both development and production modes.

Forward parallel execution only occurs in production mode.

[PreviousTest Locally](/documentation/develop/test-locally)[NextEVM](/tutorials/evm)

Last updated 10 months ago

---

## DEX Trades | Substreams
Source: https://docs.substreams.dev/tutorials/solana/dex-trades

The DEX Trades Substreams, developed by TopLedger, extracts trades from different Solana DEXs (decentralized exchanges).

## # About TopLedger

[TopLedger](https://topledger.xyz/) is SQL-based data discovery and analytics platform focused on Solana. By using Substreams, TopLedger has been able to extract data from the main Solana dapps, thus providing rich analytics products.

TopLedger is an active contributor to the Substreams community and has developed several useful ready-to-use Substreams.

## # Before You Begin

The DEX Trades Substreams requires medium to advanced Substreams knowledge. If this is the first time you are using Substreams, make sure you:
- Read the [Develop Substreams](/documentation/develop) section, which will teach you the basics of the developing Substreams modules.
- Complete the [Explore Solana](/tutorials/solana/explore-solana) tutorial, which will assist you in understanding the main pieces of the Solana Substreams.

Then, clone the [TopLedger Solana Programs](https://github.com/Topledger/solana-programs) project and navigate to the `dex-trades` folder, which contains the code of the Substreams.

## # Inspect the Substreams

The Substreams contains only one module, `map_block`:

Copy
```
modules:
- name: map_block
    kind: map
    inputs:
- source: sf.solana.type.v1.Block
    output:
      type: proto:sf.solana.dex.trades.v1.Output
```

The module receives a raw Solana block as a parameter (`sf.solana.type.v1.Block`) and emits a custom object containing the trades data (`sf.solana.dex.trades.v1.Output`). The output is a Protobut object defined in the `proto/output.proto` file:

Copy
```
message Output {
  repeated TradeData data = 1;
}
message TradeData {
  required string block_date = 1;
  required int64 block_time = 2;
  required uint64 block_slot = 3;
  required string tx_id = 4;
  required string signer = 5;
  required string pool_address = 6;
  required string base_mint = 7;
  required string quote_mint = 8;
  required string base_vault = 9;
  required string quote_vault = 10;
  required double base_amount = 11;
  required double quote_amount = 12;
  required bool is_inner_instruction = 13;
  required uint32 instruction_index = 14;
  required string instruction_type = 15;
  required uint32 inner_instruxtion_index = 16;
  required string outer_program = 17;
  required string inner_program = 18;
  required uint64 txn_fee = 19;
  required int64 signer_sol_change = 20;
}
```

The Substreams extracts trades from different DEXs. Because every DEX handles the data diffrerently, it is necessary to create a custom decoding function for every DEX. Every supported DEX has its correponding function in the `dapps` directory of the project.

## # Run the Substreams

You can run the Substreams against the Solana StreamingFast endpoint by using the Substreams CLI:

Copy
```
substreams gui -e mainnet.sol.streamingfast.io:443 \
    substreams.yaml map_block -s 138616676 -t +1
```
## # Inspect the Code

Copy
```
fn process_block(block: Block) -> Result<Output, substreams::errors::Error> {
    let slot = block.slot;
    let parent_slot = block.parent_slot;
    let timestamp = block.block_time.as_ref();
    let mut data: Vec<TradeData> = vec![]; // 1.
    if timestamp.is_some() {
        let timestamp = timestamp.unwrap().timestamp;
        for trx in block.transactions_owned() { // 2.
            let accounts = trx.resolved_accounts_as_strings(); // 3.
            if let Some(transaction) = trx.transaction {
                let meta = trx.meta.unwrap();
                let pre_balances = meta.pre_balances;
                let post_balances = meta.post_balances;
                let pre_token_balances = meta.pre_token_balances;
                let post_token_balances = meta.post_token_balances;
                let msg = transaction.message.unwrap();
                for (idx, inst) in msg.instructions.into_iter().enumerate() { // 4.
                    let inner_instructions: Vec<InnerInstructions> =
                        filter_inner_instructions(&meta.inner_instructions, idx as u32); // 5.
                    let program = &accounts[inst.program_id_index as usize]; // 6.
                    let trade_data = get_trade_instruction( // 7.
                        program,
                        inst.data,
                        &inst.accounts,
                        &accounts,
                        &pre_token_balances,
                        &post_token_balances,
                        &"".to_string(),
                        false,
                        &inner_instructions,
                    );
                    // ...code omitted...
                }
            }
        }
    }
}
```

2. Initialize an *array* to keep the trades data extracted.
5. Iterate over the transactions.
8. Get accounts of the transaction (the `resolved_accounts()` method contains also accounts stored in the [Address Lookup Tables](https://docs.solana.com/developing/lookup-tables)).
11. Iterate over the instructions within the transaction.
14. Keep only inner instructions beloging to the current top-level instruction. Becuse the inner instructions are at the transaction level, you must filter filter which inner instruction belong to the current instruction by using the `index` property.
17. Get the program account.
20. Process trade instruction by calling the `get_trade_instruction(...)` function.

Every DEX handles the data differently, so it is necessary to create a decoding function for every exchange supported. The `get_trade_instruction(...)` function receives the data of every top-level instruction and figures out whether the instruction belongs to any of the supported DEXs. If the instruction is part of a known DEX, the corresponding DEX decoding function is called and a `TradeInstruction` object is returned.

Copy
```
fn get_trade_instruction(
    dapp_address: &String,
    instruction_data: Vec<u8>,
    account_indices: &Vec<u8>,
    accounts: &Vec<String>,
    pre_token_balances: &Vec<TokenBalance>,
    post_token_balances: &Vec<TokenBalance>,
    outer_program: &String,
    is_inner: bool,
    inner_instructions: &Vec<InnerInstructions>,
) -> Option<trade_instruction::TradeInstruction> {
    let input_accounts = prepare_input_accounts(account_indices, accounts);
    let mut result = None;
    match dapp_address.as_str() { // 1.
        "CLMM9tUoggJu2wagPkkqs9eFG4BWhVBZWkP1qv3Sp7tR" => { // 2.
            result =
                dapps::dapp_CLMM9tUoggJu2wagPkkqs9eFG4BWhVBZWkP1qv3Sp7tR::parse_trade_instruction( // 3.
                    instruction_data,
                    input_accounts,
                );
        }
        "Dooar9JkhdZ7J3LHN3A7YCuoGRUggXhQaG4kijfLGU2j" => { // 4.
            result =
                dapps::dapp_Dooar9JkhdZ7J3LHN3A7YCuoGRUggXhQaG4kijfLGU2j::parse_trade_instruction(
                    instruction_data,
                    input_accounts,
                );
        }
        "Eo7WjKq67rjJQSZxS6z3YkapzY3eMj6Xy8X5EQVn5UaB" => { // 5.
            result =
                dapps::dapp_Eo7WjKq67rjJQSZxS6z3YkapzY3eMj6Xy8X5EQVn5UaB::parse_trade_instruction(
                    instruction_data,
                    input_accounts,
                );
        }
        "PhoeNiXZ8ByJGLkxNfZRnkUfjvmuYqLR89jjFHGqdXY" => {
            result =
                dapps::dapp_PhoeNiXZ8ByJGLkxNfZRnkUfjvmuYqLR89jjFHGqdXY::parse_trade_instruction(
                    instruction_data,
                    input_accounts,
                );
        }
        "SSwapUtytfBdBn1b9NUGG6foMVPtcWgpRU32HToDUZr" => {
            result =
                dapps::dapp_SSwapUtytfBdBn1b9NUGG6foMVPtcWgpRU32HToDUZr::parse_trade_instruction(
                    instruction_data,
                    input_accounts,
                );
        }
        // ...code omitted...
    }
}
```

2. Match the program account passed as a parameter.
5. Excuted if the program account is `CLMM9tUoggJu2wagPkkqs9eFG4BWhVBZWkP1qv3Sp7tR` (Crema Finance).
8. Call the decoding function of Crema Finance (`parse_trade_instruction(...)`).
11. Executed if the program account is `Dooar9JkhdZ7J3LHN3A7YCuoGRUggXhQaG4kijfLGU2j` (Dooar Exchange).
14. Executed if the program account is `Eo7WjKq67rjJQSZxS6z3YkapzY3eMj6Xy8X5EQVn5UaB` (Meteora).

You can find the decoding functions in the `dapps` folder of the project.

Back in the main function (`process_block`), if the instruction processed matches any of the supported DEXs, then the `trade_data` variable will be populated. A new `TradeData` object is created with the corresponding trading information and is added to the array as part of the output of the Substreams.

Copy
```
fn process_block(block: Block) -> Result<Output, substreams::errors::Error> {
    // ...code omitted...
        let trade_data = get_trade_instruction(
            program,
            inst.data,
            &inst.accounts,
            &accounts,
            &pre_token_balances,
            &post_token_balances,
            &"".to_string(),
            false,
            &inner_instructions,
        );
        if trade_data.is_some() {
            let td = trade_data.unwrap();
            data.push(TradeData {
                block_date: convert_to_date(timestamp),
                tx_id: bs58::encode(&transaction.signatures[0]).into_string(),
                block_slot: slot,
                block_time: timestamp,
                signer: accounts.get(0).unwrap().to_string(),
                pool_address: td.amm,
                base_mint: get_mint(&td.vault_a, &post_token_balances, &accounts),
                quote_mint: get_mint(&td.vault_b, &pre_token_balances, &accounts),
                base_amount: get_amt(
                    &td.vault_a,
                    &pre_token_balances,
                    &post_token_balances,
                    &accounts,
                ),
                quote_amount: get_amt(
                    &td.vault_b,
                    &pre_token_balances,
                    &post_token_balances,
                    &accounts,
                ),
                base_vault: td.vault_a,
                quote_vault: td.vault_b,
                is_inner_instruction: false,
                instruction_index: idx as u32,
                instruction_type: td.name,
                inner_instruxtion_index: 0,
                outer_program: td.dapp_address,
                inner_program: "".to_string(),
                txn_fee: meta.fee,
                signer_sol_change: get_signer_balance_change(
                    &pre_balances,
                    &post_balances,
                ),
            });
        }
    // ...code omitted...
}
```

Until now, the code logic has taken care of the top-level instructions. However, it is also necessary to verify if any of the inner instructions contain relevant DEX information.

The logic for the inner instruction is analogus to the logic of top-level instructions:
- Iterate over the inner instructions.
- Pass the data to the `get_trade_instruction(...)` function.
- If the `get_trade_instruction(...)` function returns a `TradeInstruction` object, then a new `TradeData` object is created and added to the array.

Copy
```
fn process_block(block: Block) -> Result<Output, substreams::errors::Error> {
    // ...code omitted...
        meta.inner_instructions
            .iter()
            .filter(|inner_instruction| inner_instruction.index == idx as u32)
            .for_each(|inner_instruction| {
                inner_instruction.instructions.iter().enumerate().for_each(
                    |(inner_idx, inner_inst)| {
                        let inner_program =
                            &accounts[inner_inst.program_id_index as usize];
                        let trade_data = get_trade_instruction(
                            inner_program,
                            inner_inst.data.clone(),
                            &inner_inst.accounts,
                            &accounts,
                            &pre_token_balances,
                            &post_token_balances,
                            &program.to_string(),
                            true,
                            &inner_instructions,
                        );
                        if trade_data.is_some() {
                            let td = trade_data.unwrap();
                            data.push(TradeData {
                                block_date: convert_to_date(timestamp),
                                tx_id: bs58::encode(&transaction.signatures[0])
                                    .into_string(),
                                block_slot: slot,
                                block_time: timestamp,
                                signer: accounts.get(0).unwrap().to_string(),
                                pool_address: td.amm,
                                base_mint: get_mint(
                                    &td.vault_a,
                                    &pre_token_balances,
                                    &accounts,
                                ),
                                quote_mint: get_mint(
                                    &td.vault_b,
                                    &pre_token_balances,
                                    &accounts,
                                ),
                                base_amount: get_amt(
                                    &td.vault_a,
                                    &pre_token_balances,
                                    &post_token_balances,
                                    &accounts,
                                ),
                                quote_amount: get_amt(
                                    &td.vault_b,
                                    &pre_token_balances,
                                    &post_token_balances,
                                    &accounts,
                                ),
                                base_vault: td.vault_a,
                                quote_vault: td.vault_b,
                                is_inner_instruction: true,
                                instruction_index: idx as u32,
                                instruction_type: td.name,
                                inner_instruxtion_index: inner_idx as u32,
                                outer_program: program.to_string(),
                                inner_program: td.dapp_address,
                                txn_fee: meta.fee,
                                signer_sol_change: get_signer_balance_change(
                                    &pre_balances,
                                    &post_balances,
                                ),
                            });
                        }
                    },
                )
            });
}
```
[PreviousNFT Trades](/tutorials/solana/nft-trades)[NextCosmos](/tutorials/cosmos)

Last updated 9 months ago

---

## Test Locally | Substreams
Source: https://docs.substreams.dev/documentation/develop/test-locally

You can run a Substreams server locally to run e2e testing.

It requires a local copy of full merged-blocks files for the range you want to test over. You can easily download those files from a Firehose endpoint.

Then run the Substreams software locally, and run tests against it

Install binaries
- ---------------

Firehose CoreFirehose Ethereum

Install the `firehose-core` single binary for most chains (those without chain-specific extensions) with brew:

Copy
```
brew install streamingfast/tap/firehose-core
```

or get a release from: <https://github.com/streamingfast/firehose-core/releases>

Install the `firehose-ethereum` single binary with brew:

Copy
```
brew install streamingfast/tap/firehose-ethereum
```

or get a release from: [https://github.com/streamingfast/firehose-ethereum/releases](https://github.com/streamingfast/firehose-core/releases)

Download merged blocks locally
- -----------------------------

Run against an endpoint for the chain you're interested in. For example:

Copy
```
fireeth tools download-from-firehose mainnet.eth.streamingfast.io:443 1000 2000 \
   ./firehose-data/storage/merged-blocks
```

which will download merged blocks to your local disk. You might need to be authenticated.

Run the Substreams engine locally
- --------------------------------

Run:

Copy
```
fireeth start substreams-tier1,substreams-tier2 --config-file= \
- -common-live-blocks-addr= --common-first-streamable-block=1000 \
- -substreams-state-bundle-size=10
```
- *Notes**:

2. the `--common-first-streamable-block` must be the lowest block available on disk, otherwise the server will fail to start.
5. if you need to do `eth_calls` with the Ethereum, you can add: `--substreams-rpc-endpoints https://example.com/json-rpc/somekeysometimes`
8. the `--substreams-state-bundle-size=10` flag will write smaller stores snapshot, suitable for dev

This will run a fully workable stack

Stream against your local instance
- ---------------------------------

Test with:

Copy
```
substreams run -e localhost:10016 --plaintext \
  https://spkg.io/streamingfast/ethereum-explorer-v0.1.2.spkg \
  map_block_meta -s 1000 -t +10
```

and enjoy.

[PreviousMaking eth\_calls](/documentation/develop/overview/evm-chain-specific-extensions/eth-calls)[NextArchitecture](/documentation/develop/architecture)

Last updated 3 months ago

---

## Simple Substreams Example | Substreams
Source: https://docs.substreams.dev/tutorials/cosmos/injective/block-stats

[PreviousInjective](/tutorials/cosmos/injective)[NextFoundational Modules](/tutorials/cosmos/injective/foundational)

Last updated 5 months ago

---

## Substreams:SQL | Substreams
Source: https://docs.substreams.dev/documentation/consume/sql

[PreviousDeployable Services](/documentation/consume/deployable-services)[NextDeployable Services](/documentation/consume/sql/deployable-services)

Last updated 10 months ago

---

## Graph Out | Substreams
Source: https://docs.substreams.dev/documentation/consume/subgraph/graph-out

If you want to include the extractions logic in Substreams to benefit from the paralellization engine, you can use the **EntityChanges** model.

Essentially, this means that you will create a `graph_out` module in Substreams, which will emit an **EntityChanges** structure representing the subgraph entities.

## # Requirements
- Install the Substreams CLI.
- Install the Graph CLI.

## # Create a Sample Project

Copy
```
graph init --from-example substreams-powered-subgraph
```
## # Defining a Substreams package

A Substreams package is composed of types (defined as [Protocol Buffers](https://protobuf.dev/)), modules (written in Rust), and a `substreams.yaml` file which references the types, and specifies how modules are triggered.

The Substreams package in question detects contract deployments on Mainnet Ethereum, tracking the creation block and timestamp for all newly deployed contracts. To do this, there is a dedicated `Contract` type in `/proto/example.proto` ([learn more about defining Protocol Buffers](https://protobuf.dev/programming-guides/proto3/#simple)):

Copy
```
syntax = "proto3";
package example;
message Contracts {
  repeated Contract contracts = 1;
}
message Contract {
    string address = 1;
    uint64 blockNumber = 2;
    string timestamp = 3;
    uint64 ordinal = 4;
}
```

The core logic of the Substreams package is a `map_contract` module in `lib.rs`, which processes every block, filtering for Create calls which did not revert, returning `Contracts`:

Copy
```
# [substreams::handlers::map]
fn map_contract(block: eth::v2::Block) -> Result<Contracts, substreams::errors::Error> {
    let contracts = block
        .transactions()
        .flat_map(|tx| {
            tx.calls
                .iter()
                .filter(|call| !call.state_reverted)
                .filter(|call| call.call_type == eth::v2::CallType::Create as i32)
                .map(|call| Contract {
                    address: format!("0x{}", Hex(&call.address)),
                    block_number: block.number,
                    timestamp: block.timestamp_seconds().to_string(),
                    ordinal: tx.begin_ordinal,
                })
        })
        .collect();
    Ok(Contracts { contracts })
}
```

A Substreams package can be used by a subgraph as long as it has a module which outputs compatible entity changes. The example Substreams package has an additional `graph_out` module in `lib.rs` which returns a `substreams_entity_change::pb::entity::EntityChanges` output, which can be processed by Graph Node.

> The `substreams_entity_change` crate also has a dedicated `Tables` function for simply generating entity changes ([documentation](https://docs.rs/substreams-entity-change/1.2.2/substreams_entity_change/tables/index.html)). The Entity Changes generated must be compatible with the `schema.graphql` entities defined in the `subgraph.graphql` of the corresponding subgraph.

Copy
```
# [substreams::handlers::map]
pub fn graph_out(contracts: Contracts) -> Result<EntityChanges, substreams::errors::Error> {
    // hash map of name to a table
    let mut tables = Tables::new();
    for contract in contracts.contracts.into_iter() {
        tables
            .create_row("Contract", contract.address)
            .set("timestamp", contract.timestamp)
            .set("blockNumber", contract.block_number);
    }
    Ok(tables.to_entity_changes())
}
```

These types and modules are pulled together in `substreams.yaml`:

Copy
```
specVersion: v0.1.0
package:
  name: 'substreams_test' # the name to be used in the .spkg
  version: v1.0.1 # the version to use when creating the .spkg
imports: # dependencies
  entity: https://github.com/streamingfast/substreams-entity-change/releases/download/v0.2.1/substreams-entity-change-v0.2.1.spkg
protobuf: # specifies custom types for use by Substreams modules
  files:
- example.proto
  importPaths:
- ./proto
binaries:
  default:
    type: wasm/rust-v1
    file: ./target/wasm32-unknown-unknown/release/substreams.wasm
modules: # specify modules with their inputs and outputs.
- name: map_contract
    kind: map
    inputs:
- source: sf.ethereum.type.v2.Block
    output:
      type: proto:test.Contracts
- name: graph_out
    kind: map
    inputs:
- map: map_contract
    output:
      type: proto:substreams.entity.v1.EntityChanges # this type can be consumed by Graph Node
```

You can check the overall "flow" from a Block, to `map_contract` to `graph_out` by running `substreams graph`:

Copy
```
graph TD;
  map_contract[map: map_contract];
  sf.ethereum.type.v2.Block[source: sf.ethereum.type.v2.Block] --> map_contract;
  graph_out[map: graph_out];
  map_contract --> graph_out;
```

To prepare this Substreams package for consumption by a subgraph, you must run the following commands:

Copy
```
yarn substreams:protogen # generates types in /src/pb
yarn substreams:build # builds the substreams
yarn substreams:package # packages the substreams in a .spkg file
# alternatively, yarn substreams:prepare calls all of the above commands
```
> These scripts are defined in the `package.json` file if you want to understand the underlying substreams commands

This generates a `spkg` file based on the package name and version from `substreams.yaml`. The `spkg` file has all the information which Graph Node needs to ingest this Substreams package.

> If you update the Substreams package, depending on the changes you make, you may need to run some or all of the above commands so that the `spkg` is up to date.

## # Defining a Substreams-powered subgraph

Substreams-powered subgraphs introduce a new `kind` of data source, "substreams". Such subgraphs can only have one data source.

This data source must specify the indexed network, the Substreams package (`spkg`) as a relative file location, and the module within that Substreams package which produces subgraph-compatible entity changes (in this case `map_entity_changes`, from the Substreams package above). The mapping is specified, but simply identifies the mapping kind ("substreams/graph-entities") and the apiVersion.

> Currently, Subgraph Studio and The Graph Network support Substreams-powered subgraphs which index `mainnet` (Mainnet Ethereum).

Copy
```
specVersion: 0.0.4
description: Ethereum Contract Tracking Subgraph (powered by Substreams)
repository: https://github.com/graphprotocol/graph-tooling
schema:
  file: schema.graphql
dataSources:
- kind: substreams
    name: substream_test
    network: mainnet
    source:
      package:
        moduleName: graph_out
        file: substreams-test-v1.0.1.spkg
    mapping:
      kind: substreams/graph-entities
      apiVersion: 0.0.5
```

The `subgraph.yaml` also references a schema file. The requirements for this file are unchanged, but the entities specified must be compatible with the entity changes produced by the Substreams module referenced in the `subgraph.yaml`.

Copy
```
type Contract @entity {
  id: ID!
  "The timestamp when the contract was deployed"
  timestamp: String!
  "The block number of the contract deployment"
  blockNumber: BigInt!
}
```

Given the above, subgraph developers can use Graph CLI to deploy this Substreams-powered subgraph.

> Substreams-powered subgraphs indexing mainnet Ethereum can be deployed to the [Subgraph Studio](https://thegraph.com/studio/).

Copy
```
yarn install # install graph-cli
yarn subgraph:build # build the subgraph
yarn subgraph:deploy # deploy the subgraph
```

That's it! You have built and deployed a Substreams-powered subgraph.

## # Serving Substreams-powered subgraphs

In order to serve Substreams-powered subgraphs, Graph Node must be configured with a Substreams provider for the relevant network, as well as a Firehose or RPC to track the chain head. These providers can be configured via a `config.toml` file:

Copy
```
[chains.mainnet]
shard = "main"
protocol = "ethereum"
provider = [
  { label = "substreams-provider-mainnet",
    details = { type = "substreams",
    url = "https://mainnet-substreams-url.grpc.substreams.io/",
    token = "exampletokenhere" }},
  { label = "firehose-provider-mainnet",
    details = { type = "firehose",
    url = "https://mainnet-firehose-url.grpc.firehose.io/",
    token = "exampletokenhere" }},
]
```
[PreviousSubstreams:Subgraph](/documentation/consume/subgraph)[NextTriggers](/documentation/consume/subgraph/triggers)

Last updated 2 months ago

---

## Initialize a Solana Substreams Project | Substreams
Source: https://docs.substreams.dev/documentation/how-to-guides/solana

In this guide, you'll learn how to initialize a Solana-based Substreams project. You’ll learn how to set up a simple project to extract raw data or filter Solana transactions based on Program IDs and Account IDs.

## # Prerequisites
- Docker and VS Code installed and up-to-date.
- Visit the [Getting Started Guide](https://github.com/streamingfast/substreams-starter) to initialize your Dev Container.

## # Step 1: Initialize Your Solana Substreams Project

1. Open your Dev Container and run the following command to initialize your project:
   
   Copy
   ```
   substreams init
   ```
2. You will be given the option to choose between two Solana project options. Select the one that best fits your requirements:
- `sol-minimal`: This option creates a simple Substreams project that extracts raw data directly from Solana blocks.
- `sol-transactions`: This option creates a Substreams project that filters Solana transactions based on one or more Program IDs and/or Account IDs, using the cached [Solana Foundational Module](https://substreams.dev/streamingfast/solana-common/v0.3.0).
   
   Note: The filtered\_transactions\_without\_votes module extracts transactions while excluding voting transactions, reducing data size and costs by 75%. To access voting transactions, use a full Solana block.

## # Step 2: Visualize the Data

1. Create your account [here](https://thegraph.market/) to generate an authentification token (JWT) and pass it as input to:
   
   Copy
   ```
   substreams auth
   ```
2. Run the following command to visualize and itterate on your filtered data model:
   
   Copy
   ```
   substreams gui
   ```

## # Step 3: Customize your Project

After initialization, you can:
- Modify your Substreams manifest to include additional filters or configurations.
- Implement custom processing logic in Rust based on the filtered data retrieved by the foundational module.

## # Additional Resources

You may find these additional resources helpful for developing your first Solana application.

### # Dev Container Reference

The [Dev Container Reference](/reference-and-specs/devcontainer-ref) helps you navigate the complete container and its common errors.

### # Gui Reference

The [GUI reference](/reference-and-specs/gui) lets you explore all the tools available in the Substreams GUI.

### # Manifests Reference

The [Manifests Reference](/reference-and-specs/manifests) helps you with editing the `substreams.yaml`.

[PreviousInitialize an EVM Substreams Project](/documentation/how-to-guides/evm)[NextInitialize a Starknet Substreams Project](/documentation/how-to-guides/starknet)

Last updated 13 days ago

---

## Mapping Blocks | Substreams
Source: https://docs.substreams.dev/tutorials/evm/exploring-ethereum/map_block_meta_module

This module takes a raw Ethereum block and returns a reduced version of a block, with just three pieces of information: hash, parent hash, and block number.
- *Tip**: This tutorial teaches you how to build a Substreams from scratch.

Remember that you can auto-generate your Substreams module by usig the code-generation tools.

Let's run the Substreams first, and then go through the code.

Running the Substreams
- ---------------------

Running a Substreams usually requires three steps: generating the Rust Protobufs, building the WASM container, and using the Substream CLI to start the streaming. Make sure to run the following commands in the `substreams-explorer/ethereum-explorer` folder:

1. **Generate the Protobuf objects:** The `.proto` files define a data model regardless of any programming language. However, in order to use this model in your Rust application, you must generate the corresponding Rust data structures. Note that running `make protogen` is only necessary when making updates to any file in the proto folder.

Copy
```
make protogen
```

1. **Build the WASM module:** The following command generates a WASM container from the Rust application, which you can find at `/target/wasm32-unknown-unknown/release/substreams.wasm`. Note that this is the same path provided in the Substreams manifest (`substreams.yml`).

Copy
```
make build
```

1. **Streaming data through the CLI:** The following command streams the Ethereum blockchain data, and applies the transformations contained in the `map_block_meta` module to every block.

Copy
```
$ substreams run -e mainnet.eth.streamingfast.io:443 substreams.yaml map_block_meta --start-block 17712040 --stop-block +1
```

Let's break down the command into pieces:
- `mainnet.eth.streamingfast.io:443`: is the StreamingFast Ethereum Mainnet endpoint where you are sending your Substreams for execution.
- `substreams.yaml`: specifies the Substreams manifest.
- `map_block_meta`: specifies the module to execute. Since the Ethereum Explorer application contains several modules, it is necessary to specify which one you want to execute.
- `--start-block 17712040`: specifies the starting block (i.e. the block where Substreams will start streaming).
- `--stop-block +1`: specifies how many blocks after the starting block should be considered. In this example, `+1` means that the streaming will start at `17712040` and finish at `17712041` (just one block).

The output of the command should be similar to:

Copy
```
...output omitted...
- ---------- BLOCK #17,712,040 (31ad07fed936990d3c75314589b15cbdec91e4cc53a984a43de622b314c38d0b) ---------------
{
  "@module": "map_block_meta",
  "@block": 17712040,
  "@type": "eth.block_meta.v1.BlockMeta",
  "@data": {
    "number": "17712040",
    "hash": "31ad07fed936990d3c75314589b15cbdec91e4cc53a984a43de622b314c38d0b",
    "parentHash": "1385f853d28b16ad7ebc5d51b6f2ef6d43df4b57bd4c6fe4ef8ccb6f266d8b91"
  }
}
all done
```

As you can see, the output is formatted as JSON, and the `@data` field contains the actual output Protobuf of the module (`BlockMeta`).

The `BlockMeta` definition:

Copy
```
syntax = "proto3";
package eth.block_meta.v1;
message BlockMeta {
  uint64 number = 1;
  string hash = 2;
  string parent_hash = 3;
}
```

The JSON output:

Copy
```
"@data": {
    "number": "17712040",
    "hash": "31ad07fed936990d3c75314589b15cbdec91e4cc53a984a43de622b314c38d0b",
    "parentHash": "1385f853d28b16ad7ebc5d51b6f2ef6d43df4b57bd4c6fe4ef8ccb6f266d8b91"
}
```

Inspecting the Code
- ------------------

Although the code (which is in the `map_block_meta.rs` file) for this module is pretty straightforward to understand, let's discuss its main parts.

Declaration of the module in the manifest (`substreams.yml`):

Copy
```
modules:
- name: map_block_meta
    kind: map
    inputs:
- source: sf.ethereum.type.v2.Block
    output:
      type: proto:eth.block_meta.v1.BlockMeta
```

Code of the module:

Copy
```
# [substreams::handlers::map]
fn map_block_meta(blk: Block) -> Result<BlockMeta, substreams::errors::Error> {
    let header = blk.header.as_ref().unwrap();
    Ok(BlockMeta {
        number: blk.number,
        hash: Hex::encode(&blk.hash),
        parent_hash: Hex::encode(&header.parent_hash),
    })
}
```

The `#[substreams::handlers::map]` attribute annotates the `map_block_meta` function as a Substreams mapper. The name of the function must match the name of the module in the Substreams manifest. The input of the function is a raw Ethereum block (`pb::eth::v2::Block`).

In order to get the block metadata, you use the `header` property.

Copy
```
let header = blk.header.as_ref().unwrap();
```

Then, you simply create a `BlockMeta` struct and return it.

Copy
```
Ok(BlockMeta {
    number: blk.number,
    hash: Hex::encode(&blk.hash),
    parent_hash: Hex::encode(&header.parent_hash),
})
```
[PreviousExploring Ethereum](/tutorials/evm/exploring-ethereum)[NextFilter Transactions](/tutorials/evm/exploring-ethereum/map_filter_transactions_module)

Last updated 5 months ago

---

## Subgraphs | Substreams
Source: https://docs.substreams.dev/tutorials/graph-node

The Graph Node is the software that indexers run to index subgraphs. This section contains useful tutorial on the usage and development of the Graph Node, specifically in the Substreams context.

[PreviousDojo DEX USDT Volume Subgraph Example](/tutorials/cosmos/injective/usdt-exchanges)[NextLocal Development](/tutorials/graph-node/local-development)

Last updated 6 months ago

---

## Module types | Substreams
Source: https://docs.substreams.dev/documentation/develop/manifest-modules/types

Module types overview
- --------------------

Substreams uses two types of modules, `map` and `store`.
- `map` modules are functions receiving bytes as input and output. These bytes are encoded protobuf messages.
- `store` modules are stateful, saving and tracking data through the use of key-value stores.

## # `store` modules

`store` modules write to key-value stores.
- *Note**: To ensure successful and proper parallelization can occur, `store` modules are not permitted to read any of their own data or values.

Stores declaring their own data types expose methods capable of mutating keys within the `store`.

## # Core principle usage of stores
- Do not save keys in stores **unless they are going to be read by a downstream module**. Substreams stores are a way to aggregate data, but they are **not meant to be a storage layer**.
- Do not save all transfers of a chain in a `store` module, rather, output them in a `map` and have a downstream system store them for querying.

There are limitations impose on store usage. Specifically, each key/value entry must be smaller than 10MiB while a store cannot exceed 1GiB total. Keys being string, each character in the key account for 1 byte of storage space.

## # Important store properties

The two important store properties are `valueType,`and `updatePolicy`.

### # `valueType` property

The `valueType` property instructs the Substreams runtime of the data to be saved in the `stores`.

| Value | Description |
| --- | --- |
| `bytes` | A basic list of bytes |
| `string` | A UTF-8 string |
| `proto:fully.qualified.Object` | Decode bytes by using the protobuf definition `fully.qualified.Object` |
| `int64` | A string-serialized integer by using int64 arithmetic operations |
| `float64` | A string-serialized floating point value, used for float64 arithmetic operations |
| `bigint` | A string-serialized integer, supporting precision of any depth |
| `bigfloat` **(DEPRECATED): Use** `bigdecimal` | A string-serialized floating point value, supporting precision up to 100 digits |
| `bigdecimal` | A string-serialized decimal value, supporting precision up to 2^63 decimal places |

### # `updatePolicy` property

The `updatePolicy` property determines what methods are available in the runtime.

The `updatePolicy` also defines the merging strategy for identical keys found in two contiguous stores produced through parallel processing.

| Method | Supported Value Types | Merge strategy\* |
| --- | --- | --- |
| `set` | `bytes`, `string`, `proto:...` | The last key wins |
| `set_if_not_exists` | `bytes`, `string`, `proto:...` | The first key wins |
| `add` | `int64`, `bigint`, `bigfloat`, `float64` | Values are summed up |
| `min` | `int64`, `bigint`, `bigfloat`, `float64` | The lowest value is kept |
| `max` | `int64`, `bigint`, `bigfloat`, `float64` | The highest value is kept |
| `set_sum` | `int64`, `bigint`, `bigfloat`, `float64` | This type has two methods: `set` to set the value, or `sum` to add the given value to the current value. |
| `append` | `string`, `bytes` | Both keys are concatenated in order. Appended values are limited to 8Kb. Aggregation pattern examples are available in the [`lib.rs`](https://github.com/streamingfast/substreams-uniswap-v3/blob/develop/src/lib.rs#L760) file |
- *Tip**: All update policies provide the `delete_prefix` method.

The merge strategy is **applied during parallel processing**.
- A module has built two partial stores containing keys for segment A, blocks 0-1000, and segment B, blocks 1000-2000, and is prepared to merge them into a complete store.
- The complete store is represented acting as if the processing was done in a linear fashion, starting at block 0 and proceeding up to block 2000.
- *Important**\_**:** \_ To preserve the parallelization capabilities of the system, **Substreams is not permitted to read what it has written or read from a** `store` **actively being written**.

A downstream module is created to read from a store by using one of its inputs to point to the output of the `store` module.

## # Ordinals

Ordinals allow a key-value store to have multiple versions of a key within a single block. The `store` APIs contain different methods of `ordinal` or `ord`.

For example, the price for a token can change after transaction B and transaction D, and a downstream module might want to know the value of a key before transaction B **and between B and D***.*
- *Important**: Ordinals **must be set every time a key is set** and **you can only set keys in increasing ordinal order**, or by using an ordinal equal to the previous.

In situations where a single key for a block is required and ordering in the store is not important, the ordinal uses a value of zero.

## # `store` modes

You can consume data in one of two modes when declaring a `store` as an input to a module.

### # `get mode`

The `get mode` function provides the module with a key-value store that is guaranteed to be synchronized up to the block being processed. It's possible to query stores by using the `get_at`, `get_last` and `get_first` methods.
- *Tip:** Lookups are local, in-memory, and **extremely high-speed**.

The definition of `store` method behavior is:
- The `get_last` method is the fastest because it queries the store directly.
- The `get_first` method first goes through the current block's deltas in reverse order, before querying the store, in case the key being queried was mutated in the block.
- The `get_at` method unwinds deltas up to a specific ordinal, ensuring values for keys set midway through a block are still reachable.
- *Example:**

Consider that you have a store with the following values:

Copy
```
let store = StoreUSDPrice {
   Block: #1000,
   Deltas: [
      Ord: 1, Key: "usd", Type: UPDATE, OldValue: 1.45, NewValue: 1.54,
      Ord: 2, Key: "usd", Type: DELETE, OldValue: 1.54, NewValue: <nil>,
      Ord: 3, Key: "usd", Type: INSERT, OldValue: <nil>, NewValue: 1.47,
      Ord: 4, Key: "usd", Type: UPDATE, OldValue: 1.47, NewValue: 1.65,
   ]
}
```
- `store.get_first() == "1.45"`: you get the *OldValue* of the first delta, which is equivalent to `StoreUSDPrice(Block #999).get_last()`
- `store.get_last() == "1.65"`: you get the *NewValue* of the last delta which is the state at end of Block #1000
- `store.get_at(1) == "1.47"`: you get the *NewValue* of the delta with *Ord == 1*, or the closest ordinal is Ord: 1 does not exist

The current implementation is as follows:
- Start with value = get\_last() (1.65)
- Iterate ord 4, value = detla.OldValue (1.47)
- Iterate ord 3, value = delta.OldValue ()
- Iterate ord 2, value = delta.OldValue (1.54)
- Iterate ord 1, ordinal == 1, return value (1.54)

### # `deltas mode`

`deltas` mode provides the module with **all the changes** occurring in the source `store` module. Updates, creates, and deletes of the keys mutated during the block processing become available.
- *Note:** When a `store` is set as an input to the module, it is read-only and you cannot modify, update or mutate them.
- *Note:** The deltas for a `set_sum` store type are always of type `bytes`, because the values are prepended with either "sum:" or "set:", depending on the method used.

[PreviousManifest & Modules](/documentation/develop/manifest-modules)[NextInputs](/documentation/develop/manifest-modules/inputs)

Last updated 4 months ago

---

## Chain-Specific Extensions | Substreams
Source: https://docs.substreams.dev/documentation/develop/overview

[EVM Chain-Specific Extensions](/documentation/develop/overview/evm-chain-specific-extensions)[PreviousParameterized Modules](/documentation/develop/parameterized-modules)[NextEVM Chain-Specific Extensions](/documentation/develop/overview/evm-chain-specific-extensions)

Last updated 3 months ago

---

## Initialize a Starknet Substreams Project | Substreams
Source: https://docs.substreams.dev/documentation/how-to-guides/starknet

In this guide, you'll learn how to initialize a Starknet-based Substreams project. You’ll learn how to set up a simple project to extract raw data or filter events from a smart contract.

## # Prerequisites
- Docker and VS Code installed and up-to-date.
- Visit the [Getting Started Guide](https://github.com/streamingfast/substreams-starter) to initialize your Dev Container.

## # Step 1: Initialize Your Starknet Substreams Project

1. Open your Dev Container and run the following command to initialize your project:
   
   Copy
   ```
   substreams init
   ```
2. You will be given the option to choose between two Starknet project options. Select the one that best fits your requirements:
- **starknet-minimal**: Creates a simple Substreams that extracts raw data from the block and generates Rust code.
- **starknet-events**: Creates a Substreams that extracts Starknet events using the cached [Starknet Foundational Module](https://substreams.dev/streamingfast/starknet-foundational/v0.1.3), filtered by one or more smart contract addresses.

## # Step 2: Visualize the Data

1. Create your account [here](https://thegraph.market/) to generate an authentification token (JWT) and pass it as input to:
   
   Copy
   ```
   substreams auth
   ```
2. Run the following command to visualize and itterate on your filtered data model:
   
   Copy
   ```
   substreams gui
   ```

## # Step 3: Customize your Project

After initialization, you can:
- Modify your Substreams manifest to include additional filters or configurations.
- Implement custom processing logic in Rust based on the filtered data retrieved by the foundational module.

## # Additional Resources

You may find these additional resources helpful for developing your first EVM application.

### # Dev Container Reference

The [Dev Container Reference](/reference-and-specs/devcontainer-ref) helps you navigate the complete container and its common errors.

### # GUI Reference

The [GUI reference](/reference-and-specs/gui) lets you explore all the tools available in the Substreams GUI.

### # Manifests Reference

The [Manifests Reference](/reference-and-specs/manifests) helps you with editing the `substreams.yaml`.

[PreviousInitialize a Solana Substreams Project](/documentation/how-to-guides/solana)[NextInitialize an Injective Substreams Project](/documentation/how-to-guides/injective)

Last updated 13 days ago

---

## EVM | Substreams
Source: https://docs.substreams.dev/tutorials/evm

This section contains Substreams tutorials specific to EVM-compatible chains (e.g. Ethereum, Polygon or BNB).

[PreviousArchitecture](/documentation/develop/architecture)[NextExploring Ethereum](/tutorials/evm/exploring-ethereum)

Last updated 10 months ago

---

## Initialize an EVM Substreams Project | Substreams
Source: https://docs.substreams.dev/documentation/how-to-guides/evm

In this guide, you'll learn how to initialize an EVM-based Substreams project. You’ll learn how to set up a simple project to extract raw data or filter EVM events and calls based on a smart-contract of interest.

## # Prerequisites
- Docker and VS Code installed and up-to-date.
- Visit the [Getting Started Guide](https://github.com/streamingfast/substreams-starter) to initialize your Dev Container.

## # Step 1: Initialize Your EVM Substreams Project

1. Open your Dev Container and run the following command to initialize your project:
   
   Copy
   ```
   substreams init
   ```
2. You will be given the option to choose between two EVM project options. Select the one that best fits your requirements:
- **evm-minimal**: Creates a simple Substreams that extracts raw data from the block and generates Rust code.
- **evm-events-calls**: Creates a Substreams that extracts EVM events and calls using the cached [EVM Foundational Module](https://substreams.dev/streamingfast/ethereum-common/v0.3.0), filtered by one or more smart contract addresses.

## # Step 2: Visualize the Data

1. Create your account [here](https://thegraph.market/) to generate an authentification token (JWT) and pass it as input to:
   
   Copy
   ```
   substreams auth
   ```
2. Run the following command to visualize and itterate on your filtered data model:
   
   Copy
   ```
   substreams gui
   ```

## # Step 3: Customize your Project

After initialization, you can:
- Modify your Substreams manifest to include additional filters or configurations.
- Implement custom processing logic in Rust based on the filtered data retrieved by the foundational module.

## # Additional Resources

You may find these additional resources helpful for developing your first EVM application.

### # Dev Container Reference

The [Dev Container Reference](/reference-and-specs/devcontainer-ref) helps you navigate the complete container and its common errors.

### # GUI Reference

The [GUI reference](/reference-and-specs/gui) lets you explore all the tools available in the Substreams GUI.

### # Manifests Reference

The [Manifests Reference](/reference-and-specs/manifests) helps you with editing the `substreams.yaml`.

[PreviousHow-To Guides](/documentation/how-to-guides)[NextInitialize a Solana Substreams Project](/documentation/how-to-guides/solana)

Last updated 13 days ago

---

## Aggregation Windows | Substreams
Source: https://docs.substreams.dev/documentation/develop/manifest-modules/aggregation-windows

Store module key-value storage can hold at most 1 GiB. It is usually enough if used correctly, but it is still a good idea (and sometimes even necessary) to free up unused keys. It is especially true for cases where you work with aggregation windows.

Consider this store module that aggregates hourly trade counter for each token:

Copy
```
# [substreams::handlers::store]
pub fn store_total_tx_counts(clock: Clock, events: Events, output: StoreAddBigInt) {
    let timestamp_seconds = clock.timestamp.unwrap().seconds;
    let hour_id = timestamp_seconds / 3600;
    let prev_hour_id = hour_id - 1;
    output.delete_prefix(0, &format!("TokenHourData:{prev_hour_id}:"));
    for event in events.pool_events {
        output.add_many(
            event.log_ordinal,
            &vec![
                format!("TokenHourData:{}:{}", hour_id, event.token0),
                format!("TokenHourData:{}:{}", hour_id, event.token1),
            ],
            &BigInt::from(1 as i32),
        );
    }
}
```

Let's break it down.

First, we use `Clock` input source to get the current and previous hour id for the block.

Copy
```
let hour_id = timestamp_seconds / 3600;
let prev_hour_id = hour_id - 1;
```

Then we build hourly keys for our counters and use `add_many` method to increment them. These counters will be consumed downstream by other modules.

Copy
```
output.add_many(
    event.log_ordinal,
    &vec![
        format!("TokenHourData:{}:{}", hour_id, event.token0),
        format!("TokenHourData:{}:{}", hour_id, event.token1),
    ],
    &BigInt::from(1 as i32),
);
```

Here's the trick. Since we don't need these counters outside of the hourly window, we can safely delete these key-value pairs for the previous hourly window and free up the memory.

This is done using `delete_prefix` method:

Copy
```
output.delete_prefix(0, &format!("TokenHourData:{prev_hour_id}:"));
```

Links
- ----
- [Uniswap-v3 Subgraph and Substreams](https://github.com/streamingfast/substreams-uniswap-v3)

[PreviousDynamic data sources](/documentation/develop/manifest-modules/dynamic-data-sources)[NextProtobuf Schemas](/documentation/develop/creating-protobuf-schemas)

Last updated 1 year ago

---

## Install the CLI | Substreams
Source: https://docs.substreams.dev/documentation/consume/installing-the-cli

## # Install the `substreams` CLI

Used for connecting to endpoints, streaming data in real time, and packaging custom modules.

### # Homebrew installation

Copy
```
brew install streamingfast/tap/substreams
```
### # Pre-compiled binary installation

There are several CLI binaries available for different operating systems. Choose the correct platform in the [CLI releases page](https://github.com/streamingfast/substreams/releases).

If you are on MacOS, you can use the following command:

Copy
```
LINK=$(curl -s https://api.github.com/repos/streamingfast/substreams/releases/latest | awk "/download.url.*$(uname -s | tr '[:upper:]' '[:lower:]')_$(uname -m)/ {print \$2}" | sed 's/"//g')
curl -L  $LINK  | tar zxf -
```

If you are on Linux, you can use the following command:

Copy
```
# Use correct binary for your platform
LINK=$(curl -s https://api.github.com/repos/streamingfast/substreams/releases/latest | awk "/download.url.*linux_$(uname -m)/ {print \$2}" | sed 's/"//g')
curl -L  $LINK  | tar zxf -
```
### # Installation from source

Copy
```
git clone https://github.com/streamingfast/substreams
cd substreams
go install -v ./cmd/substreams
```
- *Important**: Add $HOME/go/bin to the system path if it's not already present.

## # Validation of installation

Run the [`substreams` CLI](https://github.com/streamingfast/substreams/blob/develop/docs/new/reference-and-specs/command-line-interface.md) passing the `--version` flag to check the success of the installation.

Copy
```
substreams --version
```

A successful installation will print the version that you have installed.

Copy
```
substreams version dev
```
- *Note**: You can [also use Gitpod](https://github.com/streamingfast/substreams/blob/develop/docs/new/developers-guide/installation-requirements.md) instead of a local installation.

## # Install Other Developer Dependencies (Only for Substreams Developers)

If you plan to build your own Substreams (i.e. write Rust code to extract data from the blockchain), you will need several dependencies to set up your developer environment:
- *Tip**: Instructions are also provided for cloud-based Gitpod setups.

### # Rust installation

Developing Substreams modules requires a working [Rust](https://www.rust-lang.org/) compilation environment.

There are [several ways to install Rust](https://www.rust-lang.org/tools/install)**.** Install Rust through `curl` by using:

Copy
```
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
source $HOME/.cargo/env # to configure your current shell
```

`wasm32-unknown-unknown` **target**

Ensure you have the `wasm32-unknown-unknown` target installed on your Rust installation, if unsure, you can install it with:

Copy
```
rustup target add wasm32-unknown-unknown
```
### # Buf installation

Buf simplifies the generation of typed structures in any language. Buf uses a remote builder executed on the Buf server, so an internet connection is required to generate Rust bindings from Protobuf definitions.

Visit the [Buf website](https://buf.build/) for additional information and [installation instructions](https://docs.buf.build/installation).
- *Note***:* [Substreams packages](https://github.com/streamingfast/substreams/blob/develop/docs/new/reference-and-specs/packages.md) and [Buf images](https://docs.buf.build/reference/images) are compatible.

[PreviousConsume Substreams](/documentation/consume)[NextAuthentication](/documentation/consume/authentication)

Last updated 4 months ago

---

## Other Ways of Consuming | Substreams
Source: https://docs.substreams.dev/documentation/consume/other-sinks

[PreviousTriggers](/documentation/consume/subgraph/triggers)[NextFiles](/documentation/consume/other-sinks/files)

Last updated 8 months ago

---

## What is Substreams? | Substreams
Source: https://docs.substreams.dev/

[NextHow-To Guides](/documentation/how-to-guides)

Last updated 10 months ago

---
