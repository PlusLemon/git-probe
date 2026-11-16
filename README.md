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

### 2026-11-16T04:52:15

#### [awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps)

##### Commit Changes

- [c115355](https://github.com/Shubhamsaboo/awesome-llm-apps/commit/c11535552cfdcd8d3528577d7d5b9a9f27cd10fe) docs(take-back-your-tv): shorten the index entry and the README - Shubham Saboo
- [3d2821c](https://github.com/Shubhamsaboo/awesome-llm-apps/commit/3d2821c4159a5755b82200523233c923c6fb270b) feat(take-back-your-tv): add an agent playbook for cleaning up a smart TV - Shubham Saboo


##### File Content Changes

**README.md** (Modified, +3 -2 lines):

```diff
- *   [📺 Take Back Your TV - Your Photos Instead of Ads](advanced_llm_apps/take-back-your-tv/) - Hand one file to a coding agent and it turns off the junk on an Android TV or Google TV, then replaces the ad-filled home screen with your own photos, a small clock, and your four apps
- *Standalone web apps, creative tools, and browser extensions for everyday workflows.*
+ *   [📺 Take Back Your TV](advanced_llm_apps/take-back-your-tv/) - Give a coding agent one file and it swaps your smart TV's ad-filled home screen for your own photos
+ *Standalone web apps, creative tools, browser extensions, and agent playbooks for everyday workflows.*
+ *   [📺 Take Back Your TV - Your Photos Instead of Ads](advanced_llm_apps/take-back-your-tv/) - Hand one file to a coding agent and it turns off the junk on an Android TV or Google TV, then replaces the ad-filled home screen with your own photos, a small clock, and your four apps
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

