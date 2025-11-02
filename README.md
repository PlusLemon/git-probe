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

### 2025-11-02T01:36:38

#### [awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps)

##### Commit Changes

No file changes detected.

#### [awesome-gpt4o-images](https://github.com/jamez-bondos/awesome-gpt4o-images)

##### Commit Changes

No file changes detected.

#### [awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers)

##### Commit Changes

- [c99f64e](https://github.com/punkpeye/awesome-mcp-servers/commit/c99f64ea3013d776693d0ed323a686fd05b438ed) Merge pull request #1452 from Narasimhaponnada/add-mermaid-mcp-server - Frank Fiegel


##### File Content Changes

**README.md** (Modified, +8 -0 lines):

```diff
+ * 📐 - [Architecture & Design](#architecture-and-design)
+ ### 📐 <a name="architecture-and-design"></a>Architecture & Design
+ Design and visualize software architecture, system diagrams, and technical documentation. Enables AI models to generate professional diagrams and architectural documentation.
+ - [Narasimhaponnada/mermaid-mcp](https://github.com/Narasimhaponnada/mermaid-mcp) 📇 ☁️ 🍎 🪟 🐧 - AI-powered Mermaid diagram generation with 22+ diagram types including flowcharts, sequence diagrams, class diagrams, ER diagrams, architecture diagrams, state machines, and more. Features 50+ pre-built templates, advanced layout engines, SVG/PNG/PDF exports, and seamless integration with GitHub Copilot, Claude, and any MCP-compatible client. Install via NPM: `npm install -g @narasimhaponnada/mermaid-mcp-server`
```



#### [Awesome-Dify-Workflow](https://github.com/svcvit/Awesome-Dify-Workflow)

##### Commit Changes

No file changes detected.

#### [system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools)

##### Commit Changes

- [0d60d27](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools/commit/0d60d27a5589b79a2cdb6b73ed1f5c089c1bc4ad) Update PayPal contact email in README - Lucas Valbuena


##### File Content Changes

**README.md** (Modified, +1 -1 lines):

```diff
- - **PayPal:** `lucknitelol@proton.me`
+ - **PayPal:** `lucknitelol@pm.me`
```



