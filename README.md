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

### 2026-01-11T01:50:43

#### [awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps)

##### Commit Changes

No file changes detected.

#### [awesome-gpt4o-images](https://github.com/jamez-bondos/awesome-gpt4o-images)

##### Commit Changes

No file changes detected.

#### [awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers)

##### Commit Changes

- [38669ca](https://github.com/punkpeye/awesome-mcp-servers/commit/38669ca79e83b34d06cc5af83871e4f859db0184) Add cevatkerim/unsplash-mcp server - Kerim Incedayi
- [ce6e275](https://github.com/punkpeye/awesome-mcp-servers/commit/ce6e2754be5d8a2c31f07761444e8b0940f0b356) Merge pull request #1654 from disco-trooper/add-apple-notes-mcp - Frank Fiegel
- [de18133](https://github.com/punkpeye/awesome-mcp-servers/commit/de181331536ae7bb00d1ab681ff880606d7dbdee) Merge pull request #1655 from optimaquantum/main - Frank Fiegel
- [125b148](https://github.com/punkpeye/awesome-mcp-servers/commit/125b1482fb435cc17a1c1995fa3b502f15be930c) Merge pull request #1656 from Milofax/add-xert-mcp - Frank Fiegel
- [2868fe8](https://github.com/punkpeye/awesome-mcp-servers/commit/2868fe8696c3e7f2d7d49b6dd827915ec6761b2d) Merge pull request #1657 from JamsusMaximus/add-trainingpeaks-mcp - Frank Fiegel
- [1ff2aea](https://github.com/punkpeye/awesome-mcp-servers/commit/1ff2aeafc8ba94d937394e99b322488fa495075a) Add deep-research-mcp server - Pasquale Minervini
- [5bc7efb](https://github.com/punkpeye/awesome-mcp-servers/commit/5bc7efb1b1445de8cf669ba201a87c6ed8aebd8a) Merge pull request #1659 from smith-and-web/add-obsidian-mcp-server - Frank Fiegel


##### File Content Changes

**README.md** (Modified, +9 -1 lines):

```diff
- - [thinkchainai/agentinterviews_mcp](https://github.com/thinkchainai/agentinterviews_mcp) - Conduct AI-powered qualitative research interviews and surveys at scale with [Agent Interviews](https://agentinterviews.com). Create interviewers, manage research projects, recruit participants, and analyze interview data through MCP.
+ - [cevatkerim/unsplash-mcp](https://github.com/cevatkerim/unsplash-mcp) 🐍 ☁️ - Unsplash photo search with proper attribution. Returns ready-to-use attribution text and HTML for each photo, making it easy for LLMs to build content pages with properly credited images. Includes search, random photos, and download tracking.
+ - [disco-trooper/apple-notes-mcp](https://github.com/disco-trooper/apple-notes-mcp) 📇 🏠 🍎 - Apple Notes MCP with semantic search, hybrid vector+keyword search, full CRUD operations, and incremental indexing. Uses JXA for native macOS integration.
+ - [optimaquantum/claude-critical-rules-mcp](https://github.com/optimaquantum/claude-critical-rules-mcp) 📇 ☁️ 🏠 🍎 🪟 🐧 - Automatic enforcement of critical rules for Claude AI preventing 96 documented failure patterns. Provides compliance verification checklist and rules summary via MCP tools.
+ - [Milofax/xert-mcp](https://github.com/Milofax/xert-mcp) 📇 ☁️ - MCP server for XERT cycling analytics — access fitness signature (FTP, HIE, PP), training status, workouts, activities with XSS metrics, and MPA analysis.
+ - [JamsusMaximus/trainingpeaks-mcp](https://github.com/JamsusMaximus/trainingpeaks-mcp) 🐍 🏠 - Query TrainingPeaks workouts, analyze CTL/ATL/TSB fitness metrics, and compare power/pace PRs through Claude Desktop.
+ - [pminervini/deep-research-mcp](https://github.com/pminervini/deep-research-mcp) 🐍 ☁️ 🏠 - Deep research MCP server for OpenAI Responses API or Open Deep Research (smolagents), with web search and code interpreter support.
+ - [thinkchainai/agentinterviews_mcp](https://github.com/thinkchainai/agentinterviews_mcp) - Conduct AI-powered qualitative research interviews and surveys at scale with [Agent Interviews](https://agentinterviews.com). Create interviewers, manage research projects, recruit participants, and analyze interview data through MCP.
+ - [smith-and-web/obsidian-mcp-server](https://github.com/smith-and-web/obsidian-mcp-server) 📇 🏠 🍎 🪟 🐧 - SSE-enabled MCP server for remote Obsidian vault management with 29 tools for notes, directories, frontmatter, tags, search, and link operations. Docker-ready with health monitoring.
```



#### [Awesome-Dify-Workflow](https://github.com/svcvit/Awesome-Dify-Workflow)

##### Commit Changes

No file changes detected.

#### [system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools)

##### Commit Changes

No file changes detected.

