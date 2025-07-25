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

### 2025-07-26T01:39:47

#### [awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps)

##### Commit Changes

No file changes detected.

#### [awesome-gpt4o-images](https://github.com/jamez-bondos/awesome-gpt4o-images)

##### Commit Changes

No file changes detected.

#### [awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers)

##### Commit Changes

- [3d664c3](https://github.com/punkpeye/awesome-mcp-servers/commit/3d664c33a8e3a7d5c6aa7fa19df31ee9205df0a5) Merge pull request #1153 from Yutarop/add-ros2-mcp - Frank Fiegel
- [ba935d3](https://github.com/punkpeye/awesome-mcp-servers/commit/ba935d376e54fec2fcfa6581264562247beac985) Update README.md - Frank Fiegel
- [fa64572](https://github.com/punkpeye/awesome-mcp-servers/commit/fa645724acfb305a8197eb4adb8eafa3fa08acc6) Merge pull request #1152 from brightlikethelight/add-networkx-mcp-server - Frank Fiegel
- [1becd35](https://github.com/punkpeye/awesome-mcp-servers/commit/1becd35087413f2b11224932bdd27a3bb9f8193e) Merge pull request #1151 from MWGMorningwood/patch-1 - Frank Fiegel
- [3e12eb8](https://github.com/punkpeye/awesome-mcp-servers/commit/3e12eb88e81e9b221510c2f7adedd51e409c3ba3) Merge pull request #1150 from lseelenbinder/patch-1 - Frank Fiegel
- [d5ed65f](https://github.com/punkpeye/awesome-mcp-servers/commit/d5ed65f61ca530f1a310c6a5a52c52a5a9e3cec3) Merge pull request #1149 from elasticdotventures/add-rust-cratedoc - Frank Fiegel
- [8215982](https://github.com/punkpeye/awesome-mcp-servers/commit/82159828155510ac6cc3b03b744f4e236581cdfc) Update README.md - Frank Fiegel
- [5e65094](https://github.com/punkpeye/awesome-mcp-servers/commit/5e6509472596ffb02a5bafe9842b35b696766bf3) Merge pull request #1146 from amineelkouhen/add-new-server - Frank Fiegel
- [fcc7855](https://github.com/punkpeye/awesome-mcp-servers/commit/fcc7855561fb6f55275e691bfadc35a097efab77) Merge pull request #1145 from sinanefeozler/add-new-server - Frank Fiegel
- [97d11a4](https://github.com/punkpeye/awesome-mcp-servers/commit/97d11a48bdc01f098f51fde7f8759d7f3608b70d) Update README.md - Frank Fiegel


##### File Content Changes

**README.md** (Modified, +10 -4 lines):

```diff
- - [Yutarop/ros-mcp](https://github.com/Yutarop/ros-mcp) 🐍🏠🐧 - MCP server that supports ROS2 topics, services, and actions communication, and controls robots using natural language.
- - [PromptExecution/cratedocs-mcp](https://github.com/promptexecution/cratedocs-mcp) 🦀 🏠 - Outputs short-form Rust crate derived traits,interfaces, etc. from AST (uses same api as rust-analyzer), output limits (token estimation) &amp; crate docs w/regex stripping.
- - [sinanefeozler/reddit-summarizer-mcp](https://github.com/sinanefeozler/reddit-summarizer-mcp)  🐍 🏠 ☁️ - MCP server for summarizing users's reddit homepage or any subreddit based on posts and comments.
+ - [Yutarop/ros-mcp](https://github.com/Yutarop/ros-mcp) 🐍 🏠 🐧 - MCP server that supports ROS2 topics, services, and actions communication, and controls robots using natural language.
+ - [Bright-L01/networkx-mcp-server](https://github.com/Bright-L01/networkx-mcp-server) 🐍 🏠 - The first NetworkX integration for Model Context Protocol, enabling graph analysis and visualization directly in AI conversations. Supports 13 operations including centrality algorithms, community detection, PageRank, and graph visualization.
+ - [MWGMorningwood/Central-Memory-MCP](https://github.com/MWGMorningwood/Central-Memory-MCP) 📇 ☁️ - An Azure PaaS-hostable MCP server that provides a workspace-grounded knowledge graph for multiple developers using Azure Functions MCP triggers and Table storage.
+ - [stadiamaps/stadiamaps-mcp-server-ts](https://github.com/stadiamaps/stadiamaps-mcp-server-ts) 📇 ☁️ - A MCP server for Stadia Maps' Location APIs - Lookup addresses, places with geocoding, find time zones, create routes and static maps
+ - [PromptExecution/cratedocs-mcp](https://github.com/promptexecution/cratedocs-mcp) 🦀 🏠 - Outputs short-form Rust crate derived traits,interfaces, etc. from AST (uses same api as rust-analyzer), output limits (token estimation) & crate docs w/regex stripping.
+ - [amineelkouhen/mcp-cockroachdb](https://github.com/amineelkouhen/mcp-cockroachdb) 🐍 ☁️ - A Model Context Protocol server for managing, monitoring, and querying data in [CockroachDB](https://cockroachlabs.com).
+ - [sinanefeozler/reddit-summarizer-mcp](https://github.com/sinanefeozler/reddit-summarizer-mcp) 🐍 🏠 ☁️ - MCP server for summarizing users's Reddit homepage or any subreddit based on posts and comments.
```



#### [Awesome-Dify-Workflow](https://github.com/svcvit/Awesome-Dify-Workflow)

##### Commit Changes

No file changes detected.

#### [system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools)

##### Commit Changes

No file changes detected.

