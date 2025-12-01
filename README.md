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

### 2025-12-01T01:50:55

#### [awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps)

##### Commit Changes

No file changes detected.

#### [awesome-gpt4o-images](https://github.com/jamez-bondos/awesome-gpt4o-images)

##### Commit Changes

No file changes detected.

#### [awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers)

##### Commit Changes

- [712e182](https://github.com/punkpeye/awesome-mcp-servers/commit/712e1829c82c48bad1094f1d9169cc0eb4d093bb) Add kiarash-portfolio-mcp link to README - Kiarash Adl


##### File Content Changes

**README.md** (Modified, +1 -0 lines):

```diff
+ - [kiarash-portfolio-mcp](https://kiarash-adl.pages.dev/.well-known/mcp.llmfeed.json) – WebMCP-enabled portfolio with Ed25519 signed discovery. AI agents can query projects, skills, and execute terminal commands. Built on Cloudflare Pages Functions.
```



#### [Awesome-Dify-Workflow](https://github.com/svcvit/Awesome-Dify-Workflow)

##### Commit Changes

No file changes detected.

#### [system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools)

##### Commit Changes

- [18cc134](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools/commit/18cc134e9125d3de1fb82ed6602978912aec1869) Fix typo in contact section of README - Lucas Valbuena
- [1e62b95](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools/commit/1e62b959818065a7ef1b6af44d69ccd5010f9a09) Add email contact to README - Lucas Valbuena


##### File Content Changes

**README.md** (Modified, +2 -1 lines):

```diff
- - **Mail**: `lucknitelol@pm.me`
+ - **Email**: `lucknitelol@pm.me`
+ - **Mail**: `lucknitelol@pm.me`
```



