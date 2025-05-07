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

### 2025-05-07T01:24:55

#### [awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps)

##### Commit Changes

No file changes detected.

#### [awesome-gpt4o-images](https://github.com/jamez-bondos/awesome-gpt4o-images)

##### Commit Changes

- [56542fd](https://github.com/jamez-bondos/awesome-gpt4o-images/commit/56542fd585bdf0c700c60dfbd4832ea2fb24d2bb) docs: update auto-generated README files - github-actions[bot]


##### File Content Changes

**README.md** (Modified, +22 -0 lines):

```diff
+ *   [案例 90：品牌化键盘键帽 (by @egeberkina)](#cases-90)
+ <a id="cases-90"></a>
+ ### 案例 90：品牌化键盘键帽 (by [@egeberkina](https://x.com/egeberkina))
+ [原文链接](https://x.com/egeberkina/status/1918291652210311278)
+ <img src="cases/90/case.png" width="300" alt="品牌化键盘键帽">
+ **提示词**
+ ```
+ 一个超逼真的3D渲染图，展示了四个机械键盘键帽，排列成紧密的2x2网格，所有键帽相互接触。从等轴测角度观察。一个键帽是透明的，上面用红色印刷着“{just}”字样。另外三个键帽采用颜色：{黑色、紫色和白色}。一个键帽上带有Github的Logo。另外两个键帽上分别写着“{fork}”和“{it}”。逼真的塑料纹理，圆润的雕刻键帽，柔和的阴影，干净的浅灰色背景。
+ *注意： 替换品牌名、标语、键帽颜色*
+ ---
+ [⬆️ 返回案例目录](#cases-toc)
```



#### [awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers)

##### Commit Changes

- [c57ff4d](https://github.com/punkpeye/awesome-mcp-servers/commit/c57ff4dea60f19eb0aff0d5743544839cf2be905) Update README.md - Frank Fiegel
- [2934bc8](https://github.com/punkpeye/awesome-mcp-servers/commit/2934bc8c5e6d2a824bdd109f9fd83dc3160ba113) Update README.md - Jags Ramnarayan


##### File Content Changes

**README.md** (Modified, +2 -1 lines):

```diff
- - [skysqlinc/skysql-mcp](https://github.com/skysqlinc/skysql-mcp) 🎖️ ☁️ - Serverless(Free) MariaDB(MySQL compatible) Cloud DB MCP server. Tools to launch, delete, execute SQL and work with DB level AI agents for accurate text-2-sql and conversations. Essentially a "semantic layer" for your DBs enabling AI apps.
+ - [skysqlinc/skysql-mcp](https://github.com/skysqlinc/skysql-mcp) 🎖️ ☁️ - Serverless MariaDB Cloud DB MCP server. Tools to launch, delete, execute SQL and work with DB level AI agents for accurate text-2-sql and conversations.
+ - [skysqlinc/skysql-mcp](https://github.com/skysqlinc/skysql-mcp) 🎖️ ☁️ - Serverless(Free) MariaDB(MySQL compatible) Cloud DB MCP server. Tools to launch, delete, execute SQL and work with DB level AI agents for accurate text-2-sql and conversations. Essentially a "semantic layer" for your DBs enabling AI apps.
```



#### [Awesome-Dify-Workflow](https://github.com/svcvit/Awesome-Dify-Workflow)

##### Commit Changes

No file changes detected.

#### [system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools)

##### Commit Changes

No file changes detected.

