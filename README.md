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

### 2025-09-23T01:18:43

#### [awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps)

##### Commit Changes

No file changes detected.

#### [awesome-gpt4o-images](https://github.com/jamez-bondos/awesome-gpt4o-images)

##### Commit Changes

No file changes detected.

#### [awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers)

##### Commit Changes

- [eca1e46](https://github.com/punkpeye/awesome-mcp-servers/commit/eca1e463857c6e58150bf8857eaaf220ccbc60bc) Merge pull request #1356 from alexwebvizio/add-webvizio-server - Frank Fiegel
- [4ca5c75](https://github.com/punkpeye/awesome-mcp-servers/commit/4ca5c758f6d97b2f22287c340686df0b77ae52f9) Fix emojis - Alex Malashkevych


##### File Content Changes

**README.md** (Modified, +2 -1 lines):

```diff
- - [Webvizio/mcp](https://github.com/Webvizio/mcp) 🗄📋🚀 - Automatically converts feedback and bug reports from websites and web apps into actionable, context-enriched developer tasks. Delivered straight to your AI coding tools, the Webvizio MCP Server ensures your AI agent has all the data it needs to solve tasks with speed and accuracy.
+ - [Webvizio/mcp](https://github.com/Webvizio/mcp) 🎖️ 📇 - Automatically converts feedback and bug reports from websites and web apps into actionable, context-enriched developer tasks. Delivered straight to your AI coding tools, the Webvizio MCP Server ensures your AI agent has all the data it needs to solve tasks with speed and accuracy.
```



#### [Awesome-Dify-Workflow](https://github.com/svcvit/Awesome-Dify-Workflow)

##### Commit Changes

No file changes detected.

#### [system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools)

##### Commit Changes

No file changes detected.

