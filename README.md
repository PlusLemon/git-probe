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

### 2025-05-03T01:21:34

#### [awesome-gpt4o-images](https://github.com/jamez-bondos/awesome-gpt4o-images)

##### Commit Changes

No file changes detected.

##### File Content Changes

No file changes detected.

#### [awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers)

##### Commit Changes

- [2dc5837](https://github.com/punkpeye/awesome-mcp-servers/commit/2dc583769050f46359b69993963e301ff5889d91) Add ROS MCP Server - Jungsoo Lee


##### File Content Changes

**README.md** (Modified, +1 -0 lines):

```diff
+ - [lpigeon/ros-mcp-server](https://github.com/lpigeon/ros-mcp-server) 🐍 🏠 🍎 🪟 🐧 - The ROS MCP Server supports robot control by converting user-issued natural language commands into ROS or ROS2 control commands.
```



##### AI Summary

The GitHub repository `awesome-mcp-servers` added a new ROS MCP Server entry to its README (2dc5837), featuring a Python-based tool ([lpigeon/ros-mcp-server](https://github.com/lpigeon/ros-mcp-server)) that converts natural language commands into ROS/ROS2 control commands for robotics. This +1 line change expands the repository's catalog of MCP servers with a specialized solution for robot control systems. While no code was modified, the update enhances the resource list for developers working on language-to-robot command interfaces. The addition strengthens the repository's coverage of MCP server implementations across different domains.

#### [Awesome-Dify-Workflow](https://github.com/svcvit/Awesome-Dify-Workflow)

##### Commit Changes

No file changes detected.

##### File Content Changes

No file changes detected.

#### [system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools)

##### Commit Changes

No file changes detected.

##### File Content Changes

No file changes detected.

