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

### 2026-04-13T02:36:33

#### [awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps)

##### Commit Changes

No file changes detected.

#### [awesome-gpt4o-images](https://github.com/jamez-bondos/awesome-gpt4o-images)

##### Commit Changes

No file changes detected.

#### [awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers)

##### Commit Changes

- [18fba3b](https://github.com/punkpeye/awesome-mcp-servers/commit/18fba3ba5514399510158de7fa2bcb8c22dabda5) Fix entry formatting - Frank Fiegel
- [6d09b25](https://github.com/punkpeye/awesome-mcp-servers/commit/6d09b2537eb45564ebd4aa77351ca8e330833a69) Merge pull request #4470 from 3aKHP/main - Frank Fiegel
- [f2c7fa0](https://github.com/punkpeye/awesome-mcp-servers/commit/f2c7fa088377f45a484ba0b026bcd61fb412ffad) feat(gaming): add Glama badge to prts-mcp entry; sync with upstream main - 3aKHP
- [4e28758](https://github.com/punkpeye/awesome-mcp-servers/commit/4e287584fe30356b6378edd568db1d105f3ca067) Fix entry formatting - Frank Fiegel
- [1607dde](https://github.com/punkpeye/awesome-mcp-servers/commit/1607dde31a3c7987602ed3f20a421e7dd820a496) Merge pull request #4351 from sunsiyuan/add-humansurvey-mcp - Frank Fiegel
- [aa29361](https://github.com/punkpeye/awesome-mcp-servers/commit/aa293610566b09574451baa5bee8de6fa7964f59) feat(gaming): add Glama badge to prts-mcp entry - 3aKHP
- [f3940e0](https://github.com/punkpeye/awesome-mcp-servers/commit/f3940e0f1f0b8b18ee72a9ad2f33b1e9d6520ab8) Fix entry formatting - Frank Fiegel
- [3941c03](https://github.com/punkpeye/awesome-mcp-servers/commit/3941c0314335fd1b8e6d0929280d972a6ba52929) Merge pull request #4490 from baphometnxg/add-aloha-fyi - Frank Fiegel
- [1beb21c](https://github.com/punkpeye/awesome-mcp-servers/commit/1beb21c949214c784e94e049a91ec8904f88b1cd) Merge pull request #4337 from persaples/add-fundzwatch-mcp-server-v2 - Frank Fiegel
- [d7e60a8](https://github.com/punkpeye/awesome-mcp-servers/commit/d7e60a817b035a58ec1f145fec24abd3478021a8) Merge pull request #4533 from ONE8943/add-ai-furniture-hub - Frank Fiegel


##### File Content Changes

**README.md** (Modified, +2316 -2287 lines):

```diff
- - [3aKHP/prts-mcp](https://github.com/3aKHP/prts-mcp) [![MCP Server](https://glama.ai/mcp/servers/3aKHP/prts-mcp/badge)](https://glama.ai/mcp/servers/3aKHP/prts-mcp) 🐍 📇 ☁️ 🏠 - MCP Server for [Arknights](https://www.arknights.global/), querying the [PRTS Wiki](https://prts.wiki) API and serving auto-synced operator archives and voice lines from game data. Designed for fan-creation (同人創作) AI agents. Python (stdio/Docker) and TypeScript (Streamable HTTP) implementations.
- placeholder
- - [sunsiyuan/human-survey](https://github.com/sunsiyuan/human-survey) 📇 ☁️ 🍎 🪟 🐧 - Feedback collection for AI agents. Create surveys from JSON schema, collect structured responses from groups of people, and retrieve aggregated results. 4 MCP tools for long-horizon agent workflows: post-event feedback, product launches, team health checks.
- [Resource from github at repo://punkpeye/awesome-mcp-servers/sha/9735596a41dd921a321314d6b66e68b2cb89488b/contents/README.md] [![ไทย](https://img.shields.io/badge/Thai-Click-blue)](README-th.md)
- [![English](https://img.shields.io/badge/English-Click-yellow)](README.md)
- [![繁體中文](https://img.shields.io/badge/繁體中文-點擊查看-orange)](README-zh_TW.md)
- [![简体中文](https://img.shields.io/badge/简体中文-点击查看-orange)](README-zh.md)
- [![日本語](https://img.shields.io/badge/日本語-クリック-青)](README-ja.md)
- [![한국어](https://img.shields.io/badge/한국어-클릭-yellow)](README-ko.md)
- [![Português Brasileiro](https://img.shields.io/badge/Português_Brasileiro-Clique-green)](README-pt_BR.md)
- [![Discord](https://img.shields.io/discord/1312302100125843476?logo=discord&label=discord)](https://glama.ai/mcp/discord)
- [![Subreddit subscribers](https://img.shields.io/reddit/subreddit-subscribers/mcp?style=flat&logo=reddit&label=subreddit)](https://www.reddit.com/r/mcp/)
- > [!IMPORTANT]
- > Read [The State of MCP in 2025](https://glama.ai/blog/2025-12-07-the-state-of-mcp-in-2025) report.
- > [Awesome MCP Servers](https://glama.ai/mcp/servers) web directory.
- A curated list of awesome Model Context Protocol (MCP) servers.
- * [What is MCP?](#what-is-mcp)
- * [Clients](#clients)
- * [Tutorials](#tutorials)
- * [Community](#community)
- * [Legend](#legend)
- * [Server Implementations](#server-implementations)
- * [Frameworks](#frameworks)
- * [Tips & Tricks](#tips-and-tricks)
- ## What is MCP?
- [MCP](https://modelcontextprotocol.io/) is an open protocol that enables AI models to securely interact with local and remote resources through standardized server implementations. This list focuses on production-ready and experimental MCP servers that extend AI capabilities through file access, database connections, API integrations, and other contextual services.
- ## Clients
- Checkout [awesome-mcp-clients](https://github.com/punkpeye/awesome-mcp-clients/) and [glama.ai/mcp/clients](https://glama.ai/mcp/clients).
- > [!TIP]
- > [Glama Chat](https://glama.ai/chat) is a multi-modal AI client with MCP support & [AI gateway](https://glama.ai/gateway).
- ## Tutorials
- * [Model Context Protocol (MCP) Quickstart](https://glama.ai/blog/2024-11-25-model-context-protocol-quickstart)
- * [Setup Claude Desktop App to Use a SQLite Database](https://youtu.be/wxCCzo9dGj0)
- ## Community
- * [r/mcp Reddit](https://www.reddit.com/r/mcp)
- * [Discord Server](https://glama.ai/mcp/discord)
- ## Legend
- * 🎖️ – official implementation
- * programming language
- * 🐍 – Python codebase
- * 📇 – TypeScript (or JavaScript) codebase
- * 🏎️ – Go codebase
- * 🦀 – Rust codebase
- * #️⃣ - C# Codebase
- * ☕ - Java codebase
- * 🌊 – C/C++ codebase
- * 💎 - Ruby codebase
- * scope
- * ☁️ - Cloud Service
- * 🏠 - Local Service
- ... (2070 more deletions)
+ - [3aKHP/prts-mcp](https://github.com/3aKHP/prts-mcp) [![3aKHP/prts-mcp MCP server](https://glama.ai/mcp/servers/3aKHP/prts-mcp/badges/score.svg)](https://glama.ai/mcp/servers/3aKHP/prts-mcp) 🐍 📇 ☁️ 🏠 - MCP Server for [Arknights](https://www.arknights.global/), querying the [PRTS Wiki](https://prts.wiki) API and serving auto-synced operator archives and voice lines from game data. Designed for fan-creation (同人創作) AI agents. Python (stdio/Docker) and TypeScript (Streamable HTTP) implementations.
+ - [3aKHP/prts-mcp](https://github.com/3aKHP/prts-mcp) [![MCP Server](https://glama.ai/mcp/servers/3aKHP/prts-mcp/badge)](https://glama.ai/mcp/servers/3aKHP/prts-mcp) 🐍 📇 ☁️ 🏠 - MCP Server for [Arknights](https://www.arknights.global/), querying the [PRTS Wiki](https://prts.wiki) API and serving auto-synced operator archives and voice lines from game data. Designed for fan-creation (同人創作) AI agents. Python (stdio/Docker) and TypeScript (Streamable HTTP) implementations.
+ [![ไทย](https://img.shields.io/badge/Thai-Click-blue)](README-th.md)
+ [![English](https://img.shields.io/badge/English-Click-yellow)](README.md)
+ [![繁體中文](https://img.shields.io/badge/繁體中文-點擊查看-orange)](README-zh_TW.md)
+ [![简体中文](https://img.shields.io/badge/简体中文-点击查看-orange)](README-zh.md)
+ [![日本語](https://img.shields.io/badge/日本語-クリック-青)](README-ja.md)
+ [![한국어](https://img.shields.io/badge/한국어-클릭-yellow)](README-ko.md)
+ [![Português Brasileiro](https://img.shields.io/badge/Português_Brasileiro-Clique-green)](README-pt_BR.md)
+ [![Discord](https://img.shields.io/discord/1312302100125843476?logo=discord&label=discord)](https://glama.ai/mcp/discord)
+ [![Subreddit subscribers](https://img.shields.io/reddit/subreddit-subscribers/mcp?style=flat&logo=reddit&label=subreddit)](https://www.reddit.com/r/mcp/)
+ > [!IMPORTANT]
+ > Read [The State of MCP in 2025](https://glama.ai/blog/2025-12-07-the-state-of-mcp-in-2025) report.
+ > [Awesome MCP Servers](https://glama.ai/mcp/servers) web directory.
+ A curated list of awesome Model Context Protocol (MCP) servers.
+ * [What is MCP?](#what-is-mcp)
+ * [Clients](#clients)
+ * [Tutorials](#tutorials)
+ * [Community](#community)
+ * [Legend](#legend)
+ * [Server Implementations](#server-implementations)
+ * [Frameworks](#frameworks)
+ * [Tips & Tricks](#tips-and-tricks)
+ ## What is MCP?
+ [MCP](https://modelcontextprotocol.io/) is an open protocol that enables AI models to securely interact with local and remote resources through standardized server implementations. This list focuses on production-ready and experimental MCP servers that extend AI capabilities through file access, database connections, API integrations, and other contextual services.
+ ## Clients
+ Checkout [awesome-mcp-clients](https://github.com/punkpeye/awesome-mcp-clients/) and [glama.ai/mcp/clients](https://glama.ai/mcp/clients).
+ > [!TIP]
+ > [Glama Chat](https://glama.ai/chat) is a multi-modal AI client with MCP support & [AI gateway](https://glama.ai/gateway).
+ ## Tutorials
+ * [Model Context Protocol (MCP) Quickstart](https://glama.ai/blog/2024-11-25-model-context-protocol-quickstart)
+ * [Setup Claude Desktop App to Use a SQLite Database](https://youtu.be/wxCCzo9dGj0)
+ ## Community
+ * [r/mcp Reddit](https://www.reddit.com/r/mcp)
+ * [Discord Server](https://glama.ai/mcp/discord)
+ ## Legend
+ * 🎖️ – official implementation
+ * programming language
+ * 🐍 – Python codebase
+ * 📇 – TypeScript (or JavaScript) codebase
+ * 🏎️ – Go codebase
+ * 🦀 – Rust codebase
+ * #️⃣ - C# Codebase
+ * ☕ - Java codebase
+ * 🌊 – C/C++ codebase
+ * 💎 - Ruby codebase
+ * scope
+ * ☁️ - Cloud Service
+ * 🏠 - Local Service
+ * 📟 - Embedded Systems
+ ... (2095 more additions)
```



#### [Awesome-Dify-Workflow](https://github.com/svcvit/Awesome-Dify-Workflow)

##### Commit Changes

No file changes detected.

#### [system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools)

##### Commit Changes

No file changes detected.

