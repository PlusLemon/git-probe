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

### 2025-11-19T01:25:05

#### [awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps)

##### Commit Changes

No file changes detected.

#### [awesome-gpt4o-images](https://github.com/jamez-bondos/awesome-gpt4o-images)

##### Commit Changes

No file changes detected.

#### [awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers)

##### Commit Changes

No file changes detected.

#### [Awesome-Dify-Workflow](https://github.com/svcvit/Awesome-Dify-Workflow)

##### Commit Changes

No file changes detected.

#### [system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools)

##### Commit Changes

- [3b2ed91](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools/commit/3b2ed914a6df51106f36a48ba3c3fc6c0fea864c) Update README.md - Lucas Valbuena
- [9e87245](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools/commit/9e872451979fdef88edd3085127a9b93a68cd8eb) Update README.md - Lucas Valbuena
- [21b4ed1](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools/commit/21b4ed1508992cf434f5e8bac7dc9fd2f0226160) Remove Table of Contents and Available Files sections - Lucas Valbuena


##### File Content Changes

**README.md** (Modified, +3 -55 lines):

```diff
- </p>
- - **Discord**: `x1xh`
- ## 📑 Table of Contents
- - [📑 Table of Contents](#-table-of-contents)
- - [📂 Available Files](#-available-files)
- - [🛠 Roadmap \& Feedback](#-roadmap--feedback)
- - [🔗 Connect With Me](#-connect-with-me)
- - [🛡️ Security Notice for AI Startups](#️-security-notice-for-ai-startups)
- - [📊 Star History](#-star-history)
- ## 📂 Available Files
- - [**v0**](./v0%20Prompts%20and%20Tools/)
- - [**Manus**](./Manus%20Agent%20Tools%20&%20Prompt/)
- - [**Augment Code**](./Augment%20Code/)
- - [**Lovable**](./Lovable/)
- - [**Devin**](./Devin%20AI/)
- - [**Same.dev**](./Same.dev/)
- - [**Replit**](./Replit/)
- - [**Windsurf Agent**](./Windsurf/)
- - [**VSCode (Copilot) Agent**](./VSCode%20Agent/)
- - [**Cursor**](./Cursor%20Prompts/)
- - [**Dia**](./dia/)
- - [**Trae AI**](./Trae/)
- - [**Perplexity**](./Perplexity/)
- - [**Cluely**](./Cluely/)
- - [**Xcode**](./Xcode/)
- - [**Leap.new**](./Leap.new/)
- - [**Notion AI**](./NotionAi/)
- - [**Orchids.app**](./Orchids.app/)
- - [**Junie**](./Junie/)
- - [**Kiro**](./Kiro/)
- - [**Warp.dev**](./Warp.dev/)
- - [**Z.ai Code**](./Z.ai%20Code/)
- - [**Qoder**](./Qoder/)
- - [**Claude Code**](./Claude%20Code/)
- - [**Open Source prompts**](./Open%20Source%20prompts/)
- - [Codex CLI](./Open%20Source%20prompts/Codex%20CLI/)
- - [Cline](./Open%20Source%20prompts/Cline/)
- - [Bolt](./Open%20Source%20prompts/Bolt/)
- - [RooCode](./Open%20Source%20prompts/RooCode/)
- - [Lumo](./Open%20Source%20prompts/Lumo/)
- - [Gemini CLI](./Open%20Source%20prompts/Gemini%20CLI/)
- - [**CodeBuddy**](./CodeBuddy%20Prompts/)
- - [**Poke**](./Poke/)
- - [**Comet Assistant**](./Comet%20Assistant/)
- - [**Anthropic**](./Anthropic/)
- - [**Amp**](./AMp/)
- > **Latest Update:** 09/11/2025
+ </p>
+ - **Discord**: `x1xhlol`
+ > **Latest Update:** 18/11/2025
```



