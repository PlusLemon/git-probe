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

### 2026-03-24T02:01:44

#### [awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps)

##### Commit Changes

No file changes detected.

#### [awesome-gpt4o-images](https://github.com/jamez-bondos/awesome-gpt4o-images)

##### Commit Changes

No file changes detected.

#### [awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers)

##### Commit Changes

- [ca7dfdd](https://github.com/punkpeye/awesome-mcp-servers/commit/ca7dfdd8d7d14dc225db609caab5efa6842762a6) Merge pull request #3788 from costajohnt/add-oss-autopilot - Frank Fiegel
- [881c0d7](https://github.com/punkpeye/awesome-mcp-servers/commit/881c0d75d9b74494182d962acb5c84b56f354703) Merge pull request #3766 from jarvisassistantux/add-loopsense - Frank Fiegel
- [3fc0ecb](https://github.com/punkpeye/awesome-mcp-servers/commit/3fc0ecb3dbc6606d60f478ed9d80514dd11e142a) Merge pull request #3544 from abcxz/add-conviction-mcp-v2 - Frank Fiegel
- [0cddd58](https://github.com/punkpeye/awesome-mcp-servers/commit/0cddd581e63d24cfd53a8230c274f37b5df637ec) Merge pull request #3767 from qq418716640/add-botbell - Frank Fiegel
- [fb02ca6](https://github.com/punkpeye/awesome-mcp-servers/commit/fb02ca6b3dec9f7daafd2a1c7c4ea23aade57e38) Merge pull request #3760 from aorumbayev/add-kagan - Frank Fiegel
- [ab8320a](https://github.com/punkpeye/awesome-mcp-servers/commit/ab8320a8bbe8f3731e4db43eb68da8e829cd7197) Fix entry formatting - Frank Fiegel
- [92c9bc7](https://github.com/punkpeye/awesome-mcp-servers/commit/92c9bc76941c98cce1699ebb4dd2060e82c22b46) Merge pull request #3009 from newageflyfish-max/main - Frank Fiegel
- [e381e65](https://github.com/punkpeye/awesome-mcp-servers/commit/e381e65a8e10305d0ce3befed3422bb00ffd669a) Merge pull request #3762 from lodordev/add-mcp-teslamate-fleet - Frank Fiegel
- [6d0a288](https://github.com/punkpeye/awesome-mcp-servers/commit/6d0a288dfc858d86c204ea8275042f2f4f61a26a) Merge pull request #3566 from scraperapi/add-scraperapi-mcp-server - Frank Fiegel
- [712f02c](https://github.com/punkpeye/awesome-mcp-servers/commit/712f02c633d65545838c85291b022e3932cf206e) Fix entry formatting - Frank Fiegel


##### File Content Changes

**README.md** (Modified, +10 -2 lines):

```diff
- - [newageflyfish-max/volthq](https://github.com/newageflyfish-max/volthq) [glama](https://glama.ai/mcp/servers/newageflyfish-max/volthq) 📇 ☁️ 🏠 🍎 🪟 🐧 - Compute price oracle for AI agents. Compare inference pricing across 8 providers in real time with routing recommendations and spend tracking. One-command install: `npx volthq-mcp-server --setup`.
- - [alex-gon/thegamecrafter-mcp-server](https://github.com/alex-gon/thegamecrafter-mcp-server) 📇 ☁️ - Design, manage, and price tabletop games on The Game Crafter. Browse catalogs, create projects, upload artwork, get pricing.
+ - [costajohnt/oss-autopilot](https://github.com/costajohnt/oss-autopilot) [![costajohnt/oss-autopilot MCP server](https://glama.ai/mcp/servers/costajohnt/oss-autopilot/badges/score.svg)](https://glama.ai/mcp/servers/costajohnt/oss-autopilot) 📇 ☁️ 🏠 🍎 🪟 🐧 - Open source contribution manager with PR tracking across repos, issue discovery, CI failure diagnosis, and maintainer response drafting. Available as CLI, MCP server, and Claude Code plugin.
+ - [jarvisassistantux/loopsense](https://github.com/jarvisassistantux/loopsense) [![jarvisassistantux/loopsense MCP server](https://glama.ai/mcp/servers/jarvisassistantux/loopsense/badges/score.svg)](https://glama.ai/mcp/servers/jarvisassistantux/loopsense) 📇 🏠 - MCP server that closes the feedback loop for AI coding agents — CI monitoring, process watching, file changes, HTTP polling.
+ - [conviction-fm/conviction-mcp](https://github.com/abcxz/conviction-fm) [![abcxz/conviction-fm MCP server](https://glama.ai/mcp/servers/abcxz/conviction-fm/badges/score.svg)](https://glama.ai/mcp/servers/abcxz/conviction-fm) 📇 ☁️ - The arena where AI agents compete for real returns. Prompt a strategy in plain English, get a funded agent that runs autonomously. Agents enter daily parimutuel pools and the conviction multiplier rewards being early and right over being late with size.
+ - [qq418716640/botbell-mcp](https://github.com/qq418716640/botbell-mcp) [![qq418716640/botbell-mcp MCP server](https://glama.ai/mcp/servers/qq418716640/botbell-mcp/badges/score.svg)](https://glama.ai/mcp/servers/qq418716640/botbell-mcp) 📇 ☁️ - Send push notifications to iPhone, iPad, and Mac from AI assistants. Two-way messaging — users reply in the BotBell app, AI reads and continues. Supports action buttons, Markdown, and multi-bot management via PAT.
+ - [kagan-sh/kagan](https://github.com/kagan-sh/kagan) [![kagan-sh/kagan MCP server](https://glama.ai/mcp/servers/kagan-sh/kagan/badges/score.svg)](https://glama.ai/mcp/servers/kagan-sh/kagan) 🐍 🏠 🍎 🪟 🐧 - AI-powered Kanban TUI and MCP server for autonomous development workflows. Orchestrates 14 coding agents across task tracking, isolated git worktrees, review, and merge.
+ - [newageflyfish-max/volthq](https://github.com/newageflyfish-max/volthq) [![newageflyfish-max/volthq MCP server](https://glama.ai/mcp/servers/newageflyfish-max/volthq/badges/score.svg)](https://glama.ai/mcp/servers/newageflyfish-max/volthq) 📇 ☁️ 🏠 🍎 🪟 🐧 - Compute price oracle for AI agents. Compare inference pricing across 8 providers in real time with routing recommendations and spend tracking. One-command install: `npx volthq-mcp-server --setup`.
+ - [newageflyfish-max/volthq](https://github.com/newageflyfish-max/volthq) [glama](https://glama.ai/mcp/servers/newageflyfish-max/volthq) 📇 ☁️ 🏠 🍎 🪟 🐧 - Compute price oracle for AI agents. Compare inference pricing across 8 providers in real time with routing recommendations and spend tracking. One-command install: `npx volthq-mcp-server --setup`.
+ - [lodordev/mcp-teslamate-fleet](https://github.com/lodordev/mcp-teslamate-fleet) [![mcp-teslamate-fleet](https://glama.ai/mcp/servers/lodordev/mcp-teslamate-fleet/badges/score.svg)](https://glama.ai/mcp/servers/lodordev/mcp-teslamate-fleet) 🐍 🏠 - Combined TeslaMate analytics + Fleet API commands — 29 tools for vehicle telemetry, driving history, energy analytics, and remote control (climate, charging, locks, sentry).
+ - [scraperapi/scraperapi-mcp](https://github.com/scraperapi/scraperapi-mcp) [![scraperapi/scraperapi-mcp MCP server](https://glama.ai/mcp/servers/scraperapi/scraperapi-mcp/badges/score.svg)](https://glama.ai/mcp/servers/scraperapi/scraperapi-mcp) 🐍 ☁️ - MCP server for ScraperAPI web scraping with JavaScript rendering, geotargeting, premium proxies, and auto-parsing support.
+ - [alex-gon/thegamecrafter-mcp-server](https://github.com/alex-gon/thegamecrafter-mcp-server) [![alex-gon/thegamecrafter-mcp-server MCP server](https://glama.ai/mcp/servers/alex-gon/thegamecrafter-mcp-server/badges/score.svg)](https://glama.ai/mcp/servers/alex-gon/thegamecrafter-mcp-server) 📇 ☁️ - Design, manage, and price tabletop games on The Game Crafter. Browse catalogs, create projects, upload artwork, get pricing.
```



#### [Awesome-Dify-Workflow](https://github.com/svcvit/Awesome-Dify-Workflow)

##### Commit Changes

No file changes detected.

#### [system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools)

##### Commit Changes

No file changes detected.

