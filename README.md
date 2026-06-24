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

### 2026-06-24T03:30:53

#### [awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps)

##### Commit Changes

No file changes detected.

#### [awesome-gpt4o-images](https://github.com/jamez-bondos/awesome-gpt4o-images)

##### Commit Changes

No file changes detected.

#### [awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers)

##### Commit Changes

- [033a70a](https://github.com/punkpeye/awesome-mcp-servers/commit/033a70abd99a18dd8a3ea86c990ab433b2aed883) Merge pull request #8469 from japlete/add-md-vision-mcp - Frank Fiegel
- [88e21ff](https://github.com/punkpeye/awesome-mcp-servers/commit/88e21ffbaf9dd47c84bec1384c550a0a84823449) Merge pull request #8186 from SebastianGilPinzon/add-colab-mcp-fork - Frank Fiegel
- [eca7d43](https://github.com/punkpeye/awesome-mcp-servers/commit/eca7d437efb98b0b7fc2f41d043986079f4f8d99) Merge pull request #8568 from kfuras/add-notipo-server - Frank Fiegel
- [58d0c3b](https://github.com/punkpeye/awesome-mcp-servers/commit/58d0c3b881a1104a063336f18a8975a2e5d10938) Merge pull request #8515 from SurajKGoyal/add-amnesic - Frank Fiegel
- [8b7ddf4](https://github.com/punkpeye/awesome-mcp-servers/commit/8b7ddf4e61dee54106ed069932d9a180774a4ab1) Merge pull request #8525 from deslay1/add-amendor-mcp - Frank Fiegel
- [2ff48c3](https://github.com/punkpeye/awesome-mcp-servers/commit/2ff48c31239275a8293ae184e5e9d12bbfe98f93) Merge pull request #7418 from woladi/add-macos-vision-mcp - Frank Fiegel
- [c9c9194](https://github.com/punkpeye/awesome-mcp-servers/commit/c9c919417b8495ea625e0dc82575ae663718fe86) Merge pull request #8433 from Michael-WhiteCapData/add-ollama-handoff - Frank Fiegel
- [0d1ab79](https://github.com/punkpeye/awesome-mcp-servers/commit/0d1ab792e3a4878274b4a8f4986918e2905548f5) Merge pull request #8355 from mambabuilt/add-mamba-company-firmographic-enricher - Frank Fiegel
- [cbe4901](https://github.com/punkpeye/awesome-mcp-servers/commit/cbe49013c6bf631f9a552ab791f63907c5303d67) Merge pull request #8164 from InnarM/add-blank-invoice-maker-mcp - Frank Fiegel
- [5878736](https://github.com/punkpeye/awesome-mcp-servers/commit/58787366a00b3568bd8ff1bc793c4ba3742a40fa) Merge pull request #8055 from ocbenji/add-bitcoinbenji-mcp - Frank Fiegel


##### File Content Changes

**README.md** (Modified, +10 -0 lines):

```diff
+ - [japlete/md-vision-mcp](https://github.com/japlete/md-vision-mcp) [![md-vision-mcp MCP server](https://glama.ai/mcp/servers/japlete/md-vision-mcp/badges/score.svg)](https://glama.ai/mcp/servers/japlete/md-vision-mcp) 📇 🏠 🍎 🪟 🐧 - Read Markdown with inlined images and heading indexes for agentic RAG over local docs or allowed URLs.
+ - [SebastianGilPinzon/colab-mcp](https://github.com/SebastianGilPinzon/colab-mcp) [![SebastianGilPinzon/colab-mcp MCP server](https://glama.ai/mcp/servers/SebastianGilPinzon/colab-mcp/badges/score.svg)](https://glama.ai/mcp/servers/SebastianGilPinzon/colab-mcp) 🐍 🏠 🍎 🪟 🐧 - Control Google Colab notebooks and assign GPUs (T4/L4/A100) from any AI agent. Enhanced fork of Google's colab-mcp with all tools visible at startup, OAuth GPU control, and Windows support.
+ - [kfuras/notipo-app](https://github.com/kfuras/notipo-app) [![kfuras/notipo-app MCP server](https://glama.ai/mcp/servers/kfuras/notipo-app/badges/score.svg)](https://glama.ai/mcp/servers/kfuras/notipo-app) 📇 ☁️ 🏠 🍎 🪟 🐧 - WordPress publishing for AI agents. 13 tools to list, create, update, publish, and delete posts. Markdown to Gutenberg, automatic image hosting, featured image generation, SEO metadata (Rank Math / Yoast / SEOPress / AIOSEO), categories, and tags — one MCP call runs the full pipeline. Self-host with Docker or use the hosted SaaS at [notipo.com](https://notipo.com). AGPL-3.0.
+ - [SurajKGoyal/amnesic](https://github.com/SurajKGoyal/amnesic) [![SurajKGoyal/amnesic MCP server](https://glama.ai/mcp/servers/SurajKGoyal/amnesic/badges/score.svg)](https://glama.ai/mcp/servers/SurajKGoyal/amnesic) 🐍 🏠 🍎 🪟 🐧 - The MCP server that remembers your database — persists table/column annotations, an FK relationship graph, and searchable notes across sessions, so the model stops re-discovering your schema every time. PostgreSQL, MySQL, MSSQL, SQLite; read-only-enforced.
+ - [deslay1/amendor-mcp](https://github.com/deslay1/amendor-mcp) [![deslay1/amendor-mcp MCP server](https://glama.ai/mcp/servers/deslay1/amendor-mcp/badges/score.svg)](https://glama.ai/mcp/servers/deslay1/amendor-mcp) 📇 ☁️ - Lets the non-technical people you build for request UI changes directly on your live site, then pulls each request (with the exact element and page) into your coding agent so it builds it on a branch and opens a pull request. Works with Claude Code, Cursor, Cline, Codex, and remote agents over HTTP. `npx -y amendor-mcp`
+ - [woladi/macos-vision-mcp](https://github.com/woladi/macos-vision-mcp) [![macos-vision-mcp MCP server](https://glama.ai/mcp/servers/woladi/macos-vision-mcp/badges/score.svg)](https://glama.ai/mcp/servers/woladi/macos-vision-mcp) 📇 🏠 🍎 - Local OCR and image analysis via Apple Vision Framework. Wraps macOS's native Vision API to expose OCR for images and PDFs (with reading-order paragraphs, bounding boxes, line/paragraph IDs, and confidence), face / barcode / QR / document-corner detection, and image classification — all as MCP tools any client (Claude Code, Claude Desktop, Cursor, Codex CLI) can call. ~97% token savings vs sending raw images. Fully offline, no API keys, files never leave the Mac. One-line install: `npx -y macos-vision-mcp`.
+ - [Michael-WhiteCapData/ollama-handoff](https://github.com/Michael-WhiteCapData/ollama-handoff) 🐍 🏠 🍎 🪟 🐧 - Offload cheap work from your cloud LLM agent to a local Ollama model — summaries, drafts, extractions, and first-pass code reviews via purpose-built handoff tools with baked-in prompts, at zero cloud cost. [![Michael-WhiteCapData/ollama-handoff MCP server](https://glama.ai/mcp/servers/Michael-WhiteCapData/ollama-handoff/badges/score.svg)](https://glama.ai/mcp/servers/Michael-WhiteCapData/ollama-handoff)
+ - [mambalabsdev/mcp-company-firmographic-enricher](https://github.com/mambalabsdev/mcp-company-firmographic-enricher) [![mambalabsdev/mcp-company-firmographic-enricher MCP server](https://glama.ai/mcp/servers/mambalabsdev/mcp-company-firmographic-enricher/badges/score.svg)](https://glama.ai/mcp/servers/mambalabsdev/mcp-company-firmographic-enricher) 📇 ☁️ - Enriches a company domain into firmographics: employee band, industry, HQ, founded year, revenue estimate, logo, and description, with source provenance.
+ - [InnarM/blank-invoice-maker-mcp](https://github.com/InnarM/blank-invoice-maker-mcp) [![InnarM/blank-invoice-maker-mcp MCP server](https://glama.ai/mcp/servers/InnarM/blank-invoice-maker-mcp/badges/score.svg)](https://glama.ai/mcp/servers/InnarM/blank-invoice-maker-mcp) 📇 🏠 🍎 🪟 🐧 - Create free, no-signup invoices from your AI assistant. Returns a deep link that opens [Blank Invoice Maker](https://blankinvoicemaker.com) pre-filled — review and download a watermark-free PDF. Invoice data stays in the browser. `npx blank-invoice-maker-mcp`
+ - [ocbenji/bitcoinbenji-mcp](https://github.com/ocbenji/bitcoinbenji-mcp) [![ocbenji/bitcoinbenji-mcp MCP server](https://glama.ai/mcp/servers/ocbenji/bitcoinbenji-mcp/badges/score.svg)](https://glama.ai/mcp/servers/ocbenji/bitcoinbenji-mcp) 📇 ☁️ 🍎 🪟 🐧 - Lightning-paid (L402) Bitcoin mempool intelligence + sovereign on-prem AI inference. 25 pay-per-call tools: live fees with trend, whale/mempool alerts, fee prediction, tx status & exact fee quotes, plus AI summarize/translate/grammar/code-review/code-gen/extract/classify/rewrite/explain/vision/OCR/embeddings and long-context docs — all on a self-hosted solar-powered GPU, no third-party APIs, pay 2–100 sats per call. `npm i -g @bitcoinbenji/mcp`
```



#### [Awesome-Dify-Workflow](https://github.com/svcvit/Awesome-Dify-Workflow)

##### Commit Changes

No file changes detected.

#### [system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools)

##### Commit Changes

No file changes detected.

