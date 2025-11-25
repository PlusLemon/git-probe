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

### 2025-11-25T01:25:38

#### [awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps)

##### Commit Changes

- [5e48f46](https://github.com/Shubhamsaboo/awesome-llm-apps/commit/5e48f461f1fcfa9d038d817395430c6eee821912) chore: update sponsorship section in README to reflect new sponsors and links - Shubhamsaboo


##### File Content Changes

**README.md** (Modified, +16 -21 lines):

```diff
- <a href="https://getunblocked.com/unblocked-mcp/?utm_source=oss&utm_medium=sponsorship&utm_campaign=awesome-llm-apps" target="_blank" rel="noopener" title="Unblocked">
- <img src="docs/banner/sponsors/unblocked.png" alt="Unblocked" width="500">
- <a href="https://getunblocked.com/unblocked-mcp/?utm_source=oss&utm_medium=sponsorship&utm_campaign=awesome-llm-apps" target="_blank" rel="noopener" style="text-decoration: none; color: #333; font-weight: bold; font-size: 18px;">
- Unblocked
- <a href="https://okara.ai/?utm_source=oss&utm_medium=sponsorship&utm_campaign=awesome-llm-apps" title="Okara">
- <img src="docs/banner/sponsors/okara.png" alt="Okara" width="500">
- <a href="https://okara.ai/?utm_source=oss&utm_medium=sponsorship&utm_campaign=awesome-llm-apps" style="text-decoration: none; color: #333; font-weight: bold; font-size: 18px;">
- Okara AI
- <a href="https://github.com/GibsonAI/Memori" target="_blank" rel="noopener" title="Memori">
- <img src="docs/banner/sponsors/memorilabs.png" alt="Memori" width="500">
- <a href="https://github.com/GibsonAI/Memori" target="_blank" rel="noopener" style="text-decoration: none; color: #333; font-weight: bold; font-size: 18px;">
- Memori
- <a href="https://dimension.dev/" target="_blank" rel="noopener" title="Dimension AI">
- <img src="docs/banner/sponsors/dimensions.png" alt="Dimension AI" width="500">
- <a href="https://dimension.dev/" target="_blank" rel="noopener" style="text-decoration: none; color: #333; font-weight: bold; font-size: 18px;">
- Dimension AI
- <p align="center">
- <a href="https://sponsorunwindai.com" target="_blank" rel="noopener">
- <img src="https://img.shields.io/badge/_Sponsor_Us-FF69B4?style=for-the-badge&logo=github-sponsors&logoColor=white" alt="Sponsor Us">
- </a>
- </p>
+ <a href="https://dimension.dev/" target="_blank" rel="noopener" title="Dimension AI">
+ <img src="docs/banner/sponsors/dimensions.png" alt="Dimension AI" width="500">
+ <a href="https://dimension.dev/" target="_blank" rel="noopener" style="text-decoration: none; color: #333; font-weight: bold; font-size: 18px;">
+ Dimension AI
+ <a href="https://github.com/GibsonAI/Memori" target="_blank" rel="noopener" title="Memori">
+ <img src="docs/banner/sponsors/memorilabs.png" alt="Memori" width="500">
+ <a href="https://github.com/GibsonAI/Memori" target="_blank" rel="noopener" style="text-decoration: none; color: #333; font-weight: bold; font-size: 18px;">
+ Memori
+ <a href="https://okara.ai/?utm_source=oss&utm_medium=sponsorship&utm_campaign=awesome-llm-apps" title="Okara">
+ <img src="docs/banner/sponsors/okara.png" alt="Okara" width="500">
+ <a href="https://okara.ai/?utm_source=oss&utm_medium=sponsorship&utm_campaign=awesome-llm-apps" style="text-decoration: none; color: #333; font-weight: bold; font-size: 18px;">
+ Okara AI
+ <a href="https://sponsorunwindai.com/" title="Become a Sponsor">
+ <img src="docs/banner/sponsor_awesome_llm_apps.png" alt="Become a Sponsor" width="500">
+ <a href="https://sponsorunwindai.com/" style="text-decoration: none; color: #333; font-weight: bold; font-size: 18px;">
+ Become a Sponsor
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

No file changes detected.

