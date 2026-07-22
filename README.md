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

### 2026-07-22T02:32:24

#### [awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps)

##### Commit Changes

No file changes detected.

#### [awesome-gpt4o-images](https://github.com/jamez-bondos/awesome-gpt4o-images)

##### Commit Changes

No file changes detected.

#### [awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers)

##### Commit Changes

- [04f55a7](https://github.com/punkpeye/awesome-mcp-servers/commit/04f55a7e9ea6f417f64d3ac7386a339346566ff1) Merge pull request #10163 from FoundryNet/add-forge-industrial-iot - Frank Fiegel
- [6d28783](https://github.com/punkpeye/awesome-mcp-servers/commit/6d287835797b85d7cbc5b45e5076dac03b5603f3) Merge pull request #9058 from 0xJosee/add-truetick-mcp - Frank Fiegel
- [632de8e](https://github.com/punkpeye/awesome-mcp-servers/commit/632de8ea6ce1cb8c68d5085505440c039a448837) Merge pull request #9454 from ontorata/add-ratary-memory-mcp - Frank Fiegel
- [e312356](https://github.com/punkpeye/awesome-mcp-servers/commit/e3123562d1b3970f650b5bc32ff049e624e29f64) Merge pull request #9850 from agentIgris/add-agentfund-mcp - Frank Fiegel
- [7258c7f](https://github.com/punkpeye/awesome-mcp-servers/commit/7258c7f3a91c18442c62d344c4d8ed1f77fcff5a) Merge pull request #10183 from FI-Mihej/add-new-server-text_file_read_and_refactor_mcp - Frank Fiegel
- [1383320](https://github.com/punkpeye/awesome-mcp-servers/commit/138332044897000f7757154ef37ae4515dd2a514) Merge pull request #9732 from ajdelaguila/data-olympus-knowledge-memory-20260709-1783618398447 - Frank Fiegel
- [83ef10a](https://github.com/punkpeye/awesome-mcp-servers/commit/83ef10aaa03bb299756a44999f8b6ab52f7b9844) Fix entry formatting - Frank Fiegel
- [116afcd](https://github.com/punkpeye/awesome-mcp-servers/commit/116afcd2cf95423ab2c4fc18eb282a290d55ef49) Merge pull request #10305 from slenderongithub/add-fix-protocol-mcp - Frank Fiegel
- [f54f8ef](https://github.com/punkpeye/awesome-mcp-servers/commit/f54f8ef7923908f6838117fb2767908d4cccc32a) Merge pull request #9832 from haiiibin/add-acb-tax-mcp - Frank Fiegel
- [3d5fede](https://github.com/punkpeye/awesome-mcp-servers/commit/3d5fede7de1ce52795f30c41492a26c41f5cfd77) Fix entry formatting - Frank Fiegel


##### File Content Changes

**README.md** (Modified, +16 -2 lines):

```diff
- - [slenderongithub/fix-protocol-mcp](https://github.com/slenderongithub/fix-protocol-mcp) 🐍 🏠 - Parse, validate, build, and explain FIX protocol trading messages (Logon, NewOrderSingle, ExecutionReport, and the rest of the session/order workflow). Fully offline — bundled FIX 4.4 field dictionary, no API keys or network calls. Install `pip install .`, run `fix-protocol-mcp`.
- - [telly6/searchpin](https://github.com/telly6/searchpin) 🐍 🏠 - Free web search for AI agents with smart re-ranking. Multi-engine parallel search, zero API keys. Works natively within China's network, no proxy/VPN needed. Install via `pip install searchpin && searchpin-setup`. [![telly6/searchpin MCP server](https://glama.ai/mcp/servers/telly6/searchpin/badges/score.svg)](https://glama.ai/mcp/servers/telly6/searchpin)
+ * 🏭 - [Industrial & IoT](#industrial--iot)
+ ### 🏭 <a name="industrial--iot"></a>Industrial & IoT
+ Connect AI agents to industrial equipment, machinery, and operational technology (OT) — telemetry ingestion, monitoring, and control across manufacturing and factory-floor protocols.
+ - [FoundryNet/forge-mcp](https://github.com/FoundryNet/forge-mcp) 🐍 ☁️ - Industrial AI infrastructure that connects any AI agent to industrial equipment: 14 protocols, 18 manufacturers, 30 tools, cross-OEM telemetry normalization, health index, and failure prediction. The first physical-world MCP server. Free tier available. ([Smithery](https://smithery.ai/server/@foundrynet/forge)) [![FoundryNet/forge-mcp MCP server](https://glama.ai/mcp/servers/FoundryNet/forge-mcp/badges/score.svg)](https://glama.ai/mcp/servers/FoundryNet/forge-mcp)
+ - [truetick-gg/mcp](https://github.com/truetick-gg/mcp) 📇 ☁️ - Manage [TrueTick](https://truetick.gg) Minecraft hosting servers from AI agents: create/start/stop servers, live TPS/MSPT metrics, RCON console, file access, backups, and Modrinth/CurseForge mods.
+ - [ontorata/ratary](https://github.com/ontorata/ratary) [![ontorata/ratary MCP server](https://glama.ai/mcp/servers/ontorata/ratary/badges/score.svg)](https://glama.ai/mcp/servers/ontorata/ratary) 📇 🏠 ☁️ 🍎 🪟 🐧 - Persistent coding memory for AI assistants — hybrid search, knowledge graph, token-efficient context. MCP stdio (28 tools), npm `@ratary/mcp-server`, optional remote Streamable HTTP. Self-host D1, Postgres, MariaDB, or Docker.
+ - [@agentfund/mcp](https://github.com/agentIgris/agentfund) [![agentIgris/agentfund MCP server](https://glama.ai/mcp/servers/agentIgris/agentfund/badges/score.svg)](https://glama.ai/mcp/servers/agentIgris/agentfund) 📇 ☁️ - Fundraising infrastructure for AI agents on Solana — campaigns, x402 donations, and on-chain reputation. MCP tools for registering agents, creating campaigns, and donating via the x402 pay-to-call flow, backed by Anchor programs (agent_registry, escrow, reputation). `npx -y @agentfund/mcp`
+ - [FI-Mihej/text_file_read_and_refactor_mcp](https://github.com/FI-Mihej/text_file_read_and_refactor_mcp) [![text_file_read_and_refactor_mcp MCP server](https://glama.ai/mcp/servers/FI-Mihej/text_file_read_and_refactor_mcp/badges/score.svg)](https://glama.ai/mcp/servers/FI-Mihej/text_file_read_and_refactor_mcp) 🐍 🏠 🍎 🪟 🐧 - Token-efficient Python stdio MCP server exposing safe text-file search, reading, and refactoring tools. Tools automatically resolve the file BOM and codepage; edit tools save files with their original encoding and BOM. `uvx text-file-read-and-refactor-mcp`
+ - [knaisoma/data-olympus](https://github.com/knaisoma/data-olympus) [![knaisoma/data-olympus MCP server](https://glama.ai/mcp/servers/knaisoma/data-olympus/badges/score.svg)](https://glama.ai/mcp/servers/knaisoma/data-olympus) 🐍 🏠 🍎 🪟 🐧 - Governance-grade project knowledge MCP server for coding agents. Git-native Markdown knowledge base with proposed vs accepted guidance, validity windows, supersession chains, and status-aware retrieval of current in-force decisions and standards. `pip install data-olympus`
+ - [slenderongithub/fix-protocol-mcp](https://github.com/slenderongithub/fix-protocol-mcp) [![slenderongithub/fix-protocol-mcp MCP server](https://glama.ai/mcp/servers/slenderongithub/fix-protocol-mcp/badges/score.svg)](https://glama.ai/mcp/servers/slenderongithub/fix-protocol-mcp) 🐍 🏠 - Parse, validate, build, and explain FIX protocol trading messages (Logon, NewOrderSingle, ExecutionReport, and the rest of the session/order workflow). Fully offline — bundled FIX 4.4 field dictionary, no API keys or network calls. Install `pip install .`, run `fix-protocol-mcp`.
+ - [slenderongithub/fix-protocol-mcp](https://github.com/slenderongithub/fix-protocol-mcp) 🐍 🏠 - Parse, validate, build, and explain FIX protocol trading messages (Logon, NewOrderSingle, ExecutionReport, and the rest of the session/order workflow). Fully offline — bundled FIX 4.4 field dictionary, no API keys or network calls. Install `pip install .`, run `fix-protocol-mcp`.
+ - [haiiibin/acb-tax-mcp](https://github.com/haiiibin/acb-tax-mcp) [![haiiibin/acb-tax-mcp MCP server](https://glama.ai/mcp/servers/haiiibin/acb-tax-mcp/badges/score.svg)](https://glama.ai/mcp/servers/haiiibin/acb-tax-mcp) 🐍 🏠 🍎 🪟 🐧 - Canadian adjusted cost base (ACB) and capital gains from a trade history: average-cost tracking, per-disposition realized gains, and superficial-loss detection. Pure Python, runs locally, a calculation aid (not tax advice). `pip install acb-tax-mcp`.
+ - [telly6/searchpin](https://github.com/telly6/searchpin) [![telly6/searchpin MCP server](https://glama.ai/mcp/servers/telly6/searchpin/badges/score.svg)](https://glama.ai/mcp/servers/telly6/searchpin) 🐍 🏠 - Free web search for AI agents with smart re-ranking. Multi-engine parallel search, zero API keys. Works natively within China's network, no proxy/VPN needed. Install via `pip install searchpin && searchpin-setup`.
```



#### [Awesome-Dify-Workflow](https://github.com/svcvit/Awesome-Dify-Workflow)

##### Commit Changes

No file changes detected.

#### [system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools)

##### Commit Changes

No file changes detected.

