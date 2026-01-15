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

### 2026-01-15T01:41:47

#### [awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps)

##### Commit Changes

No file changes detected.

#### [awesome-gpt4o-images](https://github.com/jamez-bondos/awesome-gpt4o-images)

##### Commit Changes

No file changes detected.

#### [awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers)

##### Commit Changes

- [c177376](https://github.com/punkpeye/awesome-mcp-servers/commit/c1773762b1e83dcd39f1ce5a33af047f9c59b8ab) Update README.md - Frank Fiegel
- [3918107](https://github.com/punkpeye/awesome-mcp-servers/commit/3918107e6b7ca75af697f6a2f61da89cf286e57b) Add Lenny's Podcast Wisdom MCP server to Knowledge & Memory section - bluzername


##### File Content Changes

**README.md** (Modified, +5 -1 lines):

```diff
- > [Awesome MCP Servers](https://glama.ai/mcp/servers) web directory
+ > [Awesome MCP Servers](https://glama.ai/mcp/servers) web directory.
+ > [!IMPORTANT]
+ > Test servers using [MCP Inspector](https://glama.ai/mcp/inspector?servers=%5B%7B%22id%22%3A%22test%22%2C%22name%22%3A%22test%22%2C%22requestTimeout%22%3A10000%2C%22url%22%3A%22https%3A%2F%2Fmcp-test.glama.ai%2Fmcp%22%7D%5D).
+ - [bluzername/lennys-quotes](https://github.com/bluzername/lennys-quotes) 📇 🏠 - Query 269 episodes of Lenny's Podcast for product management wisdom. Search 51,000+ transcript segments with YouTube timestamps. Perfect for PRDs, strategy, and PM career advice.
```



#### [Awesome-Dify-Workflow](https://github.com/svcvit/Awesome-Dify-Workflow)

##### Commit Changes

No file changes detected.

#### [system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools)

##### Commit Changes

No file changes detected.

