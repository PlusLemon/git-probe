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

### 2026-08-07T02:35:24

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

- [eb111b4](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools/commit/eb111b427c647d86abfa8e398d985a50496b3b55) Update README.md - Lucas Valbuena
- [628ce7c](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools/commit/628ce7cb73be6466c5551a0a2febcbcfe3d50cf2) Update README.md - Lucas Valbuena
- [363b08c](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools/commit/363b08cf556df20cc361d29de565c4b4dfe847a6) Update README.md - Lucas Valbuena
- [d148472](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools/commit/d148472a51bb2d1e59cae382cd5c8dee6b1bed5c) Update README.md - Lucas Valbuena


##### File Content Changes

**README.md** (Modified, +14 -2 lines):

```diff
- - **Email**: `lucasvalbuena@pm.me
- <b>Gauss</b> — GPU-native CI. Run GitHub Actions on A100s and H100s with a one-line change.
+ - **Email**: `lucasvalbuena@pm.me`
+ <b>Gauss</b> — GPU-native CI.
+ <p align="center">
+ <b>Gauss</b> — GPU-native CI. Run GitHub Actions on A100s and H100s with a one-line change.
+ <br />
+ <a href="https://gauss.sh"><b>Get early access →</b></a>
+ </p>
+ <a href="https://gauss.sh" target="_blank">
+ <img src="https://gauss.sh/banner" alt="Gauss — CI that runs on real GPUs" width="1200" />
+ </a>
+ ---
```



