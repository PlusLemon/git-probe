#!/bin/bash
# Run Git Probe script

# Set up environment variables from .env file if it exists
if [ -f .env ]; then
    echo "Loading environment variables from .env file"
    export $(grep -v '^#' .env | xargs)
fi

# Check if GitHub token is set
if [ -z "$GITHUB_TOKEN" ]; then
    echo "Warning: GITHUB_TOKEN environment variable is not set."
    echo "You can set it in a .env file or export it directly."
fi

# Check if OpenAI API key is set (only if AI summaries are enabled)
if grep -q "enable_ai_summary: true" config.yaml; then
    if [ -z "$OPENAI_API_KEY" ]; then
        echo "Warning: OPENAI_API_KEY environment variable is not set but AI summaries are enabled."
        echo "You can set it in a .env file or export it directly."
    fi
fi

# Check if uv is installed
if ! command -v uv &> /dev/null; then
    echo "Installing uv package manager..."
    curl -LsSf https://astral.sh/uv/install.sh | sh
    export PATH="$HOME/.cargo/bin:$PATH"
fi

# Install Python dependencies using uv
echo "Installing dependencies with uv..."
uv pip install -r requirements.txt

# Run the script
python git_probe.py