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

### 2026-05-26T03:28:20

#### [awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps)

##### Commit Changes

No file changes detected.

#### [awesome-gpt4o-images](https://github.com/jamez-bondos/awesome-gpt4o-images)

##### Commit Changes

No file changes detected.

#### [awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers)

##### Commit Changes

- [0be8257](https://github.com/punkpeye/awesome-mcp-servers/commit/0be8257c3992868a08b1b55f0c0bec30f2d708a1) docs: add Glama score badge for pg-mnemosyne-mcp - JanadaSroor
- [e07fea1](https://github.com/punkpeye/awesome-mcp-servers/commit/e07fea1da585467317f5a784be2f7a665e05c83e) add Janadasroor/pg-mnemosyne-mcp to Databases - JanadaSroor


##### File Content Changes

**README.md** (Modified, +2 -1 lines):

```diff
- - [Janadasroor/pg-mnemosyne-mcp](https://github.com/Janadasroor/pg-mnemosyne-mcp) 🐍 🏠 - A PostgreSQL Model Context Protocol (MCP) server acting as a robust persistent super memory, task tracker, and multi-agent coordination hub for AI assistants.
+ - [Janadasroor/pg-mnemosyne-mcp](https://github.com/Janadasroor/pg-mnemosyne-mcp) [![Janadasroor/pg-mnemosyne-mcp MCP server](https://glama.ai/mcp/servers/Janadasroor/pg-mnemosyne-mcp/badges/score.svg)](https://glama.ai/mcp/servers/Janadasroor/pg-mnemosyne-mcp) 🐍 🏠 - A PostgreSQL Model Context Protocol (MCP) server acting as a robust persistent super memory, task tracker, and multi-agent coordination hub for AI assistants.
+ - [Janadasroor/pg-mnemosyne-mcp](https://github.com/Janadasroor/pg-mnemosyne-mcp) 🐍 🏠 - A PostgreSQL Model Context Protocol (MCP) server acting as a robust persistent super memory, task tracker, and multi-agent coordination hub for AI assistants.
```



#### [Awesome-Dify-Workflow](https://github.com/svcvit/Awesome-Dify-Workflow)

##### Commit Changes

No file changes detected.

#### [system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools)

##### Commit Changes

No file changes detected.

