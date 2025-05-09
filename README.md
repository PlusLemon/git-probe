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

### 2025-05-09T01:24:30

#### [awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps)

##### Commit Changes

No file changes detected.

#### [awesome-gpt4o-images](https://github.com/jamez-bondos/awesome-gpt4o-images)

##### Commit Changes

- [b5d81f9](https://github.com/jamez-bondos/awesome-gpt4o-images/commit/b5d81f96a8bc5434b1df21e4d3352e4aaa32925a) docs: update auto-generated README files - github-actions[bot]


##### File Content Changes

**README.md** (Modified, +23 -0 lines):

```diff
+ *   [案例 92：透视3D出屏效果 (by @ZHO_ZHO_ZHO)](#cases-92)
+ <a id="cases-92"></a>
+ ### 案例 92：透视3D出屏效果 (by [@ZHO_ZHO_ZHO](https://x.com/ZHO_ZHO_ZHO))
+ [原文链接](https://x.com/ZHO_ZHO_ZHO/status/1920355982703509588)
+ <img src="cases/92/perspective-3d-pop-out-effect.png" width="300" alt="透视3D出屏效果">
+ **提示词**
+ ```
+ 超写实，从上往下俯视角拍摄，一个美丽的ins模特【安妮海瑟薇 / 见参考图片】，有着精致美丽的妆容和时尚的造型，站在一部被人托起的智能手机屏幕上，画面营造出强烈的透视错觉。强调女孩从手机中站出来的三维效果。她戴着黑框眼镜，穿着高街风，俏皮地摆着可爱的pose。手机屏幕被处理成深色地板，像是一个小舞台。场景使用强烈的强制透视（forced perspective）表现手掌、手机与女孩之间的比例差异。背景为干净的灰色，使用柔和室内光，浅景深，整体风格为超现实写实合成。透视特别强
+ *注意： 可将提示词中的【安妮海瑟薇】替换为其他人物名称。或者使用一张人物照片作为参考图片。*
+ **需上传参考图片：** 可使用一张人物照片作为参考图片。本示例的参考图片是[《戴珍珠耳环的少女》](./references/Meisje_met_de_parel.jpg)。
+ ---
+ [⬆️ 返回案例目录](#cases-toc)
```



#### [awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers)

##### Commit Changes

- [a2dd679](https://github.com/punkpeye/awesome-mcp-servers/commit/a2dd6794413781d66adb80d4199334d92b2ece90) Merge pull request #855 from olalonde/patch-2 - Frank Fiegel
- [a665ada](https://github.com/punkpeye/awesome-mcp-servers/commit/a665adad83708e967a03529faf5b9b0d5744c07a) Add the MCP server for Fastly - Frank Denis


##### File Content Changes

**README.md** (Modified, +2 -0 lines):

```diff
+ - [olalonde/mcp-human](https://github.com/olalonde/mcp-human) 📇 ☁️ - When your LLM needs human assistance (through AWS Mechanical Turk)
+ - [jedisct1/fastly-mcp-server](https://github.com/jedisct1/fastly-openapi-schema) 🎖️ 📇 ☁️ - Integration with h Fastly services
```



#### [Awesome-Dify-Workflow](https://github.com/svcvit/Awesome-Dify-Workflow)

##### Commit Changes

No file changes detected.

#### [system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools)

##### Commit Changes

No file changes detected.

