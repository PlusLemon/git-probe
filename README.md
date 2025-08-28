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

### 2025-08-28T01:21:02

#### [awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps)

##### Commit Changes

- [1672412](https://github.com/Shubhamsaboo/awesome-llm-apps/commit/1672412de025a99537e63c0c9428992050714204) feat: Add Gemma 3 fine-tuning tutorial - Shubhamsaboo
- [edf042f](https://github.com/Shubhamsaboo/awesome-llm-apps/commit/edf042f10b8dd0f8c95f96ecb59b37ddefcb4d68) feat: Add OpenAI Agents SDK Crash Course - Shubhamsaboo


##### File Content Changes

**README.md** (Modified, +11 -2 lines):

```diff
- <img src="docs/banner/sponsors/unblocked.png" alt="Unblocked" width="450">
- <img src="docs/banner/sponsor_awesome_llm_apps.png" alt="Sponsor Awesome LLM Apps Repo" width="450">
+ *   [🔧 Gemma 3 Fine-tuning](advanced_llm_apps/llm_finetuning_tutorials/gemma3_finetuning/)
+ <img src="docs/banner/sponsors/unblocked.png" alt="Unblocked" width="6000">
+ <img src="docs/banner/sponsor_awesome_llm_apps.png" alt="Sponsor Awesome LLM Apps Repo" width="6000">
+ - [OpenAI Agents SDK Crash Course](ai_agent_framework_crash_course/openai_sdk_crash_course/)
+ - Starter agent; function calling; structured outputs
+ - Tools: built‑in, function, third‑party integrations
+ - Memory; callbacks; evaluation
+ - Multi‑agent patterns; agent handoffs
+ - Swarm orchestration; routing logic
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

- [ab4ff61](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools/commit/ab4ff616e3a38eafd8da821d8bbf4c8fdc6d2963) Update README.md - Lucas Valbuena
- [c93c021](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools/commit/c93c0210f77dc67fd1f012dbef0029a5603b3bb2) Update README.md - Lucas Valbuena


##### File Content Changes

**README.md** (Modified, +2 -2 lines):

```diff
- > **Latest Update:** 24/08/2025
- 📜 Over **12,000+ lines** of insights into their structure and functionality.
+ > **Latest Update:** 27/08/2025
+ 📜 Over **20,000+ lines** of insights into their structure and functionality.
```



