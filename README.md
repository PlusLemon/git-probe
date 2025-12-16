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

### 2025-12-16T01:40:01

#### [awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps)

##### Commit Changes

No file changes detected.

#### [awesome-gpt4o-images](https://github.com/jamez-bondos/awesome-gpt4o-images)

##### Commit Changes

No file changes detected.

#### [awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers)

##### Commit Changes

- [9a34351](https://github.com/punkpeye/awesome-mcp-servers/commit/9a34351428cc5c1940304345cbcbbaf5d2dcef21) Update README.md - Nicolò Boschi
- [8e97209](https://github.com/punkpeye/awesome-mcp-servers/commit/8e972090feb9b2fbd6a2694f3f217e8cae74c9fc) Update README.md - Nicolò Boschi
- [212090a](https://github.com/punkpeye/awesome-mcp-servers/commit/212090a873920343f566e8f81657950526863aa1) Add Hindsight MCP server to README - Nicolò Boschi


##### File Content Changes

**README.md** (Modified, +3 -2 lines):

```diff
- - [Hindsight](https://github.com/vectorize-io/hindsight) 🐍 ☁️ 🏠 - Hindsight: Agent Memory That Works Like Human Memory - Built for AI Agents to manage Long Term Memory
- - [Hindsight](https://github.com/vectorize-io/hindsight) - Hindsight: Agent Memory That Works Like Human Memory - Built for AI Agents to manage Long Term Memory
+ - [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) 🐍 ☁️ 🏠 - Hindsight: Agent Memory That Works Like Human Memory - Built for AI Agents to manage Long Term Memory
+ - [Hindsight](https://github.com/vectorize-io/hindsight) 🐍 ☁️ 🏠 - Hindsight: Agent Memory That Works Like Human Memory - Built for AI Agents to manage Long Term Memory
+ - [Hindsight](https://github.com/vectorize-io/hindsight) - Hindsight: Agent Memory That Works Like Human Memory - Built for AI Agents to manage Long Term Memory
```



#### [Awesome-Dify-Workflow](https://github.com/svcvit/Awesome-Dify-Workflow)

##### Commit Changes

No file changes detected.

#### [system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools)

##### Commit Changes

No file changes detected.

