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

### 2026-06-20T03:35:24

#### [awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps)

##### Commit Changes

No file changes detected.

#### [awesome-gpt4o-images](https://github.com/jamez-bondos/awesome-gpt4o-images)

##### Commit Changes

No file changes detected.

#### [awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers)

##### Commit Changes

- [e47d4dd](https://github.com/punkpeye/awesome-mcp-servers/commit/e47d4ddc7334f436a5705eaab9ab57cc576f1286) Merge pull request #8306 from baodq06/add-memocall - Frank Fiegel
- [04c0e22](https://github.com/punkpeye/awesome-mcp-servers/commit/04c0e220f50bfd731971e7973d89053e09cc5a11) Merge pull request #8351 from tushariitr-19/add-immigration-mcp - Frank Fiegel
- [caaf9ff](https://github.com/punkpeye/awesome-mcp-servers/commit/caaf9ffda46403b59f643ae614ca16d980cb6303) Merge pull request #8346 from tushariitr-19/add-patents-mcp - Frank Fiegel
- [1b718f1](https://github.com/punkpeye/awesome-mcp-servers/commit/1b718f1cafe5ea3faadcc1728aa4ea9b971b3fc9) Fix entry formatting - Frank Fiegel
- [c23b825](https://github.com/punkpeye/awesome-mcp-servers/commit/c23b8256b789ed1603dcd520f35fc980cbaa6c9c) Merge pull request #8348 from kristaffa/patch-5 - Frank Fiegel
- [38de97a](https://github.com/punkpeye/awesome-mcp-servers/commit/38de97a6e08d4de19478e02592bc03c5fe302dfe) Fix entry formatting - Frank Fiegel
- [f6e6420](https://github.com/punkpeye/awesome-mcp-servers/commit/f6e64204c7a14ee49d15734a3ec496b6520c66d4) Merge pull request #8358 from xfloukiex-lab/add-laugh-tale - Frank Fiegel
- [7145625](https://github.com/punkpeye/awesome-mcp-servers/commit/7145625ed125c873215490c395b6855cb2bce649) Fix entry formatting - Frank Fiegel
- [3d6d9e4](https://github.com/punkpeye/awesome-mcp-servers/commit/3d6d9e41f5d33afd62a9590a664fccbab3106666) Merge pull request #8354 from kristaffa/patch-8 - Frank Fiegel
- [08a70c2](https://github.com/punkpeye/awesome-mcp-servers/commit/08a70c23ebc5e4abcdfce7a9733eff90f12a49ad) Fix entry formatting - Frank Fiegel


##### File Content Changes

**README.md** (Modified, +10 -4 lines):

```diff
- - [qinisolabs/floodwise](https://github.com/qinisolabs/floodwise) 📇 🏠 - England flood-risk by postcode from official Environment Agency open data (OGL) — long-term risk band, or an honest "not found" outside England. [![qinisolabs/floodwise MCP server](https://glama.ai/mcp/servers/qinisolabs/floodwise/badges/score.svg)](https://glama.ai/mcp/servers/qinisolabs/floodwise)
- - [xfloukiex-lab/laugh-tale](https://github.com/xfloukiex-lab/laugh-tale) 🐍 🏠 🍎 🪟 🐧 - Capstone of the Grand Line MCP set: a "collect them all" server that unlocks once the other tools are installed. `pip install laugh-tale-mcp`
- - [qinisolabs/qiniso](https://github.com/qinisolabs/qiniso) 📇 🏠 ☁️ - 56 deterministic fact-checkers in one server (IBAN, VAT, VIN, GTIN/barcodes, national & tax IDs, crypto addresses, phone, dates, holidays) — verify the structured facts an agent emits against checksums and curated data. [![qinisolabs/qiniso MCP server](https://glama.ai/mcp/servers/qinisolabs/qiniso/badges/score.svg)](https://glama.ai/mcp/servers/qinisolabs/qiniso)
- - [qinisolabs/bizdays](https://github.com/qinisolabs/bizdays) 📇 🏠 ☁️ - Business-day & public-holiday calculations for 200+ countries (add/count working days, next business day, country weekend rules). [![qinisolabs/bizdays MCP server](https://glama.ai/mcp/servers/qinisolabs/bizdays/badges/score.svg)](https://glama.ai/mcp/servers/qinisolabs/bizdays)
+ - [baodq06/memocall](https://github.com/baodq06/memocall) [![baodq06/memocall MCP server](https://glama.ai/mcp/servers/baodq06/memocall/badges/score.svg)](https://glama.ai/mcp/servers/baodq06/memocall) 📇 🏠 🍎 🪟 🐧 - Recall past Claude Code conversations from any project. Lists and searches your sessions, then loads one on demand as clean, compact Markdown — with outline, turn-range, and in-session search for large sessions. Read-only over local `~/.claude` transcripts; collapses tool calls to stay under the context cap. `npx -y memocall`
+ - [tushariitr-19/immigration-mcp](https://github.com/tushariitr-19/immigration-mcp) [![tushariitr-19/immigration-mcp MCP server](https://glama.ai/mcp/servers/tushariitr-19/immigration-mcp/badges/score.svg)](https://glama.ai/mcp/servers/tushariitr-19/immigration-mcp) 🏎️ 🍎 🪟 🐧 - MCP server for US immigration guidance — live Visa Bulletin, priority date checker and immigration term explanations. Free to use.
+ - [tushariitr-19/patents-mcp](https://github.com/tushariitr-19/patents-mcp) 🏎️ ☁️ 🍎 🪟 🐧 - MCP server for patent search and prior art discovery powered by Google Patents public dataset on BigQuery. Tools: search patents, get full patent details with CPC codes and citations, fetch legal claims text. Free to use.
+ - [qinisolabs/floodwise](https://github.com/qinisolabs/floodwise) [![qinisolabs/floodwise MCP server](https://glama.ai/mcp/servers/qinisolabs/floodwise/badges/score.svg)](https://glama.ai/mcp/servers/qinisolabs/floodwise) 📇 🏠 - England flood-risk by postcode from official Environment Agency open data (OGL) — long-term risk band, or an honest "not found" outside England.
+ - [qinisolabs/floodwise](https://github.com/qinisolabs/floodwise) 📇 🏠 - England flood-risk by postcode from official Environment Agency open data (OGL) — long-term risk band, or an honest "not found" outside England. [![qinisolabs/floodwise MCP server](https://glama.ai/mcp/servers/qinisolabs/floodwise/badges/score.svg)](https://glama.ai/mcp/servers/qinisolabs/floodwise)
+ - [xfloukiex-lab/laugh-tale](https://github.com/xfloukiex-lab/laugh-tale) [![xfloukiex-lab/laugh-tale MCP server](https://glama.ai/mcp/servers/xfloukiex-lab/laugh-tale/badges/score.svg)](https://glama.ai/mcp/servers/xfloukiex-lab/laugh-tale) 🐍 🏠 🍎 🪟 🐧 - Capstone of the Grand Line MCP set: a "collect them all" server that unlocks once the other tools are installed. `pip install laugh-tale-mcp`
+ - [xfloukiex-lab/laugh-tale](https://github.com/xfloukiex-lab/laugh-tale) 🐍 🏠 🍎 🪟 🐧 - Capstone of the Grand Line MCP set: a "collect them all" server that unlocks once the other tools are installed. `pip install laugh-tale-mcp`
+ - [qinisolabs/qiniso](https://github.com/qinisolabs/qiniso) [![qinisolabs/qiniso MCP server](https://glama.ai/mcp/servers/qinisolabs/qiniso/badges/score.svg)](https://glama.ai/mcp/servers/qinisolabs/qiniso) 📇 🏠 ☁️ - 56 deterministic fact-checkers in one server (IBAN, VAT, VIN, GTIN/barcodes, national & tax IDs, crypto addresses, phone, dates, holidays) — verify the structured facts an agent emits against checksums and curated data.
+ - [qinisolabs/qiniso](https://github.com/qinisolabs/qiniso) 📇 🏠 ☁️ - 56 deterministic fact-checkers in one server (IBAN, VAT, VIN, GTIN/barcodes, national & tax IDs, crypto addresses, phone, dates, holidays) — verify the structured facts an agent emits against checksums and curated data. [![qinisolabs/qiniso MCP server](https://glama.ai/mcp/servers/qinisolabs/qiniso/badges/score.svg)](https://glama.ai/mcp/servers/qinisolabs/qiniso)
+ - [qinisolabs/bizdays](https://github.com/qinisolabs/bizdays) [![qinisolabs/bizdays MCP server](https://glama.ai/mcp/servers/qinisolabs/bizdays/badges/score.svg)](https://glama.ai/mcp/servers/qinisolabs/bizdays) 📇 🏠 ☁️ - Business-day & public-holiday calculations for 200+ countries (add/count working days, next business day, country weekend rules).
```



#### [Awesome-Dify-Workflow](https://github.com/svcvit/Awesome-Dify-Workflow)

##### Commit Changes

No file changes detected.

#### [system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools)

##### Commit Changes

No file changes detected.

