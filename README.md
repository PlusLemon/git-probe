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

### 2026-09-23T03:27:18

#### [awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps)

##### Commit Changes

No file changes detected.

#### [awesome-gpt4o-images](https://github.com/jamez-bondos/awesome-gpt4o-images)

##### Commit Changes

No file changes detected.

#### [awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers)

##### Commit Changes

- [fbc52bc](https://github.com/punkpeye/awesome-mcp-servers/commit/fbc52bcf301a3468954f6ee4fd12b75b853c93cf) Merge pull request #14766 from bricelancasterwcp-sudo/add-sensorium - Frank Fiegel
- [85e7914](https://github.com/punkpeye/awesome-mcp-servers/commit/85e7914d973bcfeb4fcd2987a864bbf6059424fc) Merge pull request #14361 from sergey-ermakovich/add-hasdata-facebook - Frank Fiegel
- [978a2f3](https://github.com/punkpeye/awesome-mcp-servers/commit/978a2f38d219cfd31a6f058922500f6f2023fec7) Merge pull request #14788 from TheoV823/codex/add-mneme-decision-mcp - Frank Fiegel
- [d1f4202](https://github.com/punkpeye/awesome-mcp-servers/commit/d1f4202d5b7df67582f105415b71cd59e40f6ce0) Merge pull request #14871 from mambabuilt/add-mcp-review-platform-reputation-enricher - Frank Fiegel
- [35adbef](https://github.com/punkpeye/awesome-mcp-servers/commit/35adbef9c5a86737e52c26d78f38fafb538d7d9d) Merge pull request #14779 from dhawalshah/add-dhawalshah-tiktok-ads-mcp - Frank Fiegel
- [f4fb6cd](https://github.com/punkpeye/awesome-mcp-servers/commit/f4fb6cd586c3a93af4c0295399d323951db65dda) Add mambalabsdev/mcp-review-platform-reputation-enricher - Mamba Labs


##### File Content Changes

**README.md** (Modified, +6 -0 lines):

```diff
+ - [bricelancasterwcp-sudo/sensorium](https://github.com/bricelancasterwcp-sudo/sensorium) [![bricelancasterwcp-sudo/sensorium MCP server](https://glama.ai/mcp/servers/bricelancasterwcp-sudo/sensorium/badges/score.svg)](https://glama.ai/mcp/servers/bricelancasterwcp-sudo/sensorium) 🐍 🦀 📇 🏠 🐧 - Record Python/Rust/TypeScript program runs to local SQLite; query call trees, exceptions, and value flow over MCP (refuses rather than guesses). Local-first for coding agents — not LLM-prompt tracing; not the unrelated Telegram `sensorium-mcp`.
+ - [HasData/facebook-mcp](https://github.com/HasData/facebook-mcp) [![HasData/facebook-mcp MCP server](https://glama.ai/mcp/servers/HasData/facebook-mcp/badges/score.svg)](https://glama.ai/mcp/servers/HasData/facebook-mcp) 📇 ☁️ - Remote MCP server for public Facebook pages and profiles: likes, followers, talking-about counts, contact details and the post feed with reactions, as JSON.
+ - [MnemeHQ/mneme](https://github.com/MnemeHQ/mneme) [![Mneme Decision MCP server](https://glama.ai/mcp/servers/MnemeHQ/mneme/badges/score.svg)](https://glama.ai/mcp/servers/MnemeHQ/mneme) 🐍 📇 🏠 🍎 🪟 🐧 - Deterministic architectural decision governance for agentic software development. Six local stdio tools let agents submit non-authoritative proposals and query canonical decisions, applicability, and lineage while human acceptance and enforcement authority remain outside the MCP surface. `uvx --from "mneme-hq[mcp]==0.9.1" mneme decision-mcp`
+ - [mambalabsdev/mcp-review-platform-reputation-enricher](https://github.com/mambalabsdev/mcp-review-platform-reputation-enricher) [![mambalabsdev/mcp-review-platform-reputation-enricher MCP server](https://glama.ai/mcp/servers/mambalabsdev/mcp-review-platform-reputation-enricher/badges/score.svg)](https://glama.ai/mcp/servers/mambalabsdev/mcp-review-platform-reputation-enricher) 📇 ☁️ - Resolves a company domain to its Trustpilot rating, review count, and claimed status.
+ - [dhawalshah/tiktok-ads-mcp](https://github.com/dhawalshah/tiktok-ads-mcp) [![dhawalshah/tiktok-ads-mcp MCP server](https://glama.ai/mcp/servers/dhawalshah/tiktok-ads-mcp/badges/score.svg)](https://glama.ai/mcp/servers/dhawalshah/tiktok-ads-mcp) 🐍 ☁️ - TikTok Ads MCP server with video performance metrics, creative fatigue scoring, industry benchmarks, and Smart+ campaign support.
```



#### [Awesome-Dify-Workflow](https://github.com/svcvit/Awesome-Dify-Workflow)

##### Commit Changes

No file changes detected.

#### [system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools)

##### Commit Changes

No file changes detected.

