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

### 2026-01-01T01:50:17

#### [awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps)

##### Commit Changes

- [40ff2e3](https://github.com/Shubhamsaboo/awesome-llm-apps/commit/40ff2e33583714d51978a37cce50df5ed514a962) Fix typo in OpenSource Voice Dictation link - Shubham Saboo
- [6192cea](https://github.com/Shubhamsaboo/awesome-llm-apps/commit/6192ceaf822ced424fc8c1d7ac386a8a3bdc7084) Revise Jarvis AI Assistant link description - Shubham Saboo


##### File Content Changes

**README.md** (Modified, +2 -3 lines):

```diff
- *   [🎙️ OpenSource Voice Dictation App (like Wispr Flow](https://github.com/akshayaggarwal99/jarvis-ai-assistant)
- *   [🎙️ Jarvis AI Assistant](https://github.com/akshayaggarwal99/jarvis-ai-assistant) - Free, open-source voice dictation app (local Whisper + Ollama, zero telemetry)
+ *   [🎙️ OpenSource Voice Dictation Agent (like Wispr Flow](https://github.com/akshayaggarwal99/jarvis-ai-assistant)
+ *   [🎙️ OpenSource Voice Dictation App (like Wispr Flow](https://github.com/akshayaggarwal99/jarvis-ai-assistant)
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

