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

### 2026-06-03T04:00:50

#### [awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps)

##### Commit Changes

- [d4a40f3](https://github.com/Shubhamsaboo/awesome-llm-apps/commit/d4a40f3463971b4d94ad8c3eb9199950e348e87c) Update README with Generative UI and Game Agents sections - Shubham Saboo
- [46b09a7](https://github.com/Shubhamsaboo/awesome-llm-apps/commit/46b09a74dd064eb8894f3978307c30e102eb1eea) Merge pull request #753 from jerelvelarde/feat/generative-ui-section - Shubham Saboo


##### File Content Changes

**README.md** (Modified, +35 -23 lines):

```diff
- - [🖼️ Generative UI and Agentic Frontends](#️-generative-ui-and-agentic-frontends)
- - [🎮 Autonomous Game-Playing Agents](#-autonomous-game-playing-agents)
- ### 🖼️ Generative UI and Agentic Frontends
- *Agents that render interactive UI components — forms, cards, charts, editable plans — not just text. Built with [CopilotKit](https://github.com/CopilotKit/CopilotKit) and [AG-UI](https://github.com/ag-ui-protocol/ag-ui).*
- *   [🗂️ Generative UI Starter Project](generative_ui_agents/generative-ui-starter-project/)
- *   [🪙 AI Financial Coach Agent](generative_ui_agents/ai-financial-coach-agent/)
- *   [📊 AI Dashboard Canvas Agent](generative_ui_agents/ai-dashboard-canvas-agent/)
- *   [🛠️ AI MCP App Builder](generative_ui_agents/ai-mcp-app-builder/)
- *   [✈️ MCP Apps Generative UI Showcase](generative_ui_agents/mcp-apps-generative-ui-showcase/)
- *   [🎛️ AI Shadcn Component Generator](generative_ui_agents/ai-shadcn-component-generator/)
- *   [🔍 AI Deep Research Agent](generative_ui_agents/ai-deep-research-agent/)
- See [`generative_ui_agents/`](generative_ui_agents/) for the category overview, conventions, and how to contribute a template.
- ### 🎮 Autonomous Game-Playing Agents
- *Agents that play games end-to-end - reasoning, strategy, and action.*
- *   [🎮 AI 3D Pygame Agent](advanced_ai_agents/autonomous_game_playing_agent_apps/ai_3dpygame_r1/)
- *   [♜ AI Chess Agent](advanced_ai_agents/autonomous_game_playing_agent_apps/ai_chess_agent/)
- *   [🎲 AI Tic-Tac-Toe Agent](advanced_ai_agents/autonomous_game_playing_agent_apps/ai_tic_tac_toe_agent/)
- <summary><strong>13 categories · Click to expand</strong></summary>
+ - [🖼️ Generative UI and Agentic Frontends](#️-generative-ui-and-agentic-frontends)
+ - [🎮 Autonomous Game-Playing Agents](#-autonomous-game-playing-agents)
+ ### 🖼️ Generative UI and Agentic Frontends
+ *Agents that render interactive UI components — forms, cards, charts, editable plans — not just text.*
+ *   [🗂️ Generative UI Starter Project](generative_ui_agents/generative-ui-starter-project/)
+ *   [🪙 AI Financial Coach Agent](generative_ui_agents/ai-financial-coach-agent/)
+ *   [📊 AI Dashboard Canvas Agent](generative_ui_agents/ai-dashboard-canvas-agent/)
+ *   [🛠️ AI MCP App Builder](generative_ui_agents/ai-mcp-app-builder/)
+ *   [✈️ MCP Apps Generative UI Showcase](generative_ui_agents/mcp-apps-generative-ui-showcase/)
+ *   [🎛️ AI Shadcn Component Generator](generative_ui_agents/ai-shadcn-component-generator/)
+ *   [🔍 AI Deep Research Agent](generative_ui_agents/ai-deep-research-agent/)
+ ### 🎮 Autonomous Game-Playing Agents
+ *Agents that play games end-to-end - reasoning, strategy, and action.*
+ *   [🎮 AI 3D Pygame Agent](advanced_ai_agents/autonomous_game_playing_agent_apps/ai_3dpygame_r1/)
+ *   [♜ AI Chess Agent](advanced_ai_agents/autonomous_game_playing_agent_apps/ai_chess_agent/)
+ *   [🎲 AI Tic-Tac-Toe Agent](advanced_ai_agents/autonomous_game_playing_agent_apps/ai_tic_tac_toe_agent/)
+ <summary><strong>14 categories · Click to expand</strong></summary>
+ *Agents that render interactive UI components — forms, cards, charts, editable plans — not just text. Built with [CopilotKit](https://github.com/CopilotKit/CopilotKit) and [AG-UI](https://github.com/ag-ui-protocol/ag-ui).*
+ See [`generative_ui_agents/`](generative_ui_agents/) for the category overview, conventions, and how to contribute a template.
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

