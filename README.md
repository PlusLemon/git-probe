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

### 2025-05-15T01:22:35

#### [awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps)

##### Commit Changes

- [7ae4d30](https://github.com/Shubhamsaboo/awesome-llm-apps/commit/7ae4d3018eece5bff0f0821149be8058404cff5b) Updated README - ShubhamSaboo


##### File Content Changes

**README.md** (Modified, +0 -1 lines):

```diff
- *   [🏠 AI Real Estate Agent](advanced_ai_agents/single_agent_apps/ai_real_estate_agent/)
```



#### [awesome-gpt4o-images](https://github.com/jamez-bondos/awesome-gpt4o-images)

##### Commit Changes

No file changes detected.

#### [awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers)

##### Commit Changes

- [a864cf8](https://github.com/punkpeye/awesome-mcp-servers/commit/a864cf896dce7372e0f37221fa037d5ca0025b22) Update README.md - Frank Fiegel
- [504f79c](https://github.com/punkpeye/awesome-mcp-servers/commit/504f79c23be49db176f0332a5744de564084fab1) Update README.md - Hagai Hen


##### File Content Changes

**README.md** (Modified, +3 -1 lines):

```diff
- - [HagaiHen/facebook-mcp-server](https://github.com/HagaiHen/facebook-mcp-server) 🐍 🏠 - Integrates with Facebook Pages to enable direct management of posts, comments, and engagement metrics through the Graph API for streamlined social media management.
+ - [HagaiHen/facebook-mcp-server](https://github.com/HagaiHen/facebook-mcp-server) 🐍 ☁️ - Integrates with Facebook Pages to enable direct management of posts, comments, and engagement metrics through the Graph API for streamlined social media management.
+ - [HagaiHen/facebook-mcp-server](https://github.com/HagaiHen/facebook-mcp-server) 🐍 🏠 - Integrates with Facebook Pages to enable direct management of posts, comments, and engagement metrics through the Graph API for streamlined social media management.
```



#### [Awesome-Dify-Workflow](https://github.com/svcvit/Awesome-Dify-Workflow)

##### Commit Changes

No file changes detected.

#### [system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools)

##### Commit Changes

No file changes detected.

