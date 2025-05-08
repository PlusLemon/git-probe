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

### 2025-05-08T01:25:07

#### [awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps)

##### Commit Changes

No file changes detected.

#### [awesome-gpt4o-images](https://github.com/jamez-bondos/awesome-gpt4o-images)

##### Commit Changes

- [c511ae8](https://github.com/jamez-bondos/awesome-gpt4o-images/commit/c511ae8b0841f6a977d82f03d4f2fa087190ce42) docs: update auto-generated README files - github-actions[bot]


##### File Content Changes

**README.md** (Modified, +22 -0 lines):

```diff
+ *   [案例 91：谷歌地图变身古代藏宝图 (by @umesh_ai)](#cases-91)
+ <a id="cases-91"></a>
+ ### 案例 91：谷歌地图变身古代藏宝图 (by [@umesh_ai](https://x.com/umesh_ai))
+ [原文链接](https://x.com/umesh_ai/status/1919701229363466328)
+ <img src="cases/91/case.png" width="300" alt="谷歌地图变身古代藏宝图">
+ **提示词**
+ ```
+ 将图像转换为绘制在古老羊皮纸上的古代藏宝图。地图包含详细的元素，如海洋上的帆船、海岸线上的古老港口或城堡、通向标记宝藏地点的大“X”的虚线路径、山脉、棕榈树和装饰性的罗盘玫瑰。整体风格让人联想到旧时的海盗冒险电影。
+ **需上传参考图片：** 需要上传一张谷歌地图截图或其他地图图片作为转换的基础。
+ ---
+ [⬆️ 返回案例目录](#cases-toc)
```



#### [awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers)

##### Commit Changes

- [16136bb](https://github.com/punkpeye/awesome-mcp-servers/commit/16136bb9391b7c088bdc07b6dddd1664cd4d2903) Merge pull request #827 from stass/patch-2 - Frank Fiegel
- [c978e90](https://github.com/punkpeye/awesome-mcp-servers/commit/c978e90dc37eb56271523808f0142e17c8741ffb) Merge pull request #830 from isaacphi/add-mcp-language-server - Frank Fiegel
- [b239d1b](https://github.com/punkpeye/awesome-mcp-servers/commit/b239d1b5c6a934dad3457bae4d56932b24d1b684) Merge pull request #833 from ferdousbhai/patch-3 - Frank Fiegel
- [dcf7648](https://github.com/punkpeye/awesome-mcp-servers/commit/dcf7648f9ec956c080d3122fb078b330aaa70635) Merge pull request #834 from mattijsdp/add-dbt-docs-mcp - Frank Fiegel
- [480670b](https://github.com/punkpeye/awesome-mcp-servers/commit/480670b640d290977b62bd0dfcef8d3bc56222ed) Merge pull request #836 from pilartomas/add-acp-mcp-adapter - Frank Fiegel
- [883793c](https://github.com/punkpeye/awesome-mcp-servers/commit/883793c0885004d56721878cb47aae8213c86fc2) Merge pull request #837 from firstorder-ai/add-authenticator-mcp - Frank Fiegel
- [2d13f6f](https://github.com/punkpeye/awesome-mcp-servers/commit/2d13f6f5b8208a97d4a05f3abe3a3ead52a898e1) Update README.md - Frank Fiegel
- [150b34a](https://github.com/punkpeye/awesome-mcp-servers/commit/150b34aa46b54dd3e04123e9eacc0bc87b1e8d70) Merge pull request #840 from narumiruna/gitingest - Frank Fiegel
- [1c6bc99](https://github.com/punkpeye/awesome-mcp-servers/commit/1c6bc99d5f752355a7437dd40f20a1669599eb15) Merge pull request #842 from TimLukaHorstmann/add-new-server - Frank Fiegel
- [d46759f](https://github.com/punkpeye/awesome-mcp-servers/commit/d46759f917ff063bc9147ccd225adc6402445a98) Merge pull request #844 from JaredHatfield/mcp-graphql-forge - Frank Fiegel


##### File Content Changes

**README.md** (Modified, +10 -1 lines):

```diff
- - [firstorderai/authenticator_mcp](https://github.com/firstorderai/authenticator_mcp) - 📇 🏠 🍎 🪟 🐧 A secure MCP (Model Context Protocol) server that enables AI agents to interact with the Authenticator App.
+ - [stass/exif-mcp](https://github.com/stass/exif-mcp) 📇 🏠 🐧 🍎 🪟 - A MCP server that allows one to examine image metadata like EXIF, XMP, JFIF and GPS.  This provides foundation for LLM-powered search and analysis of photo librares and image collections.
+ - [isaacphi/mcp-language-server](https://github.com/isaacphi/mcp-language-server) 🏎️ 🏠 - MCP Language Server helps MCP enabled clients navigate codebases more easily by giving them access to semantic tools like get definition, references, rename, and diagnostics.
+ - [ferdousbhai/wsb-analyst-mcp](https://github.com/ferdousbhai/wsb-analyst-mcp) 🐍 ☁️ - Reddit integration to analyze content on WallStreetBets community
+ - [mattijsdp/dbt-docs-mcp](https://github.com/mattijsdp/dbt-docs-mcp) 🐍 🏠 - MCP server for dbt-core (OSS) users as the official dbt MCP only supports dbt Cloud. Supports project metadata, model and column-level lineage and dbt documentation.
+ - [i-am-bee/acp-mcp](https://github.com/i-am-bee/acp-mcp) 🐍 💬 - An MCP server acting as an adapter into the [ACP](https://agentcommunicationprotocol.dev) ecosystem. Seamlessly exposes ACP agents to MCP clients, bridging the communication gap between the two protocols.
+ - [firstorderai/authenticator_mcp](https://github.com/firstorderai/authenticator_mcp) 📇 🏠 🍎 🪟 🐧 – A secure MCP (Model Context Protocol) server that enables AI agents to interact with the Authenticator App.
+ - [narumiruna/gitingest-mcp](https://github.com/narumiruna/gitingest-mcp) 🐍 🏠 - A MCP server that uses [gitingest](https://github.com/cyclotruc/gitingest) to convert any Git repository into a simple text digest of its codebase.
+ - [TimLukaHorstmann/mcp-weather](https://github.com/TimLukaHorstmann/mcp-weather) 📇 ☁️  - Accurate weather forecasts via the AccuWeather API (free tier available).
+ - [UnitVectorY-Labs/mcp-graphql-forge](https://github.com/UnitVectorY-Labs/mcp-graphql-forge) 🏎️ ☁️ 🍎 🪟 🐧 - A lightweight, configuration-driven MCP server that exposes curated GraphQL queries as modular tools, enabling intentional API interactions from your agents.
```



#### [Awesome-Dify-Workflow](https://github.com/svcvit/Awesome-Dify-Workflow)

##### Commit Changes

No file changes detected.

#### [system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools)

##### Commit Changes

No file changes detected.

