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

### 2025-07-21T01:47:53

#### [awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps)

##### Commit Changes

No file changes detected.

#### [awesome-gpt4o-images](https://github.com/jamez-bondos/awesome-gpt4o-images)

##### Commit Changes

No file changes detected.

#### [awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers)

##### Commit Changes

No file changes detected.

#### [Awesome-Dify-Workflow](https://github.com/svcvit/Awesome-Dify-Workflow)

##### Commit Changes

No file changes detected.

#### [system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools)

##### Commit Changes

- [4274d6e](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools/commit/4274d6e3409d0ece2441c942e62bbf5fcd119a36) Update README.md - Lucas Valbuena
- [5ecc7a7](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools/commit/5ecc7a724093e8d887769211af18dd78eae61321) Update README.md - Lucas Valbuena


##### File Content Changes

**README.md** (Modified, +5 -4 lines):

```diff
- 📜 Over **7500+ lines** of insights into their structure and functionality.
- # **FULL v0, Cursor, Manus, Same.dev, Lovable, Devin, Replit Agent, Windsurf Agent, VSCode Agent, Dia Browser, Trae AI, Cluely, Perplexity, Xcode & Spawn (And other Open Sourced) System Prompts, Tools & AI Models**
- - **Xcode Folder**
- > **Latest Update:** 16/07/2025
+ 📜 Over **8000+ lines** of insights into their structure and functionality.
+ # **FULL v0, Cursor, Manus, Same.dev, Lovable, Devin, Replit Agent, Windsurf Agent, VSCode Agent, Dia Browser, Trae AI, Cluely, Perplexity, Xcode, Spawn & Orchids.app (And other Open Sourced) System Prompts, Tools & AI Models**
+ - **Xcode Folder**
+ - **Orchids.app Folder**
+ > **Latest Update:** 21/07/2025
```



