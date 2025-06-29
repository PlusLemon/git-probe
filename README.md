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

### 2025-06-29T01:45:50

#### [awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps)

##### Commit Changes

No file changes detected.

#### [awesome-gpt4o-images](https://github.com/jamez-bondos/awesome-gpt4o-images)

##### Commit Changes

No file changes detected.

#### [awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers)

##### Commit Changes

- [11450c6](https://github.com/punkpeye/awesome-mcp-servers/commit/11450c641daa85d2252a871763674df27a6c4a17) Merge pull request #914 from ycjcl868/patch-1 - Frank Fiegel
- [129f055](https://github.com/punkpeye/awesome-mcp-servers/commit/129f055016a8c43cef40bcd5dbb7c2ca09479cc3) Update README.md - Frank Fiegel
- [aa5948a](https://github.com/punkpeye/awesome-mcp-servers/commit/aa5948ac7a976d470fdb88e4face7d3c49861a19) Merge branch 'main' into add-xero-mcp-server - Frank Fiegel
- [fb2615f](https://github.com/punkpeye/awesome-mcp-servers/commit/fb2615f5870de2f41fedc2fc8d8e8dfe08a5528b) Merge pull request #917 from fixparser/add-new-server-fixparser - Frank Fiegel
- [7dcecbd](https://github.com/punkpeye/awesome-mcp-servers/commit/7dcecbd06d695265171f36c52561eb439210570e) Merge pull request #926 from walshhub/add-new-server - Frank Fiegel
- [3ff77a7](https://github.com/punkpeye/awesome-mcp-servers/commit/3ff77a73805c4489b366c38a7ec96bcba1473792) Merge pull request #930 from sonirico/feat/sonirico-mpc-servers - Frank Fiegel
- [a89b5cf](https://github.com/punkpeye/awesome-mcp-servers/commit/a89b5cf2c3f80490eb886b58030dff1c8d69ca5d) Merge pull request #931 from VertexStudio/add-developer-mcp - Frank Fiegel
- [f7a39b4](https://github.com/punkpeye/awesome-mcp-servers/commit/f7a39b44d480cf0a60000db530f41d3b6314b1f6) Merge pull request #937 from antejavor/update-memgraph-links - Frank Fiegel
- [cc3b048](https://github.com/punkpeye/awesome-mcp-servers/commit/cc3b0487ae41811d550e162540952283c396b826) Merge pull request #941 from gorosun/main - Frank Fiegel
- [243b416](https://github.com/punkpeye/awesome-mcp-servers/commit/243b4162d1075ea9a7ce1996a17cc4b81fa48d84) Merge pull request #949 from JimmyWhitaker/add-label-studio-mcp - Frank Fiegel


##### File Content Changes

**README.md** (Modified, +117 -16 lines):

```diff
- - [agent-infra/mcp-server-browser](https://github.com/bytedance/UI-TARS-desktop/tree/main/packages/agent-infra/mcp-servers/browser) 📇 🏠 - Browser automation capabilities using Puppeteer, both support local and remote browser connection. This server enables LLMs to interact with web pages through structured accessibility snapshots, bypassing the need for screenshots or visually-tuned models.
- MCPをサポートするクライアントのリストです。
- * ☕ – Javaコードベース
- * 🔗 - [Aggregators](#aggregators)
- * 📂 - [ブラウザ自動化](#browser-automation)
- * 🎮 - [ ゲーミング](#gaming)
- * 🔎 - [検索](#search)
- * 🔄 - [旅行と交通](#travel-and-transportation)
- ### 📂 <a name="browser-automation"></a>ブラウザ自動化
- Webコンテンツのアクセスと自動化機能。AIに優しい形式でWebコンテンツを検索、スクレイピング、処理することができます。
- - [@executeautomation/playwright-mcp-server](https://github.com/executeautomation/mcp-playwright) 🌐⚡️ - Playwrightを使用したブラウザ自動化とWebスクレイピングのためのMCPサーバー
- - [@automatalabs/mcp-server-playwright](https://github.com/Automata-Labs-team/MCP-Server-Playwright) 🌐🖱️ - Playwrightを使用したブラウザ自動化のためのMCPサーバー
- - [@modelcontextprotocol/server-puppeteer](https://github.com/modelcontextprotocol/servers/tree/main/src/puppeteer) 📇 🏠 - Webスクレイピングとインタラクションのためのブラウザ自動化
- - [@kimtaeyoon83/mcp-server-youtube-transcript](https://github.com/kimtaeyoon83/mcp-server-youtube-transcript) 📇 ☁️ - AI分析のためのYouTube字幕とトランスクリプトの取得
- - [@kimtth/mcp-aoai-web-browsing](https://github.com/kimtth/mcp-aoai-web-browsing) 🐍 🏠 - Azure OpenAIとPlaywrightを使用した「最小限の」サーバー/クライアントMCP実装。
- - [@fradser/mcp-server-apple-reminders](https://github.com/FradSer/mcp-server-apple-reminders) 📇 🏠 🍎 - macOS 用の Apple Reminders と統合された MCP サーバーです。
- - [@34892002/bilibili-mcp-js](https://github.com/34892002/bilibili-mcp-js) 📇 🏠  - Bilibiliコンテンツの検索をサポートするMCPサーバー。LangChain連携のサンプルとテストスクリプトを提供。
- - [aircodelabs/grasp](https://github.com/aircodelabs/grasp) 📇 🏠 - MCPとA2Aをネイティブにサポートする、エージェント駆動のセルフホスト型ブラウザ。
- - [cantian-ai/bazi-mcp](https://github.com/cantian-ai/bazi-mcp) 📇 🏠 ☁️ 🍎 🪟 - 包括的で正確な八字（四柱推命）の命式作成と占い情報を提供
- - [Cloudflare MCP Server](https://github.com/cloudflare/mcp-server-cloudflare) 🎖️ 📇 ☁️ - Workers、KV、R2、D1を含むCloudflareサービスとの統合
- - [Kubernetes MCP Server](https://github.com/strowk/mcp-k8s-go) - 🏎️ ☁️ MCPを通じたKubernetesクラスター操作
- - [wenhuwang/mcp-k8s-eye](https://github.com/wenhuwang/mcp-k8s-eye) 🏎️ ☁️/🏠 Kubernetes クラスターのリソース管理と、クラスターとアプリケーションの健全性ステータスの詳細な分析を提供します。
- - [weibaohui/k8m](https://github.com/weibaohui/k8m) - 🏎️ ☁️/🏠 MCPマルチクラスターKubernetesの管理と運用を提供し、管理インターフェース、ログ機能を備え、一般的な運用・開発シナリオをカバーする約50種類のツールを内蔵。標準リソースおよびCRDリソースをサポート。
- - [weibaohui/kom](https://github.com/weibaohui/kom) - 🏎️ ☁️/🏠 MCPマルチクラスターKubernetesの管理と運用を提供。SDKとして自身のプロジェクトに統合可能で、一般的な運用・開発シナリオをカバーする約50種類のツールを内蔵。標準リソースおよびCRDリソースをサポート。
- - [silenceper/mcp-k8s](https://github.com/silenceper/mcp-k8s) 🏎️ ☁️/🏠 MCP-K8Sは、AI駆動のKubernetesリソース管理ツールで、自然言語インタラクションを通じて、ユーザーがKubernetesクラスター内の任意のリソース（ネイティブリソース（DeploymentやServiceなど）やカスタムリソース（CRD）を含む）を操作できるようにします。複雑なコマンドを覚える必要はなく、要件を説明するだけで、AIが対応するクラスター操作を正確に実行し、Kubernetesの使いやすさを大幅に向上させます。
- - [portainer/portainer-mcp](https://github.com/portainer/portainer-mcp) - 🏎️ ☁️/🏠 強力なMCPサーバーで、AIアシスタントがPortainerインスタンスとシームレスに連携し、コンテナ管理、デプロイメント操作、インフラストラクチャ監視機能に自然言語でアクセスできるようにします。
- - [qiniu/qiniu-mcp-server](https://github.com/qiniu/qiniu-mcp-server) 🐍 ☁️ - 七牛クラウド製品に基づいて構築されたMCP、七牛クラウドストレージやインテリジェントマルチメディアサービスなどへのアクセスをサポートします。
- ### 💻 <a name="developer-tools"></a>開発者ツール
- - [tumf/grafana-loki-mcp](https://github.com/tumf/grafana-loki-mcp) 🐍 🏠 - Grafana API を通じて Loki ログをクエリできる MCP サーバー。
- - [@modelcontextprotocol/server-sentry](https://github.com/modelcontextprotocol/servers/tree/main/src/sentry) 🐍 ☁️ - エラートラッキングとパフォーマンス監視のためのSentry.io統合
- - [@MindscapeHQ/server-raygun](https://github.com/MindscapeHQ/mcp-server-raygun) 📇 ☁️ - クラッシュレポートとリアルユーザーモニタリングのためのRaygun API V3統合
- ### 🔎 <a name="search"></a>検索
- - [exa-labs/exa-mcp-server](https://github.com/exa-labs/exa-mcp-server) 🎖️ 📇 ☁️ – モデルコンテキストプロトコル（MCP）サーバーは、ClaudeなどのAIアシスタントがExa AI検索APIを使用してWeb検索を行うことを可能にします。この設定により、AIモデルは安全かつ制御された方法でリアルタイムのWeb情報を取得できます。
- - [Tomatio13/mcp-server-tavily](https://github.com/Tomatio13/mcp-server-tavily) ☁️ 🐍 – Tavily AI検索API
- - [firstorderai/authenticator_mcp](https://github.com/firstorderai/authenticator_mcp) 📇 🏠 🍎 🪟 🐧 – AIエージェントが認証アプリと連携できるようにする安全なMCP（Model Context Protocol）サーバー。
- - [fosdickio/binary_ninja_mcp](https://github.com/Vector35/binaryninja-mcp) 🐍 🏠 🍎 🪟 🐧 - Binary NinjaのためのMCPサーバーとブリッジ。バイナリ分析とリバースエンジニアリングのためのツールを提供します。
- - [Security Audit MCP Server](https://github.com/qianniuspace/mcp-security-audit) 📇 ☁️ 強力なモデルコンテキストプロトコル（MCP）サーバーで、npmパッケージ依存関係のセキュリティ脆弱性を監査します。リモートnpmレジストリ統合を備えたリアルタイムセキュリティチェックを使用して構築されています。
- - [GhidraMCP](https://github.com/13bm/GhidraMCP) 🐍 ☕ 🏠 - GhidraをAIアシスタントと統合するためのMCPサーバー。このプラグインはバイナリ分析を可能にし、モデルコンテキストプロトコルを通じて関数検査、逆コンパイル、メモリ探索、インポート/エクスポート分析などのツールを提供します。
- - [apify/actors-mcp-server](https://github.com/apify/actors-mcp-server) 📇 ☁️ - 3,000以上の事前構築されたクラウドツール（Actors として知られる）を使用して、ウェブサイト、eコマース、ソーシャルメディア、検索エンジン、地図などからデータを抽出できます。
- - [githejie/mcp-server-calculator](https://github.com/githejie/mcp-server-calculator) 🐍 🏠 - このサーバーは、LLMが計算機を使用して正確な数値計算を行えるようにします
- - [zcaceres/markdownify-mcp](https://github.com/zcaceres/markdownify-mcp) 📇 🏠 - ほぼすべてのファイルやウェブコンテンツをMarkdownに変換するMCPサーバー
- - [mzxrai/mcp-openai](https://github.com/mzxrai/mcp-openai) 📇 ☁️ - OpenAIの最も賢いモデルとチャット
- - [mrjoshuak/godoc-mcp](https://github.com/mrjoshuak/godoc-mcp) 🏎️ 🏠 - Goドキュメントサーバーで、AIアシスタントがパッケージドキュメントとタイプにスマートにアクセスできるようにします。
- - [fotoetienne/gqai](https://github.com/fotoetienne/gqai) 🏎 🏠 - 通常の GraphQL クエリ/ミューテーション定義ツールを使用すると、gqai によって MCP サーバーが自動的に生成されます。
- - [pierrebrunelle/mcp-server-openai](https://github.com/pierrebrunelle/mcp-server-openai) 🐍 ☁️ - MCPプロトコルを使用してClaudeから直接OpenAIモデルにクエリを送信
- - [@modelcontextprotocol/server-everything](https://github.com/modelcontextprotocol/servers/tree/main/src/everything) 📇 🏠 - MCPプロトコルのすべての機能を実行するMCPサーバー
- - [baba786/phabricator-mcp-server](https://github.com/baba786/phabricator-mcp-server) 🐍 ☁️ - Phabricator APIとの対話
- - [MarkusPfundstein/mcp-obsidian](https://github.com/MarkusPfundstein/mcp-obsidian) 🐍 ☁️ 🏠 - REST APIを介してObsidianと対話
- - [calclavia/mcp-obsidian](https://github.com/calclavia/mcp-obsidian) 📇 🏠 - これは、Claude Desktop（または任意のMCPクライアント）がMarkdownノートを含むディレクトリ（Obsidianボールトなど）を読み取り、検索できるようにするコネクタです。
- - [anaisbetts/mcp-youtube](https://github.com/anaisbetts/mcp-youtube) 📇 ☁️ - YouTube字幕の取得
- ... (32 more deletions)
+ - [agent-infra/mcp-server-browser](https://github.com/bytedance/UI-TARS-desktop/tree/main/packages/agent-infra/mcp-servers/browser) 📇 🏠 - Browser automation capabilities using Puppeteer, both support local and remote browser connection.
+ * [クライアント](#クライアント)
+ * ☕ – Javaコードベース
+ * 🌊 – C/C++コードベース
+ * 🔗 - [アグリゲーター](#aggregators)
+ * 📂 - [ブラウザ自動化](#browser-automation)
+ * 👨‍💻 - [コード実行](#code-execution)
+ * 🤖 - [コーディングエージェント](#coding-agents)
+ * 🖥️ - [コマンドライン](#command-line)
+ * 🚚 - [配送](#delivery)
+ * 🧮 - [データサイエンスツール](#data-science-tools)
+ * 📟 - [組み込みシステム](#embedded-system)
+ * 💰 - [金融・フィンテック](#finance--fintech)
+ * 🎮 - [ゲーミング](#gaming)
+ * 🎯 - [マーケティング](#marketing)
+ * 🎥 - [マルチメディア処理](#multimedia-process)
+ * 🔎 - [検索・データ抽出](#search)
+ * 🔒 - [セキュリティ](#security)
+ * 🌐 - [ソーシャルメディア](#social-media)
+ * 🏃 - [スポーツ](#sports)
+ * 🎧 - [サポート・サービス管理](#support-and-service-management)
+ * 🎧 - [テキスト読み上げ](#text-to-speech)
+ * 🚆 - [旅行と交通](#travel-and-transportation)
+ - [mindsdb/mindsdb](https://github.com/mindsdb/mindsdb) - [MindsDBを単一のMCPサーバーとして](https://docs.mindsdb.com/mcp/overview)使用し、様々なプラットフォームとデータベース間でデータを接続・統合
+ - [glenngillen/mcpmcp-server](https://github.com/glenngillen/mcpmcp-server) ☁️ 📇 🍎 🪟 🐧 - MCPサーバーのリストを提供し、日常のワークフローを改善するために使用できるサーバーをクライアントに問い合わせることができる
+ - [pipedream/pipedream](https://github.com/PipedreamHQ/pipedream/tree/master/modelcontextprotocol) ☁️ 🏠 - 8,000以上の事前構築ツールで2,500のAPIに接続し、独自のアプリでユーザー向けサーバーを管理
+ - [VeriTeknik/pluggedin-mcp-proxy](https://github.com/VeriTeknik/pluggedin-mcp-proxy) 📇 🏠 - 複数のMCPサーバーを1つのインターフェースに統合する包括的なプロキシサーバー。サーバー間でツール、プロンプト、リソース、テンプレートの発見と管理を提供し、MCPサーバー構築時のデバッグ用プレイグラウンドも含む
+ - [WayStation-ai/mcp](https://github.com/waystation-ai/mcp) ☁️ 🍎 🪟 - Claude Desktopやその他のMCPホストを、お気に入りのアプリ（Notion、Slack、Monday、Airtableなど）にシームレスかつ安全に接続。90秒以下で完了
+ - [SureScaleAI/openai-gpt-image-mcp](https://github.com/SureScaleAI/openai-gpt-image-mcp) 📇 ☁️ - OpenAI GPT画像生成・編集MCPサーバー
+ - [abhiemj/manim-mcp-server](https://github.com/abhiemj/manim-mcp-server) 🐍 🏠 🪟 🐧 - Manimを使ってアニメーションを生成するローカルMCPサーバー
+ - [burningion/video-editing-mcp](https://github.com/burningion/video-editing-mcp) 🐍 - Video Jungle Collectionから動画編集の追加、分析、検索、生成
+ - [cswkim/discogs-mcp-server](https://github.com/cswkim/discogs-mcp-server) 📇 ☁️ - Discogs APIと連携するMCPサーバー
+ - [djalal/quran-mcp-server](https://github.com/djalal/quran-mcp-server) 📇 ☁️ 公式REST API v4を通してQuran.comコーパスと連携するMCPサーバー
+ - [mikechao/metmuseum-mcp](https://github.com/mikechao/metmuseum-mcp) 📇 ☁️ - コレクション内の芸術作品を検索・表示するメトロポリタン美術館コレクションAPI統合
+ - [r-huijts/rijksmuseum-mcp](https://github.com/r-huijts/rijksmuseum-mcp) 📇 ☁️ - 芸術作品検索、詳細、コレクションのためのライクスミュージアムAPI統合
+ - [r-huijts/oorlogsbronnen-mcp](https://github.com/r-huijts/oorlogsbronnen-mcp) 📇 ☁️ - オランダの歴史的第二次大戦記録、写真、文書（1940-1945）にアクセスするためのOorlogsbronnen（War Sources）API統合
+ - [samuelgursky/davinci-resolve-mcp](https://github.com/samuelgursky/davinci-resolve-mcp) 🐍 - 動画編集、カラーグレーディング、メディア管理、プロジェクト制御の強力なツールを提供するDaVinci Resolve用MCPサーバー統合
+ - [diivi/aseprite-mcp](https://github.com/diivi/aseprite-mcp) 🐍 🏠 - Aseprite APIを使用してピクセルアートを作成するMCPサーバー
+ - [omni-mcp/isaac-sim-mcp](https://github.com/omni-mcp/isaac-sim-mcp) 📇 ☁️ - NVIDIA Isaac Sim、Lab、OpenUSDなどの自然言語制御を可能にするMCPサーバーと拡張機能
+ - [8enSmith/mcp-open-library](https://github.com/8enSmith/mcp-open-library) 📇 ☁️ - AIアシスタントが書籍情報を検索できるOpen Library API用MCPサーバー
+ - [PatrickPalmer/MayaMCP](https://github.com/PatrickPalmer/MayaMCP) 🐍 🏠 - Autodesk Maya用MCPサーバー
+ - [cantian-ai/bazi-mcp](https://github.com/cantian-ai/bazi-mcp) 📇 🏠 ☁️ 🍎 🪟 - 包括的で正確な八字（四柱推命）の命式作成と占い情報を提供
+ - [awslabs/mcp](https://github.com/awslabs/mcp) 🎖️ ☁️ - AWSサービスとリソースとのシームレスな統合のためのAWS MCPサーバー。
+ - [qiniu/qiniu-mcp-server](https://github.com/qiniu/qiniu-mcp-server) 🐍 ☁️ - 七牛クラウド製品に基づいて構築されたMCP、七牛クラウドストレージ、メディア処理サービスなどへのアクセスをサポート。
+ - [reza-gholizade/k8s-mcp-server](https://github.com/reza-gholizade/k8s-mcp-server) 🏎️ ☁️🏠 - API リソース検出、リソース管理、Pod ログ、メトリクス、イベントなど、標準化されたインターフェースを通じて Kubernetes クラスターと対話するためのツールを提供する Kubernetes モデルコンテキストプロトコル（MCP）サーバー。
+ - [VmLia/books-mcp-server](https://github.com/VmLia/books-mcp-server) 📇 ☁️ - 書籍クエリに使用されるMCPサーバーで、Cherry Studioなどの一般的なMCPクライアントに適用できます。
+ - [alexei-led/aws-mcp-server](https://github.com/alexei-led/aws-mcp-server) 🐍 ☁️ - AIアシスタントがAWS CLIコマンドを実行し、Unixパイプを使用し、マルチアーキテクチャサポート付きの安全なDocker環境で一般的なAWSタスクのプロンプトテンプレートを適用できるようにする軽量で強力なサーバー
+ - [alexei-led/k8s-mcp-server](https://github.com/alexei-led/k8s-mcp-server) 🐍 - AIアシスタントがマルチアーキテクチャサポート付きの安全なDocker環境でKubernetes CLIコマンド（`kubectl`、`helm`、`istioctl`、`argocd`）をUnixパイプを使用して安全に実行できるようにする軽量で堅牢なサーバー。
+ - [bright8192/esxi-mcp-server](https://github.com/bright8192/esxi-mcp-server) 🐍 ☁️ - MCP（Model Control Protocol）に基づくVMware ESXi/vCenter管理サーバーで、仮想マシン管理のためのシンプルなREST APIインターフェースを提供。
+ - [cloudflare/mcp-server-cloudflare](https://github.com/cloudflare/mcp-server-cloudflare) 🎖️ 📇 ☁️ - Workers、KV、R2、D1を含むCloudflareサービスとの統合
+ ... (245 more additions)
```



#### [Awesome-Dify-Workflow](https://github.com/svcvit/Awesome-Dify-Workflow)

##### Commit Changes

No file changes detected.

#### [system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools)

##### Commit Changes

- [02b0c4d](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools/commit/02b0c4d4f51ff4e2d0aed46f8eceb888c8b1d1e7) Update README.md - Lucas Valbuena


##### File Content Changes

**README.md** (Modified, +1 -1 lines):

```diff
- > Check out **[ZeroLeaks](https://zeroleaks.lucknite.lol/)**, a service designed to help startups **identify and secure** leaks in system instructions, internal tools, and model configurations. **Get a free AI security audit** to ensure your AI is protected from vulnerabilities.
+ > Check out **[ZeroLeaks](https://zeroleaks.io/)**, a service designed to help startups **identify and secure** leaks in system instructions, internal tools, and model configurations. **Get a free AI security audit** to ensure your AI is protected from vulnerabilities.
```



