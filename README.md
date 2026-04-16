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

### 2026-04-16T02:35:36

#### [awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps)

##### Commit Changes

- [b70e077](https://github.com/Shubhamsaboo/awesome-llm-apps/commit/b70e07790cd64539ecf95515ed8576f1f871e6c3) docs: update README - Shubhamsaboo
- [8307dc1](https://github.com/Shubhamsaboo/awesome-llm-apps/commit/8307dc19dffe87dad254537518282f4e7b39a8ba) style: bold the model compatibility list in README.md - Shubhamsaboo
- [b518dec](https://github.com/Shubhamsaboo/awesome-llm-apps/commit/b518dec6b51639915a8dbd60ecfdae9d6530ff67) chore: remove icon images and simplify formatting in README.md - Shubhamsaboo
- [d1da301](https://github.com/Shubhamsaboo/awesome-llm-apps/commit/d1da301147bf61a8081aaf91cf82bc52a03a5e7f) docs: overhaul README with updated branding, project structure, and quick-start guide - Shubhamsaboo


##### File Content Changes

**README.md** (Modified, +165 -62 lines):

```diff
- | [🩺 RAG Failure Diagnostics Clinic](rag_tutorials/rag_failure_diagnostics_clinic/) | Diagnose & fix broken RAG pipelines | RAG + evals |
- | [🔍 AI Fraud Investigation Agent](advanced_ai_agents/single_agent_apps/ai_fraud_investigation_agent/) | Autonomous fraud investigator | Single-agent + tools |
- <strong>Free step-by-step tutorials on <a href="https://www.theunwindai.com">Unwind AI</a></strong><br/><br/>
- Works with Claude · Gemini · OpenAI · xAI · Qwen · Llama
- <strong>Free step-by-step tutorials on <a href="https://www.theunwindai.com">Unwind AI</a></strong><br/>
- Works with <img src="https://cdn.simpleicons.org/claude" alt="claude" width="18" height="12" style="display:inline;vertical-align:middle"> Claude · <img src="https://cdn.simpleicons.org/googlegemini" alt="gemini" width="18" height="14" style="display:inline;vertical-align:middle"> Gemini · <img src="https://cdn.jsdelivr.net/npm/simple-icons@15/icons/openai.svg" alt="openai" width="18" height="12" style="display:inline;vertical-align:middle"> OpenAI · <img src="https://cdn.simpleicons.org/x" alt="xai" width="18" height="12" style="display:inline;vertical-align:middle"> xAI · <img src="https://cdn.simpleicons.org/alibabacloud" alt="qwen" width="18" height="12" style="display:inline;vertical-align:middle"> Qwen · <img src="https://cdn.simpleicons.org/meta" alt="llama" width="18" height="12" style="display:inline;vertical-align:middle"> Llama
- ### <img src="https://cdn.simpleicons.org/modelcontextprotocol" alt="mcp logo" width="25" height="20"> MCP AI Agents
- * <img src="https://cdn.simpleicons.org/google" alt="google logo" width="20" height="15"> [Gemma 3 Fine-tuning](advanced_llm_apps/llm_finetuning_tutorials/gemma3_finetuning/)
- * <img src="https://cdn.simpleicons.org/meta" alt="meta logo" width="25" height="15"> [Llama 3.2 Fine-tuning](advanced_llm_apps/llm_finetuning_tutorials/llama3.2_finetuning/)
- <img src="https://cdn.simpleicons.org/google" alt="google logo" width="25" height="15"> [Google ADK Crash Course](ai_agent_framework_crash_course/google_adk_crash_course/)
- <img src="https://cdn.jsdelivr.net/npm/simple-icons@15/icons/openai.svg" alt="openai logo" width="25" height="15"> [OpenAI Agents SDK Crash Course](ai_agent_framework_crash_course/openai_sdk_crash_course/)
- <img src="https://img.shields.io/badge/-Follow%20Shubham%20Saboo-blue?logo=linkedin&style=flat-square" alt="LinkedIn">
- <img src="https://img.shields.io/twitter/follow/Shubham_Saboo" alt="Twitter">
- A curated collection of **Awesome LLM apps built with RAG, AI Agents, Multi-agent Teams, MCP, Voice Agents, and more.** This repository features LLM apps that use models from <img src="https://cdn.jsdelivr.net/npm/simple-icons@15/icons/openai.svg"  alt="openai logo" width="25" height="15">**OpenAI** , <img src="https://cdn.simpleicons.org/anthropic"  alt="anthropic logo" width="25" height="15">**Anthropic**, <img src="https://cdn.simpleicons.org/googlegemini"  alt="google logo" width="25" height="18">**Google**, <img src="https://cdn.simpleicons.org/x"  alt="X logo" width="25" height="15">**xAI** and open-source models like <img src="https://cdn.simpleicons.org/alibabacloud"  alt="alibaba logo" width="25" height="15">**Qwen** or  <img src="https://cdn.simpleicons.org/meta"  alt="meta logo" width="25" height="15">**Llama** that you can run locally on your computer.
- <p align="center">
- <a href="https://trendshift.io/repositories/9876" target="_blank">
- <img src="https://trendshift.io/api/badge/repositories/9876" alt="Shubhamsaboo%2Fawesome-llm-apps | Trendshift" style="width: 250px; height: 55px;" />
- </a>
- ## 🤔 Why Awesome LLM Apps?
- - 💡 Discover practical and creative ways LLMs can be applied across different domains, from code repositories to email inboxes and more.
- - 🔥 Explore apps that combine LLMs from OpenAI, Anthropic, Gemini, and open-source alternatives with AI Agents, Agent Teams, MCP & RAG.
- - 🎓 Learn from well-documented projects and contribute to the growing open-source ecosystem of LLM-powered applications.
- ## 📂 Featured AI Projects
- ### AI Agents
- *   [🧠 DevPulse AI — Multi-Agent Signal Intelligence](advanced_ai_agents/multi_agent_apps/devpulse_ai/)
- *   [🌐 Openwork - Open Browser Automation Agent](https://github.com/accomplish-ai/openwork)
- ### 🎮 Autonomous Game Playing Agents
- *   [🎙️ OpenSource Voice Dictation Agent (like Wispr Flow](https://github.com/akshayaggarwal99/jarvis-ai-assistant)
- ### <img src="https://cdn.simpleicons.org/modelcontextprotocol"  alt="mcp logo" width="25" height="20"> MCP AI Agents
- *   [📑 Notion MCP Agent](mcp_ai_agents/notion_mcp_agent)
- *   [🎯 Toonify Token Optimization](advanced_llm_apps/llm_optimization_tools/toonify_token_optimization/) - Reduce LLM API costs by 30-60% using TOON format
- *   [🧠 Headroom Context Optimization](advanced_llm_apps/llm_optimization_tools/headroom_context_optimization/) - Reduce LLM API costs by 50-90% format
- * <img src="https://cdn.simpleicons.org/google"  alt="google logo" width="20" height="15"> [Gemma 3 Fine-tuning](advanced_llm_apps/llm_finetuning_tutorials/gemma3_finetuning/)
- * <img src="https://cdn.simpleicons.org/meta"  alt="meta logo" width="25" height="15"> [Llama 3.2 Fine-tuning](advanced_llm_apps/llm_finetuning_tutorials/llama3.2_finetuning/)
- <img src="https://cdn.simpleicons.org/google"  alt="google logo" width="25" height="15"> [Google ADK Crash Course](ai_agent_framework_crash_course/google_adk_crash_course/)
- <img src="https://cdn.jsdelivr.net/npm/simple-icons@15/icons/openai.svg"  alt="openai logo" width="25" height="15"> [OpenAI Agents SDK Crash Course](ai_agent_framework_crash_course/openai_sdk_crash_course/)
- ### 🧩 Awesome Agent Skills
- *   [♾️ Self-Improving Agent Skills](awesome_agent_skills/self-improving-agent-skills/) - Automatically optimize agent skills using Gemini and ADK
- ## 🚀 Getting Started
- 1. **Clone the repository**
- ```bash
- git clone https://github.com/Shubhamsaboo/awesome-llm-apps.git
- ```
- 2. **Navigate to the desired project directory**
- cd awesome-llm-apps/starter_ai_agents/ai_travel_agent
- 3. **Install the required dependencies**
- pip install -r requirements.txt
- 4. **Follow the project-specific instructions** in each project's `README.md` file to set up and run the app.
- ### <img src="https://cdn.simpleicons.org/github"  alt="github logo" width="25" height="20"> Thank You, Community, for the Support! 🙏
- [![Star History Chart](https://api.star-history.com/svg?repos=Shubhamsaboo/awesome-llm-apps&type=Date)](https://star-history.com/#Shubhamsaboo/awesome-llm-apps&Date)
- ... (1 more deletions)
+ | [♾️ Self-Improving Agent Skills](awesome_agent_skills/self-improving-agent-skills/) | Automatically optimize agent skills using Gemini and ADK | Agent Skills + ADK |
+ <strong>Free step-by-step tutorials on <a href="https://www.theunwindai.com">Unwind AI</a></strong><br/>
+ <strong>Works with Claude · Gemini · OpenAI · xAI · Qwen · Llama</strong>
+ <strong>Free step-by-step tutorials on <a href="https://www.theunwindai.com">Unwind AI</a></strong><br/><br/>
+ Works with Claude · Gemini · OpenAI · xAI · Qwen · Llama
+ ### ♾️ MCP AI Agents
+ * [Gemma 3 Fine-tuning](advanced_llm_apps/llm_finetuning_tutorials/gemma3_finetuning/)
+ * [Llama 3.2 Fine-tuning](advanced_llm_apps/llm_finetuning_tutorials/llama3.2_finetuning/)
+ [Google ADK Crash Course](ai_agent_framework_crash_course/google_adk_crash_course/)
+ [OpenAI Agents SDK Crash Course](ai_agent_framework_crash_course/openai_sdk_crash_course/)
+ <img src="https://img.shields.io/badge/Follow%20on%20LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn">
+ <img src="https://img.shields.io/badge/Follow%20on%20𝕏-000000?style=for-the-badge&logo=x&logoColor=white" alt="X / Twitter">
+ <div align="center">
+ <p><strong>100+ AI Agent & RAG apps you can actually run — clone, customize, ship.</strong><br/>
+ AI Agents · Multi-agent Teams · MCP Agents · RAG · Voice Agents · Agent Skills · Fine-tuning</p>
+ <p>
+ Works with <img src="https://cdn.simpleicons.org/claude" alt="claude" width="18" height="12" style="display:inline;vertical-align:middle"> Claude · <img src="https://cdn.simpleicons.org/googlegemini" alt="gemini" width="18" height="14" style="display:inline;vertical-align:middle"> Gemini · <img src="https://cdn.jsdelivr.net/npm/simple-icons@15/icons/openai.svg" alt="openai" width="18" height="12" style="display:inline;vertical-align:middle"> OpenAI · <img src="https://cdn.simpleicons.org/x" alt="xai" width="18" height="12" style="display:inline;vertical-align:middle"> xAI · <img src="https://cdn.simpleicons.org/alibabacloud" alt="qwen" width="18" height="12" style="display:inline;vertical-align:middle"> Qwen · <img src="https://cdn.simpleicons.org/meta" alt="llama" width="18" height="12" style="display:inline;vertical-align:middle"> Llama
+ <a href="https://github.com/Shubhamsaboo/awesome-llm-apps/stargazers"><img src="https://img.shields.io/github/stars/Shubhamsaboo/awesome-llm-apps?style=for-the-badge&logo=github&color=FFD700" alt="Stars"></a>
+ <a href="https://github.com/Shubhamsaboo/awesome-llm-apps/network/members"><img src="https://img.shields.io/github/forks/Shubhamsaboo/awesome-llm-apps?style=for-the-badge&logo=github&color=4FC3F7" alt="Forks"></a>
+ <a href="https://github.com/Shubhamsaboo/awesome-llm-apps/graphs/contributors"><img src="https://img.shields.io/github/contributors/Shubhamsaboo/awesome-llm-apps?style=for-the-badge&color=22C55E" alt="Contributors"></a>
+ <a href="LICENSE"><img src="https://img.shields.io/github/license/Shubhamsaboo/awesome-llm-apps?style=for-the-badge&color=8B5CF6" alt="License"></a>
+ <img src="https://img.shields.io/github/last-commit/Shubhamsaboo/awesome-llm-apps?style=for-the-badge&color=F97316" alt="Last Commit">
+ </p>
+ <a href="#-quick-start"><kbd> &nbsp; 🚀 Quick Start &nbsp; </kbd></a>
+ <a href="#-featured-ai-projects"><kbd> &nbsp; 📂 Browse Templates &nbsp; </kbd></a>
+ <a href="https://www.theunwindai.com"><kbd> &nbsp; 📚 Step-by-Step Tutorials &nbsp; </kbd></a>
+ <a href="https://trendshift.io/repositories/9876" target="_blank">
+ <img src="https://trendshift.io/api/badge/repositories/9876" width="220" alt="Featured on Trendshift">
+ </a>
+ </div>
+ ---
+ ## 💡 Why this exists
+ You shouldn't have to rebuild the same RAG pipeline, agent loop, or MCP integration from scratch every time you start a new LLM project.
+ **Awesome LLM Apps is a cookbook of ready-to-run templates** - starter code you can fork, customize, and ship as a production LLM app. Every template here is self-contained with full source code, not collected from elsewhere.
+ - 🛠️ **Hand-built, not curated** - every template is original work, tested end-to-end before it ships.
+ - 🧪 **Runs in 3 commands** - no broken `requirements.txt`, no "figure it out yourself" scaffolding.
+ - 🧠 **Covers the modern AI stack** - AI Agents, Multi-agent Teams, MCP Agents, Voice AI Agents, RAG, Agent Skills, Fine-tuning.
+ - 🌐 **Provider-agnostic** - switch between Claude, Gemini, GPT, Llama, Qwen, xAI and others with a config change.
+ - 📚 **Step-by-step tutorials** - every featured template has a free walkthrough on [Unwind AI](https://www.theunwindai.com).
+ - 💸 **Apache-2.0** - fork it, ship it, sell it. No paywall, no signup, no telemetry.
+ > ⭐ **If this saves you time, [star the repo](https://github.com/Shubhamsaboo/awesome-llm-apps/stargazers) - that's how the next developer discovers it.**
+ ## 🚀 Quick Start
+ Run your first agent in **30 seconds**:
+ ```bash
+ git clone https://github.com/Shubhamsaboo/awesome-llm-apps.git
+ cd awesome-llm-apps/starter_ai_agents/ai_travel_agent
+ pip install -r requirements.txt
+ streamlit run travel_agent.py
+ ```
+ ## 🔥 Featured This Month
+ ... (84 more additions)
```



#### [awesome-gpt4o-images](https://github.com/jamez-bondos/awesome-gpt4o-images)

##### Commit Changes

No file changes detected.

#### [awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers)

##### Commit Changes

- [a56e865](https://github.com/punkpeye/awesome-mcp-servers/commit/a56e86528faea42a80df60e29c0ab3d1203af09f) Merge pull request #4813 from dobreandl/add-grovs - Frank Fiegel
- [707a0d0](https://github.com/punkpeye/awesome-mcp-servers/commit/707a0d042f0c242c85192412455689ec5983356b) Fix entry formatting - Frank Fiegel
- [56dd145](https://github.com/punkpeye/awesome-mcp-servers/commit/56dd1457d1d35d9d14e9cb88a37d71f1ba56de65) Merge pull request #4356 from codeislaw101/add-katzilla-server - Frank Fiegel
- [5ab3b29](https://github.com/punkpeye/awesome-mcp-servers/commit/5ab3b2943b1714219d9dfccbb7827e229faf175f) Merge pull request #3721 from sbuysse/add-gnome-desktop-mcp - Frank Fiegel
- [c779b83](https://github.com/punkpeye/awesome-mcp-servers/commit/c779b83da006b7e510987beec94f40aabb23bf59) Merge pull request #4881 from Gdetrane/add-gemini-media-mcp - Frank Fiegel
- [3d754d6](https://github.com/punkpeye/awesome-mcp-servers/commit/3d754d6a5f1a4ef8cc46a9ac78a831a87854eafe) Add trident-mcp to Multimedia Process - Gdetrane


##### File Content Changes

**README.md** (Modified, +12 -1 lines):

```diff
- - [codeislaw101/katzilla](https://github.com/codeislaw101/katzilla) 📇 ☁️ 🍎 🪟 🐧 - Unified data API for AI agents — 300+ free, public, and government data sources behind a single API key. Access economic (FRED, BLS), environmental (EPA, NOAA), health (CDC, FDA), weather (NWS), financial (SEC, CFPB), science (NASA, arXiv), and 30+ more categories. Install: `npx @katzilla/mcp`.
+ - [grovs-io/mcp](https://github.com/grovs-io/mcp) [![grovs-io/mcp MCP server](https://glama.ai/mcp/servers/grovs-io/mcp/badges/score.svg)](https://glama.ai/mcp/servers/grovs-io/mcp) 📇 ☁️ - Deep linking, attribution, analytics, and campaign management for mobile apps with [Grovs](https://grovs.io) — an open-source, privacy-first alternative to Branch and AppsFlyer. 16 tools for creating links, tracking installs and revenue, and configuring app settings.
+ - [codeislaw101/katzilla](https://github.com/codeislaw101/katzilla) [![codeislaw101/katzilla MCP server](https://glama.ai/mcp/servers/codeislaw101/katzilla/badges/score.svg)](https://glama.ai/mcp/servers/codeislaw101/katzilla) 📇 ☁️ 🍎 🪟 🐧 - Unified data API for AI agents — 300+ free, public, and government data sources behind a single API key. Access economic (FRED, BLS), environmental (EPA, NOAA), health (CDC, FDA), weather (NWS), financial (SEC, CFPB), science (NASA, arXiv), and 30+ more categories. Install: `npx @katzilla/mcp`.
+ - [codeislaw101/katzilla](https://github.com/codeislaw101/katzilla) 📇 ☁️ 🍎 🪟 🐧 - Unified data API for AI agents — 300+ free, public, and government data sources behind a single API key. Access economic (FRED, BLS), environmental (EPA, NOAA), health (CDC, FDA), weather (NWS), financial (SEC, CFPB), science (NASA, arXiv), and 30+ more categories. Install: `npx @katzilla/mcp`.
+ * 🖥️ - [OS Automation](#os-automation)
+ ### 🖥️ <a name="os-automation"></a>OS Automation
+ Servers for controlling the desktop operating system: screenshots, window management, mouse/keyboard input injection, and system-level automation.
+ - [sbuysse/gnome-desktop-mcp](https://github.com/sbuysse/gnome-desktop-mcp) [![gnome-desktop-mcp MCP server](https://glama.ai/mcp/servers/sbuysse/gnome-desktop-mcp/badges/score.svg)](https://glama.ai/mcp/servers/sbuysse/gnome-desktop-mcp) 🐍 🏠 🐧 - GNOME desktop automation for AI agents. 30 tools via D-Bus: screenshots, window management, mouse/keyboard injection, clipboard, workspaces, and system notifications. Works on any GNOME 45–49 Linux desktop.
+ - [mordor-forge/gemini-media-mcp](https://github.com/mordor-forge/gemini-media-mcp) [![mordor-forge/gemini-media-mcp MCP server](https://glama.ai/mcp/servers/mordor-forge/gemini-media-mcp/badges/score.svg)](https://glama.ai/mcp/servers/mordor-forge/gemini-media-mcp) 🏎️ ☁️ 🍎 🪟 🐧 - Unified Gemini media generation: Nano Banana (images, editing, multi-reference composition), Veo 3.1 (video, image-to-video, extend), TTS, and Lyria 3 (music with vocals). Single Go binary, 12 tools, supports Gemini API key and Vertex AI.
+ - [mordor-forge/trident-mcp](https://github.com/mordor-forge/trident-mcp) [![mordor-forge/trident-mcp MCP server](https://glama.ai/mcp/servers/mordor-forge/trident-mcp/badges/score.svg)](https://glama.ai/mcp/servers/mordor-forge/trident-mcp) 🏎️ ☁️ 🍎 🪟 🐧 - AI 3D model generation and post-processing: text/image/multiview-to-3D via Tripo, plus retopology, format conversion (GLB/FBX/OBJ/STL/USDZ), and stylization. Single Go binary, 10 tools, async generation with polling.
```



#### [Awesome-Dify-Workflow](https://github.com/svcvit/Awesome-Dify-Workflow)

##### Commit Changes

No file changes detected.

#### [system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools)

##### Commit Changes

No file changes detected.

