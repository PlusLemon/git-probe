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

### 2026-06-13T03:37:57

#### [awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps)

##### Commit Changes

- [c2273ff](https://github.com/Shubhamsaboo/awesome-llm-apps/commit/c2273fff203136d0320fb37af0ebea7a8dc10a8e) docs: rewrite web_scraping_ai_agent README to match shipped code - Shubhamsaboo
- [bbc1040](https://github.com/Shubhamsaboo/awesome-llm-apps/commit/bbc10405e8ada64c7ce7b36d6c36eb65a0845f2f) fix: correct broken link to multimodal_ai_agent folder - Shubhamsaboo


##### File Content Changes

**README.md** (Modified, +2 -2 lines):

```diff
- *   [🕸️ Web Scraping AI Agent (Local & Cloud SDK)](starter_ai_agents/web_scraping_ai_agent/)
- *   [✨ Gemini Multimodal Agent](starter_ai_agents/gemini_multimodal_agent_demo/)
+ *   [🕸️ Web Scraping AI Agent](starter_ai_agents/web_scraping_ai_agent/)
+ *   [✨ Gemini Multimodal Agent](starter_ai_agents/multimodal_ai_agent/)
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

