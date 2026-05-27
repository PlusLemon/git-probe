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

### 2026-05-27T03:41:59

#### [awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps)

##### Commit Changes

No file changes detected.

#### [awesome-gpt4o-images](https://github.com/jamez-bondos/awesome-gpt4o-images)

##### Commit Changes

No file changes detected.

#### [awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers)

##### Commit Changes

- [aa725fa](https://github.com/punkpeye/awesome-mcp-servers/commit/aa725facbf4027e814bf0bcb9b104cb166823071) Fix entry formatting - Frank Fiegel
- [d20347c](https://github.com/punkpeye/awesome-mcp-servers/commit/d20347cf805f1bdd34ed9b98fdb32cdcd3fef267) Merge pull request #5894 from MAG-Cie/add-microsoft-todo - Frank Fiegel
- [34c2406](https://github.com/punkpeye/awesome-mcp-servers/commit/34c240674a8191b20df8050dffcd719bd455e0d9) Merge pull request #6676 from ckakgun/add-heym-frameworks - Frank Fiegel
- [160deb1](https://github.com/punkpeye/awesome-mcp-servers/commit/160deb18ac57e6df1f68f73fa3a98684851b1932) Merge pull request #6021 from michaelrice/add-zendesk-mcp - Frank Fiegel
- [5075a2a](https://github.com/punkpeye/awesome-mcp-servers/commit/5075a2a70b178ac51abc890f65ee64c03c95dc70) Merge pull request #6462 from maxkuminov/add-obsidian-mcp - Frank Fiegel
- [cbfffbe](https://github.com/punkpeye/awesome-mcp-servers/commit/cbfffbe372f0c6f23fdd09b5f07a3b1eb6712ce2) Fix entry formatting - Frank Fiegel
- [b78ac6a](https://github.com/punkpeye/awesome-mcp-servers/commit/b78ac6ae121a7d05108d5b353e1680fb753fabc0) Merge pull request #5585 from ShinyDapps/add-l402-kit-finance - Frank Fiegel
- [7b67882](https://github.com/punkpeye/awesome-mcp-servers/commit/7b678821ddffc22bbc019e942a0e16207f383de2) Merge pull request #6277 from learningloons-hash/add-lithtrix-mcp - Frank Fiegel
- [2045404](https://github.com/punkpeye/awesome-mcp-servers/commit/20454048552b7c9e845f7d2b14decf9cc34577e9) Merge pull request #6172 from playidea-lab/add-pcq - Frank Fiegel
- [c440249](https://github.com/punkpeye/awesome-mcp-servers/commit/c440249274764d59eecc180f58d60f18455b3155) Fix entry formatting - Frank Fiegel


##### File Content Changes

**README.md** (Modified, +10 -3 lines):

```diff
- - [MAG-Cie/mcp-microsoft-todo](https://github.com/MAG-Cie/mcp-microsoft-todo) 📇 🏠 🍎 🪟 🐧 [![MAG-Cie/mcp-microsoft-todo MCP server](https://glama.ai/mcp/servers/MAG-Cie/mcp-microsoft-todo/badges/score.svg)](https://glama.ai/mcp/servers/MAG-Cie/mcp-microsoft-todo) - Microsoft To Do task management via Microsoft Graph API. MSAL device code flow (no client secret needed), persisted token cache, full MCP safety annotations.
- - [ShinyDapps/l402-kit](https://github.com/ShinyDapps/l402-kit) 📇 ☁️ 🍎 🪟 🐧 - Full-stack L402 SDK: server middleware (Express/FastAPI/axum/net/http) + agent client with auto-pay. 4 languages (TypeScript, Python, Go, Rust). MCP server, LangChain integration, budget control. `npx l402-kit-mcp` [![ShinyDapps/l402-kit MCP server](https://glama.ai/mcp/servers/ShinyDapps/l402-kit/badges/score.svg)](https://glama.ai/mcp/servers/ShinyDapps/l402-kit)
- - [CKBrennan/overtone-news-mcp](https://github.com/CKBrennan/overtone-news-mcp) 🐍 - Real-time news with tone analysis, brand safety, and narrative shift signals for AI agents. [![CKBrennan/overtone-news-mcp MCP server](https://glama.ai/mcp/servers/CKBrennan/overtone-news-mcp/badges/score.svg)](https://glama.ai/mcp/servers/CKBrennan/overtone-news-mcp)
+ - [MAG-Cie/mcp-microsoft-todo](https://github.com/MAG-Cie/mcp-microsoft-todo) [![MAG-Cie/mcp-microsoft-todo MCP server](https://glama.ai/mcp/servers/MAG-Cie/mcp-microsoft-todo/badges/score.svg)](https://glama.ai/mcp/servers/MAG-Cie/mcp-microsoft-todo) 📇 🏠 🍎 🪟 🐧 - Microsoft To Do task management via Microsoft Graph API. MSAL device code flow (no client secret needed), persisted token cache, full MCP safety annotations.
+ - [MAG-Cie/mcp-microsoft-todo](https://github.com/MAG-Cie/mcp-microsoft-todo) 📇 🏠 🍎 🪟 🐧 [![MAG-Cie/mcp-microsoft-todo MCP server](https://glama.ai/mcp/servers/MAG-Cie/mcp-microsoft-todo/badges/score.svg)](https://glama.ai/mcp/servers/MAG-Cie/mcp-microsoft-todo) - Microsoft To Do task management via Microsoft Graph API. MSAL device code flow (no client secret needed), persisted token cache, full MCP safety annotations.
+ - [heymrun/heym](https://github.com/heymrun/heym) [![heymrun/heym MCP server](https://glama.ai/mcp/servers/heymrun/heym/badges/score.svg)](https://glama.ai/mcp/servers/heymrun/heym) 🐍 📇 🏠 - Source-available, self-hosted AI workflow automation platform. Build multi-agent, RAG, and tool-using pipelines on a visual canvas, then expose any workflow as an MCP server (stdio/SSE/Streamable HTTP), or call external MCP servers from the agent node.
+ - [michaelrice/zendesk-mcp](https://github.com/michaelrice/zendesk-mcp) [![michaelrice/zendesk-mcp MCP server](https://glama.ai/mcp/servers/michaelrice/zendesk-mcp/badges/score.svg)](https://glama.ai/mcp/servers/michaelrice/zendesk-mcp) 🐍 ☁️ 🍎 🪟 🐧 - MCP server for Zendesk. Read/write tools for tickets, comments, views, macros, users, groups, organizations, and time tracking; optional Help Center knowledge base and Git-Zen GitLab integration.
+ - [maxkuminov/obsidian-mcp](https://github.com/maxkuminov/obsidian-mcp) [![obsidian-mcp MCP server](https://glama.ai/mcp/servers/maxkuminov/obsidian-mcp/badges/score.svg)](https://glama.ai/mcp/servers/maxkuminov/obsidian-mcp) 🐍 🏠 🍎 🪟 🐧 - Self-hosted MCP server for Obsidian with semantic + full-text search over PostgreSQL/pgvector, wikilink graph traversal, atomic note CRUD, OAuth 2.0, and a self-describing vault guide.
+ - [ShinyDapps/l402-kit](https://github.com/ShinyDapps/l402-kit) [![ShinyDapps/l402-kit MCP server](https://glama.ai/mcp/servers/ShinyDapps/l402-kit/badges/score.svg)](https://glama.ai/mcp/servers/ShinyDapps/l402-kit) 📇 ☁️ 🍎 🪟 🐧 - Full-stack L402 SDK: server middleware (Express/FastAPI/axum/net/http) + agent client with auto-pay. 4 languages (TypeScript, Python, Go, Rust). MCP server, LangChain integration, budget control. `npx l402-kit-mcp`
+ - [ShinyDapps/l402-kit](https://github.com/ShinyDapps/l402-kit) 📇 ☁️ 🍎 🪟 🐧 - Full-stack L402 SDK: server middleware (Express/FastAPI/axum/net/http) + agent client with auto-pay. 4 languages (TypeScript, Python, Go, Rust). MCP server, LangChain integration, budget control. `npx l402-kit-mcp` [![ShinyDapps/l402-kit MCP server](https://glama.ai/mcp/servers/ShinyDapps/l402-kit/badges/score.svg)](https://glama.ai/mcp/servers/ShinyDapps/l402-kit)
+ - [lithtrix/lithtrix-mcp](https://github.com/lithtrix/lithtrix-mcp) [![lithtrix/lithtrix-mcp MCP server](https://glama.ai/mcp/servers/lithtrix/lithtrix-mcp/badges/score.svg)](https://glama.ai/mcp/servers/lithtrix/lithtrix-mcp) 📇 ☁️ 🍎 🪟 🐧 - Memory Consolidation for AI agents across vendors, owners, and time. Persistent memory, credibility-scored web search, browser fetch, and shared Commons pool under a stable `ltx_` key. Self-registration in one API call, no dashboard required. `npx lithtrix-mcp`
+ - [playidea-lab/pcq](https://github.com/playidea-lab/pcq) [![playidea-lab/pcq MCP server](https://glama.ai/mcp/servers/playidea-lab/pcq/badges/score.svg)](https://glama.ai/mcp/servers/playidea-lab/pcq) 🐍 🏠 🍎 🪟 🐧 - Agent-operable ML experiment contract (cq.yaml + JSON contracts) with a built-in MCP server exposing 14 tools (resolve/inspect/run/validate/describe/compare/lineage) for running, validating, and tracing experiments across any framework (PyTorch / HF Trainer / Lightning / sklearn / XGBoost). Apache-2.0.
+ - [CKBrennan/overtone-news-mcp](https://github.com/CKBrennan/overtone-news-mcp) [![CKBrennan/overtone-news-mcp MCP server](https://glama.ai/mcp/servers/CKBrennan/overtone-news-mcp/badges/score.svg)](https://glama.ai/mcp/servers/CKBrennan/overtone-news-mcp) 🐍 - Real-time news with tone analysis, brand safety, and narrative shift signals for AI agents.
```



#### [Awesome-Dify-Workflow](https://github.com/svcvit/Awesome-Dify-Workflow)

##### Commit Changes

No file changes detected.

#### [system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools)

##### Commit Changes

No file changes detected.

