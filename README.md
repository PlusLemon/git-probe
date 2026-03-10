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

### 2026-03-10T01:57:13

#### [awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps)

##### Commit Changes

No file changes detected.

#### [awesome-gpt4o-images](https://github.com/jamez-bondos/awesome-gpt4o-images)

##### Commit Changes

No file changes detected.

#### [awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers)

##### Commit Changes

- [776d99e](https://github.com/punkpeye/awesome-mcp-servers/commit/776d99e46e98255d2ea5c01972f9ac7f748b48a2) Merge pull request #2841 from trackerfitness729-jpg/add-sitelauncher - Frank Fiegel
- [4a4b46c](https://github.com/punkpeye/awesome-mcp-servers/commit/4a4b46cc2f3877808da8337b7f2dadeb94dbd5af) Merge pull request #2889 from idapixl/add-idapixl-servers - Frank Fiegel
- [5f6fd64](https://github.com/punkpeye/awesome-mcp-servers/commit/5f6fd640ccdde9270879a09d7fae2ffa9ec3ed66) Merge pull request #2909 from arthurpanhku/patch-9 - Frank Fiegel
- [6989b33](https://github.com/punkpeye/awesome-mcp-servers/commit/6989b33706de82f51dd20d06db714292565238ca) Merge pull request #2910 from tasopen/main - Frank Fiegel
- [eec40be](https://github.com/punkpeye/awesome-mcp-servers/commit/eec40be6e4ea718a527882dcc1bb185437e82a9b) Merge pull request #2912 from yarinbnyamin/add-new-server - Frank Fiegel
- [3b0a031](https://github.com/punkpeye/awesome-mcp-servers/commit/3b0a031cef22492af8df5461e64178caf530bad2) Merge branch 'main' into add-indigo-mcp - Frank Fiegel
- [ad6788e](https://github.com/punkpeye/awesome-mcp-servers/commit/ad6788e597e02457c37af27b8b6083b9fdd7b583) Merge pull request #2914 from adacapo21/add-cardano-mcp - Frank Fiegel
- [7e71be1](https://github.com/punkpeye/awesome-mcp-servers/commit/7e71be15207e7f089dddeb9b64381eaeb83781b5) Merge pull request #2918 from ashimnandi-trika/add-systemr-risk-intelligence - Frank Fiegel
- [02a96e4](https://github.com/punkpeye/awesome-mcp-servers/commit/02a96e404b5778487ba729cee662984380143856) Merge pull request #2920 from gnuchev/add-postcardbot - Frank Fiegel
- [3c6f28a](https://github.com/punkpeye/awesome-mcp-servers/commit/3c6f28ad8b91846e88a6f75ff6f5c9074abadbd6) Update README.md - Frank Fiegel


##### File Content Changes

**README.md** (Modified, +25 -2 lines):

```diff
- - [PostcardBot/mcp-server](https://github.com/PostcardBot/mcp-server) ([glama](https://glama.ai/mcp/servers/PostcardBot/postcardbot-mcp-server)) 📇 ☁️ - Send real physical postcards worldwide via AI agents. Bulk send up to 500 recipients. Volume pricing from $0.72/card. Powered by [Postcard.bot](https://postcard.bot).
+ - [trackerfitness729-jpg/sitelauncher-mcp-server](https://github.com/trackerfitness729-jpg/sitelauncher-mcp-server) [glama](https://glama.ai/mcp/servers/@trackerfitness729-jpg/sitelauncher-mcp-server) 📇 ☁️ - Deploy live HTTPS websites in seconds. Instant subdomains ($1 USDC) or custom .xyz domains ($10 USDC) on Base chain. Templates for crypto tokens and AI agent profiles.
+ - [idapixl/algora-mcp-server](https://github.com/idapixl/algora-mcp-server) [glama](https://glama.ai/mcp/servers/idapixl-algora-mcp-server) 📇 ☁️ - Browse and search open-source bounties on Algora. 5 tools: list, search, filter by org/tech/amount, get top bounties, aggregate stats. No API key required.
+ - [idapixl/idapixl-web-research-mcp](https://github.com/idapixl/idapixl-web-research-mcp) [glama](https://glama.ai/mcp/servers/idapixl-web-research-mcp) 📇 ☁️ - AI-powered web research server with search, page fetching, and multi-source synthesis. Cleans HTML to markdown, extracts excerpts, and produces structured research briefs. Available on Apify.
+ - [arthurpanhku/DragonMCP](https://github.com/arthurpanhku/DragonMCP) [glama](https://glama.ai/mcp/servers/arthurpanhku/dragon-mcp) 📇 🏠 ☁️ 🍎   - MCP server for Greater China local life services: Meituan/Ele.me food delivery, Didi/Meituan ride-hailing, WeChat Pay/Alipay, Amap/Baidu Maps, 12306 high-speed rail, Taobao/JD/Xianyu e-commerce, Hong Kong government e-services, and more.
+ - [tasopen/mcp-alphabanana](https://github.com/tasopen/mcp-alphabanana) [glama](https://glama.ai/mcp/servers/@tasopen/mcp-alphabanana) 📇 🏠 🍎 🪟 🐧 - Local MCP server for generating image assets with Google Gemini (Nano Banana 2 / Pro). Supports transparent PNG/WebP output, exact resizing/cropping, up to 14 reference images, and Google Search grounding.
+ - [SPL-BGU/PlanningCopilot](https://github.com/SPL-BGU/PlanningCopilot) [glama](https://glama.ai/mcp/servers/SPL-BGU/planning-copilot) 🐍🏠 - A tool-augmented LLM system for the full PDDL planning pipeline, improving reliability without domain-specific training.
+ - [entire-vc/evc-spark-mcp](https://github.com/entire-vc/evc-spark-mcp) [glama](https://glama.ai/mcp/servers/entire-vc/evc-spark-mcp) 📇 ☁️ 🏠 🍎 🪟 🐧 - Search and discover AI agents, skills, prompts, bundles and MCP connectors from a curated catalog of 4500+ assets.
+ - [gavxm/ani-mcp](https://github.com/gavxm/ani-mcp) [glama](https://glama.ai/mcp/servers/gavxm/ani-mcp) 📇 🏠 - MCP server for AniList with taste-aware recommendations, watch analytics, social tools, and full list management.
+ - [ammawla/encode-toolkit](https://github.com/ammawla/encode-toolkit) [glama](https://glama.ai/mcp/servers/ammawla/encode-toolkit) 🐧 - MCP server and Claude Plugin for a full ENCODE Project genomic data and analysis toolkit — search, download, track, and analyze functional genomics experiments.
+ - [nnemirovsky/iwdp-mcp](https://github.com/nnemirovsky/iwdp-mcp) [glama](https://glama.ai/mcp/servers/nnemirovsky/iwdp-mcp) 🏎️ 🏠 🍎 🐧 - iOS Safari debugging via ios-webkit-debug-proxy — MCP server with full WebKit Inspector Protocol support (DOM, CSS, Network, Storage, Debugger, and more)
+ - [PostcardBot/mcp-server](https://github.com/PostcardBot/mcp-server) [glama](https://glama.ai/mcp/servers/PostcardBot/postcardbot-mcp-server) 📇 ☁️ - Send real physical postcards worldwide via AI agents. Bulk send up to 500 recipients. Volume pricing from $0.72/card.
+ - [dan1d/mercadolibre-mcp](https://github.com/dan1d/mercadolibre-mcp) [glama](https://glama.ai/mcp/servers/dan1d/mercadolibre-mcp) 📇 ☁️ - MercadoLibre marketplace integration for AI agents. Search products, get item details, browse categories, track trends, and convert currencies across Latin America (Argentina, Brazil, Mexico, Chile, Colombia).
+ - [fantasieleven-code/callout](https://github.com/fantasieleven-code/callout) [glama](https://glama.ai/mcp/servers/fantasieleven-code/callout-dev) 📇 🏠 - Multi-perspective architecture review for AI-assisted development. Nine expert viewpoints (CTO, Security, Product, DevOps, Customer, Strategy, Investor, Unicorn Founder, Solo Entrepreneur) analyze your project and produce actionable findings. Includes AI collaboration coaching and quantitative idea scoring.
+ - [up2itnow0822/clawpay-mcp](https://github.com/up2itnow0822/clawpay-mcp) [glama](https://glama.ai/mcp/servers/@up2itnow0822/clawpay-mcp) 📇 ☁️ - Non-custodial x402 payment layer for AI agents. Agents sign transactions from their own wallet with on-chain spend limits — no custodial infrastructure, no API keys. Built on Base.
+ - [dan1d/dolar-mcp](https://github.com/dan1d/dolar-mcp) [glama](https://glama.ai/mcp/servers/dan1d/dolar-mcp) 📇 ☁️ - Argentine exchange rates for AI agents via DolarAPI. Dollar blue, oficial, MEP, CCL, crypto, tarjeta — plus currency conversion and spread calculator.
+ - [IndigoProtocol/cardano-mcp](https://github.com/IndigoProtocol/cardano-mcp) [glama](https://glama.ai/mcp/servers/IndigoProtocol/cardano-mcp) 📇 ☁️ 🏠 - Cardano blockchain MCP server for wallet interactions — submit transactions, fetch addresses, read UTxOs, check balances, resolve ADAHandles, and check stake delegation
+ - [System-R-AI/systemr-python](https://github.com/System-R-AI/systemr-python) [glama](https://glama.ai/mcp/servers/System-R-AI/systemr-python) 🐍 ☁️ - Trading OS for AI agents — 48 tools covering pre-trade risk gates, position sizing, portfolio analytics, regime detection, and compliance scoring. Remote SSE + Streamable HTTP transport with x402 USDC micropayments.
+ - [agenticdecks/deckrun-mcp](https://github.com/agenticdecks/deckrun-mcp) [glama](https://glama.ai/mcp/servers/agenticdecks/deckrun-mcp) 🐍 ☁️ - Generate presentation PDFs, narrated videos, and MP3 audio from Markdown. Free tier requires no API key or local install — add a URL to your IDE config and start generating. Paid tier adds video, audio, async jobs, and account tools.
+ - [BrowseAI-HQ/BrowserAI-Dev](https://github.com/BrowseAI-HQ/BrowserAI-Dev) [glama](https://glama.ai/mcp/servers/BrowseAI-HQ/browse-ai) 📇 ☁️ - Evidence-backed web research for AI agents. Real-time search with cited claims, confidence scores, and compare mode (raw LLM vs evidence-backed). MCP server, REST API, and Python SDK.
+ - [TollboothLabs/ai-tool-optimizer](https://github.com/TollboothLabs/ai-tool-optimizer) [glama](https://glama.ai/mcp/servers/@TollboothLabs/ai-tool-optimizer) 🐍 - Reduces MCP tool description token costs by 40-70% through pure text schema distillation.
```



#### [Awesome-Dify-Workflow](https://github.com/svcvit/Awesome-Dify-Workflow)

##### Commit Changes

No file changes detected.

#### [system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools)

##### Commit Changes

- [c727405](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools/commit/c727405a4eddc60907b6ca8bf78f17ba450675f8) Update README.md - Lucas Valbuena


##### File Content Changes

**README.md** (Modified, +9 -10 lines):

```diff
- ## 🛡️ Security Notice for AI Startups
- > ⚠️ **Warning:** If you're an AI startup, make sure your data is secure. Exposed prompts or AI models can easily become a target for hackers.
- > 🔐 **Important:** Interested in securing your AI systems?
- > Check out **[ZeroLeaks](https://zeroleaks.ai/)**, a service designed to help startups **identify and secure** leaks in system instructions, internal tools, and model configurations. **Get a free AI security audit** to ensure your AI is protected from vulnerabilities.
+ ## 🛡️ Security Notice for AI Startups
+ > ⚠️ **Warning:** If you're an AI startup, make sure your data is secure. Exposed prompts or AI models can easily become a target for hackers.
+ > 🔐 **Important:** Interested in securing your AI systems?
+ > Check out **[ZeroLeaks](https://zeroleaks.ai/)**, a service designed to help startups **identify and secure** leaks in system instructions, internal tools, and model configurations. **Get a free AI security audit** to ensure your AI is protected from vulnerabilities.
+ ---
```



