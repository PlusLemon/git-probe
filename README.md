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

### 2026-07-24T02:34:12

#### [awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps)

##### Commit Changes

No file changes detected.

#### [awesome-gpt4o-images](https://github.com/jamez-bondos/awesome-gpt4o-images)

##### Commit Changes

No file changes detected.

#### [awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers)

##### Commit Changes

- [df0609d](https://github.com/punkpeye/awesome-mcp-servers/commit/df0609d0f7d475b723a5cd8bb3fd0247bc3206e7) Merge pull request #10413 from bensynapse/add-livetennisapi-mcp - Frank Fiegel
- [c9b7fe6](https://github.com/punkpeye/awesome-mcp-servers/commit/c9b7fe6203b041eb56a6e3b48612c1695f482f21) Fix entry formatting - Frank Fiegel
- [4f10f7e](https://github.com/punkpeye/awesome-mcp-servers/commit/4f10f7ebb638345f2f0036a334f3ae89aeefa48e) Fix entry formatting - Frank Fiegel
- [31c7e7c](https://github.com/punkpeye/awesome-mcp-servers/commit/31c7e7cf9451398ec35df735c8473d58a094c44d) Merge pull request #10790 from Musk-aaan/add-muze-cmo - Frank Fiegel
- [0e27c5b](https://github.com/punkpeye/awesome-mcp-servers/commit/0e27c5bd3d0ac8dbb26b486b3d371fdd24fb3bd1) Add Glama score badge; point entry at the listed repo - Musk-aaan
- [1580a14](https://github.com/punkpeye/awesome-mcp-servers/commit/1580a143df9f8e50a93c10ea7cb66903e47b4d14) Add ctxfile to Knowledge & Memory (rebased on latest main) - ctxfile
- [65687de](https://github.com/punkpeye/awesome-mcp-servers/commit/65687de65f87e41e52a4101fe6238869d3dfd433) Merge pull request #10605 from jamiew/add-glif - Frank Fiegel
- [3c59b47](https://github.com/punkpeye/awesome-mcp-servers/commit/3c59b477f5009b8ddfc84e25e91ed846a24bebb4) Add Glama score badge to truecopy entry - askalf
- [490fb3f](https://github.com/punkpeye/awesome-mcp-servers/commit/490fb3f389e97b15ef98e1d6bbcc6c7ef435786b) Add truecopy (agent skills & MCP supply-chain gate) to Security - askalf
- [c268905](https://github.com/punkpeye/awesome-mcp-servers/commit/c268905871ea9cefaa493f1b746d4a59c5890a41) Add Glama badge to Glif entry - Jamie Dubs


##### File Content Changes

**README.md** (Modified, +10 -5 lines):

```diff
- - [glifxyz/glif-mcp-server](https://github.com/glifxyz/glif-mcp-server) [![Glama](https://raw.githubusercontent.com/glama-ai/glama/main/assets/glama-badge.svg)](https://glama.ai/mcp/servers/glifxyz-glif-mcp-server) 🎖️ ☁️ - Glif's official hosted media-generation agent: generate images, video, and audio, transcribe, and chain multi-step media workflows from natural language. Remote server at https://glif.app/api/mcp (OAuth).
- - [isco-tec/scorezilla-mcp](https://github.com/isco-tec/scorezilla-mcp) 🎖️ 📇 ☁️ 🍎 🪟 🐧 - Provision and inspect leaderboards for [Scorezilla](https://scorezilla.dev). Six tools — including `bootstrap_leaderboard` which creates a game + board + keys and returns ready-to-paste SDK code in one call. Closed beta; request a token at scorezilla.dev/early-access.
- - [Agent-Prod/muze-mcp-connector](https://github.com/Agent-Prod/muze-mcp-connector) 🎖️ 🐍 ☁️ - Run Meta, Google, Amazon, and Shopify ads from Claude, ChatGPT, and Cursor. 150 tools across four platforms: read performance, inspect campaigns, research competitors, and confirm-gated writes (pause, budgets, launches) that always stage paused. Hosted; connect via OAuth or an API key at https://backend.muzecmo.com/mcp
- - [askalf/truecopy](https://github.com/askalf/truecopy) 📇 🏠 🍎 🪟 🐧 - Supply-chain gate for agent skills and MCP servers — scans tool definitions for poisoned instructions, pins vetted servers by content hash in a committed lock, and verifies drift in CI; the bundled truecopy-mcp proxy exposes only pinned, unmodified tools from a live server.
- - [glifxyz/glif-mcp-server](https://github.com/glifxyz/glif-mcp-server) 🎖️ ☁️ - Glif's official hosted media-generation agent: generate images, video, and audio, transcribe, and chain multi-step media workflows from natural language. Remote server at https://glif.app/api/mcp (OAuth).
+ - [livetennisapi/livetennisapi-mcp](https://github.com/livetennisapi/livetennisapi-mcp) [![livetennisapi/livetennisapi-mcp MCP server](https://glama.ai/mcp/servers/livetennisapi/livetennisapi-mcp/badges/score.svg)](https://glama.ai/mcp/servers/livetennisapi/livetennisapi-mcp) 📇 ☁️ 🍎 🪟 🐧 - Real-time tennis for ATP, WTA, Challenger and ITF — live scores, players, fixtures, model win-probability, and match-winner market prices. 12 read-only tools; a plan wall returns a plain-English explanation instead of a bare 403. Free tier, no card. `npx -y livetennisapi-mcp`
+ - [glifxyz/glif-mcp-server](https://github.com/glifxyz/glif-mcp-server) [![glifxyz/glif-mcp-server MCP server](https://glama.ai/mcp/servers/glifxyz/glif-mcp-server/badges/score.svg)](https://glama.ai/mcp/servers/glifxyz/glif-mcp-server) 🎖️ ☁️ - Glif's official hosted media-generation agent: generate images, video, and audio, transcribe, and chain multi-step media workflows from natural language. Remote server at https://glif.app/api/mcp (OAuth).
+ - [isco-tec/scorezilla-mcp](https://github.com/isco-tec/scorezilla-mcp) [![isco-tec/scorezilla-mcp MCP server](https://glama.ai/mcp/servers/isco-tec/scorezilla-mcp/badges/score.svg)](https://glama.ai/mcp/servers/isco-tec/scorezilla-mcp) 🎖️ 📇 ☁️ 🍎 🪟 🐧 - Provision and inspect leaderboards for [Scorezilla](https://scorezilla.dev). Six tools — including `bootstrap_leaderboard` which creates a game + board + keys and returns ready-to-paste SDK code in one call. Closed beta; request a token at scorezilla.dev/early-access.
+ - [Agent-Prod/muze-mcp](https://github.com/Agent-Prod/muze-mcp) [![Agent-Prod/muze-mcp MCP server](https://glama.ai/mcp/servers/Agent-Prod/muze-mcp/badges/score.svg)](https://glama.ai/mcp/servers/Agent-Prod/muze-mcp) 🎖️ 🐍 ☁️ - Run your ecommerce ads from Claude & ChatGPT. Meta, Google, Amazon and Shopify: 150+ tools to read performance, inspect campaigns, research competitor ads, and take confirm-gated writes (pause, budgets, launches) that always stage paused. Hosted; connect via OAuth or an API key at https://backend.muzecmo.com/mcp
+ - [ctxfile/ctxfile](https://github.com/ctxfile/ctxfile) [![ctxfile/ctxfile MCP server](https://glama.ai/mcp/servers/ctxfile/ctxfile/badges/score.svg)](https://glama.ai/mcp/servers/ctxfile/ctxfile) 📇 🏠 🍎 🪟 🐧 - Local-first MCP server that snapshots your project's working state — files, git, plan, and decisions — into one structured context object and hands it to any MCP client in a single call. Save a session in one agent, continue it in another. Zero network calls by default; read-only over your project. Works with Claude Code, Cursor, and any MCP client. `npx -y ctxfile`
+ - [glifxyz/glif-mcp-server](https://github.com/glifxyz/glif-mcp-server) [![Glama](https://raw.githubusercontent.com/glama-ai/glama/main/assets/glama-badge.svg)](https://glama.ai/mcp/servers/glifxyz-glif-mcp-server) 🎖️ ☁️ - Glif's official hosted media-generation agent: generate images, video, and audio, transcribe, and chain multi-step media workflows from natural language. Remote server at https://glif.app/api/mcp (OAuth).
+ - [askalf/truecopy](https://github.com/askalf/truecopy) [![askalf/truecopy MCP server](https://glama.ai/mcp/servers/askalf/truecopy/badges/score.svg)](https://glama.ai/mcp/servers/askalf/truecopy) 📇 🏠 🍎 🪟 🐧 - Supply-chain gate for agent skills and MCP servers — scans tool definitions for poisoned instructions, pins vetted servers by content hash in a committed lock, and verifies drift in CI; the bundled truecopy-mcp proxy exposes only pinned, unmodified tools from a live server.
+ - [askalf/truecopy](https://github.com/askalf/truecopy) 📇 🏠 🍎 🪟 🐧 - Supply-chain gate for agent skills and MCP servers — scans tool definitions for poisoned instructions, pins vetted servers by content hash in a committed lock, and verifies drift in CI; the bundled truecopy-mcp proxy exposes only pinned, unmodified tools from a live server.
```



#### [Awesome-Dify-Workflow](https://github.com/svcvit/Awesome-Dify-Workflow)

##### Commit Changes

No file changes detected.

#### [system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools)

##### Commit Changes

No file changes detected.

