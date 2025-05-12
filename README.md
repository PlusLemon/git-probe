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

### 2025-05-12T01:27:26

#### [awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps)

##### Commit Changes

No file changes detected.

#### [awesome-gpt4o-images](https://github.com/jamez-bondos/awesome-gpt4o-images)

##### Commit Changes

- [cf11a55](https://github.com/jamez-bondos/awesome-gpt4o-images/commit/cf11a55c353e728b88aa79bab684e06e0e5dc5e4) docs: update auto-generated README files - github-actions[bot]


##### File Content Changes

**README.md** (Modified, +22 -0 lines):

```diff
+ *   [案例 97：可爱温馨针织玩偶 (by @ZHO_ZHO_ZHO)](#cases-97)
+ <a id="cases-97"></a>
+ ### 案例 97：可爱温馨针织玩偶 (by [@ZHO_ZHO_ZHO](https://x.com/ZHO_ZHO_ZHO))
+ [原文链接](https://x.com/ZHO_ZHO_ZHO/status/1921148024861938077)
+ <img src="cases/97/cute_cozy_knitted_doll.png" width="300" alt="可爱温馨针织玩偶">
+ **提示词**
+ ```
+ 一张特写、构图专业的照片，展示一个手工钩织的毛线玩偶被双手轻柔地托着。玩偶造型圆润，【上传图片】人物得可爱Q版形象，色彩对比鲜明，细节丰富。持玩偶的双手自然、温柔，手指姿态清晰可见，皮肤质感与光影过渡自然，展现出温暖且真实的触感。背景轻微虚化，表现为室内环境，有温暖的木质桌面和从窗户洒入的自然光，营造出舒适、亲密的氛围。整体画面传达出精湛的工艺感与被珍视的温馨情绪。
+ **需上传参考图片：** 上传一张照片作为参考，生成其可爱Q版针织玩偶形象。
+ ---
+ [⬆️ 返回案例目录](#cases-toc)
```



#### [awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers)

##### Commit Changes

- [ed357fb](https://github.com/punkpeye/awesome-mcp-servers/commit/ed357fb8d7682070924a27bf34a7ad4005e256f6) Update README.md - Frank Fiegel
- [8a57494](https://github.com/punkpeye/awesome-mcp-servers/commit/8a57494bf10214438e39bebb3b6ce6c911f8ecbd) add mcp-js - r33drichards


##### File Content Changes

**README.md** (Modified, +2 -1 lines):

```diff
- - [r33drichards/mcp-js](https://github.com/r33drichards/mcp-js) 🦀 🏠 🐧 🍎 A Javascript code execution sandbox that uses v8 to isolate code to run AI generated javascript locally without fear. Supports heap snapshotting for persistent sessions.
+ - [r33drichards/mcp-js](https://github.com/r33drichards/mcp-js) 🦀 🏠 🐧 🍎 - A Javascript code execution sandbox that uses v8 to isolate code to run AI generated javascript locally without fear. Supports heap snapshotting for persistent sessions.
+ - [r33drichards/mcp-js](https://github.com/r33drichards/mcp-js) 🦀 🏠 🐧 🍎 A Javascript code execution sandbox that uses v8 to isolate code to run AI generated javascript locally without fear. Supports heap snapshotting for persistent sessions.
```



#### [Awesome-Dify-Workflow](https://github.com/svcvit/Awesome-Dify-Workflow)

##### Commit Changes

No file changes detected.

#### [system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools)

##### Commit Changes

No file changes detected.

