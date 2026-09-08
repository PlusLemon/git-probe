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

### 2026-09-08T03:11:11

#### [awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps)

##### Commit Changes

No file changes detected.

#### [awesome-gpt4o-images](https://github.com/jamez-bondos/awesome-gpt4o-images)

##### Commit Changes

No file changes detected.

#### [awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers)

##### Commit Changes

- [a62cced](https://github.com/punkpeye/awesome-mcp-servers/commit/a62ccedb39ba44b9a833e717960a107dacf7045a) Merge pull request #13727 from TomD4vs/add-prumo - Frank Fiegel
- [a6d0cdd](https://github.com/punkpeye/awesome-mcp-servers/commit/a6d0cddb26bba5b44a2bb2cc9d7261bb9b86ef95) Merge pull request #13610 from kev1n/add-anyapi-aggregators - Frank Fiegel
- [0bba417](https://github.com/punkpeye/awesome-mcp-servers/commit/0bba41721c5a5344fe322f0bbf835b71470023d4) Merge pull request #11679 from jubeiargh/patch-2 - Frank Fiegel
- [de66c18](https://github.com/punkpeye/awesome-mcp-servers/commit/de66c1841d8be36d0d1ed4c558bd4944ea28aa82) Merge pull request #13787 from bshea-1/routed-mcp-agent - Frank Fiegel
- [dd7341d](https://github.com/punkpeye/awesome-mcp-servers/commit/dd7341d9c6573fd2bbc8558066e7e886cb9c174b) Merge pull request #11073 from mutonby/add-upload-post - Frank Fiegel
- [a685f3f](https://github.com/punkpeye/awesome-mcp-servers/commit/a685f3f475a88026825275fe2e3672ba918eb85e) Merge pull request #13905 from Jonahbkerr/add-yocoolab - Frank Fiegel
- [7c80c18](https://github.com/punkpeye/awesome-mcp-servers/commit/7c80c18d8e0fd92e0f59e18d021b3f66428ddd49) Merge pull request #13642 from mrfelfel/add-taghvim-mcp - Frank Fiegel
- [81714b5](https://github.com/punkpeye/awesome-mcp-servers/commit/81714b54491d9dd4e01100b531cf32e247350cc8) Merge pull request #11397 from Kemetra/add-seshat-bi-governor - Frank Fiegel
- [e0d3cea](https://github.com/punkpeye/awesome-mcp-servers/commit/e0d3cea3e2fe70a372fe291d5519fc8cb3095854) Merge pull request #13327 from gordonkjlee/add-factmem - Frank Fiegel
- [ccf088e](https://github.com/punkpeye/awesome-mcp-servers/commit/ccf088ea99dba8dfce72054447d83857c7141aa4) Merge pull request #13080 from smeet666/add-mcp-ptitchef - Frank Fiegel


##### File Content Changes

**README.md** (Modified, +10 -0 lines):

```diff
+ - [TomD4vs/prumo](https://github.com/TomD4vs/prumo) [![TomD4vs/prumo MCP server](https://glama.ai/mcp/servers/TomD4vs/prumo/badges/score.svg)](https://glama.ai/mcp/servers/TomD4vs/prumo) 📇 🏠 🍎 🪟 🐧 - Checks the context files a coding agent reads (CLAUDE.md, AGENTS.md, SKILL.md, .cursor/rules) against the git index: wrong letter case, broken links, missing paths, commands nothing defines, and agent configuration that points at nothing. Two more tools report which sections drifted from the code and what each file costs.
+ - [getanyapi-com/mcp](https://github.com/getanyapi-com/mcp) [![getanyapi-com/mcp MCP server](https://glama.ai/mcp/servers/getanyapi-com/mcp/badges/score.svg)](https://glama.ai/mcp/servers/getanyapi-com/mcp) 🎖️ 📇 ☁️ 🏠 - AnyAPI: hundreds of scraping and data APIs (social media, search results, Google Maps, e-commerce, general web data) behind one MCP server - one key, USD pay-per-request, no subscriptions, normalized JSON schemas, and automatic failover across upstream providers. Agents discover, inspect, price and run any of them with the same loop (`search_apis`, `get_api`, `quote_api`, `run_api`); failed calls are never charged. Install: `npx -y anyapi-mcp`, or point a remote client straight at `https://api.getanyapi.com/mcp`.
+ - [callbk/finlight-mcp](https://github.com/callbk/finlight-mcp) [![callbk/finlight-mcp](https://glama.ai/mcp/servers/callbk/finlight-mcp/badges/score.svg)](https://glama.ai/mcp/servers/callbk/finlight-mcp) 🎖️ ☁️ - Real-time financial news: search by ticker, source, and language, with sentiment scores and tagged company entities.
+ - [bshea-1/Routed](https://github.com/bshea-1/Routed) [![bshea-1/Routed MCP server](https://glama.ai/mcp/servers/bshea-1/Routed/badges/score.svg)](https://glama.ai/mcp/servers/bshea-1/Routed) 📇 🏠 🍎 🪟 🐧 - Universal local router for Agent Skills across Cursor, Claude Code, Antigravity, and MCP clients with zero-token sub-20ms hybrid matching on local CPU.
+ - [Upload-Post/upload-post-mcp](https://github.com/Upload-Post/upload-post-mcp) [![Upload-Post/upload-post-mcp MCP server](https://glama.ai/mcp/servers/@Upload-Post/upload-post-mcp/badges/score.svg)](https://glama.ai/mcp/servers/@Upload-Post/upload-post-mcp) 🎖️ 📇 ☁️ 🏠 - Publish, schedule and analyze social media across TikTok, Instagram, YouTube, LinkedIn, Facebook, X, Threads, Pinterest, Reddit, Bluesky, Google Business, Discord and Telegram from one API. 50 tools covering uploads, scheduling queues, analytics, comments, DMs/auto-DMs and GPU video encoding. Hosted (OAuth 2.1 / API key) at `https://mcp.upload-post.com/mcp` or local stdio via `npx -y @upload-post/mcp`.
+ - [Yocoolab/mcp-server](https://github.com/Yocoolab/mcp-server) [![Yocoolab/mcp-server MCP server](https://glama.ai/mcp/servers/Yocoolab/mcp-server/badges/score.svg)](https://glama.ai/mcp/servers/Yocoolab/mcp-server) 🎖️ 📇 🏠 ☁️ 🍎 🪟 🐧 - Pin visual feedback on any live web page — localhost, staging or production — and hand it to your coding agent with the element, its CSS selector, a screenshot and the whole thread attached, then get a pull request back. Bridges to the Yocoolab browser extension locally and syncs threads through the Yocoolab API. Listed on the official MCP Registry (`io.github.Jonahbkerr/yocoolab`). `npx -y @yocoolab/mcp-server@2 setup`
+ - [mrfelfel/taghvim](https://github.com/mrfelfel/taghvim) [![mrfelfel/taghvim MCP server](https://glama.ai/mcp/servers/mrfelfel/taghvim/badges/score.svg)](https://glama.ai/mcp/servers/mrfelfel/taghvim) 📇 ☁️ - Deterministic temporal reasoning engine for AI agents. 12 tools for date/time arithmetic, timezone conversion with DST, business days across 100+ countries, public holidays, RFC 5545 recurrence, Gregorian/Persian calendar conversion, and temporal claim verification. `npx taghvim-mcp`
+ - [Kemetra/seshat-bi](https://github.com/Kemetra/Seshat-BI) [![Seshat-BI MCP server](https://glama.ai/mcp/servers/Kemetra/Seshat-BI/badges/score.svg)](https://glama.ai/mcp/servers/Kemetra/Seshat-BI) 🐍 🏠 🍎 🪟 🐧 - Read-only readiness governance for BI pipelines. Six tools report where each table sits across a seven-stage source-to-Power-BI spine, explain what is blocking the next stage, run a static SQL/TMDL/PBIR governance check, and export an evidence pack. Tools never write files, execute warehouse work, or grant approvals -- human sign-off stays a separate seam. Install: `pip install "seshat-bi[mcp]"` then `seshat mcp`.
+ - [gordonkjlee/facthouse](https://github.com/gordonkjlee/facthouse) [![gordonkjlee/facthouse MCP server](https://glama.ai/mcp/servers/gordonkjlee/facthouse/badges/score.svg)](https://glama.ai/mcp/servers/gordonkjlee/facthouse) 📇 🏠 🍎 🪟 🐧 - Local memory engine any AI tool can use; you own the SQLite file. `npx -y @facthouse/mcp`
+ - [smeet666/mcp-ptitchef](https://github.com/smeet666/mcp-ptitchef) [![smeet666/mcp-ptitchef MCP server](https://glama.ai/mcp/servers/smeet666/mcp-ptitchef/badges/score.svg)](https://glama.ai/mcp/servers/smeet666/mcp-ptitchef) 📇 ☁️ 🍎 🪟 🐧 - Search Ptitchef, browse its tree of ingredient categories, read a recipe with its ingredients, method, cost and nutrition, and ask what can be cooked from what is in the fridge. Rescales to any number of servings, and lists the other languages a recipe was published in. No API key. `npx -y mcp-ptitchef`
```



#### [Awesome-Dify-Workflow](https://github.com/svcvit/Awesome-Dify-Workflow)

##### Commit Changes

No file changes detected.

#### [system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools)

##### Commit Changes

No file changes detected.

