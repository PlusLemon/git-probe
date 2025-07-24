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

### 2025-07-24T01:42:53

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

- [2ac28d6](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools/commit/2ac28d6620d7e02591098f85f8c6b904dc3dccd3) Update README.md - Lucas Valbuena
- [437a8e6](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools/commit/437a8e6fd1edfe32b2c51be01cc993bf4a5100a7) Update README.md - Lucas Valbuena
- [a018454](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools/commit/a018454dcad54d1b1ad16793f21a137da19e6cf9) Update README.md - Lucas Valbuena
- [d07116d](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools/commit/d07116de555573a5d0dee7a34ef62c62613808de) Update README.md - Lucas Valbuena
- [28de2eb](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools/commit/28de2ebab691663770fd80ffa01afcad461cb86c) Update README.md - Lucas Valbuena
- [1709c09](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools/commit/1709c095d78e0413794d42c1cb6dc734fb63a055) Update README.md - Lucas Valbuena
- [ac4c81f](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools/commit/ac4c81f146d380d01db5c4e52af65a4a4d4db719) Update README.md - Lucas Valbuena
- [a66cbb5](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools/commit/a66cbb57986737ffdad62df40caab956e75eb9c8) Update README.md - Lucas Valbuena


##### File Content Changes

**README.md** (Modified, +31 -12 lines):

```diff
- While other tools get stuck on prompts, spawn.co uses cutting-edge AI to build and deploy complete games. I've spawned 4 complete game variants in under 20 minutes. Not prototypes - actual playable games with save systems, multiplayer, monetization ready to ship.
- # Spawn
- Build. Ship. Done.
- <div align="right">
- <a href="https://spawn.co" target="_blank" rel="noopener noreferrer">
- <img width="200" height="200" alt="Spawn.co Logo" src="https://github.com/user-attachments/assets/669cef9b-eec1-4add-9a02-fb7e12602126" />
- </a>
- </div>
- - RooCode
- > **Latest Update:** 21/07/2025
+ While other tools get stuck on prompts, [spawn.co](https://www.spawn.co/) uses cutting-edge AI to build and deploy complete games. I've spawned 4 complete game variants in under 20 minutes. Not prototypes - actual playable games with save systems, multiplayer, monetization ready to ship.
+ ---
+ # Tired of buiding trash games with generic AI tools?
+ <a href="https://spawn.co" target="_blank" rel="noopener noreferrer">
+ <img width="200" height="200" alt="Spawn.co Logo" src="https://github.com/user-attachments/assets/669cef9b-eec1-4add-9a02-fb7e12602126" align="right" />
+ </a>
+ **Build. Ship. Done.**
+ # Spawn
+ Stop **prototyping**. Start **shipping**.
+ While other tools get stuck on prompts, spawn.co uses cutting-edge AI to build and deploy complete games. I've spawned 4 complete game variants in under 20 minutes. Not prototypes - actual playable games with save systems, multiplayer, monetization ready to ship.
+ It’s not marketing fluff, it’s just a better way to build.
+ Build. Ship. Done.
+ <div align="right">
+ <img width="200" height="200" alt="Spawn.co Logo" src="https://github.com/user-attachments/assets/669cef9b-eec1-4add-9a02-fb7e12602126" />
+ </div>
+ [![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/x1xhlol/system-prompts-and-models-of-ai-tools)
+ - RooCode
+ - Lumo
+ > **Latest Update:** 23/07/2025
```



