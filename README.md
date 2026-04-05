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

### 2026-04-05T02:27:05

#### [awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps)

##### Commit Changes

No file changes detected.

#### [awesome-gpt4o-images](https://github.com/jamez-bondos/awesome-gpt4o-images)

##### Commit Changes

No file changes detected.

#### [awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers)

##### Commit Changes

- [475920c](https://github.com/punkpeye/awesome-mcp-servers/commit/475920ced8a08c15141701cb5f2d07e52c4a92c5) Fix entry formatting - Frank Fiegel
- [6332689](https://github.com/punkpeye/awesome-mcp-servers/commit/633268970c64bef07281627019c43fd4d2152d77) Merge pull request #4164 from ypollak2/add-llm-router - Frank Fiegel
- [947fa17](https://github.com/punkpeye/awesome-mcp-servers/commit/947fa179534b2c3af614c890f2526c81b95cde22) Add ThinkNEO Control Plane MCP server to Monitoring section - thinkneo-ai
- [7aad13f](https://github.com/punkpeye/awesome-mcp-servers/commit/7aad13f990cc5cdb5fec411e160d3a11a2bd200d) Merge pull request #4135 from AIMLPM/add-markcrawl - Frank Fiegel
- [92b5558](https://github.com/punkpeye/awesome-mcp-servers/commit/92b5558015a708dabe68c4faa0680282b05becca) feat: add Glama score badge to ypollak2/llm-router entry - ypollak2
- [e4413ba](https://github.com/punkpeye/awesome-mcp-servers/commit/e4413ba7fa881a44d1106300d06ed6ad06ce43a2) feat: add ypollak2/llm-router to Developer Tools - Yali Pollak
- [0b65b85](https://github.com/punkpeye/awesome-mcp-servers/commit/0b65b85c94483156e7956e31e0b6934db3e4a1a8) Merge pull request #4131 from goklab/add-guardvibe - Frank Fiegel
- [5b46576](https://github.com/punkpeye/awesome-mcp-servers/commit/5b46576ae5081cd324470860b993215939ca557c) Add Glama score badge for AIMLPM/markcrawl - AIMLPM
- [f2f3bd8](https://github.com/punkpeye/awesome-mcp-servers/commit/f2f3bd8ae992e60149867204aa23eea03fd783b4) Merge pull request #4156 from AliceLJY/add-recallnest-with-badge - Frank Fiegel
- [816bf0a](https://github.com/punkpeye/awesome-mcp-servers/commit/816bf0a4c4de59284e53e0faed18712145da86f7) add Glama badge, update to v2.7.4 (330 rules, 29 tools) - MediumEditor


##### File Content Changes

**README.md** (Modified, +10 -4 lines):

```diff
- - [ypollak2/llm-router](https://github.com/ypollak2/llm-router) 🐍 🏠 🍎 🪟 🐧 - Subscription-aware LLM router for Claude Code. Routes tasks to 20+ providers (OpenAI, Gemini, Groq, Ollama, Codex) based on complexity classification, Claude subscription pressure, and cost. Free tasks stay on Claude subscription; expensive tasks fall back to the cheapest capable model. Includes 30 MCP tools, 6 auto-routing hooks, semantic dedup cache, prompt caching, daily spend cap, and a live web dashboard. [![ypollak2/llm-router MCP server](https://glama.ai/mcp/servers/ypollak2/llm-router/badges/score.svg)](https://glama.ai/mcp/servers/ypollak2/llm-router)
- - [ypollak2/llm-router](https://github.com/ypollak2/llm-router) 🐍 🏠 🍎 🪟 🐧 - Subscription-aware LLM router for Claude Code. Routes tasks to 20+ providers (OpenAI, Gemini, Groq, Ollama, Codex) based on complexity classification, Claude subscription pressure, and cost. Free tasks stay on Claude subscription; expensive tasks fall back to the cheapest capable model. Includes 30 MCP tools, 6 auto-routing hooks, semantic dedup cache, prompt caching, daily spend cap, and a live web dashboard.
- - [AIMLPM/markcrawl](https://github.com/AIMLPM/markcrawl) 🐍 🏠 - Crawl websites into clean Markdown, search pages, and extract structured data with LLMs. Built-in MCP server for web research and RAG pipelines.
- - [goklab/guardvibe](https://github.com/goklab/guardvibe) 📇 🏠 🍎 🪟 🐧 - Security MCP for vibe coding with 313 rules and 25 tools. Purpose-built for AI-generated code — scans Next.js, Supabase, Clerk, Stripe, Prisma, Hono, GraphQL, and 23+ modules. Auto-fix, SARIF export, pre-commit hook, and CVE version detection. Zero config, runs locally.
+ - [ypollak2/llm-router](https://github.com/ypollak2/llm-router) [![ypollak2/llm-router MCP server](https://glama.ai/mcp/servers/ypollak2/llm-router/badges/score.svg)](https://glama.ai/mcp/servers/ypollak2/llm-router) 🐍 🏠 🍎 🪟 🐧 - Subscription-aware LLM router for Claude Code. Routes tasks to 20+ providers (OpenAI, Gemini, Groq, Ollama, Codex) based on complexity classification, Claude subscription pressure, and cost. Free tasks stay on Claude subscription; expensive tasks fall back to the cheapest capable model. Includes 30 MCP tools, 6 auto-routing hooks, semantic dedup cache, prompt caching, daily spend cap, and a live web dashboard.
+ - [ypollak2/llm-router](https://github.com/ypollak2/llm-router) 🐍 🏠 🍎 🪟 🐧 - Subscription-aware LLM router for Claude Code. Routes tasks to 20+ providers (OpenAI, Gemini, Groq, Ollama, Codex) based on complexity classification, Claude subscription pressure, and cost. Free tasks stay on Claude subscription; expensive tasks fall back to the cheapest capable model. Includes 30 MCP tools, 6 auto-routing hooks, semantic dedup cache, prompt caching, daily spend cap, and a live web dashboard. [![ypollak2/llm-router MCP server](https://glama.ai/mcp/servers/ypollak2/llm-router/badges/score.svg)](https://glama.ai/mcp/servers/ypollak2/llm-router)
+ - [ThinkneoAI/mcp-server](https://github.com/ThinkneoAI/mcp-server) [![ThinkneoAI/mcp-server MCP server](https://glama.ai/mcp/servers/ThinkneoAI/mcp-server/badges/score.svg)](https://glama.ai/mcp/servers/ThinkneoAI/mcp-server) 🐍 ☁️ - ThinkNEO Control Plane — Enterprise AI governance MCP server with runtime guardrails, observability, AI FinOps, and agent lifecycle control.
+ - [AIMLPM/markcrawl](https://github.com/AIMLPM/markcrawl) [![AIMLPM/markcrawl MCP server](https://glama.ai/mcp/servers/AIMLPM/markcrawl/badges/score.svg)](https://glama.ai/mcp/servers/AIMLPM/markcrawl) 🐍 🏠 - Crawl websites into clean Markdown, search pages, and extract structured data with LLMs. Built-in MCP server for web research and RAG pipelines.
+ - [ypollak2/llm-router](https://github.com/ypollak2/llm-router) 🐍 🏠 🍎 🪟 🐧 - Subscription-aware LLM router for Claude Code. Routes tasks to 20+ providers (OpenAI, Gemini, Groq, Ollama, Codex) based on complexity classification, Claude subscription pressure, and cost. Free tasks stay on Claude subscription; expensive tasks fall back to the cheapest capable model. Includes 30 MCP tools, 6 auto-routing hooks, semantic dedup cache, prompt caching, daily spend cap, and a live web dashboard.
+ - [goklab/guardvibe](https://github.com/goklab/guardvibe) [![MCP Server](https://glama.ai/mcp/servers/goklab/guardvibe/badge)](https://glama.ai/mcp/servers/goklab/guardvibe) 📇 🏠 🍎 🪟 🐧 - Security MCP for vibe coding with 330 rules and 29 tools. Purpose-built for AI-generated code — scans Next.js, Supabase, Clerk, Stripe, Prisma, Hono, GraphQL, and 25+ modules. Cross-file taint analysis, host security audit, auto-fix, SARIF export, pre-commit hook, and CVE version detection. Zero config, runs locally.
+ - [AliceLJY/recallnest](https://github.com/AliceLJY/recallnest) [![recallnest MCP server](https://glama.ai/mcp/servers/AliceLJY/recallnest/badges/score.svg)](https://glama.ai/mcp/servers/AliceLJY/recallnest) 📇 🏠 🍎 🪟 🐧 - Persistent memory MCP server for AI coding agents (Claude Code, Codex, Gemini CLI). Hybrid retrieval (vector + BM25), cross-encoder reranking, knowledge graph with PPR traversal, session checkpoint/resume, and multi-scope isolation. Local-first with LanceDB + SQLite, zero external dependencies.
```



#### [Awesome-Dify-Workflow](https://github.com/svcvit/Awesome-Dify-Workflow)

##### Commit Changes

No file changes detected.

#### [system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools)

##### Commit Changes

No file changes detected.

