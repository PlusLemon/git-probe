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

### 2025-05-18T01:38:32

#### [awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps)

##### Commit Changes

No file changes detected.

#### [awesome-gpt4o-images](https://github.com/jamez-bondos/awesome-gpt4o-images)

##### Commit Changes

No file changes detected.

#### [awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers)

##### Commit Changes

- [06b9dcb](https://github.com/punkpeye/awesome-mcp-servers/commit/06b9dcbc2990f6ba50cceeb7a04b15a84a6cc320) Merge pull request #881 from kaiyuanxiaobing/add-new-server - TerminalMan


##### File Content Changes

**README.md** (Modified, +1 -0 lines):

```diff
+ - [kaiyuanxiaobing/atomgit-mcp-server](https://github.com/kaiyuanxiaobing/atomgit-mcp-server) 📇 ☁️ - Official AtomGit server for integration with repository management, PRs, issues, branches, labels, and more.
```



#### [Awesome-Dify-Workflow](https://github.com/svcvit/Awesome-Dify-Workflow)

##### Commit Changes

No file changes detected.

#### [system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools)

##### Commit Changes

- [421b73c](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools/commit/421b73c2cc2170210f7a3acdf25d30ebeb39fec6) Update README.md - Lucas Valbuena


##### File Content Changes

**README.md** (Modified, +19 -18 lines):

```diff
- ## 📊 **Star History**
- <a href="https://www.star-history.com/#x1xhlol/system-prompts-and-models-of-ai-tools&Date">
- <picture>
- <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=x1xhlol/system-prompts-and-models-of-ai-tools&type=Date&theme=dark" />
- <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=x1xhlol/system-prompts-and-models-of-ai-tools&type=Date" />
- <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=x1xhlol/system-prompts-and-models-of-ai-tools&type=Date" />
- </picture>
- </a>
- ## 🗓️ **Zero Calendar**
- **An Open-Source AI-Powered Calendar for the Future of Scheduling**
- Zero Calendar is an open-source AI calendar solution that gives users the power to manage their schedule intelligently while integrating with external services like Google Calendar and other calendar providers. Our goal is to modernize and improve scheduling through AI agents to truly revolutionize how we manage our time.
- For more details, check out the [Zero Calendar repository](https://github.com/Zero-Calendar/zero-calendar).
+ ## 📊 **Star History**
+ <a href="https://www.star-history.com/#x1xhlol/system-prompts-and-models-of-ai-tools&Date">
+ <picture>
+ <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=x1xhlol/system-prompts-and-models-of-ai-tools&type=Date&theme=dark" />
+ <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=x1xhlol/system-prompts-and-models-of-ai-tools&type=Date" />
+ <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=x1xhlol/system-prompts-and-models-of-ai-tools&type=Date" />
+ </picture>
+ </a>
+ ## 🗓️ **Zero Calendar**
+ **An Open-Source AI-Powered Calendar for the Future of Scheduling**
+ Zero Calendar is an open-source AI calendar solution that gives users the power to manage their schedule intelligently while integrating with external services like Google Calendar and other calendar providers. Our goal is to modernize and improve scheduling through AI agents to truly revolutionize how we manage our time.
+ For more details, check out the [Zero Calendar repository](https://github.com/Zero-Calendar/zero-calendar).
```



