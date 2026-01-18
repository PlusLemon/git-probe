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

### 2026-01-18T01:49:40

#### [awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps)

##### Commit Changes

No file changes detected.

#### [awesome-gpt4o-images](https://github.com/jamez-bondos/awesome-gpt4o-images)

##### Commit Changes

No file changes detected.

#### [awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers)

##### Commit Changes

- [508c4d2](https://github.com/punkpeye/awesome-mcp-servers/commit/508c4d2b8a7e97ae3ab8fd336fcbce95e60ee2ec) Add lightningfaucet/mcp-server - Bitcoin Lightning wallet for AI agents - Alex Sato
- [a451dad](https://github.com/punkpeye/awesome-mcp-servers/commit/a451dadbf9eaf06abb0b6cccab1788f57911d64c) Add oci-pricing-mcp to Cloud Platforms section - Jason Wilbur


##### File Content Changes

**README.md** (Modified, +2 -0 lines):

```diff
+ - [lightningfaucet/mcp-server](https://github.com/lightningfaucet/mcp-server) 📇 ☁️ - AI Agent Bitcoin wallet with L402 payments - operators fund agents, agents make autonomous Lightning Network payments.
+ - [jasonwilbur/oci-pricing-mcp](https://github.com/jasonwilbur/oci-pricing-mcp) 📇 ☁️ - Oracle Cloud Infrastructure pricing data with 602 products, cost calculators, and cross-provider comparisons. One-command install for Claude.
```



#### [Awesome-Dify-Workflow](https://github.com/svcvit/Awesome-Dify-Workflow)

##### Commit Changes

No file changes detected.

#### [system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools)

##### Commit Changes

- [aaafe4d](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools/commit/aaafe4d73995228420315aceb20bde8cc709594e) Update README.md - Lucas Valbuena
- [0b30fc8](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools/commit/0b30fc82cb61041c3e80707e02fe2b0a3a9b5a08) Update README.md - Lucas Valbuena


##### File Content Changes

**README.md** (Modified, +4 -1 lines):

```diff
- <a href="https://bags.fm/DEffWzJyaFRNyA4ogUox631hfHuv3KLeCcpBh2ipBAGS">Bags.fm</a>
+ <a href="https://bags.fm/DEffWzJyaFRNyA4ogUox631hfHuv3KLeCcpBh2ipBAGS">Bags.fm</a> •
+ <a href="https://jup.ag/tokens/DEffWzJyaFRNyA4ogUox631hfHuv3KLeCcpBh2ipBAGS">Jupiter</a> •
+ <a href="https://photon-sol.tinyastro.io/en/lp/Qa5ZCCwrWoPYckNXXMCAhCsw8gafgYFAu1Qes3Grgv5?handle=">Photon</a> •
+ <a href="https://dexscreener.com/solana/qa5zccwrwopycknxxmcahcsw8gafgyfau1qes3grgv5">DEXScreener</a>
```



