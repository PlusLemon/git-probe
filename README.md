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

### 2025-10-01T01:27:57

#### [awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps)

##### Commit Changes

No file changes detected.

#### [awesome-gpt4o-images](https://github.com/jamez-bondos/awesome-gpt4o-images)

##### Commit Changes

No file changes detected.

#### [awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers)

##### Commit Changes

- [3784ff0](https://github.com/punkpeye/awesome-mcp-servers/commit/3784ff0a9d69890e6f0892fc13ff5cdd78f14c96) Add new tmdb server - Drakonkat
- [6971d57](https://github.com/punkpeye/awesome-mcp-servers/commit/6971d578735175dc0bfb67691da0576847a3e6aa) Add new tmdb server - Drakonkat
- [6fd8f95](https://github.com/punkpeye/awesome-mcp-servers/commit/6fd8f959a02d979092fde144aaca27d4719abea2) Add OneDev MCP server link to README - Robin Shen


##### File Content Changes

**README.md** (Modified, +3 -1 lines):

```diff
- - [drakonkat/wizzy-mcp-tmdb](https://github.com/drakonkat/wizzy-mcp-tmdb) 🎥 📺 - A MCP server for The Movie Database API that enables AI assistants to search and retrieve movie, TV show, and person information.
+ - [drakonkat/wizzy-mcp-tmdb](https://github.com/drakonkat/wizzy-mcp-tmdb) 📇 ☁️ - A MCP server for The Movie Database API that enables AI assistants to search and retrieve movie, TV show, and person information.
+ - [drakonkat/wizzy-mcp-tmdb](https://github.com/drakonkat/wizzy-mcp-tmdb) 🎥 📺 - A MCP server for The Movie Database API that enables AI assistants to search and retrieve movie, TV show, and person information.
+ - [theonedev/tod](https://github.com/theonedev/tod/blob/main/mcp.md) 🏎️ 🏠 - A MCP server for OneDev for CI/CD pipeline editing, issue workflow automation, and pull request review
```



#### [Awesome-Dify-Workflow](https://github.com/svcvit/Awesome-Dify-Workflow)

##### Commit Changes

No file changes detected.

#### [system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools)

##### Commit Changes

- [2166f9b](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools/commit/2166f9bc7beb330eb900e403ed2e60c5f4c48a02) Update README.md - Lucas Valbuena


##### File Content Changes

**README.md** (Modified, +1 -0 lines):

```diff
+ - [**Amp**](./AMp/)
```



