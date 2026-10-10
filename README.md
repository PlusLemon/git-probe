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

### 2026-10-10T04:27:30

#### [awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps)

##### Commit Changes

No file changes detected.

#### [awesome-gpt4o-images](https://github.com/jamez-bondos/awesome-gpt4o-images)

##### Commit Changes

No file changes detected.

#### [awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers)

##### Commit Changes

- [cc7f1f4](https://github.com/punkpeye/awesome-mcp-servers/commit/cc7f1f42c3fa8ced6fd5c0e02ea366ef7ed8cf1b) Merge pull request #13388 from clawdbotworker/add-forgemeshlabs-aso-score-mcp - Frank Fiegel
- [6982e27](https://github.com/punkpeye/awesome-mcp-servers/commit/6982e271f0b50c17a559c59e65a92efab183e6cf) Merge pull request #15556 from festuscharles-n/main - Frank Fiegel
- [1a76760](https://github.com/punkpeye/awesome-mcp-servers/commit/1a76760a22e269a46f536677598b45c87f86928b) Merge pull request #15652 from andrewbabu/add-loggly-mcp - Frank Fiegel
- [9fcff51](https://github.com/punkpeye/awesome-mcp-servers/commit/9fcff5199848a969205ec5f400caae6e73f95c08) Fix entry formatting - Frank Fiegel
- [bf00bbf](https://github.com/punkpeye/awesome-mcp-servers/commit/bf00bbfcfa4d8f3d2bcf3ebbc817b7e2b9304ba2) Merge pull request #15945 from MattStellisoft/add-stellify-mcp - Frank Fiegel
- [4f0a17d](https://github.com/punkpeye/awesome-mcp-servers/commit/4f0a17d40f3b548b28ea12d5a43a03d3bab8e17f) Merge pull request #15038 from ly8427/add-mcp-review-board - Frank Fiegel
- [baae356](https://github.com/punkpeye/awesome-mcp-servers/commit/baae356cb09eae1afb27ac703b0c6c459bd2a353) Merge pull request #15811 from Rikinshah787/add-dotpals - Frank Fiegel
- [31f0b23](https://github.com/punkpeye/awesome-mcp-servers/commit/31f0b23c5b20ba226d0730bfd16f5d151560e18d) Fix entry formatting - Frank Fiegel
- [5e58878](https://github.com/punkpeye/awesome-mcp-servers/commit/5e58878983923c69c5fd7ec203068a853a5c0ecc) Merge pull request #14838 from dchlamond/add-cos-codex-bridge - Frank Fiegel
- [a6ace5a](https://github.com/punkpeye/awesome-mcp-servers/commit/a6ace5a5c3754a45bc34ea1fc83c5d60f2b3aa6a) Merge pull request #15809 from Farenhytee/add-database-sentinel - Frank Fiegel


##### File Content Changes

**README.md** (Modified, +10 -2 lines):

```diff
- - [Stellify-Software-Ltd/stellify-mcp](https://github.com/Stellify-Software-Ltd/stellify-mcp) 📇 ☁️ - Build Laravel apps through conversation on the Stellify platform: code stored as structured JSON for surgical statement-level edits, with a shared reuse library, CRUD scaffolding, migrations and studio test runs.
- - [AV-Labs-Co/cos-codex-bridge](https://github.com/AV-Labs-Co/cos-codex-bridge) 📇 🏠 🍎 - Local MCP that lets a Chief of Staff client find, create and register Codex projects; submit exact prompts; track durable receipts; continue existing tasks; and organize scoped work inside allowlisted directories. [![AV-Labs-Co/cos-codex-bridge MCP server](https://glama.ai/mcp/servers/AV-Labs-Co/cos-codex-bridge/badges/score.svg)](https://glama.ai/mcp/servers/AV-Labs-Co/cos-codex-bridge)
+ - [forgemeshlabs/aso-score-mcp](https://github.com/forgemeshlabs/aso-score-mcp) [![forgemeshlabs/aso-score-mcp MCP server](https://glama.ai/mcp/servers/forgemeshlabs/aso-score-mcp/badges/score.svg)](https://glama.ai/mcp/servers/forgemeshlabs/aso-score-mcp) 📇 🏠 ☁️ 🍎 🪟 🐧 - Free ASO Score (Agent Signal Optimization) scanner scoring discovery, identity, trust, commerce, reputation, and memory signals, with maturity levels, evidence, and prioritized fix plans. Local stdio, no API key required. `npx -y @forgemeshlabs/aso-score-mcp`
+ - [SnapBlock/hai-browser](https://github.com/SnapBlock/hai-browser) [![SnapBlock/hai-browser MCP server](https://glama.ai/mcp/servers/SnapBlock/hai-browser/badges/score.svg)](https://glama.ai/mcp/servers/SnapBlock/hai-browser) 📇 🏠 🍎 🐧 - Let coding agents drive VS Code's Integrated Browser alongside you: snapshots, mouse and keyboard, forms, tabs, screenshots, console and network logs, a visible agent cursor, and click-to-source for React (Vite, Next.js).
+ - [andrewbabu/loggly-mcp](https://github.com/andrewbabu/loggly-mcp) [![andrewbabu/loggly-mcp MCP server](https://glama.ai/mcp/servers/andrewbabu/loggly-mcp/badges/score.svg)](https://glama.ai/mcp/servers/andrewbabu/loggly-mcp) 📇 ☁️ 🏠 🍎 🪟 🐧 - Read-only Loggly search and analytics with aggregation-first traffic tools and IP intelligence (RDAP, GreyNoise, AbuseIPDB).
+ - [Stellify-Software-Ltd/stellify-mcp](https://github.com/Stellify-Software-Ltd/stellify-mcp) [![Stellify-Software-Ltd/stellify-mcp MCP server](https://glama.ai/mcp/servers/Stellify-Software-Ltd/stellify-mcp/badges/score.svg)](https://glama.ai/mcp/servers/Stellify-Software-Ltd/stellify-mcp) 📇 ☁️ - Build Laravel apps through conversation on the Stellify platform: code stored as structured JSON for surgical statement-level edits, with a shared reuse library, CRUD scaffolding, migrations and studio test runs.
+ - [Stellify-Software-Ltd/stellify-mcp](https://github.com/Stellify-Software-Ltd/stellify-mcp) 📇 ☁️ - Build Laravel apps through conversation on the Stellify platform: code stored as structured JSON for surgical statement-level edits, with a shared reuse library, CRUD scaffolding, migrations and studio test runs.
+ - [ly8427/mcp-review-board](https://github.com/ly8427/mcp-review-board) [![ly8427/mcp-review-board MCP server](https://glama.ai/mcp/servers/ly8427/mcp-review-board/badges/score.svg)](https://glama.ai/mcp/servers/ly8427/mcp-review-board) 🐍 🏠 🍎 🪟 🐧 - Localhost review board where different coding agents (Claude Code, Codex, OpenCode, Trae, ZCode) review each other's work: objections must state flip conditions, revisions clear all verdicts, resolution requires the whole active quorum, and every vote is append-only audited. Ships its own audited self-review history as evidence. Install: `pipx install mcp-review-board`.
+ - [Rikinshah787/dotpals](https://github.com/Rikinshah787/dotpals) [![Rikinshah787/dotpals MCP server](https://glama.ai/mcp/servers/Rikinshah787/dotpals/badges/score.svg)](https://glama.ai/mcp/servers/Rikinshah787/dotpals) 📇 🏠 🍎 🪟 🐧 - Checks what local coding agents such as Claude Code, Codex and Cursor really did: files changed, commands run and test results read from test output, not the agent's word. Read-only.
+ - [AV-Labs-Co/cos-codex-bridge](https://github.com/AV-Labs-Co/cos-codex-bridge) [![AV-Labs-Co/cos-codex-bridge MCP server](https://glama.ai/mcp/servers/AV-Labs-Co/cos-codex-bridge/badges/score.svg)](https://glama.ai/mcp/servers/AV-Labs-Co/cos-codex-bridge) 📇 🏠 🍎 - Local MCP that lets a Chief of Staff client find, create and register Codex projects; submit exact prompts; track durable receipts; continue existing tasks; and organize scoped work inside allowlisted directories.
+ - [AV-Labs-Co/cos-codex-bridge](https://github.com/AV-Labs-Co/cos-codex-bridge) 📇 🏠 🍎 - Local MCP that lets a Chief of Staff client find, create and register Codex projects; submit exact prompts; track durable receipts; continue existing tasks; and organize scoped work inside allowlisted directories. [![AV-Labs-Co/cos-codex-bridge MCP server](https://glama.ai/mcp/servers/AV-Labs-Co/cos-codex-bridge/badges/score.svg)](https://glama.ai/mcp/servers/AV-Labs-Co/cos-codex-bridge)
+ - [Farenhytee/database-sentinel](https://github.com/Farenhytee/database-sentinel) [![Farenhytee/database-sentinel MCP server](https://glama.ai/mcp/servers/Farenhytee/database-sentinel/badges/score.svg)](https://glama.ai/mcp/servers/Farenhytee/database-sentinel) 🐍 ☁️ - Read-only security audit for Supabase. Four tools surface RLS gaps, permissive policies, exposed functions and grants; an `audit` prompt returns scored findings with fix SQL.
```



#### [Awesome-Dify-Workflow](https://github.com/svcvit/Awesome-Dify-Workflow)

##### Commit Changes

No file changes detected.

#### [system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools)

##### Commit Changes

No file changes detected.

