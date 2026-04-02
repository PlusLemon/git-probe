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

### 2026-04-02T02:11:13

#### [awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps)

##### Commit Changes

No file changes detected.

#### [awesome-gpt4o-images](https://github.com/jamez-bondos/awesome-gpt4o-images)

##### Commit Changes

No file changes detected.

#### [awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers)

##### Commit Changes

- [1e8f925](https://github.com/punkpeye/awesome-mcp-servers/commit/1e8f9250f5850984395b28aa2e17b1967e339e03) Merge pull request #2358 from Higangssh/add-homebutler - Frank Fiegel
- [456bb74](https://github.com/punkpeye/awesome-mcp-servers/commit/456bb74ff3b835fae814513393fe1b91566d60b0) Merge pull request #2431 from davidsimoes/add-digisign-mcp - Frank Fiegel
- [ec6c61f](https://github.com/punkpeye/awesome-mcp-servers/commit/ec6c61f1a5a0cd26e207b78e2532f35b6bff4ec3) Merge pull request #2444 from jonradoff/add-lightcms - Frank Fiegel
- [b82367c](https://github.com/punkpeye/awesome-mcp-servers/commit/b82367c50879a5b2b4cda68e23c382bf326df401) Update README.md - Frank Fiegel


##### File Content Changes

**README.md** (Modified, +4 -1 lines):

```diff
- - [jonradoff/lightcms](https://github.com/jonradoff/lightcms) 🏎️ ☁️ - AI-native CMS with 72 MCP tools for managing websites through natural language. Create and publish content, manage templates, assets, snippets, themes, collections, redirects, and multi-site forks — with full content versioning and semantic search. [![jonradoff/lightcms MCP server](https://glama.ai/mcp/servers/jonradoff/lightcms/badges/score.svg)](https://glama.ai/mcp/servers/jonradoff/lightcms)
+ - [Higangssh/homebutler](https://github.com/Higangssh/homebutler) [![homebutler MCP server](https://glama.ai/mcp/servers/Higangssh/homebutler/badges/score.svg)](https://glama.ai/mcp/servers/Higangssh/homebutler) 🏎️ 🏠 - All-in-one homelab management MCP server. Monitor system resources, manage Docker containers, Wake-on-LAN, scan networks, check open ports, and run alerts — across multiple servers via SSH. Single 10MB binary, zero dependencies.
+ - [davidsimoes/digisign-mcp](https://github.com/davidsimoes/digisign-mcp) [![davidsimoes/digisign-mcp MCP server](https://glama.ai/mcp/servers/davidsimoes/digisign-mcp/badges/score.svg)](https://glama.ai/mcp/servers/davidsimoes/digisign-mcp) 📇 ☁️ - MCP server for DigiSign.cz digital signature API — create, send, and manage digital signature envelopes.
+ - [jonradoff/lightcms](https://github.com/jonradoff/lightcms) [![jonradoff/lightcms MCP server](https://glama.ai/mcp/servers/jonradoff/lightcms/badges/score.svg)](https://glama.ai/mcp/servers/jonradoff/lightcms) 🏎️ ☁️ - AI-native CMS with 72 MCP tools for managing websites through natural language. Create and publish content, manage templates, assets, snippets, themes, collections, redirects, and multi-site forks — with full content versioning and semantic search.
```



#### [Awesome-Dify-Workflow](https://github.com/svcvit/Awesome-Dify-Workflow)

##### Commit Changes

No file changes detected.

#### [system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools)

##### Commit Changes

No file changes detected.

