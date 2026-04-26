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

### 2026-04-26T02:39:56

#### [awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps)

##### Commit Changes

No file changes detected.

#### [awesome-gpt4o-images](https://github.com/jamez-bondos/awesome-gpt4o-images)

##### Commit Changes

No file changes detected.

#### [awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers)

##### Commit Changes

- [b3352d5](https://github.com/punkpeye/awesome-mcp-servers/commit/b3352d54921703c3f4a4775ae395dd079f621667) Merge pull request #5296 from crabsmadethis/add-d2r-horadric-tools - Frank Fiegel
- [97ed524](https://github.com/punkpeye/awesome-mcp-servers/commit/97ed5243fbc07efd84141321affafbf26f0edea3) Merge pull request #5013 from Mike25app/add-scaleforge-meta-ads-mcp - Frank Fiegel
- [3d64659](https://github.com/punkpeye/awesome-mcp-servers/commit/3d6465986abad9063650d6093ec066f5f028d885) Merge pull request #5372 from bezata/add-kobsidian-mcp-glama - Frank Fiegel
- [b96fb6c](https://github.com/punkpeye/awesome-mcp-servers/commit/b96fb6cdc59a201bea0a3a484d535cd9af2664ed) Merge pull request #4488 from VladUZH/add-mcp-guard - Frank Fiegel
- [d688954](https://github.com/punkpeye/awesome-mcp-servers/commit/d688954c85eb195e382582f9ef00ee011d2fcae7) Merge pull request #5376 from LukeLamb/add-claude-ollama-mcp - Frank Fiegel
- [b6ebe1c](https://github.com/punkpeye/awesome-mcp-servers/commit/b6ebe1c09177c9396cc471137a78371f090bb1e0) Merge pull request #5354 from Agnuxo1/fix-enigmagent-mcp-rebase - Frank Fiegel
- [a59f4ca](https://github.com/punkpeye/awesome-mcp-servers/commit/a59f4cab245255e5339db794d8e9e0e2170392f2) Merge pull request #5366 from him229/add-stays-mcp-server - Frank Fiegel
- [e4e8451](https://github.com/punkpeye/awesome-mcp-servers/commit/e4e845157dca9f31c5f9ed88c5df08f4c0628f5c) Merge pull request #5306 from sailorpepe/add-undesirables-mcp-server - Frank Fiegel
- [3835ffb](https://github.com/punkpeye/awesome-mcp-servers/commit/3835ffb86d253cb12da43b0f2580f8efefb7d3fe) Merge pull request #5394 from re-bruce-wayne/add-trade-router - Frank Fiegel
- [f9a451f](https://github.com/punkpeye/awesome-mcp-servers/commit/f9a451fb3819e9a6afb1bc31dd8c5e2510125705) Merge pull request #5016 from cloudforgetech6-ctrl/add-cloudforge-mcp - Frank Fiegel


##### File Content Changes

**README.md** (Modified, +10 -0 lines):

```diff
+ - [crabsmadethis/d2r-horadric-tools](https://github.com/crabsmadethis/d2r-horadric-tools) [![crabsmadethis/d2r-horadric-tools MCP server](https://glama.ai/mcp/servers/crabsmadethis/d2r-horadric-tools/badges/score.svg)](https://glama.ai/mcp/servers/crabsmadethis/d2r-horadric-tools) 🐍 🏠 🐧 - First read/write MCP toolchain for a shipped commercial game. 23 tools for Diablo II: Resurrected covering game-data lookups (uniques, sets, runewords, skills, stats), binary save-file (`.d2s`) inspection and diff, declarative YAML → playable save character builder with structural safety guards, and a CASC-backed mod build/deploy pipeline (overlays, JSON string patches, dataversionbuild). Linux / Steam Deck (Proton).
+ - [Mike25app/scaleforge-mcp-meta-ads](https://github.com/Mike25app/scaleforge-mcp-meta-ads) [![scaleforge-mcp-meta-ads MCP server](https://glama.ai/mcp/servers/Mike25app/scaleforge-mcp-meta-ads/badges/score.svg)](https://glama.ai/mcp/servers/Mike25app/scaleforge-mcp-meta-ads) 📇 🏠 - **Meta Ads MCP by [ScaleForge](https://getscaleforge.com)** — direct Meta Graph API v24.0 wrapper with 32 tools for Facebook & Instagram Ads. Auto-batch for bulk ops (sidesteps rate-limit code #17), pre-flight 250-ads-per-Page check, PBIA auto-provisioning, and enhanced token-expiry errors. No backend — token stays local.
+ - [bezata/kObsidian](https://github.com/bezata/kObsidian) [![bezata/kObsidian MCP server](https://glama.ai/mcp/servers/bezata/kObsidian/badges/score.svg)](https://glama.ai/mcp/servers/bezata/kObsidian) 📇 🏠 🍎 🪟 🐧 - Filesystem-first MCP server for Obsidian vaults with an LLM-Wiki layer (Karpathy pattern: persistent, LLM-maintained Sources/Concepts/Entities + greppable log). 66 tools across vaults, notes, links, tags, tasks, Dataview, Canvas, Kanban, Mermaid, Marp, Templates. Multi-vault discovery + in-session switching, stdio + Streamable HTTP. `npx -y kobsidian-mcp`
+ - [sidclawhq/mcp-guard](https://github.com/sidclawhq/mcp-guard) [![sidclawhq/mcp-guard MCP server](https://glama.ai/mcp/servers/sidclawhq/platform/badges/score.svg)](https://glama.ai/mcp/servers/sidclawhq/platform) 📇 🏠 🍎 🪟 🐧 - Policy-based guardrails for MCP servers. Wraps any MCP server with allow/block/hold-for-approval rules using YAML policies. Standalone CLI — no SDK needed.
+ - [LukeLamb/claude-ollama-mcp](https://github.com/LukeLamb/claude-ollama-mcp) [![LukeLamb/claude-ollama-mcp MCP server](https://glama.ai/mcp/servers/LukeLamb/claude-ollama-mcp/badges/score.svg)](https://glama.ai/mcp/servers/LukeLamb/claude-ollama-mcp) 📇 🏠 🐧 🍎 🪟 - Lets Claude query and manage a local Ollama server: list/show/pull/delete models, run generate/chat completions. Zero npm deps, pure Node over the HTTP API.
+ - [Agnuxo1/enigmagent-mcp](https://github.com/Agnuxo1/enigmagent-mcp) [![enigmagent-mcp MCP server](https://glama.ai/mcp/servers/Agnuxo1/enigmagent-mcp/badges/score.svg)](https://glama.ai/mcp/servers/Agnuxo1/enigmagent-mcp) 📇 🏠 🍎 🪟 🐧 - Encrypted local vault for AI agents. Resolve `{{SECRET}}` placeholders in prompts at runtime — the LLM never sees real API keys. AES-256-GCM + Argon2id, zero cloud, browser extension included. `npx enigmagent-mcp`
+ - [him229/stays](https://github.com/him229/stays) [![him229/stays MCP server](https://glama.ai/mcp/servers/him229/stays/badges/score.svg)](https://glama.ai/mcp/servers/him229/stays) 🐍 ☁️ 🍎 🪟 🐧 - Google Hotels MCP server via direct RPC — no scraping, no browser automation. Three tools: hotel list search (16 filter slots: stars, price, amenities, brands, free cancellation), per-OTA rate plans and cancellation policies for a single hotel, and parallel top-N enrichment. One-command setup for Claude Code, Codex, and ChatGPT; `pipx install stays`.
+ - [sailorpepe/undesirables-mcp-server](https://github.com/sailorpepe/undesirables-mcp-server) [![sailorpepe/undesirables-mcp-server MCP server](https://glama.ai/mcp/servers/sailorpepe/undesirables-mcp-server/badges/score.svg)](https://glama.ai/mcp/servers/sailorpepe/undesirables-mcp-server) 🐍 🏠 - 35+ tool MCP server for TCG collectibles. Vision AI card grading (PSA/Beckett), Monte Carlo price simulation (Heston/Merton/Kou), AI music generation, local image generation, TTS, RAG memory, and financial analytics. Zero telemetry, 100% local compute. `pip install undesirables-mcp-server`
+ - [TradeRouter/trade-router-mcp](https://github.com/TradeRouter/trade-router-mcp) [![TradeRouter/trade-router-mcp MCP server](https://glama.ai/mcp/servers/@traderouter/trade-router-mcp/badges/score.svg)](https://glama.ai/mcp/servers/@traderouter/trade-router-mcp) 📇 ☁️ - Non-custodial Solana swap & limit-order MCP server. 21 tools (swap, limit, trailing, TWAP, DCA, combo orders) across Raydium, PumpSwap, Orca, and Meteora. Jito MEV-protected. Ed25519 server-message verification. Private key never leaves the agent. `npx -y @traderouter/trade-router-mcp`.
+ - [cloudforgetech6-ctrl/mcp_server](https://github.com/cloudforgetech6-ctrl/mcp_server) [![cloudforge-mcp MCP server](https://glama.ai/mcp/servers/cloudforgetech6-ctrl/mcp_server/badges/score.svg)](https://glama.ai/mcp/servers/cloudforgetech6-ctrl/mcp_server) 📇 ☁️ - Visualise cloud architecture diagrams, generate Terraform HCL, import existing IaC, and manage Azure/AWS/GCP resources with AI. Authenticate with a CloudForge API key from cloudforge.cloud.
```



#### [Awesome-Dify-Workflow](https://github.com/svcvit/Awesome-Dify-Workflow)

##### Commit Changes

No file changes detected.

#### [system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools)

##### Commit Changes

No file changes detected.

