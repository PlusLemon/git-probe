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

### 2025-11-30T01:43:53

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

- [35b05e3](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools/commit/35b05e3e59a89c106d5d29b1501cfc344a1a5b74) Enhance README with Trendshift badge - Lucas Valbuena
- [6368f9b](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools/commit/6368f9b040b00c5a63fc9866d84c5f072bb9f66a) Refactor README for clarity and update date - Lucas Valbuena


##### File Content Changes

**README.md** (Modified, +4 -11 lines):

```diff
- ⭐ **Star to follow updates**
- > **Join the Conversation:** New system instructions are released on Discord **before** they appear in this repository. Get early access and discuss them in real time.
- If you find this collection valuable and appreciate the effort involved in obtaining and sharing these insights, please consider supporting the project. Your contribution helps keep this resource updated and allows for further exploration.
- ## Support the Future of AI Development
- Sponsor the most comprehensive collection of AI system prompts and reach thousands of developers building the next generation of AI applications.
- > **Latest Update:** 19/11/2025
- *The company is mine, this is NOT a 3rd party AD.*
+ If you find this collection valuable and appreciate the effort involved in obtaining and sharing these insights, please consider supporting the project.
+ Sponsor the most comprehensive repository of AI system prompts and reach thousands of developers.
+ > **Latest Update:** 29/11/2025
```



