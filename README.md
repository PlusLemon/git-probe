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

### 2026-10-09T04:41:45

#### [awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps)

##### Commit Changes

No file changes detected.

#### [awesome-gpt4o-images](https://github.com/jamez-bondos/awesome-gpt4o-images)

##### Commit Changes

No file changes detected.

#### [awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers)

##### Commit Changes

- [f105299](https://github.com/punkpeye/awesome-mcp-servers/commit/f105299ee206f1a86cccd2e7d51363fbc6eab84d) Merge pull request #14510 from michal-wrzosek/add-gitwarren - Frank Fiegel
- [b29ce7a](https://github.com/punkpeye/awesome-mcp-servers/commit/b29ce7ad983997ea902f6bdf5ca5cc5db1e76c7f) Merge pull request #11576 from XZXZZX-Ai/codex/add-bilibili-mcp - Frank Fiegel
- [833a9af](https://github.com/punkpeye/awesome-mcp-servers/commit/833a9af322fbfc72b3c2270c5c3d2f6297ee2d0b) Merge pull request #15722 from tunahanaliozturk/add-derbent - Frank Fiegel
- [12c572e](https://github.com/punkpeye/awesome-mcp-servers/commit/12c572ead75fa69eba9e974a69c859d5e72f276c) Merge pull request #15634 from Scormave/codex/add-gramps-web-mcp - Frank Fiegel
- [f78f401](https://github.com/punkpeye/awesome-mcp-servers/commit/f78f40115b1521539a8227dc215c3417bf775886) Merge pull request #8652 from PattrickChenforclaudeuse/add-mythsensus-mcp - Frank Fiegel
- [f8a4fde](https://github.com/punkpeye/awesome-mcp-servers/commit/f8a4fde0dc79f85b4005e41334037c4ec8627caa) Merge pull request #12882 from M-T-D-N/patch-1 - Frank Fiegel
- [8b6dc62](https://github.com/punkpeye/awesome-mcp-servers/commit/8b6dc62ff04beceed27aee1782373716caed31a5) Merge pull request #15301 from Philongevity/patch-1 - Frank Fiegel
- [115aaf0](https://github.com/punkpeye/awesome-mcp-servers/commit/115aaf09a2d0fdb2eb2362183588a84bf380d73b) Merge pull request #15498 from phetzy/add-osnova - Frank Fiegel
- [081dc49](https://github.com/punkpeye/awesome-mcp-servers/commit/081dc4934e7b8f36ba0a7341e1d545349687a4cd) Merge pull request #15284 from engineerdeep/patch-1 - Frank Fiegel
- [1f13b24](https://github.com/punkpeye/awesome-mcp-servers/commit/1f13b24a61e407adcd9e417f27fe65cb95cf2ba6) Merge pull request #15516 from Gatyh/add-3dtexel - Frank Fiegel


##### File Content Changes

**README.md** (Modified, +10 -0 lines):

```diff
+ - [klarluft/gitwarren-app](https://github.com/klarluft/gitwarren-app) [![klarluft/gitwarren-app MCP server](https://glama.ai/mcp/servers/klarluft/gitwarren-app/badges/score.svg)](https://glama.ai/mcp/servers/klarluft/gitwarren-app) 🎖️ 📇 🏠 🍎 🪟 🐧 - Local code review for you and your coding agent: the agent opens a review of its changes, you comment on lines, it replies and resolves. Reads the git worktree directly, uncommitted work included; nothing leaves your machine.
+ - [XZXZZX-Ai/bilibili-mcp](https://github.com/XZXZZX-Ai/bilibili-mcp) [![XZXZZX-Ai/bilibili-mcp MCP server](https://glama.ai/mcp/servers/XZXZZX-Ai/bilibili-mcp/badges/score.svg)](https://glama.ai/mcp/servers/XZXZZX-Ai/bilibili-mcp) 📇 🏠 🍎 🪟 🐧 - Local-first Bilibili MCP server for video metadata, subtitles and structured transcripts, chapters, popular comments, and optional local ASR fallback. Published on npm as `@xzxzzx/bilibili-mcp` with bilingual documentation.
+ - [tunahanaliozturk/derbent](https://github.com/tunahanaliozturk/derbent) [![tunahanaliozturk/derbent MCP server](https://glama.ai/mcp/servers/tunahanaliozturk/derbent/badges/score.svg)](https://glama.ai/mcp/servers/tunahanaliozturk/derbent) 🏎️ 🏠 🍎 🪟 🐧 - One local gate for Claude Code, Codex, Copilot CLI and Antigravity: allow, deny and ask rules over MCP and built-in tool calls, approvals from a terminal UI, and hash-chained receipts.
+ - [Scormave/gramps-web-mcp](https://github.com/Scormave/gramps-web-mcp) [![Scormave/gramps-web-mcp MCP server](https://glama.ai/mcp/servers/Scormave/gramps-web-mcp/badges/score.svg)](https://glama.ai/mcp/servers/Scormave/gramps-web-mcp) #️⃣ 🏠 🍎 🪟 🐧 - Gramps Web genealogy: search and edit family tree records, explore ancestors, descendants, relationships and timelines, and read media with privacy-aware previews. Includes a read-only mode and Claude Desktop bundles.
+ - [PattrickChenforclaudeuse/mythsensus-mcp](https://github.com/PattrickChenforclaudeuse/mythsensus-mcp) [![PattrickChenforclaudeuse/mythsensus-mcp MCP server](https://glama.ai/mcp/servers/PattrickChenforclaudeuse/mythsensus-mcp/badges/score.svg)](https://glama.ai/mcp/servers/PattrickChenforclaudeuse/mythsensus-mcp) 📇 🏠 🍎 🪟 🐧 - Synthesizes 26 ancient divination systems (BaZi, Vedic Jyotish, Western, Nine Star Ki, Thai Seven Number, Mayan, Norse Runes, Human Design and 18 more) into a single consensus Cosmic Score showing where the traditions agree vs contradict. Deterministic (no LLM in the math), fully local — no birth data leaves the process. Official MCP for mythsensus.com. Install: `npx -y mythsensus-mcp`.
+ - [M-T-D-N/agentmemory-codex-windows](https://github.com/M-T-D-N/agentmemory-codex-windows) [![M-T-D-N/agentmemory-codex-windows MCP server](https://glama.ai/mcp/servers/M-T-D-N/agentmemory-codex-windows/badges/score.svg)](https://glama.ai/mcp/servers/M-T-D-N/agentmemory-codex-windows) 📇 🏠 🪟 - Windows AgentMemory downstream for Codex with project-scoped persistent memory, bounded cross-project recall, and an authenticated loopback MCP service; prebuilt Windows releases are available as an unsigned Technical Preview.
+ - [Philongevity/phi-mcp-server](https://github.com/Philongevity/phi-mcp-server) [![Philongevity/phi-mcp-server MCP server](https://glama.ai/mcp/servers/Philongevity/phi-mcp-server/badges/score.svg)](https://glama.ai/mcp/servers/Philongevity/phi-mcp-server) 📇 ☁️ - Guideline-cited lab-results analysis for chronic conditions (type 2 diabetes, kidney, lupus, cancer survivorship): flags missing or overdue tests with the guideline cited. Free sample report; synthetic/de-identified values only.
+ - [getdomovoi/osnova](https://github.com/getdomovoi/osnova) [![getdomovoi/osnova MCP server](https://glama.ai/mcp/servers/getdomovoi/osnova/badges/score.svg)](https://glama.ai/mcp/servers/getdomovoi/osnova) 📇 🏠 🍎 🪟 🐧 - Deterministic code map for AI coding agents: a tree-sitter symbol and call graph with exact file:line callers and callees, the evidence behind each edge, diff impact and test discovery across 20 languages.
+ - [engineerdeep/buildtree-mcp](https://github.com/engineerdeep/buildtree-mcp) [![engineerdeep/buildtree-mcp MCP server](https://glama.ai/mcp/servers/engineerdeep/buildtree-mcp/badges/score.svg)](https://glama.ai/mcp/servers/engineerdeep/buildtree-mcp) 📇 ☁️ 🏠 🍎 🪟 🐧 - Share Android and iOS builds with testers: detects Expo, React Native or Flutter, runs the build, uploads the .apk or .ipa to buildtree, and returns install links, a QR code image and tester feedback.
+ - [Gatyh/3dtexel-mcp](https://github.com/Gatyh/3dtexel-mcp) [![Gatyh/3dtexel-mcp MCP server](https://glama.ai/mcp/servers/Gatyh/3dtexel-mcp/badges/score.svg)](https://glama.ai/mcp/servers/Gatyh/3dtexel-mcp) 🎖️ 📇 ☁️ - Official 3D Texel server: search and download 7,000+ PBR materials, HDRIs, decals and 3D assets (1,600+ free CC0) and generate seamless PBR materials and HDRI skyboxes with credits.
```



#### [Awesome-Dify-Workflow](https://github.com/svcvit/Awesome-Dify-Workflow)

##### Commit Changes

No file changes detected.

#### [system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools)

##### Commit Changes

No file changes detected.

