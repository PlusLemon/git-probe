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

### 2025-09-18T01:17:59

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

- [037c0dc](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools/commit/037c0dc161e81c8318f65f7c876f10e55e771edb) Update README.md - Lucas Valbuena
- [0928cfd](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools/commit/0928cfd1fe40b7667239a51844adf1d9d1896806) Update README.md - Paula Cavero
- [f658499](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools/commit/f658499524e06bd935dc77cd20de83c52efc32dc) Update README.md - Paula Cavero


##### File Content Changes

**README.md** (Modified, +21 -2 lines):

```diff
- <sub>Sponsored by</sub>
- ### [The tools you need for reliable Agents and Prompts](https://latitude.so/developers?utm_source=github&utm_medium=readme&utm_campaign=prompt_repo_sponsorship)
+ <sub>Special thanks to</sub>
+ ### [The tools you need for building reliable Agents and Prompts](https://latitude.so/developers?utm_source=github&utm_medium=readme&utm_campaign=prompt_repo_sponsorship)
+ ---
+ <p align="center">
+ <sub>Sponsored by</sub>
+ </p>
+ <a href="https://latitude.so/developers?utm_source=github&utm_medium=readme&utm_campaign=prompt_repo_sponsorship">
+ <img src="assets/Latitude_logo.png" alt="Latitude Logo" width="700"/>
+ </a>
+ <div align="center" markdown="1">
+ ### [The tools you need for reliable Agents and Prompts](https://latitude.so/developers?utm_source=github&utm_medium=readme&utm_campaign=prompt_repo_sponsorship)
+ [Open Source AI Engineering Platform](https://latitude.so/developers?utm_source=github&utm_medium=readme&utm_campaign=prompt_repo_sponsorship)<br>
+ </div>
```



