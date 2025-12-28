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

### 2025-12-28T01:49:32

#### [awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps)

##### Commit Changes

No file changes detected.

#### [awesome-gpt4o-images](https://github.com/jamez-bondos/awesome-gpt4o-images)

##### Commit Changes

No file changes detected.

#### [awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers)

##### Commit Changes

- [a3e0336](https://github.com/punkpeye/awesome-mcp-servers/commit/a3e0336988e9ea7f97c9a26ebd20106768aeba0e) Adding Crawleo.dev Service - Crawleo
- [f2fac20](https://github.com/punkpeye/awesome-mcp-servers/commit/f2fac20fadbe4a03f3cf018895db4a7b9825537b) Update README.md - Crawleo


##### File Content Changes

**README.md** (Modified, +2 -0 lines):

```diff
+ - [Crawleo/Crawleo-MCP](https://github.com/Crawleo/Crawleo-MCP) ☁️ 🐍 – Crawleo Search & Crawl API
+ - [Crawleo/Crawleo-MCP](https://github.com/Crawleo/Crawleo-MCP) ☁️ 🐍 – Crawleo search & Crawling API
```



#### [Awesome-Dify-Workflow](https://github.com/svcvit/Awesome-Dify-Workflow)

##### Commit Changes

No file changes detected.

#### [system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools)

##### Commit Changes

No file changes detected.

