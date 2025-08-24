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

### 2025-08-24T01:39:55

#### [awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps)

##### Commit Changes

- [ba4a2d4](https://github.com/Shubhamsaboo/awesome-llm-apps/commit/ba4a2d418347885cebfbffe7c25f9cdb873dd4e0) Change sponsor text to 'Become a Sponsor' - Shubham Saboo
- [ce4500b](https://github.com/Shubhamsaboo/awesome-llm-apps/commit/ce4500b0375bab6af33dd374db94c0ce6f6ea2ab) feat: Add sponsor section to README.md with links and images - Shubhamsaboo


##### File Content Changes

**README.md** (Modified, +28 -3 lines):

```diff
- Sponsor Awesome LLM Apps Repo
+ Become a Sponsor
+ ## 🙏 Thanks to our sponsors
+ <table align="center" cellpadding="16" cellspacing="12">
+ <tr>
+ <td align="center">
+ <a href="https://getunblocked.com/unblocked-mcp/?utm_source=oss&utm_medium=sponsorship&utm_campaign=awesome-llm-apps" target="_blank" rel="noopener" title="Unblocked">
+ <img src="docs/banner/sponsors/unblocked.png" alt="Unblocked" width="450">
+ </a>
+ <br>
+ <a href="https://getunblocked.com/unblocked-mcp/?utm_source=oss&utm_medium=sponsorship&utm_campaign=awesome-llm-apps" target="_blank" rel="noopener" style="text-decoration: none; color: #333; font-weight: bold; font-size: 18px;">
+ Unblocked
+ </td>
+ <a href="https://sponsorunwindai.com/" title="Sponsor Awesome LLM Apps Repo">
+ <img src="docs/banner/sponsor_awesome_llm_apps.png" alt="Sponsor Awesome LLM Apps Repo" width="450">
+ <a href="https://sponsorunwindai.com/" style="text-decoration: none; color: #333; font-weight: bold; font-size: 18px;">
+ Sponsor Awesome LLM Apps Repo
+ </tr>
+ </table>
```



#### [awesome-gpt4o-images](https://github.com/jamez-bondos/awesome-gpt4o-images)

##### Commit Changes

No file changes detected.

#### [awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers)

##### Commit Changes

- [cf1f0ac](https://github.com/punkpeye/awesome-mcp-servers/commit/cf1f0ac61dfea727952e09b2ec2130355dde00d1) Merge pull request #1293 from wyattjoh/add-jsr-mcp - Frank Fiegel
- [200b7e1](https://github.com/punkpeye/awesome-mcp-servers/commit/200b7e1dce01e301d33063c4fc13bd5d55bd9f9a) feat: add jsr-mcp to Developer Tools section - Wyatt Johnson
- [55febb8](https://github.com/punkpeye/awesome-mcp-servers/commit/55febb8c60ba946993819c3786c63f0af8e8962d) feat: add imessage-mcp to Communication section - Wyatt Johnson
- [75b09d2](https://github.com/punkpeye/awesome-mcp-servers/commit/75b09d2ae48f632b638eb4e13bdac4bb9a194283) Fix link to IO Aerospace MCP Server repository in Aerospace & Astrodynamics section - Sylvain Guillet
- [483b415](https://github.com/punkpeye/awesome-mcp-servers/commit/483b415d6058bc8c6d14497f92c69b3beda462cf) Add Aerospace & Astrodynamics section with IO-Aerospace MCP server - Sylvain Guillet


##### File Content Changes

**README.md** (Modified, +8 -1 lines):

```diff
- - [IO-Aerospace-software-engineering/mcp-server](https://github.com/IO-Aerospace-software-engineering/mcp-server) #️⃣ ☁️/🏠 🐧 - IO Aerospace MCP Server: a .NET-based MCP server for aerospace & astrodynamics — ephemeris, orbital conversions, DSS tools, time conversions, and unit/math utilities. Supports STDIO and SSE transports; Docker and native .NET deployment documented.
+ - [wyattjoh/jsr-mcp](https://github.com/wyattjoh/jsr-mcp) 📇 ☁️ - Model Context Protocol server for the JSR (JavaScript Registry)
+ - [wyattjoh/imessage-mcp](https://github.com/wyattjoh/imessage-mcp) 📇 🏠 🍎 - A Model Context Protocol server for reading iMessage data from macOS.
+ - [IO-Aerospace-software-community/mcp-server](https://github.com/IO-Aerospace-software-engineering/mcp-server) #️⃣ ☁️/🏠 🐧 - IO Aerospace MCP Server: a .NET-based MCP server for aerospace & astrodynamics — ephemeris, orbital conversions, DSS tools, time conversions, and unit/math utilities. Supports STDIO and SSE transports; Docker and native .NET deployment documented.
+ ### 🚀 <a name="aerospace-and-astrodynamics"></a>Aerospace & Astrodynamics
+ - [IO-Aerospace-software-engineering/mcp-server](https://github.com/IO-Aerospace-software-engineering/mcp-server) #️⃣ ☁️/🏠 🐧 - IO Aerospace MCP Server: a .NET-based MCP server for aerospace & astrodynamics — ephemeris, orbital conversions, DSS tools, time conversions, and unit/math utilities. Supports STDIO and SSE transports; Docker and native .NET deployment documented.
```



#### [Awesome-Dify-Workflow](https://github.com/svcvit/Awesome-Dify-Workflow)

##### Commit Changes

No file changes detected.

#### [system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools)

##### Commit Changes

- [c96561e](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools/commit/c96561e6938389e2b57f2c5188abb7e2ac7a9c19) Update README.md - Lucas Valbuena


##### File Content Changes

**README.md** (Modified, +1 -1 lines):

```diff
- > **Latest Update:** 22/08/2025
+ > **Latest Update:** 24/08/2025
```



