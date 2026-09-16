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

### 2026-09-16T03:27:43

#### [awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps)

##### Commit Changes

No file changes detected.

#### [awesome-gpt4o-images](https://github.com/jamez-bondos/awesome-gpt4o-images)

##### Commit Changes

No file changes detected.

#### [awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers)

##### Commit Changes

- [393b4e9](https://github.com/punkpeye/awesome-mcp-servers/commit/393b4e9fafb0348e5a1c2a4ef5a8719b0d85e061) Merge pull request #13298 from Celestial105/feat-add-dros-vajraclaw - Frank Fiegel
- [30b615f](https://github.com/punkpeye/awesome-mcp-servers/commit/30b615f27f19682d0a11ea57fb091cc448206246) Merge pull request #11528 from fireostendere/add-diptrace-mcp - Frank Fiegel
- [64d9df1](https://github.com/punkpeye/awesome-mcp-servers/commit/64d9df10151571a482b4d29362d6c0f4e299aaad) fix: place permitted emoji tags after badge as per Legend specification - Jimmy
- [c32fd37](https://github.com/punkpeye/awesome-mcp-servers/commit/c32fd37671096cca5091ed4f943be17283bbcad8) Add 402Signal to Aggregators - Ross
- [d7f9feb](https://github.com/punkpeye/awesome-mcp-servers/commit/d7f9febb5c4316edb0a6cac4b9f96ec7ff71b1b2) Merge pull request #13114 from chryaner/add-terrarium - Frank Fiegel
- [03e47f3](https://github.com/punkpeye/awesome-mcp-servers/commit/03e47f383bf08759b55d8a3ffa5a636fbf820c10) Rebase DipTrace MCP entry onto latest main - github-actions[bot]
- [c959369](https://github.com/punkpeye/awesome-mcp-servers/commit/c9593691889e5dbc61528ddd3482285317bd7a03) Add terrarium to OS Automation - Eiliya Raizis
- [ab175ef](https://github.com/punkpeye/awesome-mcp-servers/commit/ab175efcdb9828f8aed79218d2d93aca3d7929d1) Add frsorrentino/chrome-bridge (Browser Automation) 🤖🤖🤖 - frsorrentino
- [41d3f69](https://github.com/punkpeye/awesome-mcp-servers/commit/41d3f6906a6ad7dcc683aec8944f0672a48aebe3) Add skillmem to Knowledge & Memory - Sergey Petrukovich
- [e3912fc](https://github.com/punkpeye/awesome-mcp-servers/commit/e3912fc2e940cd0d8460e6c30a3f06451e92ae35) Merge pull request #13111 from Bristlecone2026/patch-1 - Frank Fiegel


##### File Content Changes

**README.md** (Modified, +14 -1 lines):

```diff
- - [Top-Celestial-Company-Ltd/DROS-VajraClaw-Hacker](https://github.com/Top-Celestial-Company-Ltd/DROS-VajraClaw-Hacker) 🐍 🐳 [![Top-Celestial-Company-Ltd/DROS-VajraClaw-Hacker MCP server](https://glama.ai/mcp/servers/Top-Celestial-Company-Ltd/DROS-VajraClaw-Hacker/badges/score.svg)](https://glama.ai/mcp/servers/Top-Celestial-Company-Ltd/DROS-VajraClaw-Hacker) - Deterministic in-band execution governance gateway and W3C DID security guardrail for AI Agent MCP tool calls.
+ ### 🔒 Security & Governance
+ - [Top-Celestial-Company-Ltd/DROS-VajraClaw-Hacker](https://github.com/Top-Celestial-Company-Ltd/DROS-VajraClaw-Hacker) [![Top-Celestial-Company-Ltd/DROS-VajraClaw-Hacker MCP server](https://glama.ai/mcp/servers/Top-Celestial-Company-Ltd/DROS-VajraClaw-Hacker/badges/score.svg)](https://glama.ai/mcp/servers/Top-Celestial-Company-Ltd/DROS-VajraClaw-Hacker) 🐍 🏠 🐧 🪟 🍎 - Deterministic in-band execution governance gateway and W3C DID security guardrail for AI Agent MCP tool calls.
+ - [fireostendere/mcp_diptrace](https://github.com/fireostendere/mcp_diptrace) [![fireostendere/mcp_diptrace MCP server](https://glama.ai/mcp/servers/fireostendere/mcp_diptrace/badges/score.svg)](https://glama.ai/mcp/servers/fireostendere/mcp_diptrace) 🐍 🏠 🪟 - Local MCP server and Windows bridge for reading, reviewing, and guarded editing of DipTrace PCB and schematic projects, with cross-platform offline XML analysis.
+ - [402signalhq/402signal](https://github.com/402signalhq/402signal) [![402Signal MCP server](https://glama.ai/mcp/servers/402signalhq/402signal/badges/score.svg)](https://glama.ai/mcp/servers/402signalhq/402signal) 🐍 ☁️ - Checks live x402 routes across Base, Solana, and Algorand. $0.003 USDC settles only for a valid live eligible route; normal typed misses are not settled. Free preview and validate tools. Seller payment is separate; the agent keeps its wallet. Remote MCP: https://402signal.com/mcp (x402-capable client required for paid routing).
+ - [chryaner/terrarium](https://github.com/chryaner/terrarium) [![chryaner/terrarium MCP server](https://glama.ai/mcp/servers/chryaner/terrarium/badges/score.svg)](https://glama.ai/mcp/servers/chryaner/terrarium) 🏎️ 🏠 🪟 - Fork, break, and revert real VirtualBox VMs as MCP tools. Forks are linked clones (~0.1s) and revert restores a RAM snapshot in seconds. Drives GUI-only guests through the hypervisor with screenshot, click, scroll, type and keys, so an agent controls a machine with no SSH, guest agent, or network, including Windows XP. Windows host with VirtualBox required. `npx -y terrarium-mcp mcp`
+ - [frsorrentino/chrome-bridge](https://github.com/frsorrentino/chrome-bridge) [![frsorrentino/chrome-bridge MCP server](https://glama.ai/mcp/servers/frsorrentino/chrome-bridge/badges/score.svg)](https://glama.ai/mcp/servers/frsorrentino/chrome-bridge) 📇 🏠 🍎 🪟 🐧 - MCP server + Chrome extension that drive the user's real, logged-in Chrome over a local WebSocket. 59 token-efficient web-dev tools: compact element refs instead of screenshots, server-side table filtering, visual regression, accessibility/SEO/security audits, network mocking. Also runs on ChromeOS/Crostini.
+ - [liza-studio/skillmem](https://github.com/liza-studio/skillmem) [![liza-studio/skillmem MCP server](https://glama.ai/mcp/servers/liza-studio/skillmem/badges/score.svg)](https://glama.ai/mcp/servers/liza-studio/skillmem) 🐍 🏠 🍎 🪟 🐧 - Self-improving skill memory for coding agents: skills that help get reinforced, unused ones fade on an Ebbinghaus decay curve. $0 write path (SQLite FTS5 + local ONNX embeddings, no LLM calls), bilingual EN/RU hybrid search, SHA256 tamper-evident history, deterministic LongMemEval benchmark in-repo (hit@5 0.871). 8 mem_* tools; deep Claude Code hook integration optional. `pip install skillmem`
+ - [Bristlecone-Logic/bristlecone-logic](https://github.com/Bristlecone2026/bristlecone-logic) [![Bristlecone-Logic/bristlecone-logic MCP server](https://glama.ai/mcp/servers/Bristlecone2026/bristlecone-logic/badges/score.svg)](https://glama.ai/mcp/servers/Bristlecone2026/bristlecone-logic) 🐍 ☁️ - Deterministic execution guardrails, isolated AST math evaluation, SSRF-safe DNS routing, and autonomous malformed JSON repair.
```



#### [Awesome-Dify-Workflow](https://github.com/svcvit/Awesome-Dify-Workflow)

##### Commit Changes

No file changes detected.

#### [system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools)

##### Commit Changes

No file changes detected.

