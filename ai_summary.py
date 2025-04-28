#!/usr/bin/env python3
import os
import yaml
import requests
import datetime
import re
from pathlib import Path

class AISummary:
    def __init__(self):
        self.config = self.load_yaml('config.yaml')
        self.enable_ai_summary = self.config.get('enable_ai_summary', False)
        
        # OpenAI API settings - Prefer environment variables, then config file
        self.api_key = os.environ.get('OPENAI_API_KEY') or self.config.get('openai_api_key')
        self.model = os.environ.get('OPENAI_MODEL') or self.config.get('ai_model', 'gpt-3.5-turbo')
        
        # Add support for custom API base URL
        self.api_base = os.environ.get('OPENAI_API_BASE') or self.config.get('openai_api_base', 'https://api.openai.com/v1')
        
        # Get today's date
        self.today = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d')
        
        # Create summaries directory if it doesn't exist
        self.summaries_dir = Path('summaries')
        self.summaries_dir.mkdir(exist_ok=True)
        
    def load_yaml(self, filename):
        with open(filename, 'r') as file:
            return yaml.safe_load(file) or {}
    
    def generate_summary(self, commit_section, file_changes_section, repo_name):
        """Generate an AI summary of the changes using OpenAI API"""
        if not self.enable_ai_summary or not self.api_key:
            return None
            
        prompt = f"""
        Summarize the following GitHub changes for the repository {repo_name}:
        
        COMMIT CHANGES:
        {commit_section}
        
        FILE CONTENT CHANGES:
        {file_changes_section}
        
        Provide a concise summary highlighting:
        1. The key changes and what they mean for the project
        2. Any significant code additions or deletions
        3. Overall impact of these changes
        
        Focus on technical details when relevant. Limit your response to 3-5 sentences.
        """
        
        # Determine if using OpenRouter API
        is_openrouter = 'openrouter.ai' in self.api_base
        
        # Basic request data
        data = {
            'model': self.model,
            'messages': [
                {'role': 'system', 'content': 'You are a helpful assistant that summarizes GitHub repository changes with technical accuracy.'},
                {'role': 'user', 'content': prompt}
            ]
        }
        

        headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }
        
        # 使用自定义API base URL
        endpoint = f"{self.api_base.rstrip('/')}/chat/completions"
        print(f"Sending request to API at: {endpoint}")
        print(f"Using model: {self.model}")
        
        # Maximum retry attempts
        max_retries = 3
        retry_count = 0
        
        while retry_count < max_retries:
            try:
                print(f"Attempt {retry_count+1}/{max_retries} to generate summary...")
                
                response = requests.post(
                    endpoint,
                    headers=headers,
                    json=data,
                    timeout=60  # 添加超时设置
                )                
                if response.status_code == 200:
                    result = response.json()
                    # Parse result according to different API providers
                    try:
                        if 'choices' in result and len(result['choices']) > 0:
                            if 'message' in result['choices'][0]:
                                summary = result['choices'][0]['message']['content'].strip()
                                return summary
                            elif 'text' in result['choices'][0]:  # Some APIs may have different formats
                                summary = result['choices'][0]['text'].strip()
                                return summary
                        print(f"Unexpected result format: {result}")
                        return None
                    except Exception as parse_error:
                        print(f"Error parsing successful response: {parse_error}")
                        print(f"Response content: {result}")
                        return None
                elif response.status_code == 429:
                    # Rate limited, wait and retry
                    retry_count += 1
                    wait_time = min(2 ** retry_count, 60)  # Exponential backoff, max 60 seconds
                    print(f"Rate limited. Waiting {wait_time} seconds before retry.")
                    import time
                    time.sleep(wait_time)
                elif response.status_code >= 500:
                    # Server error, can retry
                    retry_count += 1
                    wait_time = min(2 ** retry_count, 60)
                    print(f"Server error ({response.status_code}). Waiting {wait_time} seconds before retry.")
                    print(f"Error details: {response.text}")
                    # If using OpenRouter and model may be problematic, try fallback model
                    if is_openrouter and retry_count == max_retries - 1:
                        # Last attempt use more general model
                        print("Trying with a fallback model...")
                        fallback_model = "openai/gpt-3.5-turbo"
                        data['model'] = fallback_model
                        print(f"Switched to fallback model: {fallback_model}")
                    import time
                    time.sleep(wait_time)
                else:
                    # Other errors, print details and stop retrying
                    print(f"Error generating AI summary: {response.status_code} - {response.text}")
                    print("Request data:", data)
                    return None
                    
            except requests.exceptions.RequestException as e:
                print(f"Network error during API request: {str(e)}")
                retry_count += 1
                if retry_count < max_retries:
                    wait_time = min(2 ** retry_count, 60)
                    print(f"Waiting {wait_time} seconds before retry.")
                    import time
                    time.sleep(wait_time)
                else:
                    print("Maximum retry attempts reached. Failed to generate summary.")
                    return None
        
        print("All retry attempts failed. Could not generate summary.")
        return None
    
    def process_history_file(self, history_file):
        """Process a history file and add AI summary if enabled"""
        if not self.enable_ai_summary or not self.api_key:
            return
            
        file_path = Path(history_file)
        if not file_path.exists():
            return
            
        # Read the original content
        with open(file_path, 'r') as f:
            content = f.read()
            
        # Extract repo name from filename
        repo_name = file_path.stem.split('_')[0]
        
        # Generate summary
        summary = self.generate_summary(content, repo_name)
        
        if summary:
            # Add summary to the history file if it doesn't already have one
            if "## AI Summary" not in content:
                with open(file_path, 'w') as f:
                    f.write(content)
                    f.write("\n\n## AI Summary\n\n")
                    f.write(summary)
            
            # Also create/update a repository-specific summary file
            self._update_repo_summary(repo_name, summary, content)
            
            print(f"Added AI summary to {history_file}")
    
    def _update_repo_summary(self, repo_name, summary, content):
        """Create or update repository-specific summary file"""
        summary_file = self.summaries_dir / f"{repo_name}_summary.md"
        
        # Create entry for today's summary
        today_entry = f"## Summary for {self.today}\n\n{summary}\n\n"
        
        if summary_file.exists():
            # If the file exists, add the new summary at the top
            with open(summary_file, 'r') as f:
                existing_content = f.read()
                
            # Check if today's summary already exists
            if f"## Summary for {self.today}" in existing_content:
                # Replace today's entry
                with open(summary_file, 'w') as f:
                    f.write(f"# AI Summaries for {repo_name}\n\n")
                    f.write(today_entry)
                    f.write(existing_content[existing_content.find('\n## Summary for'):])
            else:
                # Add today's entry at the top
                with open(summary_file, 'w') as f:
                    f.write(f"# AI Summaries for {repo_name}\n\n")
                    f.write(today_entry)
                    if "# AI Summaries for" in existing_content:
                        f.write(existing_content[existing_content.find('\n## Summary for'):])
                    else:
                        f.write(existing_content)
        else:
            # Create a new file
            with open(summary_file, 'w') as f:
                f.write(f"# AI Summaries for {repo_name}\n\n")
                f.write(today_entry)
                
        print(f"Updated repository summary for {repo_name}")
            
    def process_all_history_files(self):
        """Process all history files in the history directory"""
        history_dir = Path('history')
        if not history_dir.exists():
            return
            
        # Only process today's history files to avoid reprocessing old files
        today_pattern = f"*_{self.today}.md"
        for file_path in history_dir.glob(today_pattern):
            self.process_history_file(file_path)

if __name__ == "__main__":
    summarizer = AISummary()
    summarizer.process_all_history_files() 