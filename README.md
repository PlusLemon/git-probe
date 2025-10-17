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

### 2025-10-17T01:21:00

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

- [d9bbe08](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools/commit/d9bbe08fb14c234d2a8bddf87ead113874fb7b09) Update README.md - Lucas Valbuena
- [77ca45b](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools/commit/77ca45bbceb2519164370fdd5f417074d385ff48) Update README.md - Lucas Valbuena
- [9ac30b5](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools/commit/9ac30b5a03e20d91280cdd8849161644b6fec7e6) Remove unnecessary div tag from README - Lucas Valbuena
- [7658c38](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools/commit/7658c3888437b1122393acc77767aa92b1ac0c22) Update README.md - Lucas Valbuena
- [962f44b](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools/commit/962f44bd8db90584d7633f9d2ed3c1fa2acbd455) Update README.md - Lucas Valbuena
- [38ad815](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools/commit/38ad81548c481c13387ceefc745e876357559ddf) Convert links to anchor tags in README - Lucas Valbuena
- [b4031c8](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools/commit/b4031c8f971ae870f9399ff1081f8d3c0bc6b4de) Update README.md - Lucas Valbuena


##### File Content Changes

**README.md** (Modified, +19 -20 lines):

```diff
- <a href="https://latitude.so/developers?utm_source=github&utm_medium=readme&utm_campaign=prompt_repo_sponsorship">
- ### [The tools you need for building reliable Agents and Prompts](https://latitude.so/developers?utm_source=github&utm_medium=readme&utm_campaign=prompt_repo_sponsorship)
- [Open Source AI Engineering Platform](https://latitude.so/developers?utm_source=github&utm_medium=readme&utm_campaign=prompt_repo_sponsorship)<br>
- <a href="https://latitude.so/developers?utm_source=github&utm_medium=readme&utm_campaign=prompt_repo_sponsorship" target="_blank">
- ### <a href="https://latitude.so/developers?utm_source=github&utm_medium=readme&utm_campaign=prompt_repo_sponsorship" target="_blank">The tools you need for building reliable Agents and Prompts</a>
- <a href="https://latitude.so/developers?utm_source=github&utm_medium=readme&utm_campaign=prompt_repo_sponsorship" target="_blank">Open Source AI Engineering Platform</a><br>
- <div>
- </div>
- ### <a href="https://latitude.so/developers?utm_source=github&utm_medium=readme&utm_campaign=prompt_repo_sponsorship" target="_blank">[The tools you need for building reliable Agents and Prompts]</a>
- <a href="https://latitude.so/developers?utm_source=github&utm_medium=readme&utm_campaign=prompt_repo_sponsorship" target="_blank">[Open Source AI Engineering Platform]</a><br>
+ <a href="https://latitude.so/developers?utm_source=github&utm_medium=readme&utm_campaign=prompt_repo_sponsorship" target="_blank">
+ ### <a href="https://latitude.so/developers?utm_source=github&utm_medium=readme&utm_campaign=prompt_repo_sponsorship" target="_blank">The tools you need for building reliable Agents and Prompts</a>
+ <a href="https://latitude.so/developers?utm_source=github&utm_medium=readme&utm_campaign=prompt_repo_sponsorship" target="_blank">Open Source AI Engineering Platform</a><br>
+ <a href="https://latitude.so/developers?utm_source=github&utm_medium=readme&utm_campaign=prompt_repo_sponsorship">
+ ### [The tools you need for building reliable Agents and Prompts](https://latitude.so/developers?utm_source=github&utm_medium=readme&utm_campaign=prompt_repo_sponsorship)
+ [Open Source AI Engineering Platform](https://latitude.so/developers?utm_source=github&utm_medium=readme&utm_campaign=prompt_repo_sponsorship)<br>
+ </div>
+ <div>
+ ### <a href="https://latitude.so/developers?utm_source=github&utm_medium=readme&utm_campaign=prompt_repo_sponsorship" target="_blank">[The tools you need for building reliable Agents and Prompts]</a>
+ <a href="https://latitude.so/developers?utm_source=github&utm_medium=readme&utm_campaign=prompt_repo_sponsorship" target="_blank">[Open Source AI Engineering Platform]</a><br>
```



