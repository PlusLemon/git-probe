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

### 2026-09-11T03:08:38

#### [awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps)

##### Commit Changes

- [67c4047](https://github.com/Shubhamsaboo/awesome-llm-apps/commit/67c4047b9181372722dbda2f82f95d08bb16e1fe) chore(advisor-orchestrator-worker): Fable 5.1 advisor, GPT-6 Astra orchestrator, Gemini 3.8 Flash workers - Shubham Saboo
- [7afced7](https://github.com/Shubhamsaboo/awesome-llm-apps/commit/7afced7c218d0a94aad37a80af7864a5108e0429) docs(first-reader): plain one-sentence catalog line - Shubham Saboo
- [6a69f02](https://github.com/Shubhamsaboo/awesome-llm-apps/commit/6a69f02651f314605978d38b155b99133b6060f1) docs(first-reader): shorter catalog one-liner - Shubham Saboo
- [0ce85da](https://github.com/Shubhamsaboo/awesome-llm-apps/commit/0ce85da5efb797756d3464558ac89d7b96454979) docs(first-reader): align README with the collection, rewrite evals, list in catalog - Shubham Saboo


##### File Content Changes

**README.md** (Modified, +4 -3 lines):

```diff
- *   [🧠 Advisor Orchestrator Worker](agent_skills/advisor-orchestrator-worker/) - Meta Loop with Claude Fable 5 as advisor, GPT-5.6 as orchestrator, and Gemini 3.7 Flash as worker
- *   [👁️ First Reader](agent_skills/first-reader/) - Simulated readers meet your draft cold and report where they lean in, where they quit, and what they remember tomorrow. Ask them why. Nobody rewrites
- *   [👁️ First Reader](agent_skills/first-reader/) - Puts two simulated readers in front of your draft, one passage at a time, and tells you where they leaned in, where they quit, and what they remembered the next day; you can ask them follow-ups, and nobody rewrites anything
+ *   [🧠 Advisor Orchestrator Worker](agent_skills/advisor-orchestrator-worker/) - Meta Loop with Claude Fable 5.1 as advisor, GPT-6 Astra as orchestrator, and Gemini 3.8 Flash as worker
+ *   [👁️ First Reader](agent_skills/first-reader/) - Simulates real readers going through your draft and reports where they lose interest, where they stop reading, and what they remember afterward, without rewriting a word
+ *   [👁️ First Reader](agent_skills/first-reader/) - Simulated readers meet your draft cold and report where they lean in, where they quit, and what they remember tomorrow. Ask them why. Nobody rewrites
+ *   [👁️ First Reader](agent_skills/first-reader/) - Puts two simulated readers in front of your draft, one passage at a time, and tells you where they leaned in, where they quit, and what they remembered the next day; you can ask them follow-ups, and nobody rewrites anything
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

