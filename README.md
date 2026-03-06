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

### 2026-03-06T02:01:31

#### [awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps)

##### Commit Changes

No file changes detected.

#### [awesome-gpt4o-images](https://github.com/jamez-bondos/awesome-gpt4o-images)

##### Commit Changes

No file changes detected.

#### [awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers)

##### Commit Changes

- [bc51fe0](https://github.com/punkpeye/awesome-mcp-servers/commit/bc51fe0af7d4f5f2c656ce46e8f04d8e694e3a92) Merge pull request #2164 from ChesterHsu/add-flyto-core - Frank Fiegel
- [83ef475](https://github.com/punkpeye/awesome-mcp-servers/commit/83ef475f8f21bc5fac0c0933fc90fb7fd58c427b) Merge pull request #2413 from rplryan/add-x402-discovery-mcp - Frank Fiegel
- [64926f2](https://github.com/punkpeye/awesome-mcp-servers/commit/64926f2f8a9bd11f90976b5f35f99a9b583821f7) Merge pull request #2748 from meetclawdius/add-measure-events - Frank Fiegel
- [d358e12](https://github.com/punkpeye/awesome-mcp-servers/commit/d358e129341e1ca90b27ebd3da358372073d5bda) Add Glama link for pmptwiki/pmpt-cli - raunplaymore
- [eb82e4a](https://github.com/punkpeye/awesome-mcp-servers/commit/eb82e4aacf6a6f30634e0515d438c9418bebfd73) Revert: remove Glama link from README entry - raunplaymore
- [07e1820](https://github.com/punkpeye/awesome-mcp-servers/commit/07e1820f00384702eae0815536c881fa83d7377d) Add Glama link for pmptwiki/pmpt-cli - raunplaymore
- [075cb67](https://github.com/punkpeye/awesome-mcp-servers/commit/075cb6708f3355a0a075e5d5a019047cb78c6a13) Add Glama listing link for flyto-core - Chester
- [e5f6872](https://github.com/punkpeye/awesome-mcp-servers/commit/e5f6872826123822e648b847797b38ed8a16bb84) Add pmptwiki/pmpt-cli to Developer Tools - raunplaymore
- [5e3233d](https://github.com/punkpeye/awesome-mcp-servers/commit/5e3233d1bdfe8adef82afe685b3ad7d2c4064c8c) Add Measure.events MCP Server with glama link - EC2 Default User
- [04229f1](https://github.com/punkpeye/awesome-mcp-servers/commit/04229f16c3a541b59f8afe734ed7f5e4e2437b59) fix: update entry with correct GitHub URL and add Glama badge - rplryan


##### File Content Changes

**README.md** (Modified, +10 -5 lines):

```diff
- - [pmptwiki/pmpt-cli](https://github.com/pmptwiki/pmpt-cli) 📇 🏠 - Record and share your AI-driven development journey. Auto-saves project milestones with summaries, generates structured AI prompts via 5-question planning, and publishes to [pmptwiki.com](https://pmptwiki.com) community platform.
- - [pmptwiki/pmpt-cli](https://github.com/pmptwiki/pmpt-cli) [glama](https://glama.ai/mcp/servers/@pmptwiki/pmpt-mcp) 📇 🏠 - Record and share your AI-driven development journey. Auto-saves project milestones with summaries, generates structured AI prompts via 5-question planning, and publishes to [pmptwiki.com](https://pmptwiki.com) community platform.
- - [flytohub/flyto-core](https://github.com/flytohub/flyto-core) 🐍 🏠 - Deterministic execution engine for AI agents with 412 modules across 78 categories (browser, file, Docker, data, crypto, scheduling). Features execution trace, evidence snapshots, replay from any step, and supports both STDIO and Streamable HTTP transport.
- - [rplryan/x402-discovery](https://github.com/rplryan/ouroboros/tree/ouroboros/agent_economy/discovery_api) 🐍 ☁️ - Runtime discovery layer for x402-payable APIs. Agents query to find pay-per-call endpoints by capability, get quality-ranked results (uptime%, latency, health), and pay $0.005 USDC per query via x402 — the discovery itself is x402-gated. Includes Python SDK, LangChain/LlamaIndex/AutoGen/CrewAI plugins on PyPI.
+ - [flytohub/flyto-core](https://github.com/flytohub/flyto-core) [glama](https://glama.ai/mcp/servers/@flytohub/flyto-core) 🐍 🏠 - Deterministic execution engine for AI agents with 412 modules across 78 categories (browser, file, Docker, data, crypto, scheduling). Features execution trace, evidence snapshots, replay from any step, and supports both STDIO and Streamable HTTP transport.
+ - [rplryan/x402-discovery-mcp](https://github.com/rplryan/x402-discovery-mcp) [glama](https://glama.ai/mcp/servers/@rplryan/x402-discovery-mcp) 🐍 ☁️ - Runtime discovery layer for x402-payable APIs. Agents discover and route to pay-per-call x402 endpoints by capability, get quality-ranked results with trust scores (0-100), and pay per query via x402. Includes MCP server, Python SDK, and CLI (npm install -g x402scout).
+ - [Turbo-Puffin/measure-mcp-server](https://github.com/Turbo-Puffin/measure-mcp-server) [glama](https://glama.ai/mcp/servers/@Turbo-Puffin/measure-mcp-server) ☁️ - Privacy-first web analytics with native MCP server. Query pageviews, referrers, trends, and AI-generated insights for your sites.
+ - [pmptwiki/pmpt-cli](https://github.com/pmptwiki/pmpt-cli) [glama](https://glama.ai/mcp/servers/@pmptwiki/pmpt-mcp) 📇 🏠 - Record and share your AI-driven development journey. Auto-saves project milestones with summaries, generates structured AI prompts via 5-question planning, and publishes to [pmptwiki.com](https://pmptwiki.com) community platform.
+ - [pmptwiki/pmpt-cli](https://github.com/pmptwiki/pmpt-cli) 📇 🏠 - Record and share your AI-driven development journey. Auto-saves project milestones with summaries, generates structured AI prompts via 5-question planning, and publishes to [pmptwiki.com](https://pmptwiki.com) community platform.
```



#### [Awesome-Dify-Workflow](https://github.com/svcvit/Awesome-Dify-Workflow)

##### Commit Changes

No file changes detected.

#### [system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools)

##### Commit Changes

- [dae78f5](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools/commit/dae78f56b04b760003f0cf83ce73908985bbe810) Update README.md - Lucas Valbuena


##### File Content Changes

**README.md** (Modified, +17 -17 lines):

```diff
- <sub>Special thanks to</sub>
- <td align="center" valign="top">
- <a href="https://www.tembo.io/?utm_source=github&utm_medium=readme&utm_campaign=prompt_repo_sponsorship#gh-light-mode-only" target="_blank">
- <img src="assets/tembo-dark.png#gh-light-mode-only" alt="Tembo Logo" width="750" height="210"/>
- </a>
- <a href="https://www.tembo.io/?utm_source=github&utm_medium=readme&utm_campaign=prompt_repo_sponsorship#gh-dark-mode-only" target="_blank">
- <img src="assets/tembo-light.png#gh-dark-mode-only" alt="Tembo Logo" width="750" height="210"/>
- <br><br>
- <strong><a href="https://www.tembo.io/?utm_source=github&utm_medium=readme&utm_campaign=prompt_repo_sponsorship" target="_blank">Put any coding agent to work while you sleep</a></strong>
- <br>
- <a href="https://www.tembo.io/?utm_source=github&utm_medium=readme&utm_campaign=prompt_repo_sponsorship" target="_blank">Tembo – The Background Coding Agents Company</a>
- <a href="https://www.tembo.io/?utm_source=github&utm_medium=readme&utm_campaign=prompt_repo_sponsorship" target="_blank">[Get started for free]</a>
- </td>
- <strong><a href="https://latitude.so/developers?utm_source=github&utm_medium=readme&utm_campaign=prompt_repo_sponsorship" target="_blank">Make your LLM predictable in production</a></strong>
- <a href="https://latitude.so/developers?utm_source=github&utm_medium=readme&utm_campaign=prompt_repo_sponsorship" target="_blank">Open Source AI Engineering Platform</a>
+ <p align="center">
+ ❤️ Love when open-source tools give back to open-source repos. Kilo Code is an AI coding agent with the system prompt, source code, and agent architecture all in the open on their GitHub repo.
+ <a href="https://github.com/Kilo-Org/kilocode">Let’s show them some love</a> ❤️
+ </p>
+ ---
+ <sub>Special thanks to</sub>
+ <strong>
+ <a href="https://latitude.so/developers?utm_source=github&utm_medium=readme&utm_campaign=prompt_repo_sponsorship" target="_blank">
+ Make your LLM predictable in production
+ </a>
+ </strong>
+ Open Source AI Engineering Platform
```



