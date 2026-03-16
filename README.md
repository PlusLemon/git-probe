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

### 2026-03-16T02:24:33

#### [awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps)

##### Commit Changes

No file changes detected.

#### [awesome-gpt4o-images](https://github.com/jamez-bondos/awesome-gpt4o-images)

##### Commit Changes

No file changes detected.

#### [awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers)

##### Commit Changes

- [ed1aa4f](https://github.com/punkpeye/awesome-mcp-servers/commit/ed1aa4fbeb0006e9c2be7594b494910a948d83ae) Merge pull request #2135 from y11t0/patch-2 - Frank Fiegel
- [51ebe05](https://github.com/punkpeye/awesome-mcp-servers/commit/51ebe05d346f8e0b25b43c11f6299e063458aab0) Update README.md - Frank Fiegel
- [5a29671](https://github.com/punkpeye/awesome-mcp-servers/commit/5a2967104077891d18e5fe533455b12d03183879) Merge pull request #2516 from Jovancoding/add-network-ai - Frank Fiegel
- [024caba](https://github.com/punkpeye/awesome-mcp-servers/commit/024cabae7d26096f4b47aa6104ae04e4a1cc9534) Update README.md - Frank Fiegel
- [84122f3](https://github.com/punkpeye/awesome-mcp-servers/commit/84122f37d10369ef04920f65ce1734f39cc43b20) Merge branch 'main' into add-botindex-mcp-server - Frank Fiegel
- [7f543c4](https://github.com/punkpeye/awesome-mcp-servers/commit/7f543c463491e09a301f249c3ad33924eb393bb4) Fix formatting for Cyberweasel777 botindex entry - Frank Fiegel
- [69a01f8](https://github.com/punkpeye/awesome-mcp-servers/commit/69a01f87797318ed6e85999497d5091953a6ac8d) Merge pull request #2928 from vikramgorla/add-mcp-swiss - Frank Fiegel
- [21b6659](https://github.com/punkpeye/awesome-mcp-servers/commit/21b66595f5a2dcf46efa9bdeaa5acee73a086c07) Update README.md - Frank Fiegel
- [1f7ca0c](https://github.com/punkpeye/awesome-mcp-servers/commit/1f7ca0c1835c47286356170755350fc411330f8e) Merge branch 'main' into add-lego-oracle - Frank Fiegel
- [c88932d](https://github.com/punkpeye/awesome-mcp-servers/commit/c88932dc4cff8b5f2c24d03f9ad2c7c013bf8d47) Merge pull request #3242 from overpod/add-mcp-telegram - Frank Fiegel


##### File Content Changes

**README.md** (Modified, +287 -12 lines):

```diff
- - [corebasehq/coremcp](https://github.com/corebasehq/coremcp) [glama](https://glama.ai/mcp/servers/CoreBaseHQ/coremcp) 🏎️ ☁️ 🏠 - A secure, tunnel-native database bridge for AI agents. Connects localhost & on-premise databases (MSSQL, etc.) to LLMs with AST-based query safety and PII masking.
- - [Jovancoding/Network-AI](https://github.com/Jovancoding/Network-AI) [glama](https://glama.ai/mcp/servers/Jovancoding/network-ai) 📇 🏠 🍎 🪟 🐧 - Multi-agent orchestration MCP server with race-condition-safe shared blackboard. 20+ MCP tools: blackboard read/write, agent spawn/stop, FSM transitions, budget tracking, token management, and audit log query. `npx network-ai-server --port 3001`.
- - [Cyberweasel777/botindex-mcp-server](https://github.com/Cyberweasel777/botindex-mcp-server) [glama](https://glama.ai/mcp/servers/Cyberweasel777/botindex-mcp-server) 📇 ☁️ - BotIndex + Agorion MCP server — AI signal intelligence API + agent service discovery network. x402 payment gating on premium endpoints.
- - [vikramgorla/mcp-swiss](https://github.com/vikramgorla/mcp-swiss) [glama](https://glama.ai/mcp/servers/vikramgorla/mcp-swiss) 📇 ☁️ - 68 tools for Swiss open data: transport, weather, geodata, companies, parliament, and more. Zero API keys required.
+ - [corebasehq/coremcp](https://github.com/corebasehq/coremcp) [![coremcp](https://glama.ai/mcp/servers/CoreBaseHQ/coremcp/badges/score.svg)](https://glama.ai/mcp/servers/CoreBaseHQ/coremcp) 🏎️ ☁️ 🏠 - A secure, tunnel-native database bridge for AI agents. Connects localhost & on-premise databases (MSSQL, etc.) to LLMs with AST-based query safety and PII masking.
+ - [Jovancoding/Network-AI](https://github.com/Jovancoding/Network-AI) [![network](https://glama.ai/mcp/servers/Jovancoding/network-ai/badges/score.svg)](https://glama.ai/mcp/servers/Jovancoding/network-ai) 📇 🏠 🍎 🪟 🐧 - Multi-agent orchestration MCP server with race-condition-safe shared blackboard. 20+ MCP tools: blackboard read/write, agent spawn/stop, FSM transitions, budget tracking, token management, and audit log query. `npx network-ai-server --port 3001`.
+ name: Check Glama Link
+ on:
+ pull_request_target:
+ types: [opened, edited, synchronize, closed]
+ permissions:
+ contents: read
+ pull-requests: write
+ issues: write
+ jobs:
+ # Post-merge welcome comment
+ welcome:
+ if: github.event.action == 'closed' && github.event.pull_request.merged == true
+ runs-on: ubuntu-latest
+ steps:
+ - name: Post welcome comment
+ uses: actions/github-script@v7
+ with:
+ script: |
+ const { owner, repo } = context.repo;
+ const pr_number = context.payload.pull_request.number;
+ const marker = '<!-- welcome-comment -->';
+ const { data: comments } = await github.rest.issues.listComments({
+ owner,
+ repo,
+ issue_number: pr_number,
+ per_page: 100,
+ });
+ if (!comments.some(c => c.body.includes(marker))) {
+ await github.rest.issues.createComment({
+ body: `${marker}\nThank you for your contribution! Your server has been merged.
+ Are you in the MCP [Discord](https://glama.ai/mcp/discord)? Let me know your Discord username and I will give you a **server-author** flair.
+ If you also have a remote server, you can list it under https://glama.ai/mcp/connectors`
+ }
+ # Validation checks (only on open PRs)
+ check-submission:
+ if: github.event.action != 'closed'
+ - name: Checkout base branch
+ uses: actions/checkout@v4
+ ref: ${{ github.event.pull_request.base.ref }}
+ - name: Validate PR submission
+ const fs = require('fs');
+ // Read existing README to check for duplicates
+ const readme = fs.readFileSync('README.md', 'utf8');
+ const existingUrls = new Set();
+ const urlRegex = /\(https:\/\/github\.com\/[^)]+\)/gi;
+ for (const match of readme.matchAll(urlRegex)) {
+ existingUrls.add(match[0].toLowerCase());
+ // Get the PR diff
+ ... (183 more additions)
```



#### [Awesome-Dify-Workflow](https://github.com/svcvit/Awesome-Dify-Workflow)

##### Commit Changes

No file changes detected.

#### [system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools)

##### Commit Changes

No file changes detected.

