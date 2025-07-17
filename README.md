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

### 2025-07-17T01:42:31

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

- [86943b1](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools/commit/86943b19f4e5f81bcabc5bba8a0f5fdbce7373b9) Update README.md - Lucas Valbuena
- [b012425](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools/commit/b012425c7d9612e2ff93be99dd1e857a86f9d71a) Update README.md - Lucas Valbuena
- [e0ce74b](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools/commit/e0ce74bead81fcab19c1a8350abddcf465073649) Update README.md - Lucas Valbuena
- [58de542](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools/commit/58de54233278a5dd5cb49550e02bcb531e647a22) Update README.md - Lucas Valbuena
- [297b7c7](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools/commit/297b7c74de5ca1d435f805c822da443fe9304558) Update README.md - Lucas Valbuena


##### File Content Changes

**README.md** (Modified, +8 -8 lines):

```diff
- - **Patreon:** `https://patreon.com/lucknite`
- - **PayPal:** `lucknitelol@proton.me`
- > **Note:** We no longer use GitHub issues for roadmap and feedback.
- > Please visit [System Prompts Roadmap & Feedback](https://systemprompts.featurebase.app/) to share your suggestions and track upcoming features.
- > **Latest Update:** 04/07/2025
- - **Discord:** `x1xh`
- - **Trae AI Folder**
- # **FULL v0, Cursor, Manus, Same.dev, Lovable, Devin, Replit Agent, Windsurf Agent, VSCode Agent, Dia Browser, Trae AI, Cluely, Xcode & Spawn (And other Open Sourced) System Prompts, Tools & AI Models**
+ - **Patreon:** https://patreon.com/lucknite
+ - **PayPal:** `lucknitelol@proton.me`
+ - **Patreon:** `https://patreon.com/lucknite`
+ > Open an issue.
+ > **Latest Update:** 16/07/2025
+ - **Trae AI Folder**
+ - **Perplexity Folder**
+ # **FULL v0, Cursor, Manus, Same.dev, Lovable, Devin, Replit Agent, Windsurf Agent, VSCode Agent, Dia Browser, Trae AI, Cluely, Perplexity, Xcode & Spawn (And other Open Sourced) System Prompts, Tools & AI Models**
```



