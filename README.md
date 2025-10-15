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

### 2025-10-15T01:21:35

#### [awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps)

##### Commit Changes

- [de6f0f3](https://github.com/Shubhamsaboo/awesome-llm-apps/commit/de6f0f385b9f3d880d3d298fd8747d424ae24cfd) fix: Update sponsor section in README - Shubhamsaboo


##### File Content Changes

**README.md** (Modified, +4 -10 lines):

```diff
- <a href="https://github.com/emcie-co/parlant" title="Parlant">
- <img src="docs/banner/sponsors/parlant.png" alt="Parlant" width="500">
- <a href="https://github.com/emcie-co/parlant" style="text-decoration: none; color: #333; font-weight: bold; font-size: 18px;">
- Parlant
- <p align="center">
- <a href="https://sponsorunwindai.com" target="_blank" rel="noopener">
- <img src="https://img.shields.io/badge/_Sponsor_Us-FF69B4?style=for-the-badge&logo=github-sponsors&logoColor=white" alt="Sponsor Us">
- </a>
- </p>
+ <a href="https://sponsorunwindai.com/" title="Parlant">
+ <img src="docs/banner/sponsor_awesome_llm_apps.png" alt="Parlant" width="500">
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

