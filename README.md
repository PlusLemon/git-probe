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

### 2025-09-26T01:19:22

#### [awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps)

##### Commit Changes

No file changes detected.

#### [awesome-gpt4o-images](https://github.com/jamez-bondos/awesome-gpt4o-images)

##### Commit Changes

No file changes detected.

#### [awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers)

##### Commit Changes

- [f84eb8d](https://github.com/punkpeye/awesome-mcp-servers/commit/f84eb8d9ec5a1b9efe2572fd4757c1f0acdb6554) Update README.md - Frank Fiegel


##### File Content Changes

**README.md** (Modified, +1 -1 lines):

```diff
- - [box/mcp-server-box-remote](https://github.com/box/mcp-server-box-remote/) 🎖️ ☁️ - The Box MCP server allows third party AI agents to securely and seamlessly access Box content and use tools such as search, asking questions from files and folders, and data extraction. This hosted server complements the [local MCP server](https://github.com/box-community/mcp-server-box) which enables connections to desktop applications and systems running in your local environment.
+ - [box/mcp-server-box-remote](https://github.com/box/mcp-server-box-remote/) 🎖️ ☁️ - The Box MCP server allows third party AI agents to securely and seamlessly access Box content and use tools such as search, asking questions from files and folders, and data extraction.
```



#### [Awesome-Dify-Workflow](https://github.com/svcvit/Awesome-Dify-Workflow)

##### Commit Changes

No file changes detected.

#### [system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools)

##### Commit Changes

- [8c0ce72](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools/commit/8c0ce729861bb1f196adfbaeaee5b7e8f4c5b553) Update README.md - Lucas Valbuena


##### File Content Changes

**README.md** (Modified, +2 -1 lines):

```diff
- > **Latest Update:** 16/09/2025
+ - [**Comet Assistant**](./Comet%20Assistant/)
+ > **Latest Update:** 25/09/2025
```



