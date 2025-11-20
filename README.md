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

### 2025-11-20T01:23:52

#### [awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps)

##### Commit Changes

- [a5d9589](https://github.com/Shubhamsaboo/awesome-llm-apps/commit/a5d9589258831f8b97ccdb1c4ac7cb24d38860cd) fix: update sponsor name - Shubhamsaboo
- [23114ce](https://github.com/Shubhamsaboo/awesome-llm-apps/commit/23114ce01f3e00d4104e110328070791865fb5e2) feat: update sponsorship section in README - Shubhamsaboo


##### File Content Changes

**README.md** (Modified, +12 -7 lines):

```diff
- <a href="https://dimension.dev/" target="_blank" rel="noopener" title="Dimensions">
- <img src="docs/banner/sponsors/dimensions.png" alt="Dimensions" width="500">
- Dimensions
- <a href="https://sponsorunwindai.com/" target="_blank" rel="noopener" title="Become a Sponsor">
- <img src="docs/banner/sponsor_awesome_llm_apps.png" alt="Become a Sponsor" width="500">
- <a href="https://sponsorunwindai.com/" target="_blank" rel="noopener" style="text-decoration: none; color: #333; font-weight: bold; font-size: 18px;">
- Become a Sponsor
+ <a href="https://dimension.dev/" target="_blank" rel="noopener" title="Dimension AI">
+ <img src="docs/banner/sponsors/dimensions.png" alt="Dimension AI" width="500">
+ Dimension AI
+ <a href="https://dimension.dev/" target="_blank" rel="noopener" title="Dimensions">
+ <img src="docs/banner/sponsors/dimensions.png" alt="Dimensions" width="500">
+ <a href="https://dimension.dev/" target="_blank" rel="noopener" style="text-decoration: none; color: #333; font-weight: bold; font-size: 18px;">
+ Dimensions
+ <p align="center">
+ <a href="https://sponsorunwindai.com" target="_blank" rel="noopener">
+ <img src="https://img.shields.io/badge/_Sponsor_Us-FF69B4?style=for-the-badge&logo=github-sponsors&logoColor=white" alt="Sponsor Us">
+ </a>
+ </p>
```



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

- [b77ac4d](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools/commit/b77ac4ddea857a76929aa5c948bf4a7b33305047) Update README.md - Lucas Valbuena


##### File Content Changes

**README.md** (Modified, +1 -1 lines):

```diff
- > **Latest Update:** 18/11/2025
+ > **Latest Update:** 19/11/2025
```



