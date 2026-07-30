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

### 2026-07-30T02:13:42

#### [awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps)

##### Commit Changes

No file changes detected.

#### [awesome-gpt4o-images](https://github.com/jamez-bondos/awesome-gpt4o-images)

##### Commit Changes

No file changes detected.

#### [awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers)

##### Commit Changes

- [375407c](https://github.com/punkpeye/awesome-mcp-servers/commit/375407c7290dd99d305938983f37adffa9d44275) Merge pull request #10893 from marccrutzen269-lab/add-departi-v2 - Frank Fiegel
- [9a6239e](https://github.com/punkpeye/awesome-mcp-servers/commit/9a6239e018b7168b5106834da989886a178c3b6a) Merge pull request #11068 from Alepha188838884/add-context-firewall - Frank Fiegel
- [706ef89](https://github.com/punkpeye/awesome-mcp-servers/commit/706ef898ea9ba14ca3d5b1dcafbd235976e4110b) Merge pull request #10561 from khrystynaDal/patch-1 - Frank Fiegel
- [8855694](https://github.com/punkpeye/awesome-mcp-servers/commit/8855694329fb63126788f724f157ac9c701b6142) Update drawing-converter-mcp entry in README - khrystynaDal
- [00fe496](https://github.com/punkpeye/awesome-mcp-servers/commit/00fe496716040e3cc6d5808ea9d5dcdb213d279c) Merge pull request #11011 from gerard-kanters/cursor/add-mcp-linux-tools-88ed - Frank Fiegel


##### File Content Changes

**README.md** (Modified, +5 -1 lines):

```diff
- - [imnoo-team/drawing-converter-mcp](https://github.com/imnoo-team/drawing-converter-mcp) 📇 🏠 🍎 🪟 🐧 - Convert technical-drawing PDFs and engineering callouts between metric and imperial — dimensions, ± tolerances, ISO fit classes, M⇄UNC threads, surface roughness — with converted values stamped in place on the PDF. Install via NPM: `npx -y drawing-converter-mcp`
+ - [Departi/mcp-server](https://github.com/Departi/mcp-server) [![Departi/mcp-server MCP server](https://glama.ai/mcp/servers/Departi/mcp-server/badges/score.svg)](https://glama.ai/mcp/servers/Departi/mcp-server) ☁️ - Travel compliance and curated booking for digital nomads — visa requirements, tax residency analysis, Schengen 90/180-day tracking, accommodation, transport, and experiences across 189 European destinations. Hosted at https://mcp.departi.eu/v3 (Streamable HTTP, OAuth 2.1).
+ - [Alepha188838884/context-firewall](https://github.com/Alepha188838884/context-firewall) [![Alepha188838884/context-firewall MCP server](https://glama.ai/mcp/servers/Alepha188838884/context-firewall/badges/score.svg)](https://glama.ai/mcp/servers/Alepha188838884/context-firewall) 📇 🏠 🍎 🪟 🐧 - Local proxy that collapses N downstream MCP servers into 4 meta-tools with progressive tool discovery (measured: 122 tools → 4, ~28.6K tokens of definitions saved), compresses large tool outputs (HTML→Markdown, JSON structure summarization, base64 stripping — 60–95% measured on real pages/APIs) with full-output retrieval via `read_more`, and prints a per-session token-savings report. Security-relevant outputs are never silently compressed. Install: `npx -y context-firewall --config config.json`
+ - [imnoo-team/drawing-converter-mcp](https://github.com/imnoo-team/drawing-converter-mcp) [![drawing-converter-mcp MCP server](https://glama.ai/mcp/servers/imnoo-team/drawing-converter-mcp/badges/score.svg)](https://glama.ai/mcp/servers/imnoo-team/drawing-converter-mcp) 📇 🏠 🍎 🪟 🐧 - Convert technical-drawing PDFs and engineering callouts between metric and imperial — dimensions, ± tolerances, ISO fit classes, M⇄UNC threads, surface roughness — with converted values stamped in place on the PDF. Install via NPM: `npx -y drawing-converter-mcp`
+ - [gerard-kanters/mcp-linux-tools](https://github.com/gerard-kanters/mcp-linux-tools) [![gerard-kanters/mcp-linux-tools MCP server](https://glama.ai/mcp/servers/gerard-kanters/mcp-linux-tools/badges/score.svg)](https://glama.ai/mcp/servers/gerard-kanters/mcp-linux-tools) 🐍 🏠 🐧 - Administer a Linux server from an MCP client such as Cursor or VS Code: read files and tail logs, check/reload/restart systemd services, manage cron jobs inside a dedicated crontab section, run read-only MySQL queries, drive WP-CLI on WordPress sites, run safe Git commands, and execute sandboxed Python. Directories, services and WordPress sites are allowlisted in `config.json`, and every tool returns a uniform `{success, data, error, meta}` response. Runs as a systemd service over HTTP.
```



#### [Awesome-Dify-Workflow](https://github.com/svcvit/Awesome-Dify-Workflow)

##### Commit Changes

No file changes detected.

#### [system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools)

##### Commit Changes

No file changes detected.

