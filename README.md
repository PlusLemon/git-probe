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

### 2026-02-23T02:06:22

#### [awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps)

##### Commit Changes

No file changes detected.

#### [awesome-gpt4o-images](https://github.com/jamez-bondos/awesome-gpt4o-images)

##### Commit Changes

No file changes detected.

#### [awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers)

##### Commit Changes

- [8953e54](https://github.com/punkpeye/awesome-mcp-servers/commit/8953e5467bc18c27965e80aaa7c4d34a8a4b60ef) fix: correct several typos from 'MPC' to 'MCP' - Ename7
- [1b6465c](https://github.com/punkpeye/awesome-mcp-servers/commit/1b6465cddb64acfd2f0944d8b0e37c581293f78f) Add japan-corporate-mcp to Finance & Fintech - yamariki-hub


##### File Content Changes

**README.md** (Modified, +3 -2 lines):

```diff
- - [zhsama/duckduckgo-mcp-server](https://github.com/zhsama/duckduckgo-mpc-server/) 📇 🏠 ☁️ - This is a TypeScript-based MCP server that provides DuckDuckGo search functionality.
- - [rae-api-com/rae-mcp](https://github.com/rae-api-com/rae-mcp) - 🏎️ ☁️ 🍎 🪟 🐧 MPC Server to connect your preferred model with https://rae-api.com, Roya Academy of Spanish Dictionary
+ - [zhsama/duckduckgo-mcp-server](https://github.com/zhsama/duckduckgo-mcp-server/) 📇 🏠 ☁️ - This is a TypeScript-based MCP server that provides DuckDuckGo search functionality.
+ - [rae-api-com/rae-mcp](https://github.com/rae-api-com/rae-mcp) - 🏎️ ☁️ 🍎 🪟 🐧 MCP Server to connect your preferred model with https://rae-api.com, Roya Academy of Spanish Dictionary
+ - [yamariki-hub/japan-corporate-mcp](https://github.com/yamariki-hub/japan-corporate-mcp) 🐍 ☁️ - Japanese corporate data via government APIs (gBizINFO, EDINET, e-Stat). Search companies, financials, patents, subsidies, procurement, and government statistics.
```



#### [Awesome-Dify-Workflow](https://github.com/svcvit/Awesome-Dify-Workflow)

##### Commit Changes

No file changes detected.

#### [system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools)

##### Commit Changes

No file changes detected.

