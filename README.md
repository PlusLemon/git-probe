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

### 2026-11-27T06:51:11

#### [awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps)

##### Commit Changes

No file changes detected.

#### [awesome-gpt4o-images](https://github.com/jamez-bondos/awesome-gpt4o-images)

##### Commit Changes

No file changes detected.

#### [awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers)

##### Commit Changes

- [27551f1](https://github.com/punkpeye/awesome-mcp-servers/commit/27551f13dd8ae3929f1cdff66724e2e64e49da7f) Merge pull request #14315 from kevmoz/add-macaroon-bible-evidence - Frank Fiegel
- [77ddf9a](https://github.com/punkpeye/awesome-mcp-servers/commit/77ddf9a67d2e21a44865ed50dee98bde7e9d7376) Merge pull request #19469 from seyone22/add-ikman-gateway - Frank Fiegel
- [4177a2c](https://github.com/punkpeye/awesome-mcp-servers/commit/4177a2cb0afe5f906615d5f3797373d3d5330380) Fix entry formatting - Frank
- [37f7a79](https://github.com/punkpeye/awesome-mcp-servers/commit/37f7a7989938209bd185fbbc6e2359adfe6d135b) Merge pull request #18757 from RizgarOzan/add-playcal - Frank Fiegel
- [7f7bd7a](https://github.com/punkpeye/awesome-mcp-servers/commit/7f7bd7aa5e743aae37e623aa25d3dc578ad876a9) Merge pull request #19053 from calligraphysystems/main - Frank Fiegel
- [08ac613](https://github.com/punkpeye/awesome-mcp-servers/commit/08ac61357678ca0d567de207195864ef64de2b8c) Merge pull request #19875 from tomwaye/patch-1 - Frank Fiegel
- [ad27bb7](https://github.com/punkpeye/awesome-mcp-servers/commit/ad27bb7428ff811ca124d56da0f0b59e82cbec92) Merge pull request #19805 from leonhardprinz/add-healthaccess-mcp - Frank Fiegel
- [43e9a61](https://github.com/punkpeye/awesome-mcp-servers/commit/43e9a611b8f766142287192a60478a23470bfcdd) Merge pull request #16081 from thekevinm/add-faucetdb-faucet - Frank Fiegel
- [13e438e](https://github.com/punkpeye/awesome-mcp-servers/commit/13e438e343f7ca853ed596e2288b7bae49ae3ce6) Merge pull request #20400 from ColinGPT9/add-clips-kitty - Frank Fiegel
- [a6b47bd](https://github.com/punkpeye/awesome-mcp-servers/commit/a6b47bd82422e64b566864233cb252e64ee69807) Merge pull request #18144 from TillaCrypto/patch-1 - Frank Fiegel


##### File Content Changes

**README.md** (Modified, +10 -1 lines):

```diff
- - [RizgarOzan/playcal](https://github.com/RizgarOzan/playcal) 🐍 🏠 🍎 🪟 🐧 - Edit-settle-verify loop for coding agents in Unity and Godot: waits for the editor to finish importing, confirms the change landed, returns the first real error with file and line. Also flaky-vs-real playtests and texture/audio import checks.
+ - [kevmoz/macaroon-bible-evidence-mcp](https://github.com/kevmoz/macaroon-bible-evidence-mcp) [![kevmoz/macaroon-bible-evidence-mcp MCP server](https://glama.ai/mcp/servers/kevmoz/macaroon-bible-evidence-mcp/badges/score.svg)](https://glama.ai/mcp/servers/kevmoz/macaroon-bible-evidence-mcp) 🐍 ☁️ - Macaroon Bible Evidence: free, read-only Christian Scripture evidence over MCP -- exact Berean Standard Bible / World English Bible verse lookup, passage context, translation comparison, cross-references, keyword search and topic guides. Every response carries a source label, corpus version and deterministic content hash; no wallet, purchase or execution tool is exposed. Hosted remote server, no install, listed in the official MCP Registry as `com.macaroonnetwork/bible-evidence`: `https://api.macaroonnetwork.com/mcp-faith-evidence-v1/mcp/`
+ - [seyone22/ikman-gateway](https://github.com/seyone22/ikman-gateway) [![seyone22/ikman-gateway MCP server](https://glama.ai/mcp/servers/seyone22/ikman-gateway/badges/score.svg)](https://glama.ai/mcp/servers/seyone22/ikman-gateway) 📇 ☁️ 🍎 🪟 🐧 - Search Sri Lanka's ikman.lk classifieds marketplace with true low-to-high price sorting, dummy-price spam filtering, category and location taxonomies, and full ad details with seller phone numbers.
+ - [RizgarOzan/playcal](https://github.com/RizgarOzan/playcal) [![RizgarOzan/playcal MCP server](https://glama.ai/mcp/servers/RizgarOzan/playcal/badges/score.svg)](https://glama.ai/mcp/servers/RizgarOzan/playcal) 🐍 🏠 🍎 🪟 🐧 - Edit-settle-verify loop for coding agents in Unity and Godot: waits for the editor to finish importing, confirms the change landed, returns the first real error with file and line. Also flaky-vs-real playtests and texture/audio import checks.
+ - [RizgarOzan/playcal](https://github.com/RizgarOzan/playcal) 🐍 🏠 🍎 🪟 🐧 - Edit-settle-verify loop for coding agents in Unity and Godot: waits for the editor to finish importing, confirms the change landed, returns the first real error with file and line. Also flaky-vs-real playtests and texture/audio import checks.
+ - [calligraphysystems/vibe-hardware-mcp](https://github.com/calligraphysystems/vibe-hardware-mcp) [![calligraphysystems/vibe-hardware-mcp MCP server](https://glama.ai/mcp/servers/calligraphysystems/vibe-hardware-mcp/badges/score.svg)](https://glama.ai/mcp/servers/calligraphysystems/vibe-hardware-mcp) 🐍 ☁️ - Autonomous PCB routing and native KiCad DRC verification MCP server for hardware engineers and vibe-coding agents (KiCad, Altium, Eagle, Specctra DSN).
+ - [VerbatimCV/verbatimcv-mcp](https://github.com/VerbatimCV/verbatimcv-mcp) [![VerbatimCV/verbatimcv-mcp MCP server](https://glama.ai/mcp/servers/VerbatimCV/verbatimcv-mcp/badges/score.svg)](https://glama.ai/mcp/servers/VerbatimCV/verbatimcv-mcp) 🎖️ 🐍 ☁️ 🍎 🪟 🐧 - Official VerbatimCV server: parse CVs and resumes (PDF or DOCX, local file or URL) into versioned JSON where every candidate preference carries the verbatim quote it came from, nothing is invented, and hidden prompt injection is removed and reported. Free API key, no card.
+ - [leonhardprinz/healthaccess-mcp](https://github.com/leonhardprinz/healthaccess-mcp) [![leonhardprinz/healthaccess-mcp MCP server](https://glama.ai/mcp/servers/leonhardprinz/healthaccess-mcp/badges/score.svg)](https://glama.ai/mcp/servers/leonhardprinz/healthaccess-mcp) 🦀 🏠 🍎 🪟 🐧 - Apple Health and Apple Watch data from local files: workouts with every interval and pool length, daily sleep, HRV and vitals, written as JSON by a free iPhone app into a folder you own. Also puts AI-written workout plans back on the Apple Watch.
+ - [faucetdb/faucet](https://github.com/faucetdb/faucet) [![faucetdb/faucet MCP server](https://glama.ai/mcp/servers/faucetdb/faucet/badges/score.svg)](https://glama.ai/mcp/servers/faucetdb/faucet) 🎖️ 🏎️ 🏠 ☁️ 🍎 🪟 🐧 - Turn PostgreSQL, MySQL, MariaDB, SQL Server, Oracle, SQLite or Snowflake into MCP tools and a REST API, with API keys and per-table role-based access.
+ - [ColinGPT9/clips-studio](https://github.com/ColinGPT9/clips-studio) [![ColinGPT9/clips-studio MCP server](https://glama.ai/mcp/servers/ColinGPT9/clips-studio/badges/score.svg)](https://glama.ai/mcp/servers/ColinGPT9/clips-studio) 🎖️ 🐍 🏠 🪟 - Drive the Clips Kitty desktop clipper over stdio: queue a Twitch, Kick or YouTube VOD or a local video, start the queue, follow the job, list the 9:16 clips it picked, read their captions, schedule posts to the user's own connected accounts and read each post's live link. Transcription, highlight picking and speaker tracking run on the user's PC.
+ - [TillaCrypto/tilla](https://github.com/TillaCrypto/tilla) [![TillaCrypto/tilla MCP server](https://glama.ai/mcp/servers/TillaCrypto/tilla/badges/score.svg)](https://glama.ai/mcp/servers/TillaCrypto/tilla) 🐍 ☁️ - Market data for AI agents: crypto, US stocks, FX, macro, fund-by-fund Bitcoin and Ether spot ETF flows and a Bitcoin node on one UTC clock, with 280,675 no-look-ahead indicators. Refills missed bars and later corrections.
```



#### [Awesome-Dify-Workflow](https://github.com/svcvit/Awesome-Dify-Workflow)

##### Commit Changes

No file changes detected.

#### [system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools)

##### Commit Changes

No file changes detected.

