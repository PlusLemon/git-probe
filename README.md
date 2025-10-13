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

### 2025-10-13T01:24:47

#### [awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps)

##### Commit Changes

No file changes detected.

#### [awesome-gpt4o-images](https://github.com/jamez-bondos/awesome-gpt4o-images)

##### Commit Changes

No file changes detected.

#### [awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers)

##### Commit Changes

- [0f64297](https://github.com/punkpeye/awesome-mcp-servers/commit/0f64297bb004fe5f6369516f7f9ee655563b059e) Merge pull request #1411 from tonychang04/add-insforge-mcp-server - Frank Fiegel
- [2be8a1c](https://github.com/punkpeye/awesome-mcp-servers/commit/2be8a1ca847f7fa39b38366b15ab3638352f5cba) Add Insforge MCP server to Developer Tools - yaowenc2
- [6e61f18](https://github.com/punkpeye/awesome-mcp-servers/commit/6e61f184c23f77034a30d4d4b31d2034c91dabbe) Add Buildkite MCP server - Christian Nunciato


##### File Content Changes

**README.md** (Modified, +3 -0 lines):

```diff
+ - [InsForge/insforge-mcp](https://github.com/InsForge/insforge-mcp) 📇 ☁️ - AI-native backend-as-a-service platform enabling AI agents to build and manage full-stack applications. Provides Auth, Database (PostgreSQL), Storage, and Functions as production-grade infrastructure, reducing MVP development time from weeks to hours.
+ - [buildkite/buildkite-mcp-server](https://github.com/buildkite/buildkite-mcp-server) 🎖️ 🏎️ 🏠 ☁️ 🍎 🪟 🐧 - Official MCP server for Buildkite. Create new pipelines, diagnose and fix failures, trigger builds, monitor job queues, and more.
```



#### [Awesome-Dify-Workflow](https://github.com/svcvit/Awesome-Dify-Workflow)

##### Commit Changes

No file changes detected.

#### [system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools)

##### Commit Changes

No file changes detected.

