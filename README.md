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

### 2026-03-19T02:08:25

#### [awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps)

##### Commit Changes

No file changes detected.

#### [awesome-gpt4o-images](https://github.com/jamez-bondos/awesome-gpt4o-images)

##### Commit Changes

No file changes detected.

#### [awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers)

##### Commit Changes

- [a03020d](https://github.com/punkpeye/awesome-mcp-servers/commit/a03020dfe3e52a4930c9ac550dccaeee2a8bd1bc) Merge branch 'main' into add-agentdeals-v2 - Frank Fiegel
- [03b679e](https://github.com/punkpeye/awesome-mcp-servers/commit/03b679edc308c434e674f85c41e1da39c011f169) Add robhunter/agentdeals to Aggregators - robhunterpmagent


##### File Content Changes

**README.md** (Modified, +309 -8 lines):

```diff
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
+ const { data: files } = await github.rest.pulls.listFiles({
+ pull_number: pr_number,
+ ... (176 more additions)
```



#### [Awesome-Dify-Workflow](https://github.com/svcvit/Awesome-Dify-Workflow)

##### Commit Changes

No file changes detected.

#### [system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools)

##### Commit Changes

No file changes detected.

