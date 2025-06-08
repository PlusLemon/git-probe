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

### 2025-06-08T01:42:36

#### [awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps)

##### Commit Changes

No file changes detected.

#### [awesome-gpt4o-images](https://github.com/jamez-bondos/awesome-gpt4o-images)

##### Commit Changes

No file changes detected.

#### [awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers)

##### Commit Changes

- [0f2eb4c](https://github.com/punkpeye/awesome-mcp-servers/commit/0f2eb4c764a8403d6379bff61b319102adfa360a) Update README.md - Frank Fiegel
- [8447467](https://github.com/punkpeye/awesome-mcp-servers/commit/84474675c8764036fc9f28e53992479583a02582) MacroCosmos Social Media MCP - arrmlet
- [0e3eac7](https://github.com/punkpeye/awesome-mcp-servers/commit/0e3eac7deb30c2b5e978b0034b64c4aed5a941e2) Update README.md - Frank Fiegel


##### File Content Changes

**README.md** (Modified, +4 -3 lines):

```diff
- - [macrocosm-os/macrocosmos-mcp](https://github.com/macrocosm-os/macrocosmos-mcp) - 🐍 ☁️ Access real-time X/Reddit/YouTube data directly in your LLM applications  with search phrases, users, and date filtering.
- - [Netdata](https://github.com/netdata/netdata/blob/master/src/web/mcp/README.md) 🎖️ 🏠 ☁️ 📟 🍎 🪟 🐧 - Discovery, exploration, reporting and root cause analysis using all observability data, including metrics, logs, systems, containers, processes, and network connections
+ - [macrocosm-os/macrocosmos-mcp](https://github.com/macrocosm-os/macrocosmos-mcp) - 🎖️ 🐍 ☁️ Access real-time X/Reddit/YouTube data directly in your LLM applications  with search phrases, users, and date filtering.
+ - [macrocosm-os/macrocosmos-mcp](https://github.com/macrocosm-os/macrocosmos-mcp) - 🐍 ☁️ Access real-time X/Reddit/YouTube data directly in your LLM applications  with search phrases, users, and date filtering.
+ - [netdata/netdata#Netdata](https://github.com/netdata/netdata/blob/master/src/web/mcp/README.md) 🎖️ 🏠 ☁️ 📟 🍎 🪟 🐧 - Discovery, exploration, reporting and root cause analysis using all observability data, including metrics, logs, systems, containers, processes, and network connections
```



#### [Awesome-Dify-Workflow](https://github.com/svcvit/Awesome-Dify-Workflow)

##### Commit Changes

No file changes detected.

#### [system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools)

##### Commit Changes

No file changes detected.

