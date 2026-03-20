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

### 2026-03-20T02:02:19

#### [awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps)

##### Commit Changes

No file changes detected.

#### [awesome-gpt4o-images](https://github.com/jamez-bondos/awesome-gpt4o-images)

##### Commit Changes

No file changes detected.

#### [awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers)

##### Commit Changes

- [b42f59a](https://github.com/punkpeye/awesome-mcp-servers/commit/b42f59a82a263e9dc1af6d66a0982334ba1c6371) Merge pull request #3515 from Winify/add-wdio-mcp-server - Frank Fiegel
- [bdbe056](https://github.com/punkpeye/awesome-mcp-servers/commit/bdbe0564c64dceecadc5565aab41dc812c5f6e00) Fix formatting and update webdriverio/mcp entry - Frank Fiegel
- [ed9e252](https://github.com/punkpeye/awesome-mcp-servers/commit/ed9e252a5a9b218c9981fd42c5ac94ae5ef98770) Update README.md - Frank Fiegel
- [013ac4c](https://github.com/punkpeye/awesome-mcp-servers/commit/013ac4c7b1058087b077cdb391b7301f0e7d3e31) Merge pull request #3504 from KryptosAI/add-mcp-observatory - Frank Fiegel
- [e11b419](https://github.com/punkpeye/awesome-mcp-servers/commit/e11b4192b6279a5ff4cf7bd11a52a17ed2a04875) Update README.md - Frank Fiegel
- [3697436](https://github.com/punkpeye/awesome-mcp-servers/commit/36974361fe22370742287ac6c8d2bd1a1665b06a) Update mcp-observatory description with latest features - William Weishuhn
- [5ea304e](https://github.com/punkpeye/awesome-mcp-servers/commit/5ea304e6e6b0274620882fd580fec23bb5c876a1) Add Glama score badge for knowledge-rag - Lyon.
- [97f0180](https://github.com/punkpeye/awesome-mcp-servers/commit/97f0180314a94bc2b06fe27ac833a27f04c07caa) Add knowledge-rag to Knowledge and Memory section - Lyon.
- [fda5380](https://github.com/punkpeye/awesome-mcp-servers/commit/fda53807b99ea00adb0a5454e806d98614046cf8) Merge pull request #1866 from shibley/add-apistatuscheck-mcp - Frank Fiegel
- [2b74f32](https://github.com/punkpeye/awesome-mcp-servers/commit/2b74f320c1420104b957cacac869447e479c70ae) Update README.md - Frank Fiegel


##### File Content Changes

**README.md** (Modified, +9 -6 lines):

```diff
- - [webdriverio/mcp](https://github.com/webdriverio/mcp) 📇 🏠 [![mcp MCP server](https://glama.ai/mcp/servers/webdriverio/mcp/badges/score.svg)](https://glama.ai/mcp/servers/webdriverio/mcp) - Browser and mobile app automation using WebdriverIO, enabling AI agents to control browsers, interact with web elements, and automate native Android and iOS apps via the WebDriver and Appium protocols.
- - [lyonzin/knowledge-rag](https://github.com/lyonzin/knowledge-rag) 🐍 🏠 🍎 🪟 🐧 - Local RAG system for Claude Code with hybrid search (BM25 + semantic), cross-encoder reranking, markdown-aware chunking, query expansion, and 12 MCP tools. Runs entirely offline with zero external servers. Available on [PyPI](https://pypi.org/project/knowledge-rag/). [![lyonzin/knowledge-rag MCP server](https://glama.ai/mcp/servers/lyonzin/knowledge-rag/badges/score.svg)](https://glama.ai/mcp/servers/lyonzin/knowledge-rag)
- - [KryptosAI/mcp-observatory](https://github.com/KryptosAI/mcp-observatory) [![mcp-observatory MCP server](https://glama.ai/mcp/servers/KryptosAI/mcp-observatory/badges/score.svg)](https://glama.ai/mcp/servers/KryptosAI/mcp-observatory) 📇 🏠 🍎 🪟 🐧 - Auto-discovers MCP servers from your Claude config and runs health checks against tools, prompts, and resources. Snapshot diffing catches capability regressions between runs. Includes watch mode for CI.
- - [lyonzin/knowledge-rag](https://github.com/lyonzin/knowledge-rag) 🐍 🏠 🍎 🪟 🐧 - Local RAG system for Claude Code with hybrid search (BM25 + semantic), cross-encoder reranking, markdown-aware chunking, query expansion, and 12 MCP tools. Runs entirely offline with zero external servers. Available on [PyPI](https://pypi.org/project/knowledge-rag/).
- - [shibley/apistatuscheck-mcp-server](https://github.com/shibley/apistatuscheck-mcp-server) 📇 ☁️ - Check real-time operational status of 114+ cloud services and APIs (AWS, GitHub, Stripe, OpenAI, Vercel, etc.) directly from AI assistants. Published on npm.
+ - [webdriverio/mcp](https://github.com/webdriverio/mcp) [![mcp MCP server](https://glama.ai/mcp/servers/webdriverio/mcp/badges/score.svg)](https://glama.ai/mcp/servers/webdriverio/mcp) 📇 🏠 - Browser and mobile app automation using WebdriverIO, enabling AI agents to control browsers, interact with web elements, and automate native Android and iOS apps via the WebDriver and Appium protocols.
+ - [KryptosAI/mcp-observatory](https://github.com/KryptosAI/mcp-observatory) [![mcp-observatory MCP server](https://glama.ai/mcp/servers/KryptosAI/mcp-observatory/badges/score.svg)](https://glama.ai/mcp/servers/KryptosAI/mcp-observatory) 📇 🏠 🍎 🪟 🐧 - Regression testing for MCP servers. Auto-discovers servers from Claude configs, checks capabilities, invokes tools, detects schema drift between versions, and recommends new servers based on your environment. Works as both a CLI and an MCP server.
+ - [lyonzin/knowledge-rag](https://github.com/lyonzin/knowledge-rag) [![lyonzin/knowledge-rag MCP server](https://glama.ai/mcp/servers/lyonzin/knowledge-rag/badges/score.svg)](https://glama.ai/mcp/servers/lyonzin/knowledge-rag) 🐍 🏠 🍎 🪟 🐧 - Local RAG system for Claude Code with hybrid search (BM25 + semantic), cross-encoder reranking, markdown-aware chunking, query expansion, and 12 MCP tools. Runs entirely offline with zero external servers.
+ - [lyonzin/knowledge-rag](https://github.com/lyonzin/knowledge-rag) 🐍 🏠 🍎 🪟 🐧 - Local RAG system for Claude Code with hybrid search (BM25 + semantic), cross-encoder reranking, markdown-aware chunking, query expansion, and 12 MCP tools. Runs entirely offline with zero external servers. Available on [PyPI](https://pypi.org/project/knowledge-rag/). [![lyonzin/knowledge-rag MCP server](https://glama.ai/mcp/servers/lyonzin/knowledge-rag/badges/score.svg)](https://glama.ai/mcp/servers/lyonzin/knowledge-rag)
+ - [lyonzin/knowledge-rag](https://github.com/lyonzin/knowledge-rag) 🐍 🏠 🍎 🪟 🐧 - Local RAG system for Claude Code with hybrid search (BM25 + semantic), cross-encoder reranking, markdown-aware chunking, query expansion, and 12 MCP tools. Runs entirely offline with zero external servers. Available on [PyPI](https://pypi.org/project/knowledge-rag/).
+ - [shibley/apistatuscheck-mcp-server](https://github.com/shibley/apistatuscheck-mcp-server) [![apistatuscheck-mcp-server MCP server](https://glama.ai/mcp/servers/shibley/apistatuscheck-mcp-server/badges/score.svg)](https://glama.ai/mcp/servers/shibley/apistatuscheck-mcp-server) 📇 ☁️ - Check real-time operational status of 114+ cloud services and APIs (AWS, GitHub, Stripe, OpenAI, Vercel, etc.) directly from AI assistants. Published on npm.
```



#### [Awesome-Dify-Workflow](https://github.com/svcvit/Awesome-Dify-Workflow)

##### Commit Changes

No file changes detected.

#### [system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools)

##### Commit Changes

No file changes detected.

