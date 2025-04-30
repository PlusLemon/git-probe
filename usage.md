## Configuration

### probe.yaml

This file specifies which GitHub repositories and files/directories to monitor:

```yaml
repositories:
  repo-name:
    url: https://github.com/owner/repo
    branch: main
    paths:
      - specific/file/to/monitor.md
      - directory/to/monitor/
```

If `paths` is empty (or contains an empty list), Git Probe will monitor the entire repository:

```yaml
repositories:
  full-repo-monitor:
    url: https://github.com/owner/repo
    branch: main
    paths: []  # Monitor the entire repository
```

### config.yaml

This file contains project settings:

```yaml
enable_ai_summary: false   # Whether to use AI to summarize changes
github_token: ${GH_TOKEN}  # GitHub token for API access (can use env vars)
update_frequency: daily    # How often to check for updates
readme_max_changes: 10     # Maximum number of changes to display in README
history_format: markdown   # Format for history files
timezone: UTC             # Timezone for timestamps
max_diff_lines: 30        # Maximum number of diff lines to display
show_diff: true           # Whether to show file diffs in reports
```

### Environment Variables

Sensitive values like API keys can be set using environment variables in a `.env` file:

1. Copy the example file: `cp env.example .env`
2. Edit `.env` and add your credentials
3. Git Probe will automatically load values from this file

Available environment variables:
- `GH_TOKEN`: Your GitHub API token
- `OPENAI_API_KEY`: Your OpenAI API key (for AI summaries)
- `OPENAI_API_BASE`: Custom base URL for OpenAI API
- `OPENAI_MODEL`: AI model to use for summaries

The `.env` file is gitignored by default for security.

## Usage

The project runs automatically via GitHub Actions. To run manually:

1. Run the script: `./run.sh` (automatically installs dependencies using UV)

### Dependencies

This project uses [UV](https://github.com/astral-sh/uv) for fast dependency management. The run script will automatically install UV if it's not already available.

To manually install dependencies:

```bash
# Install UV first if you don't have it
curl -LsSf https://astral.sh/uv/install.sh | sh

# Then install dependencies
uv pip install -r requirements.txt
```

## Daily Report Format

Each daily report consists of these sections for each monitored repository:

1. **Commit Changes**: List of recent commits with authors and messages
2. **File Content Changes**: Consolidated diff outputs organized by file, showing:
   - File name and status (Added/Modified/Deleted/Renamed)
   - Number of lines added/deleted
   - Combined diff from all commits affecting that file
   - All changes are grouped in a single diff block per file for better readability
3. **AI Summary**: A concise summary of the changes and their impact (if enabled)

This optimized format provides a clearer picture of what changed in each file, rather than fragmenting changes by individual commits.

## Directory Structure

- `history/`: Contains daily archives of changes for each repository
  - Format: `repo_name_YYYY-MM-DD.md`

## Thanks

If you find this project helpful, please consider giving it a star ⭐️. Thank you for your support!