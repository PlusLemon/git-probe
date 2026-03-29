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

### 2026-03-29T02:24:49

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

- [db9f7d8](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools/commit/db9f7d8b9f36ea384bcaad298e231cdbc688dd8d) Update contact email in README - Lucas Valbuena
- [5bc553f](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools/commit/5bc553f065fd82d86c053e8b07e3cd0b61a58808) Update README.md - Lucas Valbuena


##### File Content Changes

**README.md** (Modified, +1 -29 lines):

```diff
- [Get Started](mailto:lucknitelol@proton.me)
- <p align="center">
- <sub>Special thanks to</sub>
- </p>
- <table width="100%">
- <tr>
- <td align="center" valign="top">
- <a href="https://latitude.so/developers?utm_source=github&utm_medium=readme&utm_campaign=prompt_repo_sponsorship" target="_blank">
- <img src="assets/Latitude_logo.png" alt="Latitude Logo" width="750" height="210"/>
- </a>
- <br><br>
- <strong>
- Make your LLM predictable in production
- </strong>
- <br>
- Open Source AI Engineering Platform
- &nbsp;
- </td>
- </tr>
- </table>
+ [Get Started](mailto:lucknitelol@pm.me)
```



