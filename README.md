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

### 2025-07-10T01:39:04

#### [awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps)

##### Commit Changes

No file changes detected.

#### [awesome-gpt4o-images](https://github.com/jamez-bondos/awesome-gpt4o-images)

##### Commit Changes

No file changes detected.

#### [awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers)

##### Commit Changes

- [79fcf34](https://github.com/punkpeye/awesome-mcp-servers/commit/79fcf34930c34fede8afd0c2b105c18003c4fb49) Update README.md - Frank Fiegel
- [becc0c8](https://github.com/punkpeye/awesome-mcp-servers/commit/becc0c82b358d3516b60343f011be6f1a5951786) Add new Google Workspace MCP server - Giuseppe Coco


##### File Content Changes

**README.md** (Modified, +11 -10 lines):

```diff
- * 🏢 - [Workspace Management] (#workspace-management)
- - [MarkusPfundstein/mcp-gsuite](https://github.com/MarkusPfundstein/mcp-gsuite) 🐍 ☁️ - Integration with gmail and Google Calendar.
- - [takumi0706/google-calendar-mcp](https://github.com/takumi0706/google-calendar-mcp) 📇 ☁️ - An MCP server to interface with the Google Calendar API. Based on TypeScript.
- - [taylorwilsdon/google_workspace_mcp](https://github.com/taylorwilsdon/google_workspace_mcp) 🐍 ☁️ 🍎 🪟 🐧 - Comprehensive Google Workspace MCP server with full support for Google Calendar, Drive, Gmail, and Docs, Forms, Chats, Slides and Sheets over stdio, Streamable HTTP and SSE transports.
- ### 🏢 <a name="workspace-management"></a>Workspace Management
+ * 🏢 - [Workplace & Productivity](#workplace-and-productivity)
+ ### 🏢 <a name="workplace-and-productivity"></a>Workplace & Productivity
+ - [MarkusPfundstein/mcp-gsuite](https://github.com/MarkusPfundstein/mcp-gsuite) 🐍 ☁️ - Integration with gmail and Google Calendar.
+ - [takumi0706/google-calendar-mcp](https://github.com/takumi0706/google-calendar-mcp) 📇 ☁️ - An MCP server to interface with the Google Calendar API. Based on TypeScript.
+ - [taylorwilsdon/google_workspace_mcp](https://github.com/taylorwilsdon/google_workspace_mcp) 🐍 ☁️ 🍎 🪟 🐧 - Comprehensive Google Workspace MCP server with full support for Google Calendar, Drive, Gmail, and Docs, Forms, Chats, Slides and Sheets over stdio, Streamable HTTP and SSE transports.
+ * 🏢 - [Workspace Management] (#workspace-management)
+ ### 🏢 <a name="workspace-management"></a>Workspace Management
+ - [giuseppe-coco/Google-Workspace-MCP-Server](https://github.com/giuseppe-coco/Google-Workspace-MCP-Server) 🐍 ☁️ 🍎 🪟 🐧 - MCP server that seamlessly interacts with your Google Calendar, Gmail, Drive and so on.
```



#### [Awesome-Dify-Workflow](https://github.com/svcvit/Awesome-Dify-Workflow)

##### Commit Changes

No file changes detected.

#### [system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools)

##### Commit Changes

No file changes detected.

