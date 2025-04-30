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

### 2025-04-30T01:23:12

#### [awesome-gpt4o-images](https://github.com/jamez-bondos/awesome-gpt4o-images)

##### Commit Changes

- [e8e25de](https://github.com/jamez-bondos/awesome-gpt4o-images/commit/e8e25de69f7a7bae2bd29132a094b341db95c5eb) 案例 76：怀旧动漫风格电影海报 (by photis (Sora)) (#36) - JamezBondos
- [4f8768e](https://github.com/jamez-bondos/awesome-gpt4o-images/commit/4f8768e5727da5afc4c79a0dd38528d48762c2fa) 案例 75：社交媒体相框融合 (by @dotey) (#34) - JamezBondos


##### File Content Changes

**README.md** (Modified, +41 -0 lines):

```diff
+ *   [案例 76：怀旧动漫风格电影海报 (by photis (Sora))](#examples-76)
+ <a id="examples-76"></a>
+ ## 案例 76：怀旧动漫风格电影海报 (by photis (Sora))
+ [原文链接](https://sora.com/g/gen_01jsfxrdpjfpebnyed8yaz42nf)
+ <img src="./examples/example_anime_nostalgic_poster.png" width="300" alt="High School DXD 风格怀旧动漫电影海报，带有折痕和磨损效果">
+ **提示词：**
+ ```
+ {The Lord of the Rings} 的动漫电影海报，这张动漫海报的风格参考了《恶魔高中DXD（High School DXD）》。
+ 海报上可以清晰看到折叠的痕迹，因为长时间以来被反复折叠，导致在褶皱处出现了物理性的损伤和擦痕，颜色也在部分区域出现了褪色。
+ 由于来回搬动，海报表面散布着无规律的折痕、翻折痕迹和细微划痕，这些微小但不断累积的损耗，正如无法逃避的熵增过程一样，渐渐扩展。
+ 然而，留存在我们心中的美好回忆却始终完整无缺。
+ 当你凝视这张充满怀旧气息的海报时，所能感受到的，正是那些随着岁月积累、变得无比珍贵的点点收藏物所承载的情感本质。
+ *注意：可替换提示词中的电影名{The Lord of the Rings}为其他电影，某些电影可能会触发内容审核。参考的动漫风格也可以修改。*
+ [⬆️ 返回案例目录](#example-toc)
+ *   [photis (Sora Profile)](https://sora.com/explore?user=user-sydD5ZkXZsDaL0BriQa010dQ)
+ *   [案例 75：社交媒体相框融合 (by @dotey)](#examples-75)
+ <a id="examples-75"></a>
+ ## 案例 75：社交媒体相框融合 (by [@dotey](https://x.com/dotey))
+ [原文链接](https://x.com/dotey/status/1917042797506662560)
+ <img src="./examples/example_instagram_frame_pearl_earring.png" width="300" alt="戴珍珠耳环的少女 Q版 3D 形象俏皮地坐在 Instagram 相框边缘比心">
+ 根据所附照片创建一个风格化的3D Q版人物角色，准确保留人物的面部特征和服装细节。角色的左手比心（手指上方有红色爱心元素），姿势俏皮地坐在一个巨大的Instagram相框边缘，双腿悬挂在框外。相框顶部显示用户名『Beauty』，四周漂浮着社交媒体图标（点赞、评论、转发）。
+ *注意：可替换提示词中的用户名『Beauty』及图标。原图由 Sora 生成。*
+ **需上传参考图片：** 需要上传一张图片作为参考。
```



##### AI Summary

1. **Key Changes**: Two new GPT-4 image generation examples were added - a nostalgic anime-style movie poster (Case 76) and a social media frame integration (Case 75), each with detailed prompts and implementation notes.

2. **Code Changes**: No code modifications - all changes are documentation updates (+41 lines) in README.md adding structured example sections with markdown-formatted prompts, images, and attribution links.

3. **Impact**: Enhances the repository's utility as a prompt engineering reference, particularly for anime stylization and social media content creation use cases, while maintaining consistent documentation structure.

#### [Awesome-Dify-Workflow](https://github.com/svcvit/Awesome-Dify-Workflow)

##### Commit Changes

This repository has changes, but they are not within the monitored paths.

##### File Content Changes

This repository has changes, but they are not within the monitored paths.

