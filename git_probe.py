#!/usr/bin/env python3
import os
import yaml
import datetime
import requests
import base64
import re
from pathlib import Path
try:
    from dotenv import load_dotenv
    # 加载.env文件中的环境变量
    load_dotenv()
except ImportError:
    print("python-dotenv package not found. Environment variables from .env file will not be loaded.")
    # 如果dotenv未安装，仍可继续，但不会从.env文件加载
    pass

from ai_summary import AISummary

class GitProbe:
    def __init__(self):
        self.config = self.load_yaml('config.yaml')
        self.probe_config = self.load_yaml('probe.yaml')
        
        # 优先使用环境变量，然后是配置文件
        self.github_token = os.environ.get('GH_TOKEN') or self.config.get('github_token')
        self.today = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d')
        self.yesterday = (datetime.datetime.now(datetime.timezone.utc) - 
                         datetime.timedelta(days=1)).strftime('%Y-%m-%d')
        
        # Create history directory if it doesn't exist
        self.history_dir = Path('history')
        self.history_dir.mkdir(exist_ok=True)
        
        # Load configuration values with defaults
        self.max_diff_lines = self.config.get('max_diff_lines', 30)
        self.show_diff = self.config.get('show_diff', True)
        
        # Initialize AI summary if enabled
        self.enable_ai_summary = self.config.get('enable_ai_summary', False)
        if self.enable_ai_summary:
            self.ai_summary = AISummary()
        
    def load_yaml(self, filename):
        with open(filename, 'r') as file:
            return yaml.safe_load(file) or {}
            
    def get_github_headers(self):
        return {
            'Authorization': f'token {self.github_token}',
            'Accept': 'application/vnd.github.v3+json'
        }
        
    def get_file_content(self, repo_url, branch, file_path):
        # Extract owner and repo from URL
        parts = repo_url.rstrip('/').split('/')
        owner, repo = parts[-2], parts[-1]
        
        api_url = f'https://api.github.com/repos/{owner}/{repo}/contents/{file_path}?ref={branch}'
        response = requests.get(api_url, headers=self.get_github_headers())
        
        if response.status_code == 200:
            content = response.json()
            return base64.b64decode(content['content']).decode('utf-8')
        return None
        
    def get_commits_for_path(self, repo_url, branch, path=None, since_date=None):
        # Extract owner and repo from URL
        parts = repo_url.rstrip('/').split('/')
        owner, repo = parts[-2], parts[-1]
        
        api_url = f'https://api.github.com/repos/{owner}/{repo}/commits'
        params = {'sha': branch}
        
        if path:
            params['path'] = path
            
        if since_date:
            params['since'] = since_date
            
        response = requests.get(api_url, headers=self.get_github_headers(), params=params)
        
        if response.status_code == 200:
            return response.json()
        return []
        
    def check_repo_has_any_commits(self, repo_url, branch, since_date=None):
        """Check if repository has any commits regardless of path"""
        parts = repo_url.rstrip('/').split('/')
        owner, repo = parts[-2], parts[-1]
        
        api_url = f'https://api.github.com/repos/{owner}/{repo}/commits'
        params = {'sha': branch}
        
        if since_date:
            params['since'] = since_date
            
        response = requests.get(api_url, headers=self.get_github_headers(), params=params)
        
        if response.status_code == 200:
            return len(response.json()) > 0
        return False
        
    def get_commit_details(self, repo_url, commit_sha):
        """Get detailed changes in a commit"""
        parts = repo_url.rstrip('/').split('/')
        owner, repo = parts[-2], parts[-1]
        
        api_url = f'https://api.github.com/repos/{owner}/{repo}/commits/{commit_sha}'
        response = requests.get(api_url, headers=self.get_github_headers())
        
        if response.status_code == 200:
            return response.json()
        return None
        
    def compare_commits(self, repo_url, base_commit, head_commit):
        # Extract owner and repo from URL
        parts = repo_url.rstrip('/').split('/')
        owner, repo = parts[-2], parts[-1]
        
        api_url = f'https://api.github.com/repos/{owner}/{repo}/compare/{base_commit}...{head_commit}'
        response = requests.get(api_url, headers=self.get_github_headers())
        
        if response.status_code == 200:
            return response.json()
        return None
        
    def get_file_diff(self, repo_url, commit_sha, file_path):
        """Get the diff for a specific file in a commit"""
        parts = repo_url.rstrip('/').split('/')
        owner, repo = parts[-2], parts[-1]
        
        # Get the diff using the GitHub API
        headers = self.get_github_headers()
        headers['Accept'] = 'application/vnd.github.v3.diff'
        
        api_url = f'https://api.github.com/repos/{owner}/{repo}/commits/{commit_sha}'
        response = requests.get(api_url, headers=headers)
        
        if response.status_code == 200:
            diff_text = response.text
            
            # Parse the diff to find the specific file
            file_diffs = diff_text.split('diff --git')
            
            for diff in file_diffs:
                if file_path in diff:
                    return diff
                    
        return None
        
    def get_repository_files(self, repo_url, branch):
        """Get all files in a repository"""
        parts = repo_url.rstrip('/').split('/')
        owner, repo = parts[-2], parts[-1]
        
        # Get the repository's default branch files recursively
        api_url = f'https://api.github.com/repos/{owner}/{repo}/git/trees/{branch}?recursive=1'
        response = requests.get(api_url, headers=self.get_github_headers())
        
        files = []
        if response.status_code == 200:
            tree = response.json().get('tree', [])
            # Only include blob objects (files)
            files = [item['path'] for item in tree if item['type'] == 'blob']
        
        return files
            
    def archive_previous_readme(self):
        """Archive previous README content to history folder"""
        try:
            # Read current README
            with open('README.md', 'r') as f:
                readme_content = f.read()
            
            # Extract the Latest Changes section
            changes_match = re.search(r'## Latest Changes\s+(.+?)(?=\n#|\Z)', readme_content, re.DOTALL)
            
            if changes_match:
                changes_content = changes_match.group(1).strip()
                
                # Check if there's a date header
                date_match = re.search(r'### (\d{4}-\d{2}-\d{2})', changes_content)
                if date_match:
                    date = date_match.group(1)
                    
                    # Save to history file
                    archive_file = self.history_dir / f"readme_changes_{date}.md"
                    with open(archive_file, 'w') as f:
                        f.write(f"# README Changes for {date}\n\n")
                        f.write(changes_content)
                    
                    print(f"Archived previous README changes to {archive_file}")
        except Exception as e:
            print(f"Error archiving README: {str(e)}")
            
    def archive_latest_changes(self):
        """Archive entire Latest Changes section to a single history file"""
        try:
            # 按行读取README.md文件
            with open('README.md', 'r') as f:
                lines = f.readlines()
            
            latest_changes_content = []
            found_latest_changes = False
            date_str = self.yesterday  # 默认使用昨天的日期
            
            for i, line in enumerate(lines):
                # 找到Latest Changes部分
                if line.strip() == "## Latest Changes":
                    found_latest_changes = True
                    continue
                
                # 如果已经找到Latest Changes部分
                if found_latest_changes:
                    latest_changes_content.append(line)
            
            # 如果找到了内容
            if latest_changes_content:
                # 移除开头和结尾的空行
                while latest_changes_content and latest_changes_content[0].strip() == "":
                    latest_changes_content.pop(0)
                while latest_changes_content and latest_changes_content[-1].strip() == "":
                    latest_changes_content.pop()
                
                if latest_changes_content:
                    # 保存到历史文件
                    archive_file = self.history_dir / f"changes_{self.yesterday}.md"
                    with open(archive_file, 'w') as f:
                        f.write(f"# Changes Summary for {date_str}\n\n")
                        f.writelines(latest_changes_content)
                    
                    print(f"Archived Latest Changes to {archive_file}")
                else:
                    print("No content found in Latest Changes section after date header")
            else:
                print("No content found in Latest Changes section")
                
        except Exception as e:
            print(f"Error archiving Latest Changes: {str(e)}")
            
    def update_readme(self, all_changes, all_file_changes, all_summaries):
        # Archive Latest Changes section as a daily history file
        self.archive_latest_changes()
        
        # Update README with latest changes from all repositories
        try:
            with open('README.md', 'r') as f:
                readme_content = f.read()
                
            # Find and remove the entire "Latest Changes" section
            if "## Latest Changes" in readme_content:
                # Split the content at the Latest Changes header
                parts = readme_content.split('## Latest Changes')
                # Keep the first part (content before Latest Changes)
                first_part = parts[0]
                
                # Check if there's another section after Latest Changes
                remaining_content = parts[1]
                next_section_match = re.search(r'\n##\s+', remaining_content)
                if next_section_match:
                    # If there's another section, keep everything from that point forward
                    remaining_part = remaining_content[next_section_match.start():]
                else:
                    # If no next section, just use an empty string
                    remaining_part = ""
                
                # Reconstruct with empty Latest Changes section
                readme_content = first_part + "## Latest Changes\n\n" + remaining_part
            else:
                # If section doesn't exist, add it at the end
                readme_content += "\n\n## Latest Changes\n\n"
            
            # Add today's date and changes
            readme_content += f"### {self.today}\n\n"
            
            # Add each repository's changes with its own section
            for repo_name in all_changes.keys():
                readme_content += f"#### {repo_name}\n\n"
                
                # Add commit changes
                readme_content += "##### Commit Changes\n\n"
                readme_content += all_changes[repo_name]
                readme_content += "\n\n"
                
                # Add file content changes
                readme_content += "##### File Content Changes\n\n"
                readme_content += all_file_changes[repo_name]
                readme_content += "\n\n"
                
                # Add AI summary if available
                if repo_name in all_summaries:
                    readme_content += "##### AI Summary\n\n"
                    readme_content += all_summaries[repo_name]
                    readme_content += "\n\n"
            
            with open('README.md', 'w') as f:
                f.write(readme_content)
        except Exception as e:
            print(f"Error updating README: {str(e)}")

    def format_changes(self, repo_name, repo_url, commits, max_commits=10):
        # 限制显示数量
        display_commits = commits[:max_commits]
        
        # Format commits into markdown
        changes = ""
        
        for i, commit in enumerate(display_commits):
            author = commit.get('commit', {}).get('author', {}).get('name', 'Unknown')
            message = commit.get('commit', {}).get('message', '').split('\n')[0]
            commit_url = commit.get('html_url', '')
            sha = commit.get('sha', '')[:7]  # 可能是合并后的多个SHA
            
            changes += f"- [{sha}]({commit_url}) {message} - {author}\n"
            
        return changes
    
    def format_file_changes_by_file(self, repo_url, commits, max_diff_lines=None):
        """Format file content changes grouped by file rather than commit"""
        if not commits:
            return "No file changes detected."
        
        # Use provided max_diff_lines or fall back to config value
        max_diff_lines = max_diff_lines or self.max_diff_lines
            
        # First collect all changed files from all commits
        all_files = {}
        for commit in commits[:5]:  # Limit to 5 most recent commits
            commit_details = self.get_commit_details(repo_url, commit.get('sha'))
            if commit_details and 'files' in commit_details:
                for file_info in commit_details['files']:
                    filename = file_info.get('filename')
                    if not filename:
                        continue
                        
                    # Initialize file entry if it doesn't exist
                    if filename not in all_files:
                        all_files[filename] = {
                            'additions': 0,
                            'deletions': 0,
                            'status': file_info.get('status', 'modified'),
                            'commits': []
                        }
                    
                    # Update stats
                    all_files[filename]['additions'] += file_info.get('additions', 0)
                    all_files[filename]['deletions'] += file_info.get('deletions', 0)
                    all_files[filename]['commits'].append(commit.get('sha'))
        
        # Now format the changes grouped by file
        formatted_changes = ""
        
        for filename, info in all_files.items():
            # Skip files with no changes or binary files
            if info['additions'] + info['deletions'] == 0:
                continue
                
            # Get extension for syntax highlighting
            file_ext = Path(filename).suffix.lstrip('.')
            if not file_ext:
                file_ext = 'text'
                
            # Create a header for the file
            status_text = {
                'added': '新增',
                'modified': '修改',
                'removed': '删除',
                'renamed': '重命名'
            }.get(info['status'], info['status'])
            
            formatted_changes += f"**{filename}** ({status_text}, +{info['additions']} -{info['deletions']}行):\n\n"
            
            # Always get combined diff content from all commits for processing
            # (needed for AI summary even if not displayed)
            all_additions = []
            all_deletions = []
            
            for commit_sha in info['commits']:
                diff = self.get_file_diff(repo_url, commit_sha, filename)
                if diff:
                    diff_lines = diff.split('\n')
                    
                    for line in diff_lines:
                        if line.startswith('+') and not line.startswith('+++'):
                            content = line[1:].strip()
                            if content and content not in all_additions:
                                all_additions.append(content)
                        elif line.startswith('-') and not line.startswith('---'):
                            content = line[1:].strip()
                            if content and content not in all_deletions:
                                all_deletions.append(content)
            
            # Format and display deletions and additions only if show_diff is enabled
            if self.show_diff and (all_deletions or all_additions):
                formatted_changes += f"```diff\n"
                
                # Limit the number of lines to display
                max_lines = max(1, max_diff_lines // 2)
                
                # Display deletions
                for i, line in enumerate(all_deletions[:max_lines]):
                    formatted_changes += f"- {line}\n"
                if len(all_deletions) > max_lines:
                    formatted_changes += f"- ... ({len(all_deletions) - max_lines} more deletions)\n"
                    
                # Display additions
                for i, line in enumerate(all_additions[:max_lines]):
                    formatted_changes += f"+ {line}\n"
                if len(all_additions) > max_lines:
                    formatted_changes += f"+ ... ({len(all_additions) - max_lines} more additions)\n"
                    
                formatted_changes += "```\n\n"
            
        return formatted_changes or "No significant content changes detected."
    
    def is_file_in_paths(self, file_path, paths):
        """Check if a file is within any of the specified paths"""
        for path in paths:
            if path == file_path:  # Exact file match
                return True
            elif file_path.startswith(path + '/'):  # File is in directory
                return True
        return False
        
    def run(self):
        all_changes = {}
        all_file_changes = {}
        all_summaries = {}
        
        # Process each repository in probe.yaml
        for repo_name, repo_config in self.probe_config.get('repositories', {}).items():
            repo_url = repo_config.get('url')
            branch = repo_config.get('branch', 'main')
            paths = repo_config.get('paths', [])
            
            # Get yesterday's date for filtering commits
            yesterday = (datetime.datetime.now(datetime.timezone.utc) - 
                         datetime.timedelta(days=1)).isoformat()
            
            repo_changes = ""
            
            # If paths is empty, monitor the entire repository
            if not paths:
                print(f"No paths specified for {repo_name}, monitoring entire repository")
                commits = self.get_commits_for_path(repo_url, branch, None, since_date=yesterday)
                
                if commits:
                    repo_changes += self.format_changes(f"{repo_name} - entire repository", repo_url, commits)
                    # Format file changes by file, not by commit
                    repo_file_changes = self.format_file_changes_by_file(repo_url, commits)
            else:
                # Process specified paths
                all_commits = []
                
                for path in paths:
                    commits = self.get_commits_for_path(repo_url, branch, path, since_date=yesterday)
                    if commits:
                        # Format the commits
                        path_changes = self.format_changes(f"{repo_name} - {path}", repo_url, commits)
                        repo_changes += path_changes
                        
                        # Add unique commits to the list
                        for commit in commits:
                            if commit not in all_commits:
                                all_commits.append(commit)
                
                # Format all file changes after gathering all commits
                if all_commits:
                    # Get all file changes but filter them to only include files in the specified paths
                    all_changed_files = {}
                    
                    # First, collect all changed files
                    for commit in all_commits[:5]:  # Limit to 5 most recent commits
                        commit_details = self.get_commit_details(repo_url, commit.get('sha'))
                        if commit_details and 'files' in commit_details:
                            for file_info in commit_details['files']:
                                filename = file_info.get('filename')
                                if not filename:
                                    continue
                                    
                                # Only include files that are in the specified paths
                                if self.is_file_in_paths(filename, paths):
                                    # Initialize file entry if it doesn't exist
                                    if filename not in all_changed_files:
                                        all_changed_files[filename] = {
                                            'additions': 0,
                                            'deletions': 0,
                                            'status': file_info.get('status', 'modified'),
                                            'commits': []
                                        }
                                    
                                    # Update stats
                                    all_changed_files[filename]['additions'] += file_info.get('additions', 0)
                                    all_changed_files[filename]['deletions'] += file_info.get('deletions', 0)
                                    all_changed_files[filename]['commits'].append(commit.get('sha'))
                    
                    # Now format the changes for files in the specified paths
                    if all_changed_files:
                        formatted_changes = ""
                        
                        for filename, info in all_changed_files.items():
                            # Skip files with no changes or binary files
                            if info['additions'] + info['deletions'] == 0:
                                continue
                                
                            # Get extension for syntax highlighting
                            file_ext = Path(filename).suffix.lstrip('.')
                            if not file_ext:
                                file_ext = 'text'
                                
                            # Create a header for the file
                            status_text = {
                                'added': '新增',
                                'modified': '修改',
                                'removed': '删除',
                                'renamed': '重命名'
                            }.get(info['status'], info['status'])
                            
                            formatted_changes += f"**{filename}** ({status_text}, +{info['additions']} -{info['deletions']}行):\n\n"
                            
                            # Always get combined diff content for processing (needed for AI summary)
                            all_additions = []
                            all_deletions = []
                            
                            for commit_sha in info['commits']:
                                diff = self.get_file_diff(repo_url, commit_sha, filename)
                                if diff:
                                    diff_lines = diff.split('\n')
                                    
                                    for line in diff_lines:
                                        if line.startswith('+') and not line.startswith('+++'):
                                            content = line[1:].strip()
                                            if content and content not in all_additions:
                                                all_additions.append(content)
                                        elif line.startswith('-') and not line.startswith('---'):
                                            content = line[1:].strip()
                                            if content and content not in all_deletions:
                                                all_deletions.append(content)
                            
                            # Format and display the diff only if show_diff is enabled
                            if self.show_diff and (all_deletions or all_additions):
                                formatted_changes += f"```diff\n"
                                
                                # Limit the number of lines to display
                                max_lines = max(1, self.max_diff_lines // 2)
                                
                                # Display deletions
                                for i, line in enumerate(all_deletions[:max_lines]):
                                    formatted_changes += f"- {line}\n"
                                if len(all_deletions) > max_lines:
                                    formatted_changes += f"- ... ({len(all_deletions) - max_lines} more deletions)\n"
                                    
                                # Display additions
                                for i, line in enumerate(all_additions[:max_lines]):
                                    formatted_changes += f"+ {line}\n"
                                if len(all_additions) > max_lines:
                                    formatted_changes += f"+ ... ({len(all_additions) - max_lines} more additions)\n"
                                    
                                formatted_changes += "```\n\n"
                        
                        repo_file_changes = formatted_changes or "No significant content changes detected."
                    else:
                        # Check if the repository has any commits at all
                        if self.check_repo_has_any_commits(repo_url, branch, since_date=yesterday):
                            repo_file_changes = "该仓库有变更，但变更不在监控的 paths 范围内。"
                        else:
                            repo_file_changes = "No file changes detected."
                else:
                    # Check if the repository has any commits at all
                    if self.check_repo_has_any_commits(repo_url, branch, since_date=yesterday):
                        repo_file_changes = "该仓库有变更，但变更不在监控的 paths 范围内。"
                        # Also add a note to the commit changes section
                        if not repo_changes:
                            repo_changes = "该仓库有变更，但变更不在监控的 paths 范围内。"
                    else:
                        repo_file_changes = "No file changes detected."
            
            # Save changes to history and update all_changes
            if repo_changes:
                all_changes[repo_name] = repo_changes
                all_file_changes[repo_name] = repo_file_changes

                # If AI summary is enabled, get the summary for this repo
                if self.enable_ai_summary:
                    all_summaries[repo_name] = self.ai_summary.generate_summary(repo_changes, repo_file_changes, repo_name)
        
        # Update README with all changes
        if all_changes:
            self.update_readme(all_changes, all_file_changes, all_summaries)
            print(f"Updated README.md with changes for {self.today}")
        else:
            print(f"No changes found for {self.today}")

if __name__ == "__main__":
    probe = GitProbe()
    probe.run()