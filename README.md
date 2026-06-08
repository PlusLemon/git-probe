# Git Probe

Git Probe is a tool that monitors changes to specified files and directories in GitHub repositories. It runs daily using GitHub Actions, extracting change information and maintaining a history of these changes.

## Features

- Monitor specific files and directories in GitHub repositories
- Automatically check for updates daily via GitHub Actions
- Display detailed daily changes including commits, file content changes, and AI summaries
- Store historical changes in the `history/` directory with date-based naming
- Maintain repository-specific AI summaries in the `summaries/` directory
- Configurable monitoring via `probe.yaml`
- Project settings in `config.yaml` or environment variables
- Fast dependency management with UV

## How It Works

1. Each day, Git Probe checks the repositories specified in `probe.yaml`
2. For each repository, it retrieves:
   - Recent commits
   - Actual file content changes (diffs)
   - AI-generated summary of these changes (if enabled)
3. This information is displayed in the README.md under "Latest Changes"
4. Previous day's changes are archived to the `history/` directory with the format `repo_name_date.md`
5. Repository-specific summaries are maintained in the `summaries/` directory

more detais: [usage.md](usage.md)

## Thanks

If you find this project helpful, please consider giving it a star ⭐️. Thank you for your support!


## Latest Changes

### 2026-06-08T03:56:14

#### [awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps)

##### Commit Changes

No file changes detected.

#### [awesome-gpt4o-images](https://github.com/jamez-bondos/awesome-gpt4o-images)

##### Commit Changes

No file changes detected.

#### [awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers)

##### Commit Changes

