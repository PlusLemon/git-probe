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

### 2026-03-07T01:54:10

#### [awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps)

##### Commit Changes

No file changes detected.

#### [awesome-gpt4o-images](https://github.com/jamez-bondos/awesome-gpt4o-images)

##### Commit Changes

No file changes detected.

#### [awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers)

##### Commit Changes

- [d6ad44e](https://github.com/punkpeye/awesome-mcp-servers/commit/d6ad44e13cf0ff595003ed831c2396a9139cd293) Merge pull request #2467 from roomi-fields/add-notebooklm-mcp - Frank Fiegel
- [8e269cd](https://github.com/punkpeye/awesome-mcp-servers/commit/8e269cd9ed332e8e40a28aeedeb4189b44dddcc3) Merge pull request #2403 from bncbodrogi/add-vesselapi-mcp - Frank Fiegel
- [955f13b](https://github.com/punkpeye/awesome-mcp-servers/commit/955f13b91be7bd769cb291825e48b1febe1fae1f) Merge branch 'main' into add-notebooklm-mcp - Frank Fiegel
- [80c523f](https://github.com/punkpeye/awesome-mcp-servers/commit/80c523f922c20e84530e889d3c16eda5cd24425a) Merge pull request #2779 from 0xtus/add-azeth-mcp-server - Frank Fiegel
- [681537b](https://github.com/punkpeye/awesome-mcp-servers/commit/681537b2bc64a44a3431914103cee54895431aaf) Merge pull request #2800 from PatrickSys/add-codebase-context - Frank Fiegel
- [092efdc](https://github.com/punkpeye/awesome-mcp-servers/commit/092efdc463a58b2041c70a55c51e72318504b6f3) Merge pull request #2806 from duriantaco/duriantaco-patch-1-1 - Frank Fiegel
- [52ead89](https://github.com/punkpeye/awesome-mcp-servers/commit/52ead89dd9e55c5e76235d7b8949fa306e6ad468) add Glama listing link - Bence Bodrogi
- [d3c3a89](https://github.com/punkpeye/awesome-mcp-servers/commit/d3c3a89c33b2b12399b71615dda0ae3447e302a9) Update Skylos link with Glama integration - oha
- [ff537d1](https://github.com/punkpeye/awesome-mcp-servers/commit/ff537d19b5fb0d02822f03b02c2355928a12bfeb) Add Glama verification link for azeth-protocol/mcp-server - RF31
- [e995ccd](https://github.com/punkpeye/awesome-mcp-servers/commit/e995ccd388b322cea548f3d2ee2f235de1cc5357) Add glama listing link - PatrickSys


##### File Content Changes

**README.md** (Modified, +101 -6 lines):

```diff
- - [vessel-api/vesselapi-mcp](https://github.com/vessel-api/vesselapi-mcp) 📇 ☁️ - Maritime vessel tracking via VesselAPI. Search vessels, get real-time positions, ETAs, port events, emissions, inspections, and NAVTEX safety messages.
- - [duriantaco/skylos](https://github.com/duriantaco/skylos) 🐍 🏠 🍎 🪟  🐧 - Dead code detection, security scanning, and code quality      analysis for Python, TypeScript, and Go. 98% recall with fewer false positives than Vulture. Includes AI-powered remediation.
- - [azeth-protocol/mcp-server](https://github.com/azeth-protocol/mcp-server) 📇 ☁️ - Trust infrastructure for the machine economy — non-custodial ERC-4337 smart accounts, x402 payments, on-chain reputation via ERC-8004, and service discovery for AI agents.
- - [PatrickSys/codebase-context](https://github.com/PatrickSys/codebase-context) 📇 🏠 🍎 🪟 🐧 - Local MCP server that shows AI agents which patterns your team actually uses, what files a change will affect, and when there is not enough context to trust an edit. 30+ languages, fully local.
+ - [roomi-fields/notebooklm-mcp](https://github.com/roomi-fields/notebooklm-mcp) ([glama](https://glama.ai/mcp/servers/@roomi-fields/notebooklm-mcp)) 📇 🏠 🍎 🪟 🐧 - Full automation of Google NotebookLM — Q&A with citations, audio podcasts, video, content generation, source management, and notebook library. MCP + HTTP REST API.
+ - [vessel-api/vesselapi-mcp](https://github.com/vessel-api/vesselapi-mcp) [glama](https://glama.ai/mcp/servers/@vessel-api/vessel-api-mcp-server) 📇 ☁️ - Maritime vessel tracking via VesselAPI. Search vessels, get real-time positions, ETAs, port events, emissions, inspections, and NAVTEX safety messages.
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
+ ... (164 more additions)
```



#### [Awesome-Dify-Workflow](https://github.com/svcvit/Awesome-Dify-Workflow)

##### Commit Changes

No file changes detected.

#### [system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools)

##### Commit Changes

No file changes detected.

