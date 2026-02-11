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

### 2026-02-11T02:21:02

#### [awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps)

##### Commit Changes

- [a346cc8](https://github.com/Shubhamsaboo/awesome-llm-apps/commit/a346cc8669a0350783e4c5070cd7a815976fd9b5) feat: add TinyFish banner and remove Okara AI - Shubhamsaboo


##### File Content Changes

**README.md** (Modified, +11 -11 lines):

```diff
- </tr>
- <tr>
- <td align="center">
- <a href="https://okara.ai/?utm_source=oss&utm_medium=sponsorship&utm_campaign=awesome-llm-apps" title="Okara">
- <img src="docs/banner/sponsors/okara.png" alt="Okara" width="500">
- </a>
- <br>
- <a href="https://okara.ai/?utm_source=oss&utm_medium=sponsorship&utm_campaign=awesome-llm-apps" style="text-decoration: none; color: #333; font-weight: bold; font-size: 18px;">
- Okara AI
- </td>
+ <td align="center">
+ <a href="https://bit.ly/4ci0r4v" target="_blank" rel="noopener" title="TinyFish">
+ <img src="docs/banner/sponsors/tinyfish.png" alt="TinyFish" width="500">
+ </a>
+ <br>
+ <a href="https://bit.ly/4ci0r4v" target="_blank" rel="noopener" style="text-decoration: none; color: #333; font-weight: bold; font-size: 18px;">
+ TinyFish
+ </td>
+ </tr>
+ <tr>
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

