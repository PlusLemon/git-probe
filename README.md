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

### 2025-10-12T01:23:08

#### [awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps)

##### Commit Changes

- [ec0990b](https://github.com/Shubhamsaboo/awesome-llm-apps/commit/ec0990b29c57973688cc550255c8ab9ac1ecce62) feat: Add Multimodal UI/UX Feedback Agent Team - Shubhamsaboo


##### File Content Changes

**README.md** (Modified, +1 -0 lines):

```diff
+ *   [🎨 🍌 Multimodal UI/UX Feedback Agent Team with Nano Banana](advanced_ai_agents/multi_agent_apps/agent_teams/multimodal_uiux_feedback_agent_team/)
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

- [e215c61](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools/commit/e215c619a1adbcc0e6dfa935e006593d5558aaa3) Update README.md - Lucas Valbuena
- [7bcefc2](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools/commit/7bcefc20dc6615d1f972d6251e321b5fbfb49ee2) Update README.md - Lucas Valbuena


##### File Content Changes

**README.md** (Modified, +13 -3 lines):

```diff
- ## Sponsors
- # Support the Future of AI Development
- > **Latest Update:** 02/10/2025
+ # Sponsors
+ ## Support the Future of AI Development
+ ## Sponsors
+ # Support the Future of AI Development
+ Sponsor the most comprehensive collection of AI system prompts and reach thousands of developers building the next generation of AI applications.
+ [Get Started](https://www.promptleaks.dev/sponsor)
+ ---
+ > **Latest Update:** 12/10/2025
```



