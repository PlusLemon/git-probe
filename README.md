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

### 2025-05-04T01:39:05

#### [awesome-gpt4o-images](https://github.com/jamez-bondos/awesome-gpt4o-images)

##### Commit Changes

- [7c47cb4](https://github.com/jamez-bondos/awesome-gpt4o-images/commit/7c47cb4719dba5959618f5e8f5a4b511c0b34de3) 输出根目录README - JamezBondos


##### File Content Changes

**README.md** (Modified, +1013 -614 lines):

```diff
- <a id="contents-toc"></a>
- - [🎨 GPT‑4o介绍](#gpt4o-toc)
- - [📖 案例目录](#example-toc)
- - [🛠️ 工具介绍](#tools-toc)
- - [💡 提示词技巧](#prompting-toc)
- - [🤝 如何贡献](#contribute-toc)
- - [🙏 致谢](#acknowledgements-toc)
- - [🌟 Star历史](#starhistory-toc)
- <a id="gpt4o-toc"></a>
- <a id="example-toc"></a>
- *   [案例 80：代码风格名片 (by @umesh_ai)](#examples-80)
- *   [案例 79：乐高城市景观 (by @dotey)](#examples-79)
- *   [案例 78：玻璃材质重塑 (by @egeberkina)](#examples-78)
- *   [案例 77：水晶球故事场景 (by @dotey)](#examples-77)
- *   [案例 76：怀旧动漫风格电影海报 (by photis (Sora))](#examples-76)
- *   [案例 75：社交媒体相框融合 (by @dotey)](#examples-75)
- *   [案例 74：Logo 形状创意书架 (by @umesh_ai)](#examples-74)
- *   [案例 73：定制Q版钥匙串 (by @azed_ai)](#examples-73)
- *   [案例 72：金色吊坠项链 (by @azed_ai)](#examples-72)
- *   [案例 71：迷你 Cyberpunk 傾斜移軸景觀 (by terry623)](#examples-71)
- *   [案例 70：原创宝可梦生成 (by @Anima_Labs)](#examples-70)
- *   [案例 69：剪影艺术 (by @umesh_ai)](#examples-69)
- *   [案例 68：未来主义 Logo 交易卡 (by @hewarsaber)](#examples-68)
- *   [案例 67：超写实3D游戏 (by @ZHO_ZHO_ZHO)](#examples-67)
- *   [案例 66：创意丝绸宇宙 (by @ZHO_ZHO_ZHO)](#examples-66)
- *   [案例 65：Trompe-l'œil 三维空间艺术 (by @madpencil_)](#examples-65)
- *   [案例 64：蒸汽朋克机械鱼 (by @f-is-h)](#examples-64)
- *   [案例 63：Emoji 奶油雪糕 (by @ZHO_ZHO_ZHO)](#examples-63)
- *   [案例 62：可爱珐琅别针 (by @gnrlyxyz)](#examples-62)
- *   [案例 61：虚构推文截图 (爱因斯坦) (by @egeberkina)](#examples-61)
- *   [案例 60：Emoji 簇绒地毯 (by @gizakdag)](#examples-60)
- *   [案例 59：彩色矢量艺术海报 (by @michaelrabone)](#examples-59)
- *   [案例 58：云彩艺术 (by @umesh_ai)](#examples-58)
- *   [案例 57：8位像素图标 (by @egeberkina)](#examples-57)
- *   [案例 56：迷你 3D 建筑 (by @dotey)](#examples-56)
- *   [案例 55：低多边形 (Low-Poly) 3D 渲染 (by @azed_ai)](#examples-55)
- *   [案例 54：“极其平凡”的iPhone自拍 (by @jiamimaodashu)](#examples-54)
- *   [案例 53：Emoji 充气感靠垫 (by @gizakdag)](#examples-53)
- *   [案例 52：纸艺风格 Emoji 图标 (by @egeberkina)](#examples-52)
- *   [案例 51：护照入境印章 (by @ZHO_ZHO_ZHO)](#examples-51)
- *   [案例 50：物理破坏效果卡片 (劳拉) (by @op7418)](#examples-50)
- *   [案例 49：时尚杂志封面风格 (by @dotey)](#examples-49)
- *   [案例 48：体素风格 3D 图标转换 (by @BrettFromDJ)](#examples-48)
- *   [案例 47：键盘ESC 键帽微型立体模型 (by @egeberkina)](#examples-47)
- *   [案例 46：快乐胶囊制作 (by @ZHO_ZHO_ZHO)](#examples-46)
- *   [案例 45：3D Q版大学拟人化形象 (by @dotey)](#examples-45)
- *   [案例 44：RPG 风格角色卡片制作 (by @berryxia_ai)](#examples-44)
- *   [案例 43：Q版可爱俄罗斯套娃 (戴珍珠耳环的少女) (by @ZHO_ZHO_ZHO)](#examples-43)
- *   [案例 42：3D Q版情侣水晶球 (by @balconychy)](#examples-42)
- *   [案例 41：微型立体场景 (孙悟空三打白骨精) (by @dotey)](#examples-41)
- ... (392 more deletions)
+ <a id="table-of-contents"></a>
+ - [🎨 GPT‑4o介绍](#gpt4o-intro)
+ - [📖 案例目录](#cases-toc)
+ - [🛠️ 工具介绍](#tools-intro)
+ - [💡 提示词技巧](#prompting-tips)
+ - [🤝 如何贡献](#how-to-contribute)
+ - [🙏 致谢](#acknowledgements)
+ - [🌟 Star历史](#star-history)
+ ---
+ <a id="gpt4o-intro"></a>
+ <a id="cases-toc"></a>
+ *   [案例 82：特色城市天气预报 (by @dotey)](#cases-82)
+ *   [案例 81：半透明玻璃质感变换 (by @azed_ai)](#cases-81)
+ *   [案例 80：代码风格名片 (by @umesh_ai)](#cases-80)
+ *   [案例 79：乐高城市景观 (by @dotey)](#cases-79)
+ *   [案例 78：玻璃材质重塑 (by @egeberkina)](#cases-78)
+ *   [案例 77：水晶球故事场景 (by @dotey)](#cases-77)
+ *   [案例 76：怀旧动漫风格电影海报 (by photis (Sora))](#cases-76)
+ *   [案例 75：社交媒体相框融合 (by @dotey)](#cases-75)
+ *   [案例 74：Logo 形状创意书架 (by @umesh_ai)](#cases-74)
+ *   [案例 73：定制Q版钥匙串 (by @azed_ai)](#cases-73)
+ *   [案例 72：金色吊坠项链 (by @azed_ai)](#cases-72)
+ *   [案例 71：迷你 Cyberpunk 傾斜移軸景觀 (by terry623)](#cases-71)
+ *   [案例 70：原创宝可梦生成 (by @Anima_Labs)](#cases-70)
+ *   [案例 69：剪影艺术 (by @umesh_ai)](#cases-69)
+ *   [案例 68：未来主义 Logo 交易卡 (by @hewarsaber)](#cases-68)
+ *   [案例 67：超写实3D游戏 (by @ZHO_ZHO_ZHO)](#cases-67)
+ *   [案例 66：创意丝绸宇宙 (by @ZHO_ZHO_ZHO)](#cases-66)
+ *   [案例 65：Trompe-l'œil 三维空间艺术 (by @madpencil_)](#cases-65)
+ *   [案例 64：蒸汽朋克机械鱼 (by @f-is-h)](#cases-64)
+ *   [案例 63：Emoji 奶油雪糕 (by @ZHO_ZHO_ZHO)](#cases-63)
+ *   [案例 62：可爱珐琅别针 (by @gnrlyxyz)](#cases-62)
+ *   [案例 61：虚构推文截图 (爱因斯坦) (by @egeberkina)](#cases-61)
+ *   [案例 60：Emoji 簇绒地毯 (by @gizakdag)](#cases-60)
+ *   [案例 59：彩色矢量艺术海报 (by @michaelrabone)](#cases-59)
+ *   [案例 58：云彩艺术 (by @umesh_ai)](#cases-58)
+ *   [案例 57：8位像素图标 (by @egeberkina)](#cases-57)
+ *   [案例 56：迷你 3D 建筑 (by @dotey)](#cases-56)
+ *   [案例 55：低多边形 (Low-Poly) 3D 渲染 (by @azed_ai)](#cases-55)
+ *   [案例 54：“极其平凡”的iPhone自拍 (by @jiamimaodashu)](#cases-54)
+ *   [案例 53：Emoji 充气感靠垫 (by @gizakdag)](#cases-53)
+ *   [案例 52：纸艺风格 Emoji 图标 (by @egeberkina)](#cases-52)
+ *   [案例 51：护照入境印章 (by @M_w14_)](#cases-51)
+ *   [案例 50：物理破坏效果卡片 (劳拉) (by @op7418)](#cases-50)
+ *   [案例 49：时尚杂志封面风格 (by @dotey)](#cases-49)
+ *   [案例 48：体素风格 3D 图标转换 (by @BrettFromDJ)](#cases-48)
+ *   [案例 47：键盘ESC 键帽微型立体模型 (by @egeberkina)](#cases-47)
+ *   [案例 46：快乐胶囊制作 (by @ZHO_ZHO_ZHO)](#cases-46)
+ *   [案例 45：3D Q版大学拟人化形象 (by @dotey)](#cases-45)
+ *   [案例 44：RPG 风格角色卡片制作 (by @berryxia_ai)](#cases-44)
+ ... (396 more additions)
```



##### AI Summary

1. The commit restructures the README's table of contents with clearer anchor IDs (e.g., `#gpt4o-intro` instead of `#gpt4o-toc`) and adds 2 new showcase cases (82, 81) while updating a contributor credit for case 51.

2. Significant changes include +1013/-614 lines, primarily reorganizing content with more descriptive section labels and adding a separator (`---`) between the TOC and content sections.

3. This improves documentation clarity and maintainability, though breaks existing deep links using old anchor IDs. The update keeps the showcase current by adding latest GPT-4o image generation examples while preserving most existing content.

#### [awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers)

##### Commit Changes

No file changes detected.

##### File Content Changes

No file changes detected.

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

