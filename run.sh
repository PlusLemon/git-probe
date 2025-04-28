#!/bin/bash
# Run Git Probe script

# 1. Check if uv is installed
if ! command -v uv &> /dev/null; then
    echo "Error: uv is not installed. Please install uv (https://github.com/astral-sh/uv) before running this script."
    exit 1
fi

# 2. Check required environment variables
missing_vars=()
[ -z "$GITHUB_TOKEN" ] && missing_vars+=("GITHUB_TOKEN")
[ -z "$OPENAI_API_KEY" ] && missing_vars+=("OPENAI_API_KEY")
[ -z "$OPENAI_API_BASE" ] && missing_vars+=("OPENAI_API_BASE")
[ -z "$OPENAI_MODEL" ] && missing_vars+=("OPENAI_MODEL")

if [ ${#missing_vars[@]} -ne 0 ]; then
    echo "Error: The following environment variables are not set: ${missing_vars[*]}"
    echo "Please set them in your environment or in a .env file."
    exit 1
fi

# 3. Sync dependencies
uv sync

# 4. Run the script with uv
uv python git_probe.py