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

### 2026-09-29T04:23:18

#### [awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps)

##### Commit Changes

- [45f867f](https://github.com/Shubhamsaboo/awesome-llm-apps/commit/45f867fa57108d1cfa4b4e2471b241b6f53d76a1) docs(readme): put TinyFish banner in the two-column sponsor table - Shubham Saboo
- [d25f821](https://github.com/Shubhamsaboo/awesome-llm-apps/commit/d25f821cb0e59af43e4cbeb70b5eec933971530f) docs(readme): add TinyFish sponsor banner, drop top Unwind banner - Shubham Saboo


##### File Content Changes

**README.md** (Modified, +32 -13 lines):

```diff
- <p align="center">
- <a href="https://www.tinyfish.ai/ambassadors" target="_blank" rel="noopener" title="TinyFish Community Programs">
- <img src="docs/banner/sponsors/tinyfish_community.png" width="900px" alt="TinyFish Community Programs: join the Students and Ambassadors programs for free credits, bounties, gift cards, swag, certifications, and event budget">
- </a>
- </p>
- <p align="center"><sub><b>TinyFish Community Programs:</b> <a href="https://www.tinyfish.ai/students">Students</a> · <a href="https://www.tinyfish.ai/ambassadors">Ambassadors</a> · <a href="https://sponsorunwindai.com/">Become a sponsor</a></sub></p>
- <a href="http://www.theunwindai.com">
- <img src="docs/banner/unwind_black.png" width="900px" alt="Unwind AI">
+ <table align="center" cellpadding="16" cellspacing="12">
+ <tr>
+ <td align="center">
+ <a href="https://www.tinyfish.ai/ambassadors" target="_blank" rel="noopener" title="TinyFish">
+ <img src="docs/banner/sponsors/tinyfish_community.png" alt="TinyFish Community Programs: join the Students and Ambassadors programs" width="500">
+ </a>
+ <br>
+ <a href="https://www.tinyfish.ai/ambassadors" target="_blank" rel="noopener" style="text-decoration: none; color: #333; font-weight: bold; font-size: 18px;">
+ TinyFish
+ </td>
+ <a href="https://sponsorunwindai.com/" title="Become a Sponsor">
+ <img src="docs/banner/sponsor_awesome_llm_apps.png" alt="Become a Sponsor" width="500">
+ <a href="https://sponsorunwindai.com/" style="text-decoration: none; color: #333; font-weight: bold; font-size: 18px;">
+ Become a Sponsor
+ </tr>
+ </table>
+ ## 🙏 Thanks to our sponsors
+ <p align="center">
+ <a href="https://www.tinyfish.ai/ambassadors" target="_blank" rel="noopener" title="TinyFish Community Programs">
+ <img src="docs/banner/sponsors/tinyfish_community.png" width="900px" alt="TinyFish Community Programs: join the Students and Ambassadors programs for free credits, bounties, gift cards, swag, certifications, and event budget">
+ </p>
+ <p align="center"><sub><b>TinyFish Community Programs:</b> <a href="https://www.tinyfish.ai/students">Students</a> · <a href="https://www.tinyfish.ai/ambassadors">Ambassadors</a> · <a href="https://sponsorunwindai.com/">Become a sponsor</a></sub></p>
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

