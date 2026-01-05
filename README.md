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

### 2026-01-05T01:50:42

#### [awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps)

##### Commit Changes

- [6494e19](https://github.com/Shubhamsaboo/awesome-llm-apps/commit/6494e19060a5a30f2c15e839a2d60956fe2547c4) feat: Add AI Due Diligence Agent with multi-agent pipeline for startup investment analysis, including company research, market analysis, financial modeling, risk assessment, and report generation. - Shubhamsaboo
- [3dd5b60](https://github.com/Shubhamsaboo/awesome-llm-apps/commit/3dd5b600fc572e3c555530dbbdd0bef2fcec333a) fix: Update README to reflect the change from Gemini Interactions API to Google's Interactions API for the AI Research Planner & Executor Agent - Shubhamsaboo


##### File Content Changes

**README.md** (Modified, +3 -2 lines):

```diff
- *   [🏚️ 🍌 AI Home Renovation Agent with Nano Banana](advanced_ai_agents/multi_agent_apps/ai_home_renovation_agent)
- *   [🔬 AI Research Planner & Executor (Gemini Interactions API)](advanced_ai_agents/single_agent_apps/research_agent_gemini_interaction_api)
+ *   [🏚️ 🍌 AI Home Renovation Agent with Nano Banana Pro](advanced_ai_agents/multi_agent_apps/ai_home_renovation_agent)
+ *   [📊 AI Due Diligence Agent with Gemini 3 and Nano Banana Pro](advanced_ai_agents/multi_agent_apps/ai_due_diligence_agent)
+ *   [🔬 AI Research Planner & Executor (Google Interactions API)](advanced_ai_agents/single_agent_apps/research_agent_gemini_interaction_api)
```



#### [awesome-gpt4o-images](https://github.com/jamez-bondos/awesome-gpt4o-images)

##### Commit Changes

No file changes detected.

#### [awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers)

##### Commit Changes

- [001f594](https://github.com/punkpeye/awesome-mcp-servers/commit/001f5942d8a835e6f5841a2397c7356eb2cb69d5) Add rescuedogs-mcp-server - ssatama


##### File Content Changes

**README.md** (Modified, +3 -2 lines):

```diff
- - [molanojustin/smithsonian-mcp](https://github.com/molanojustin/smithsonian-mcp) 🐍 ☁️ - MCP server that provides AI assistants with access to the Smithsonian Institution's Open Access collections.
- - [trycourier/courier-mcp](https://github.com/trycourier/courier-mcp) 🎖️ 💬 ☁️ 🛠️ 📇 🤖 - Build multi-channel notifications into your product, send messages, update lists, invoke automations, all without leaving your AI coding space.
+ - [molanojustin/smithsonian-mcp](https://github.com/molanojustin/smithsonian-mcp) 🐍 ☁️ - MCP server that provides AI assistants with access to the Smithsonian Institution's Open Access collections.
+ - [trycourier/courier-mcp](https://github.com/trycourier/courier-mcp) 🎖️ 💬 ☁️ 🛠️ 📇 🤖 - Build multi-channel notifications into your product, send messages, update lists, invoke automations, all without leaving your AI coding space.
+ - [ssatama/rescuedogs-mcp-server](https://github.com/ssatama/rescuedogs-mcp-server) 📇 ☁️ - Search and discover rescue dogs from European and UK organizations with AI-powered personality matching and detailed profiles.
```



#### [Awesome-Dify-Workflow](https://github.com/svcvit/Awesome-Dify-Workflow)

##### Commit Changes

No file changes detected.

#### [system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools)

##### Commit Changes

- [f71da8d](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools/commit/f71da8d538b6c0396b688aff409e991821609dff) Update README.md - Lucas Valbuena


##### File Content Changes

**README.md** (Modified, +1 -1 lines):



