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

### 2025-12-06T01:23:41

#### [awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps)

##### Commit Changes

No file changes detected.

#### [awesome-gpt4o-images](https://github.com/jamez-bondos/awesome-gpt4o-images)

##### Commit Changes

No file changes detected.

#### [awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers)

##### Commit Changes

- [7a3f715](https://github.com/punkpeye/awesome-mcp-servers/commit/7a3f71568c9b84e699ee7df56e207448f38eb79b) Merge pull request #1517 from sbroenne/add-excel-mcp-server - Frank Fiegel
- [17282af](https://github.com/punkpeye/awesome-mcp-servers/commit/17282afe8e9a34e166b607eafd7a0762bd235695) Add sbroenne/mcp-server-excel to Developer Tools - Stefan Broenner
- [d758c1c](https://github.com/punkpeye/awesome-mcp-servers/commit/d758c1c3d64e88d97e12d99d41e5b6ce15a26d06) Add JetBrains Index MCP Plugin to README.md - Carmel Hecht
- [75bc74c](https://github.com/punkpeye/awesome-mcp-servers/commit/75bc74c9bfb66172e79c9020ad3b9f6b68fddb56) Merge pull request #1216 from AndrasEszes/add-bitrise-mcp-server - Frank Fiegel
- [9737656](https://github.com/punkpeye/awesome-mcp-servers/commit/973765600ea4489604d220145ff340576bb9f4fb) Merge pull request #1225 from kukapay/main - Frank Fiegel
- [5ede1c6](https://github.com/punkpeye/awesome-mcp-servers/commit/5ede1c620911700b72c1e5a64e9b0c5130008bdd) Merge pull request #1367 from wenb1n-dev/main - Frank Fiegel
- [65a96a8](https://github.com/punkpeye/awesome-mcp-servers/commit/65a96a8f858445bdb96f6d8a8c67d6ba81e24bc3) Merge branch 'main' into add-ncp-orchestrator - Frank Fiegel
- [d0e9fd2](https://github.com/punkpeye/awesome-mcp-servers/commit/d0e9fd214a2986653e4e937a23ff968f3d030108) Update README.md - Frank Fiegel
- [a3e6232](https://github.com/punkpeye/awesome-mcp-servers/commit/a3e6232f18d36fef44021d7e4471ad234e598780) Merge pull request #1402 from wenerme/add-wener-mssql-mcp - Frank Fiegel
- [3e23e3f](https://github.com/punkpeye/awesome-mcp-servers/commit/3e23e3fe4ff75c68a72e63ee8382a929b0b980e4) Merge branch 'main' into add-new-server - Frank Fiegel


##### File Content Changes

**README.md** (Modified, +310 -30 lines):

```diff
- - [portel-dev/ncp](https://github.com/portel-dev/ncp) 📇 ☁️ 🏠 🍎 🪟 🐧 - **1 MCP to rule them all** - NCP orchestrates your entire MCP ecosystem through intelligent discovery, eliminating token overhead while maintaining 98.2% accuracy. Transform 100+ tools into 2 unified interfaces, achieve 94.8% token savings, and let your AI focus on what matters - not tool schemas.
+ - [sbroenne/mcp-server-excel](https://github.com/sbroenne/mcp-server-excel) #️⃣ 🏠 🪟 - Full-featured Excel MCP server. 173 operations: Power Query, DAX, VBA, PivotTables, Tables, Charts, ranges, formatting. 100% Excel compatibility - uses Excel app instead of creating .xlsx files. Windows only.
+ - [hechtcarmel/jetbrains-index-mcp-plugin](https://github.com/hechtcarmel/jetbrains-index-mcp-plugin) ☕ 🏠 - A JetBrains IDE plugin that exposes an MCP server, enabling AI coding assistants to leverage the IDE's indexing and refactoring capabilities (rename, safe delete, find references, call hierarchy, type hierarchy, diagnostics and more).
+ - [bitrise-io/bitrise-mcp](https://github.com/bitrise-io/bitrise-mcp) 🎖️ 🐍 ☁️ 🍎 🪟 🐧 - MCP Server for the [Bitrise](https://bitrise.io) API, enabling app management, build operations, artifact management and more.
+ - [kukapay/bitcoin-utxo-mcp](https://github.com/kukapay/bitcoin-utxo-mcp) 🐍 ☁️ - An MCP server that tracks Bitcoin's Unspent Transaction Outputs (UTXO) and block statistics.
+ - [kukapay/bridge-metrics-mcp](https://github.com/kukapay/bridge-metrics-mcp) 📇 ☁️ - Providing real-time cross-chain bridge metrics.
+ - [kukapay/crypto-funds-mcp](https://github.com/kukapay/crypto-funds-mcp) 🐍 ☁️ -  Providing AI agents with structured, real-time data on cryptocurrency investment funds.
+ - [kukapay/crypto-stocks-mcp](https://github.com/kukapay/crypto-stocks-mcp) 🐍 ☁️ - An MCP server that tracks real-time data for major crypto-related stocks.
+ - [kukapay/dex-pools-mcp](https://github.com/kukapay/dex-pools-mcp) 🐍 ☁️ - An MCP server that provides AI agents with real-time access to DEX liquidity pool data.
+ - [kukapay/ethereum-validator-queue-mcp](https://github.com/kukapay/ethereum-validator-queue-mcp) 🐍 ☁️ -  An MCP server that tracks Ethereum’s validator activation and exit queues in real time.
+ - [kukapay/polymarket-predictions-mcp](https://github.com/kukapay/polymarket-predictions-mcp) 🐍 ☁️ - An MCP server that delivers real-time market odds from Polymarket.
+ - [kukapay/stargate-bridge-mcp](https://github.com/kukapay/stargate-bridge-mcp) 📇 ☁️ - An MCP server that enables cross-chain token transfers via the Stargate protocol.
+ - [wenb1n-dev/SmartDB_MCP](https://github.com/wenb1n-dev/SmartDB_MCP)  🐍 🏠 - A universal database MCP server supporting simultaneous connections to multiple databases. It provides tools for database operations, health analysis, SQL optimization, and more. Compatible with mainstream databases including MySQL, PostgreSQL, SQL Server, MariaDB, Dameng, and Oracle. Supports Streamable HTTP, SSE, and STDIO; integrates OAuth 2.0; and is designed for easy customization and extension by developers.
+ --- شروع فایل README.md ---
+ # سرورهای MCP عالی [![عالی](https://awesome.re/badge.svg)](https://awesome.re)
+ [![ไทย](https://img.shields.io/badge/Thai-Click-blue)](README-th.md)
+ [![English](https://img.shields.io/badge/English-Click-yellow)](README.md)
+ [![繁體中文](https://img.shields.io/badge/繁體中文-點擊查看-orange)](README-zh_TW.md)
+ [![简体中文](https://img.shields.io/badge/简体中文-点击查看-orange)](README-zh.md)
+ [![日本語](https://img.shields.io/badge/日本語-クリック-青)](README-ja.md)
+ [![한국어](https://img.shields.io/badge/한국어-클릭-yellow)](README-ko.md)
+ [![Português Brasileiro](https://img.shields.io/badge/Português_Brasileiro-Clique-green)](README-pt_BR.md)
+ [![Discord](https://img.shields.io/discord/1312302100125843476?logo=discord&label=discord)](https://glama.ai/mcp/discord)
+ [![Subreddit subscribers](https://img.shields.io/reddit/subreddit-subscribers/mcp?style=flat&logo=reddit&label=subreddit)](https://www.reddit.com/r/mcp/)
+ یک لیست منتخب از سرورهای عالی Model Context Protocol (MCP).
+ * [MCP چیست؟](#what-is-mcp)
+ * [کلاینت‌ها](#clients)
+ * [آموزش‌ها](#tutorials)
+ * [جامعه](#community)
+ * [راهنما](#legend)
+ * [پیاده‌سازی‌های سرور](#server-implementations)
+ * [چارچوب‌ها](#frameworks)
+ * [نکات و ترفندها](#tips-and-tricks)
+ ## MCP چیست؟
+ [MCP](https://modelcontextprotocol.io/) یک پروتکل باز است که به مدل‌های هوش مصنوعی امکان تعامل امن با منابع محلی و راه دور را از طریق پیاده‌سازی‌های سرور استاندارد شده می‌دهد. این لیست بر روی سرورهای MCP آماده برای تولید و آزمایشی تمرکز دارد که قابلیت‌های هوش مصنوعی را از طریق دسترسی به فایل، اتصالات پایگاه داده، یکپارچه‌سازی API و سایر خدمات متنی گسترش می‌دهند.
+ ## کلاینت‌ها
+ [awesome-mcp-clients](https://github.com/punkpeye/awesome-mcp-clients/) و [glama.ai/mcp/clients](https://glama.ai/mcp/clients) را بررسی کنید.
+ > [!TIP]
+ > [Glama Chat](https://glama.ai/chat) یک کلاینت هوش مصنوعی چندوجهی با پشتیبانی از MCP و [دروازه هوش مصنوعی](https://glama.ai/gateway) است.
+ ## آموزش‌ها
+ * [شروع سریع پروتکل زمینه مدل (MCP)](https://glama.ai/blog/2024-11-25-model-context-protocol-quickstart)
+ * [تنظیم برنامه دسکتاپ Claude برای استفاده از پایگاه داده SQLite](https://youtu.be/wxCCzo9dGj0)
+ ## جامعه
+ * [r/mcp Reddit](https://www.reddit.com/r/mcp)
+ * [سرور دیسکورد](https://glama.ai/mcp/discord)
+ ## راهنما
+ * 🎖️ – پیاده‌سازی رسمی
+ * زبان برنامه‌نویسی
+ * 🐍 – کدبیس Python
+ * 📇 – کدبیس TypeScript (یا JavaScript)
+ * 🏎️ – کدبیس Go
+ ... (1108 more additions)
```



#### [Awesome-Dify-Workflow](https://github.com/svcvit/Awesome-Dify-Workflow)

##### Commit Changes

No file changes detected.

#### [system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools)

##### Commit Changes

No file changes detected.

