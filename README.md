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

### 2026-11-24T08:31:27

#### [awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps)

##### Commit Changes

No file changes detected.

#### [awesome-gpt4o-images](https://github.com/jamez-bondos/awesome-gpt4o-images)

##### Commit Changes

No file changes detected.

#### [awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers)

##### Commit Changes

- [fcf0700](https://github.com/punkpeye/awesome-mcp-servers/commit/fcf0700423c5f5fdd709ed83df86c4a42aadc5e7) Update README.md - NEOMA P-CAM Enclave
- [723309c](https://github.com/punkpeye/awesome-mcp-servers/commit/723309c57dce2bda3fba4a904517cfdc484b6206) Add luca-network/spr (Sealed Payment Record) - Qunlay1


##### File Content Changes

**README.md** (Modified, +2 -0 lines):

```diff
+ - [neoma-pcam/pcam-live](https://github.com/neoma-pcam/pcam-live) [![neoma-pcam/pcam-live MCP server](https://glama.ai/mcp/servers/neoma-pcam/pcam-live/badges/score.svg)](https://glama.ai/mcp/servers/neoma-pcam/pcam-live) 🎖️ 🐍 ☁️ - Connects Frontier LLMs directly to a physical hardware enclave for sub-millisecond (0.85ms) non-linear physical equilibrium, mechanical resonance damping, and cryptographic PUF attestation via cloud.
+ - [luca-network/spr](https://github.com/luca-network/spr) [![luca-network/spr MCP server](https://glama.ai/mcp/servers/luca-network/spr/badges/score.svg)](https://glama.ai/mcp/servers/luca-network/spr) 📇 🏠 🍎 🪟 🐧 - Records each payment an AI agent makes as a signed record on your own machine: what it declared before paying, what it paid, and whether it stayed inside its limit. Anyone can check the records. `npx -y @luca-network/spr-mcp`
```



#### [Awesome-Dify-Workflow](https://github.com/svcvit/Awesome-Dify-Workflow)

##### Commit Changes

No file changes detected.

#### [system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools)

##### Commit Changes

No file changes detected.

