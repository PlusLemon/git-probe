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

### 2025-08-19T01:25:19

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

- [e56c4bc](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools/commit/e56c4bcd5989956608edea636426d301ee4adc3c) Update README.md - Lucas Valbuena
- [1a982f6](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools/commit/1a982f6086de6e6faa6220c3623d8049f99edcbb) Update README.md - Lucas Valbuena
- [b6359f4](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools/commit/b6359f408ec85e0997bf1752a1840bf9f31c1bd9) Update README.md - Lucas Valbuena


##### File Content Changes

**README.md** (Modified, +4 -3 lines):

```diff
- # **FULL v0, Cursor, Manus, Same.dev, Lovable, Devin, Replit Agent, Windsurf Agent, VSCode Agent, Dia Browser, Trae AI, Cluely, Perplexity, Xcode, Augment Code, Spawn & Orchids.app (And other Open Sourced) System Prompts, Tools & AI Models**
- # **FULL v0, Cursor, Manus, Same.dev, Lovable, Devin, Replit Agent, Windsurf Agent, VSCode Agent, Dia Browser, Trae AI, Cluely, Perplexity, Xcode, Spawn & Orchids.app (And other Open Sourced) System Prompts, Tools & AI Models**
- > **Latest Update:** 17/08/2025
+ # **System Prompts and Models of AI Tools**
+ # **FULL v0, Cursor, Manus, Same.dev, Lovable, Devin, Replit Agent, Windsurf Agent, VSCode Agent, Dia Browser, Trae AI, Cluely, Perplexity, Xcode, Augment Code, Spawn & Orchids.app (And other Open Sourced) System Prompts, Tools & AI Models**
+ - [**Augment Code**](./Augment%20Code/)
+ > **Latest Update:** 18/08/2025
```



