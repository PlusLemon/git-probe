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

### 2025-05-20T01:26:35

#### [awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps)

##### Commit Changes

No file changes detected.

#### [awesome-gpt4o-images](https://github.com/jamez-bondos/awesome-gpt4o-images)

##### Commit Changes

No file changes detected.

#### [awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers)

##### Commit Changes

- [b1b75f3](https://github.com/punkpeye/awesome-mcp-servers/commit/b1b75f33ee3b55ad763b8c00ae93841b97ec5a38) YouTube MCP Server - Emils
- [1ab4420](https://github.com/punkpeye/awesome-mcp-servers/commit/1ab442074c4e2f1ea4f02aacc5044e7db94c3700) Update README.md - Emils


##### File Content Changes

**README.md** (Modified, +2 -1 lines):

```diff
- - [Xyber-Labs/mcp-servers/tree/main/mcp-server-youtube](https://github.com/Xyber-Labs/mcp-servers/tree/main/mcp-server-youtube) 🐍 ☁️ - This repository implements an MCP (Model Context Protocol) server for YouTube search and transcript retrieval functionality. It allows language models or other agents to easily query YouTube content through a standardized protocol.
+ - [Xyber-Labs/mcp-server-youtube](https://github.com/Xyber-Labs/mcp-servers/tree/main/mcp-server-youtube) 🐍 ☁️ - This repository implements an MCP (Model Context Protocol) server for YouTube search and transcript retrieval functionality. It allows language models or other agents to easily query YouTube content through a standardized protocol.
+ - [Xyber-Labs/mcp-servers/tree/main/mcp-server-youtube](https://github.com/Xyber-Labs/mcp-servers/tree/main/mcp-server-youtube) 🐍 ☁️ - This repository implements an MCP (Model Context Protocol) server for YouTube search and transcript retrieval functionality. It allows language models or other agents to easily query YouTube content through a standardized protocol.
```



#### [Awesome-Dify-Workflow](https://github.com/svcvit/Awesome-Dify-Workflow)

##### Commit Changes

No file changes detected.

#### [system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools)

##### Commit Changes

No file changes detected.

