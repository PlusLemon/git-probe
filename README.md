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

### 2025-06-22T01:43:51

#### [awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps)

##### Commit Changes

- [d8e5574](https://github.com/Shubhamsaboo/awesome-llm-apps/commit/d8e5574bb8242d2f21e5e2f56cd28724a05df9c9) Update README.md - Arun
- [eb3c89b](https://github.com/Shubhamsaboo/awesome-llm-apps/commit/eb3c89b084cbd42f3febd5c42f7be6e00af76185) adding beifongai project - carlfeynman
- [d986551](https://github.com/Shubhamsaboo/awesome-llm-apps/commit/d986551e050afe5ed4c622f136e7c76fb4805040) adding beifongai project - carlfeynman


##### File Content Changes

**README.md** (Modified, +4 -3 lines):

```diff
- advanced_ai_agents/multi_agent_apps
- *   [🎧 AI Social Media News and Podcast Agent](advanced_ai_agents/multi_agent_apps/ai_news_and_podcast_agent/)
+ *   [🎧 AI Social Media News and Podcast Agent](advanced_ai_agents/multi_agent_apps/ai_news_and_podcast_agents/)
+ advanced_ai_agents/multi_agent_apps
+ *   [🎧 AI Social Media News and Podcast Agent](advanced_ai_agents/multi_agent_apps/ai_news_and_podcast_agent/)
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

- [233cfd9](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools/commit/233cfd984700be6823ac61a3c88a2caacd3a959c) Update README.md - Lucas Valbuena


##### File Content Changes

**README.md** (Modified, +2 -0 lines):

```diff
+ [![Build Status](https://app.cloudback.it/badge/x1xhlol/system-prompts-and-models-of-ai-tools)](https://cloudback.it)
```



