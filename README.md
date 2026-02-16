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

### 2026-02-16T02:05:36

#### [awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps)

##### Commit Changes

- [88b778f](https://github.com/Shubhamsaboo/awesome-llm-apps/commit/88b778fe59e9933653124a182cac65dad9fa5307) Update image links in README.md - Shubham Saboo


##### File Content Changes

**README.md** (Modified, +2 -2 lines):

```diff
- A curated collection of **Awesome LLM apps built with RAG, AI Agents, Multi-agent Teams, MCP, Voice Agents, and more.** This repository features LLM apps that use models from <img src="https://cdn.simpleicons.org/openai"  alt="openai logo" width="25" height="15">**OpenAI** , <img src="https://cdn.simpleicons.org/anthropic"  alt="anthropic logo" width="25" height="15">**Anthropic**, <img src="https://cdn.simpleicons.org/googlegemini"  alt="google logo" width="25" height="18">**Google**, <img src="https://cdn.simpleicons.org/x"  alt="X logo" width="25" height="15">**xAI** and open-source models like <img src="https://cdn.simpleicons.org/alibabacloud"  alt="alibaba logo" width="25" height="15">**Qwen** or  <img src="https://cdn.simpleicons.org/meta"  alt="meta logo" width="25" height="15">**Llama** that you can run locally on your computer.
- <img src="https://cdn.simpleicons.org/openai"  alt="openai logo" width="25" height="15"> [OpenAI Agents SDK Crash Course](ai_agent_framework_crash_course/openai_sdk_crash_course/)
+ A curated collection of **Awesome LLM apps built with RAG, AI Agents, Multi-agent Teams, MCP, Voice Agents, and more.** This repository features LLM apps that use models from <img src="https://cdn.jsdelivr.net/npm/simple-icons@15/icons/openai.svg"  alt="openai logo" width="25" height="15">**OpenAI** , <img src="https://cdn.simpleicons.org/anthropic"  alt="anthropic logo" width="25" height="15">**Anthropic**, <img src="https://cdn.simpleicons.org/googlegemini"  alt="google logo" width="25" height="18">**Google**, <img src="https://cdn.simpleicons.org/x"  alt="X logo" width="25" height="15">**xAI** and open-source models like <img src="https://cdn.simpleicons.org/alibabacloud"  alt="alibaba logo" width="25" height="15">**Qwen** or  <img src="https://cdn.simpleicons.org/meta"  alt="meta logo" width="25" height="15">**Llama** that you can run locally on your computer.
+ <img src="https://cdn.jsdelivr.net/npm/simple-icons@15/icons/openai.svg"  alt="openai logo" width="25" height="15"> [OpenAI Agents SDK Crash Course](ai_agent_framework_crash_course/openai_sdk_crash_course/)
```



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

No file changes detected.

