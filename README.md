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

### 2026-04-03T02:12:52

#### [awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps)

##### Commit Changes

No file changes detected.

#### [awesome-gpt4o-images](https://github.com/jamez-bondos/awesome-gpt4o-images)

##### Commit Changes

No file changes detected.

#### [awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers)

##### Commit Changes

- [9fb2f7d](https://github.com/punkpeye/awesome-mcp-servers/commit/9fb2f7d654e3cdfd2be8a1a0b40f03b62a9c155c) Merge pull request #3709 from eyloni/add-pythia-oracle - Frank Fiegel
- [0232c37](https://github.com/punkpeye/awesome-mcp-servers/commit/0232c3761cdce40aade1336f6bab08ed4658fc82) Merge pull request #3834 from ndjordjevic/add-ndjordjevic-pinrag - Frank Fiegel
- [113071d](https://github.com/punkpeye/awesome-mcp-servers/commit/113071d8d580fb236d78b0f0365773aba26f9e0b) Merge pull request #3845 from kimimgo/add-viznoir - Frank Fiegel
- [5df6251](https://github.com/punkpeye/awesome-mcp-servers/commit/5df62510ea4760a6047010c1969a1acff99c580a) Merge pull request #3877 from paladini/add-devutils-mcp-server - Frank Fiegel
- [066d217](https://github.com/punkpeye/awesome-mcp-servers/commit/066d217a43d7276f5b503fbf620e490a9c584da5) Merge pull request #3400 from fjnunezp75/add-gpu-bridge - Frank Fiegel
- [73c6115](https://github.com/punkpeye/awesome-mcp-servers/commit/73c6115620df41d51c5c3955074483bfd4e4b3df) Merge pull request #3850 from runtimeguard/add-runtime-guard - Frank Fiegel
- [7756542](https://github.com/punkpeye/awesome-mcp-servers/commit/77565421fb47d756d94fa3f5c7c5e56fb32eb41b) Merge pull request #3832 from AceDataCloud/add-mcp-shorturl - Frank Fiegel
- [18c217a](https://github.com/punkpeye/awesome-mcp-servers/commit/18c217a2708329bb234649e8a7f4c7ce250acf45) Merge pull request #4027 from achiya-automation/add-safari-mcp - Frank Fiegel
- [8dd7d3f](https://github.com/punkpeye/awesome-mcp-servers/commit/8dd7d3f16b96094517a17fca805291b41f18a161) Merge pull request #2347 from benswel/add-qr-for-agent - Frank Fiegel
- [5e75b74](https://github.com/punkpeye/awesome-mcp-servers/commit/5e75b7403f1d77b1c8f1beba1bfff2f3686ac677) Merge pull request #4031 from nk3750/add-jitapi - Frank Fiegel


##### File Content Changes

**README.md** (Modified, +10 -0 lines):

```diff
+ - [eyloni/pythia-oracle](https://github.com/eyloni/pythia-oracle) [![pythia-oracle MCP server](https://glama.ai/mcp/servers/eyloni/pythia-oracle/badges/score.svg)](https://glama.ai/mcp/servers/eyloni/pythia-oracle) 🐍 ☁️ - Oracle for AI agents that need to think past obvious answers. One tool, one reading. Free tier included.
+ - [ndjordjevic/pinrag](https://github.com/ndjordjevic/pinrag) [![ndjordjevic/pinrag MCP server](https://glama.ai/mcp/servers/ndjordjevic/pinrag/badges/score.svg)](https://glama.ai/mcp/servers/ndjordjevic/pinrag) 🐍 🏠 - RAG for PDFs, YouTube, GitHub repos, Discord exports; index documents and query with citations.
+ - [kimimgo/viznoir](https://github.com/kimimgo/viznoir) [![viznoir MCP server](https://glama.ai/mcp/servers/kimimgo/viznoir/badges/score.svg)](https://glama.ai/mcp/servers/kimimgo/viznoir) 🐍 🏠 🐧 - Cinema-quality science visualization MCP server for CFD/FEA/SPH. 22 tools for rendering, slicing, contouring, volume rendering, and animating OpenFOAM/VTK/CGNS data. Headless EGL/OSMesa.
+ - [paladini/devutils-mcp-server](https://github.com/paladini/devutils-mcp-server) [![paladini/devutils-mcp-server MCP server](https://glama.ai/mcp/servers/paladini/devutils-mcp-server/badges/score.svg)](https://glama.ai/mcp/servers/paladini/devutils-mcp-server) 📇 🏠 🍎 🪟 🐧 - 36 zero-auth developer utilities: MD5/SHA/bcrypt hashing, Base64/hex/URL encoding, UUID/password/passphrase generation, JWT decoding, JSON/YAML/XML formatting, timestamp conversion, CIDR calculator, and text tools.
+ - [gpu-bridge/mcp-server](https://github.com/gpu-bridge/mcp-server) [![gpu-bridge-mcp-server MCP server](https://glama.ai/mcp/servers/gpu-bridge/mcp-server/badges/score.svg)](https://glama.ai/mcp/servers/gpu-bridge/mcp-server) 📇 ☁️ 🍎 🪟 🐧 - Unified GPU inference API with 30 AI services (LLM, image gen, video, TTS, whisper, embeddings, reranking, OCR) as MCP tools. Pay-per-use via x402 USDC or API key credits.
+ - [jimmyracheta/AI-Runtime-Guard](https://github.com/runtimeguard/runtime-guard)[![runtime-guard MCP server](https://glama.ai/mcp/servers/runtimeguard/runtime-guard/badges/score.svg)](https://glama.ai/mcp/servers/runtimeguard/runtime-guard)🐍 🏠🍎 🪟 - Runtime policy enforcement for AI agents - prevents accidental damage to your systems, unauthorized agent access and automates backup-before-write for any touched files.
+ - [AceDataCloud/MCPShortURL](https://github.com/AceDataCloud/MCPShortURL) [![AceDataCloud/MCPShortURL MCP server](https://glama.ai/mcp/servers/AceDataCloud/MCPShortURL/badges/score.svg)](https://glama.ai/mcp/servers/AceDataCloud/MCPShortURL) 🐍 ☁️ - Free URL shortening with batch support (up to 10 URLs), permanent `surl.id` short links, zero credit consumption.
+ - [achiya-automation/safari-mcp](https://github.com/achiya-automation/safari-mcp) [![safari-mcp MCP server](https://glama.ai/mcp/servers/achiya-automation/safari-mcp/badges/score.svg)](https://glama.ai/mcp/servers/achiya-automation/safari-mcp) 📇 🏠 🍎 - Native Safari browser automation for AI agents with 80+ tools. No Chrome dependency, optimized for Apple Silicon with 60% less CPU overhead.
+ - [benswel/qr-agent-core](https://github.com/benswel/qr-agent-core) [![benswel/qr-agent-core MCP server](https://glama.ai/mcp/servers/benswel/qr-agent-core/badges/score.svg)](https://glama.ai/mcp/servers/benswel/qr-agent-core) 📇 ☁️ - Dynamic QR code service for AI agents. Create, update, track, and retarget QR codes without regenerating images. 37 tools covering 11 QR types, one-command install via `npx qr-for-agent`.
+ - [nk3750/jitapi](https://github.com/nk3750/jitapi) [![nk3750/jitapi MCP server](https://glama.ai/mcp/servers/nk3750/jitapi/badges/score.svg)](https://glama.ai/mcp/servers/nk3750/jitapi) 🐍 ☁️ 🏠 🍎 🪟 🐧 - Dynamic API discovery and execution from OpenAPI specs. Uses semantic search and dependency graphs to find relevant endpoints across multiple registered APIs, plan multi-step workflows, and execute API calls — without dumping entire specs into context.
```



#### [Awesome-Dify-Workflow](https://github.com/svcvit/Awesome-Dify-Workflow)

##### Commit Changes

No file changes detected.

#### [system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools)

##### Commit Changes

No file changes detected.

