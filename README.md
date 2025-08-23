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

### 2025-08-23T01:20:34

#### [awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps)

##### Commit Changes

No file changes detected.

#### [awesome-gpt4o-images](https://github.com/jamez-bondos/awesome-gpt4o-images)

##### Commit Changes

No file changes detected.

#### [awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers)

##### Commit Changes

- [aba6172](https://github.com/punkpeye/awesome-mcp-servers/commit/aba61725d9b808140e0560e5d5a31be6e4969338) Update README.md - Frank Fiegel


##### File Content Changes

**README.md** (Modified, +1 -1 lines):

```diff
- - [gerkensm/callcenter.js-mcp](https://github.com/gerkensm/callcenter.js-mcp) 📇 ☁️ An MCP server to make phone calls using VoIP/SIP and OpenAI's Realtime API and observe the transcript.
+ - [gerkensm/callcenter.js-mcp](https://github.com/gerkensm/callcenter.js-mcp) 📇 ☁️ - An MCP server to make phone calls using VoIP/SIP and OpenAI's Realtime API and observe the transcript.
```



#### [Awesome-Dify-Workflow](https://github.com/svcvit/Awesome-Dify-Workflow)

##### Commit Changes

No file changes detected.

#### [system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools)

##### Commit Changes

- [73fc745](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools/commit/73fc74521ddcedba9a48b00f5a67b26c4d45ce3b) Update README.md - Lucas Valbuena
- [ad4adbc](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools/commit/ad4adbcb693190cf185c48c323547f6d054e7578) Update README.md - Lucas Valbuena
- [33ccaa5](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools/commit/33ccaa562d6672d8ed7bc0565df5797df50a0aef) Update README.md - Fromsko
- [5bf7efa](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools/commit/5bf7efa4f719c8b23cecb81e03f52584fddb7380) Update README.md - Lucas Valbuena
- [ae9d14c](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools/commit/ae9d14ca3e568823d52fcef40cfb312cee34465f) Merge branch 'main' into main - moqimoqidea
- [156e376](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools/commit/156e3764330b596784a45218b9f1d71ac791481d) Rename system prompt files and update README.md to include new entries for Claude Code and Gemini CLI - moqi
- [b892cb9](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools/commit/b892cb99b0dc62a53937e262387c5b5b44470f67) Update README.md - Lucas Valbuena
- [9a9d07a](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools/commit/9a9d07a612e36bd38ceaf977ffe42399e586f486) Add Qoder AI Assistant system prompt and update README with Qoder link - 4regab


##### File Content Changes

**README.md** (Modified, +32 -26 lines):

```diff
- - [**Open Source prompts Folder**](./Open%20Source%20prompts/)
- - [**System Prompts and Models of AI Tools**](#system-prompts-and-models-of-ai-tools)
- 1. [Available Files](#-available-files)
- 2. [Roadmap & Feedback](#-roadmap--feedback)
- 3. [Connect With Me](#-connect-with-me)
- 4. [Security Notice for AI Startups](#%EF%B8%8F-security-notice-for-ai-startups)
- 5. [Star History](#-star-history)
- - [**v0 Folder**](./v0%20Prompts%20and%20Tools/)
- - [**Spawn Folder**](./-Spawn/)
- - [**Manus Folder**](./Manus%20Agent%20Tools%20&%20Prompt/)
- - [**Lovable Folder**](./Lovable/)
- - [**Devin Folder**](./Devin%20AI/)
- - [**Same.dev Folder**](./Same.dev/)
- - [**Replit Folder**](./Replit/)
- - [**Windsurf Agent Folder**](./Windsurf/)
- - [**VSCode (Copilot) Agent Folder**](./VSCode%20Agent/)
- - [**Cursor Folder**](./Cursor%20Prompts/)
- - [**Dia Folder**](./dia/)
- - [**Trae AI Folder**](./Trae/)
- - [**Perplexity Folder**](./Perplexity/)
- - [**Cluely Folder**](./Cluely/)
- - [**Xcode Folder**](./Xcode/)
- - [**Orchids.app Folder**](./Orchids.app/)
- - [**Junie Folder**](./Junie/)
- > **Latest Update:** 18/08/2025
+ - [**Open Source prompts**](./Open%20Source%20prompts/)
+ - [**System Prompts and Models of AI Tools**](#system-prompts-and-models-of-ai-tools)
+ - [❤️ Support the Project](#️-support-the-project)
+ - [📑 Table of Contents](#-table-of-contents)
+ - [📂 Available Files](#-available-files)
+ - [🛠 Roadmap \& Feedback](#-roadmap--feedback)
+ - [🔗 Connect With Me](#-connect-with-me)
+ - [🛡️ Security Notice for AI Startups](#️-security-notice-for-ai-startups)
+ - [📊 Star History](#-star-history)
+ - [**CodeBuddy**](./CodeBuddy%20Prompts/)
+ - [**v0**](./v0%20Prompts%20and%20Tools/)
+ - [**Manus**](./Manus%20Agent%20Tools%20&%20Prompt/)
+ - [**Lovable**](./Lovable/)
+ - [**Devin**](./Devin%20AI/)
+ - [**Same.dev**](./Same.dev/)
+ - [**Replit**](./Replit/)
+ - [**Windsurf Agent**](./Windsurf/)
+ - [**VSCode (Copilot) Agent**](./VSCode%20Agent/)
+ - [**Cursor**](./Cursor%20Prompts/)
+ - [**Dia**](./dia/)
+ - [**Trae AI**](./Trae/)
+ - [**Perplexity**](./Perplexity/)
+ - [**Cluely**](./Cluely/)
+ - [**Xcode**](./Xcode/)
+ - [**Orchids.app**](./Orchids.app/)
+ - [**Junie**](./Junie/)
+ - [**Qoder**](./Qoder/)
+ > **Latest Update:** 22/08/2025
+ - [**Claude Code**](./Claude%20Code/)
+ - [Gemini CLI](./Open%20Source%20prompts/Gemini%20CLI/)
```



