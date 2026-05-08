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

### 2026-05-08T02:50:48

#### [awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps)

##### Commit Changes

- [18454ec](https://github.com/Shubhamsaboo/awesome-llm-apps/commit/18454ecfd628fae20039bd0ba09bc0c4d39fd77e) Use signal emoji for earnings call analyst - Shubhamsaboo
- [b463ffc](https://github.com/Shubhamsaboo/awesome-llm-apps/commit/b463ffc974e09e0fce1fd39f1b78351a5cae7677) Polish earnings call analyst entry - Shubhamsaboo
- [854f521](https://github.com/Shubhamsaboo/awesome-llm-apps/commit/854f521186089273bfda0480a27524396bb0d612) Add earnings call analyst agent - Shubhamsaboo


##### File Content Changes

**README.md** (Modified, +6 -4 lines):

```diff
- | [🧾 Earnings Call Analyst Agent](advanced_ai_agents/single_agent_apps/earnings_call_analyst_agent/) | YouTube earnings calls become quote-synced analyst cards with ADK, Gemini, filings, and grounded market news | ADK + Gemini |
- *   [🧾 Earnings Call Analyst Agent](advanced_ai_agents/single_agent_apps/earnings_call_analyst_agent/)
- | [📈 Earnings Call Analyst Agent](advanced_ai_agents/single_agent_apps/earnings_call_analyst_agent/) | YouTube earnings calls become quote-synced analyst cards with ADK, Gemini, filings, and grounded market news | ADK + Gemini |
- *   [📈 Earnings Call Analyst Agent](advanced_ai_agents/single_agent_apps/earnings_call_analyst_agent/)
+ | [📡 Earnings Call Analyst Agent](advanced_ai_agents/single_agent_apps/earnings_call_analyst_agent/) | YouTube earnings calls become quote-synced analyst cards with ADK, Gemini, filings, and grounded market news | ADK + Gemini |
+ *   [📡 Earnings Call Analyst Agent](advanced_ai_agents/single_agent_apps/earnings_call_analyst_agent/)
+ | [🧾 Earnings Call Analyst Agent](advanced_ai_agents/single_agent_apps/earnings_call_analyst_agent/) | YouTube earnings calls become quote-synced analyst cards with ADK, Gemini, filings, and grounded market news | ADK + Gemini |
+ *   [🧾 Earnings Call Analyst Agent](advanced_ai_agents/single_agent_apps/earnings_call_analyst_agent/)
+ | [📈 Earnings Call Analyst Agent](advanced_ai_agents/single_agent_apps/earnings_call_analyst_agent/) | YouTube earnings calls become quote-synced analyst cards with ADK, Gemini, filings, and grounded market news | ADK + Gemini |
+ *   [📈 Earnings Call Analyst Agent](advanced_ai_agents/single_agent_apps/earnings_call_analyst_agent/)
```



#### [awesome-gpt4o-images](https://github.com/jamez-bondos/awesome-gpt4o-images)

##### Commit Changes

No file changes detected.

#### [awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers)

##### Commit Changes

No file changes detected.

#### [Awesome-Dify-Workflow](https://github.com/svcvit/Awesome-Dify-Workflow)

##### Commit Changes

No file changes detected.

#### [system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools)

##### Commit Changes

- [b4adf2b](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools/commit/b4adf2bce980a19a9f81bcd951902fa93010f1dd) Update Latitude links to new landing page with UTMs - Paula Cavero


##### File Content Changes

**README.md** (Modified, +3 -3 lines):

```diff
- <a href="https://github.com/latitude-dev/latitude-llm">
- ### [Issue Tracking for AI Agents](https://github.com/latitude-dev/latitude-llm)
- [Open Source Monitoring platform](https://github.com/latitude-dev/latitude-llm)
+ <a href="https://latitude.so/?utm_source=github&utm_medium=readme&utm_campaign=sponsorship">
+ ### [Issue Tracking for AI Agents](https://latitude.so/?utm_source=github&utm_medium=readme&utm_campaign=sponsorship)
+ [Open Source Monitoring platform](https://latitude.so/?utm_source=github&utm_medium=readme&utm_campaign=sponsorship)
```



