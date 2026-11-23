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

### 2026-11-23T05:53:17

#### [awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps)

##### Commit Changes

No file changes detected.

#### [awesome-gpt4o-images](https://github.com/jamez-bondos/awesome-gpt4o-images)

##### Commit Changes

No file changes detected.

#### [awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers)

##### Commit Changes

- [a51d937](https://github.com/punkpeye/awesome-mcp-servers/commit/a51d93735d8e8d2f08acf71b4b34a1162f230237) Lathe: Glama score badge - Joel Taddei
- [feeb99c](https://github.com/punkpeye/awesome-mcp-servers/commit/feeb99c6a5e24183870d32ae4ad77c0bdfdded8f) Add Lathe, a DAW with its own MCP server - Joel Taddei
- [e7416b4](https://github.com/punkpeye/awesome-mcp-servers/commit/e7416b463efdb31e956fabb1fbbe962b444c6956) Add scrapecrate/mcp-server - ScrapeCrate


##### File Content Changes

**README.md** (Modified, +3 -1 lines):

```diff
- - [taddeimania/lathe](https://github.com/taddeimania/lathe) 🎖️ 🌊 🏠 🍎 🪟 🐧 - A free, open-source DAW with its own MCP server: read the session, play any bars, build tracks and plug-in chains, write MIDI in a compact note notation, mix with channel EQ and sends, set the song's keys, convert audio to MIDI and export audio, each change one undo step in the app.
+ - [taddeimania/lathe](https://github.com/taddeimania/lathe) [![taddeimania/lathe MCP server](https://glama.ai/mcp/servers/taddeimania/lathe/badges/score.svg)](https://glama.ai/mcp/servers/taddeimania/lathe) 🎖️ 🌊 🏠 🍎 🪟 🐧 - A free, open-source DAW with its own MCP server: read the session, play any bars, build tracks and plug-in chains, write MIDI in a compact note notation, mix with channel EQ and sends, set the song's keys, convert audio to MIDI and export audio, each change one undo step in the app.
+ - [taddeimania/lathe](https://github.com/taddeimania/lathe) 🎖️ 🌊 🏠 🍎 🪟 🐧 - A free, open-source DAW with its own MCP server: read the session, play any bars, build tracks and plug-in chains, write MIDI in a compact note notation, mix with channel EQ and sends, set the song's keys, convert audio to MIDI and export audio, each change one undo step in the app.
+ - [scrapecrate/mcp-server](https://github.com/scrapecrate/mcp-server) [![scrapecrate/mcp-server MCP server](https://glama.ai/mcp/servers/scrapecrate/mcp-server/badges/score.svg)](https://glama.ai/mcp/servers/scrapecrate/mcp-server) 🐍 ☁️ 🍎 🪟 🐧 - One API key for YouTube transcripts and metadata, Google Maps places and reviews, Trustpilot reviews and the Meta Ad Library, via the ScrapeCrate API.
```



#### [Awesome-Dify-Workflow](https://github.com/svcvit/Awesome-Dify-Workflow)

##### Commit Changes

No file changes detected.

#### [system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools)

##### Commit Changes

No file changes detected.

