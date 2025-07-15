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

### 2025-07-15T01:44:57

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

- [7f10715](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools/commit/7f10715dc9ef830296ada1d2a39f7ac157094916) Update README.md - Lucas Valbuena


##### File Content Changes

**README.md** (Modified, +20 -20 lines):

```diff
- 3. [Support the Project](#%EF%B8%8F-support-the-project)
- 4. [Connect With Me](#-connect-with-me)
- 5. [Security Notice for AI Startups](#%EF%B8%8F-security-notice-for-ai-startups)
- 6. [Star History](#-star-history)
- ## ❤️ Support the Project
- If you find this collection valuable and appreciate the effort involved in obtaining and sharing these insights, please consider supporting the project. Your contribution helps keep this resource updated and allows for further exploration.
- You can show your support via:
- - **PayPal:** `lucknitelol@proton.me`
- - **Cryptocurrency:**
- - **BTC:** `bc1q7zldmzjwspnaa48udvelwe6k3fef7xrrhg5625`
- - **LTC:** `LRWgqwEYDwqau1WeiTs6Mjg85NJ7m3fsdQ`
- - **ETH:** `0x3f844B2cc3c4b7242964373fB0A41C4fdffB192A`
- 🙏 Thank you for your support!
+ ---
+ ## ❤️ Support the Project
+ If you find this collection valuable and appreciate the effort involved in obtaining and sharing these insights, please consider supporting the project. Your contribution helps keep this resource updated and allows for further exploration.
+ You can show your support via:
+ - **PayPal:** `lucknitelol@proton.me`
+ - **Cryptocurrency:**
+ - **BTC:** `bc1q7zldmzjwspnaa48udvelwe6k3fef7xrrhg5625`
+ - **LTC:** `LRWgqwEYDwqau1WeiTs6Mjg85NJ7m3fsdQ`
+ - **ETH:** `0x3f844B2cc3c4b7242964373fB0A41C4fdffB192A`
+ 🙏 Thank you for your support!
+ 3. [Connect With Me](#-connect-with-me)
+ 4. [Security Notice for AI Startups](#%EF%B8%8F-security-notice-for-ai-startups)
+ 5. [Star History](#-star-history)
```