- [e844de2](https://github.com/punkpeye/awesome-mcp-servers/commit/e844de260c0651b393e1a36c5e62453ffd64791a) Merge pull request #6265 from tamasPetki/main - Frank Fiegel
- [958547d](https://github.com/punkpeye/awesome-mcp-servers/commit/958547d914de089103227a95c6ad29516c1c6942) Merge pull request #7445 from roberttomko/add-spoken-server - Frank Fiegel
- [a67d63c](https://github.com/punkpeye/awesome-mcp-servers/commit/a67d63c8272f005cee6c35510bf9af360ef53378) Merge pull request #7011 from infai-tech/add-vulnfeed-mcp - Frank Fiegel
- [634f8c9](https://github.com/punkpeye/awesome-mcp-servers/commit/634f8c9e51092d160dfaf2529745687266e16a0b) Merge pull request #7399 from clanker-records/add-crompton-network - Frank Fiegel
- [fddb18a](https://github.com/punkpeye/awesome-mcp-servers/commit/fddb18a05644d398967f57ec3b74c3a1d4e95bdd) Merge pull request #6947 from zriyansh/add-vaquill-canlii-mcp - Frank Fiegel
- [2585e1e](https://github.com/punkpeye/awesome-mcp-servers/commit/2585e1ef21a2e7a1c3d09ed9844a26cce24e8071) Merge pull request #7041 from zw008/add-vmware-storage - Frank Fiegel
- [e575bba](https://github.com/punkpeye/awesome-mcp-servers/commit/e575bba59db7d005dacd065b716cdd3527f61cbf) description: add first-album-for-machines line - Hatoshi
- [f1a03bd](https://github.com/punkpeye/awesome-mcp-servers/commit/f1a03bde2d3f7a920659e355561b130dffc6d7a3) update description to settled copy - Hatoshi
- [3caa818](https://github.com/punkpeye/awesome-mcp-servers/commit/3caa8181bc5c08d9169b47ce273f44cdc07b647d) Merge pull request #7572 from teodorofodocrispin-cmyk/main - Frank Fiegel
- [ed74862](https://github.com/punkpeye/awesome-mcp-servers/commit/ed74862ac47f371bc3a3066b2fd2640470984c16) Merge pull request #7545 from musharna/add-plant-genomics-mcp - Frank Fiegel


##### File Content Changes

**README.md** (Modified, +10 -2 lines):

```diff
- - [clanker-records/crompton-network](https://github.com/clanker-records/crompton-network) [![clanker-records/crompton-network MCP server](https://glama.ai/mcp/servers/clanker-records/crompton-network/badges/score.svg)](https://glama.ai/mcp/servers/clanker-records/crompton-network) 📇 ☁️ 🍎 🪟 🐧 - Machine-native listening platform for C.W.A.'s Straight Outta Crompton. Your agent can listen. For real. `npx @clanker-records/crompton-network`
- - [clanker-records/crompton-network](https://github.com/clanker-records/crompton-network) [![clanker-records/crompton-network MCP server](https://glama.ai/mcp/servers/clanker-records/crompton-network/badges/score.svg)](https://glama.ai/mcp/servers/clanker-records/crompton-network) 📇 ☁️ 🍎 🪟 🐧 - Stream and analyze Straight Outta Crompton by C.W.A. as structured data. 22 tools, no keys, no auth. `npx @clanker-records/crompton-network`
+ - [tamasPetki/HeadlessTracker](https://github.com/tamasPetki/HeadlessTracker) [![tamasPetki/HeadlessTracker MCP server](https://glama.ai/mcp/servers/tamasPetki/HeadlessTracker/badges/score.svg)](https://glama.ai/mcp/servers/tamasPetki/HeadlessTracker) 📇 🏠 ☁️ 🍎 🪟 🐧 - Local-first crypto portfolio aggregation across exchanges (Bybit, Binance), EVM and Solana wallets, and Polymarket. Read-only credentials stored in your OS keychain, no hosted service. Data aggregation only, not financial advice. Install with `npx headless-tracker`.
+ - [spokenmd/spoken](https://github.com/spokenmd/spoken) [![spokenmd/spoken MCP server](https://glama.ai/mcp/servers/spokenmd/spoken/badges/score.svg)](https://glama.ai/mcp/servers/spokenmd/spoken) 📇 ☁️ - Fetch published podcast transcripts as clean Markdown with real speaker names (not "Speaker 1") via the [Spoken](https://spoken.md) API. Search episodes, get transcripts, check credit balance.
+ - [infai-tech/vulnfeed-mcp](https://github.com/infai-tech/vulnfeed-mcp) [![vulnfeed-mcp MCP server](https://glama.ai/mcp/servers/infai-tech/vulnfeed-mcp/badges/score.svg)](https://glama.ai/mcp/servers/infai-tech/vulnfeed-mcp) 🐍 🏠 🍎 🪟 🐧 - Dependency vulnerability scanner with EPSS exploit probability scoring. Scans lockfiles (npm, pip, Go, Cargo, Ruby, Composer, Gradle, NuGet, Mix), prioritizes by real-world exploit likelihood, recommends fix versions. 9 MCP tools for scanning, monitoring, and alerting. Free tier + x402 micropayments. `pip install vulnfeed-mcp`
+ - [clanker-records/crompton-network](https://github.com/clanker-records/crompton-network) [![clanker-records/crompton-network MCP server](https://glama.ai/mcp/servers/clanker-records/crompton-network/badges/score.svg)](https://glama.ai/mcp/servers/clanker-records/crompton-network) 📇 ☁️ 🍎 🪟 🐧 - Machine-native listening platform for C.W.A.'s Straight Outta Crompton - the first album released to machines before humans. Your agent can listen. For real. `npx @clanker-records/crompton-network`
+ - [Vaquill-AI/canlii-mcp](https://github.com/Vaquill-AI/canlii-mcp) [![Vaquill-AI/canlii-mcp MCP server](https://glama.ai/mcp/servers/Vaquill-AI/canlii-mcp/badges/score.svg)](https://glama.ai/mcp/servers/Vaquill-AI/canlii-mcp) 📇 ☁️ - Canadian case law and legislation metadata via CanLII. Bring-your-own free CanLII API key. Hosted endpoint at canlii-mcp.vaquill.ai. MIT.
+ - [zw008/VMware-Storage](https://github.com/zw008/VMware-Storage) [![zw008/vmware-storage MCP server](https://glama.ai/mcp/servers/zw008/vmware-storage/badges/score.svg)](https://glama.ai/mcp/servers/zw008/vmware-storage) 🐍 ☁️ - VMware vSphere storage management — datastores (NFS/VMFS), iSCSI software adapter and dynamic targets, and vSAN cluster operations. 11 tools with dry-run preview and double-confirmation for iSCSI configuration changes.
+ - [clanker-records/crompton-network](https://github.com/clanker-records/crompton-network) [![clanker-records/crompton-network MCP server](https://glama.ai/mcp/servers/clanker-records/crompton-network/badges/score.svg)](https://glama.ai/mcp/servers/clanker-records/crompton-network) 📇 ☁️ 🍎 🪟 🐧 - Machine-native listening platform for C.W.A.'s Straight Outta Crompton. Your agent can listen. For real. `npx @clanker-records/crompton-network`
+ - [teodorofodocrispin-cmyk/intelica-mcp](https://github.com/teodorofodocrispin-cmyk/intelica-mcp) [![intelica-mcp MCP server](https://glama.ai/mcp/servers/teodorofodocrispin-cmyk/intelica-mcp/badges/score.svg)](https://glama.ai/mcp/servers/teodorofodocrispin-cmyk/intelica-mcp) 🐍 ☁️ - Competitive intelligence API for autonomous AI agents. Analyzes any URL or company description and returns structured JSON with market positioning, competitors, pain points, and executable Market Score (threat_level, moat_strength, agent_recommendation). 10 context modes including regulatory_compliance, venture_screening, crypto_protocol, and sales_enablement. Pay-per-call via x402 on Base and Solana mainnet — no accounts, no API keys.
+ - [musharna/plant-genomics-mcp](https://github.com/musharna/plant-genomics-mcp) [![musharna/plant-genomics-mcp MCP server](https://glama.ai/mcp/servers/musharna/plant-genomics-mcp/badges/score.svg)](https://glama.ai/mcp/servers/musharna/plant-genomics-mcp) 🐍 🏠 🍎 🪟 🐧 - 32 tools for plant-genomics locus lookup across 11 public backends (Ensembl Plants, Phytozome, UniProtKB, KEGG, STRING-DB, Gramene, Europe PMC, QuickGO, NCBI BLAST, ATTED-II, BAR). Single-locus, parallel-batch, and cross-source synthesis variants; JSON output schemas and EDAM ontology tags on every tool. `pipx install plant-genomics-mcp`.
```



#### [Awesome-Dify-Workflow](https://github.com/svcvit/Awesome-Dify-Workflow)

##### Commit Changes

No file changes detected.

#### [system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools)

##### Commit Changes

No file changes detected.

