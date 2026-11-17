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

### 2026-11-17T06:40:14

#### [awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps)

##### Commit Changes

No file changes detected.

#### [awesome-gpt4o-images](https://github.com/jamez-bondos/awesome-gpt4o-images)

##### Commit Changes

No file changes detected.

#### [awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers)

##### Commit Changes

- [5fb385c](https://github.com/punkpeye/awesome-mcp-servers/commit/5fb385c3c56a004eacad6a21cb446205c787926b) Merge pull request #19103 from tl-sl/add-zerostack-mcp - Frank Fiegel
- [50fe60e](https://github.com/punkpeye/awesome-mcp-servers/commit/50fe60e4fe128aaa83aa7072746cb396d6477e71) Merge pull request #19570 from Dinoctor/add-dinoctor - Frank Fiegel
- [7bafd92](https://github.com/punkpeye/awesome-mcp-servers/commit/7bafd92b2c5c04b7ecaac454b6e66758bbaaad7d) Merge pull request #19129 from mambabuilt/add-mcp-dutch-rental-listings - Frank Fiegel
- [ffaf57c](https://github.com/punkpeye/awesome-mcp-servers/commit/ffaf57ca293d36651e4d214d648937b0eee398f8) Merge pull request #15468 from robyroro/add-personamcp - Frank Fiegel
- [3311a8e](https://github.com/punkpeye/awesome-mcp-servers/commit/3311a8ed89f1a5e186a2b2b6c823b1411be2b651) Merge pull request #18029 from Stefan39/patch-1 - Frank Fiegel
- [f03458c](https://github.com/punkpeye/awesome-mcp-servers/commit/f03458c7e0f71ca87562a88be87dd306f3dde310) Fix entry formatting - Frank Fiegel
- [96fc17a](https://github.com/punkpeye/awesome-mcp-servers/commit/96fc17ac3900b7dfd0cd8f3f0c3e59986cfde344) Merge pull request #16212 from seanebones-lang/codex/add-deadbolt - Frank Fiegel
- [0979edb](https://github.com/punkpeye/awesome-mcp-servers/commit/0979edb3d40980edb189c6502835ead60ed377d7) Merge pull request #15469 from seungmiyoon/add-korean-tax-mcp - Frank Fiegel
- [9f32e65](https://github.com/punkpeye/awesome-mcp-servers/commit/9f32e65fb50bf47e7a7db985b0b749521575108d) Merge pull request #18153 from neilmorse/codex/add-spring-runtime-mcp - Frank Fiegel
- [eab24ec](https://github.com/punkpeye/awesome-mcp-servers/commit/eab24ecfdd7a0f7a7291aa74d7b9002f46eabc01) Merge pull request #16456 from pattalkslaw-del/add-tremelay - Frank Fiegel


##### File Content Changes

**README.md** (Modified, +10 -2 lines):

```diff
- - [seanebones-lang/deadbolt](https://github.com/seanebones-lang/deadbolt) 🦀 🏠 🍎 🪟 🐧 - Local stdio MCP proxy that checks policy before forwarding tool calls, with expiring leases, operator approval, kill controls and decision records. Protects routed tool calls; the child server remains trusted. [![seanebones-lang/deadbolt MCP server](https://glama.ai/mcp/servers/seanebones-lang/deadbolt/badges/score.svg)](https://glama.ai/mcp/servers/seanebones-lang/deadbolt)
+ - [zerostack-rf/zerostack-mcp](https://github.com/zerostack-rf/zerostack-mcp) [![zerostack-rf/zerostack-mcp MCP server](https://glama.ai/mcp/servers/zerostack-rf/zerostack-mcp/badges/score.svg)](https://glama.ai/mcp/servers/zerostack-rf/zerostack-mcp) 🎖️ 🐍 🏠 📟 🍎 🪟 🐧 - Deterministic root-cause diagnostics for Zigbee2MQTT, Home Assistant ZHA, OpenThread, and IEEE 802.15.4 logs, silicon register decoding for TI SimpleLink F2 and Silicon Labs EFR32 coordinators, mesh capacity checks, and `DWT->CYCCNT` benchmarks.
+ - [Dinoctor/dinoctor-mcp](https://github.com/Dinoctor/dinoctor-mcp) [![Dinoctor/dinoctor-mcp MCP server](https://glama.ai/mcp/servers/Dinoctor/dinoctor-mcp/badges/score.svg)](https://glama.ai/mcp/servers/Dinoctor/dinoctor-mcp) 📇 🏠 🍎 🪟 - Make animated videos in the free Dinoctor desktop app while you watch: write the script, build scenes and shots with places, characters, camera moves, lighting and transitions, add voice and music, and render an MP4. Open-source stdio server (`npx -y dinoctor-mcp`); paid AI steps ask before spending credits.
+ - [mambalabsdev/mcp-dutch-rental-listings](https://github.com/mambalabsdev/mcp-dutch-rental-listings) [![mambalabsdev/mcp-dutch-rental-listings MCP server](https://glama.ai/mcp/servers/mambalabsdev/mcp-dutch-rental-listings/badges/score.svg)](https://glama.ai/mcp/servers/mambalabsdev/mcp-dutch-rental-listings) 📇 ☁️ - Netherlands rental listings from Kamernet, HousingAnywhere, and anti-squat agencies
+ - [robyroro/PersonaMCP](https://github.com/robyroro/PersonaMCP) [![robyroro/PersonaMCP MCP server](https://glama.ai/mcp/servers/robyroro/PersonaMCP/badges/score.svg)](https://glama.ai/mcp/servers/robyroro/PersonaMCP) 🐍 🏠 🪟 🐧 - Local-first communication memory: imports your chat exports, measures how you write and gives agents a style profile plus relevant past replies. Raw history never leaves your machine.
+ - [Stefan39/mite-mcp-server](https://github.com/Stefan39/mite-mcp-server) [![Stefan39/mite-mcp-server MCP server](https://glama.ai/mcp/servers/Stefan39/mite-mcp-server/badges/score.svg)](https://glama.ai/mcp/servers/Stefan39/mite-mcp-server) 📇 ☁️ 🍎 🪟 🐧 - mite time tracking: hours and revenue reports aggregated on the mite server (per project and month, budgets, billable ratio), time entries, tracker and master data. Read-only by default; writing is opt-in, deletes need a confirmation token.
+ - [seanebones-lang/deadbolt](https://github.com/seanebones-lang/deadbolt) [![seanebones-lang/deadbolt MCP server](https://glama.ai/mcp/servers/seanebones-lang/deadbolt/badges/score.svg)](https://glama.ai/mcp/servers/seanebones-lang/deadbolt) 🦀 🏠 🍎 🪟 🐧 - Local stdio MCP proxy that checks policy before forwarding tool calls, with expiring leases, operator approval, kill controls and decision records. Protects routed tool calls; the child server remains trusted.
+ - [seanebones-lang/deadbolt](https://github.com/seanebones-lang/deadbolt) 🦀 🏠 🍎 🪟 🐧 - Local stdio MCP proxy that checks policy before forwarding tool calls, with expiring leases, operator approval, kill controls and decision records. Protects routed tool calls; the child server remains trusted. [![seanebones-lang/deadbolt MCP server](https://glama.ai/mcp/servers/seanebones-lang/deadbolt/badges/score.svg)](https://glama.ai/mcp/servers/seanebones-lang/deadbolt)
+ - [seungmiyoon/korean-tax-mcp](https://github.com/seungmiyoon/korean-tax-mcp) [![seungmiyoon/korean-tax-mcp MCP server](https://glama.ai/mcp/servers/seungmiyoon/korean-tax-mcp/badges/score.svg)](https://glama.ai/mcp/servers/seungmiyoon/korean-tax-mcp) 🐍 ☁️ 🍎 🪟 🐧 - Korean tax law sources: National Tax Service rulings, court and Tax Tribunal decisions, basic rules, execution standards, and point-in-time statutes with Act → Decree → Rule delegation.
+ - [neilmorse/spring-runtime-mcp](https://github.com/neilmorse/spring-runtime-mcp) [![neilmorse/spring-runtime-mcp MCP server](https://glama.ai/mcp/servers/neilmorse/spring-runtime-mcp/badges/score.svg)](https://glama.ai/mcp/servers/neilmorse/spring-runtime-mcp) 🐍 🏠 - Read-only Spring Boot runtime diagnostics: beans and conditions, routes, health, migrations, startup, config origin, OpenAPI and drift. Loopback-only, sanitized, bounded responses.
+ - [CharitonMedia/Tremelay](https://github.com/CharitonMedia/Tremelay) [![CharitonMedia/Tremelay MCP server](https://glama.ai/mcp/servers/CharitonMedia/Tremelay/badges/score.svg)](https://glama.ai/mcp/servers/CharitonMedia/Tremelay) 🏎️ 🏠 🍎 🪟 🐧 - Local credential broker: keep API keys and SSH keys in an encrypted vault on your own machine and let agents use them over MCP without ever receiving the raw secret. Scoped, expiring, revocable grants, deny by default, hash-chained audit log.
```



#### [Awesome-Dify-Workflow](https://github.com/svcvit/Awesome-Dify-Workflow)

##### Commit Changes

No file changes detected.

#### [system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools)

##### Commit Changes

No file changes detected.

