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

### 2025-07-02T01:37:03

#### [awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps)

##### Commit Changes

No file changes detected.

#### [awesome-gpt4o-images](https://github.com/jamez-bondos/awesome-gpt4o-images)

##### Commit Changes

No file changes detected.

#### [awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers)

##### Commit Changes

- [85d409a](https://github.com/punkpeye/awesome-mcp-servers/commit/85d409acb8f48e6017e28bc2c2230548e12b1835) remove duplicates - Frank Fiegel
- [ae1e614](https://github.com/punkpeye/awesome-mcp-servers/commit/ae1e61449424ac5ddf6bbc14d5ecbee0f75a1de1) sort alphabetically - Frank Fiegel
- [f3029ff](https://github.com/punkpeye/awesome-mcp-servers/commit/f3029ff542e44883bf6beacc6aaf0533f8613f65) Merge branch 'main' into main - Frank Fiegel
- [3691662](https://github.com/punkpeye/awesome-mcp-servers/commit/3691662702b1b017e5a7d61ff8c90c4be4fa72dd) Merge branch 'main' into add-dappier-mcp-server - Frank Fiegel
- [b12bd9d](https://github.com/punkpeye/awesome-mcp-servers/commit/b12bd9d124ca585a9f28a44d7b19447f3dd104c2) Merge branch 'main' into add-new-server - Frank Fiegel
- [ffc753b](https://github.com/punkpeye/awesome-mcp-servers/commit/ffc753b282445a01e4f106dbcd322d3cf6a62ee5) Merge branch 'main' into main - Frank Fiegel
- [fe0f59c](https://github.com/punkpeye/awesome-mcp-servers/commit/fe0f59c836e5aa9f2c9fe73278d4a77817f4ea6d) Merge pull request #1023 from toshihikoyanase/add-optuna-mcp - Frank Fiegel


##### File Content Changes

**README.md** (Modified, +1304 -436 lines):

```diff
- - [HuggingAGI/mcp-baostock-server](https://github.com/HuggingAGI/mcp-baostock-server) 🐍 ☁️ - MCP server based on baostock, providing access and analysis capabilities for Chinese stock market data.
- - [janswist/mcp-dexscreener](https://github.com/janswist/mcp-dexscreener) 📇 ☁️ - Real-time on-chain market prices using open and free Dexscreener API
- - [RomThpt/xrpl-mcp-server](https://github.com/RomThpt/mcp-xrpl) 📇 ☁️ - MCP server for the XRP Ledger that provides access to account information, transaction history, and network data. Allows querying ledger objects, submitting transactions, and monitoring the XRPL network.
- - [mcp-summarizer](https://github.com/0xshellming/mcp-summarizer) 📕 ☁️ - AI Summarization MCP Server, Support for multiple content types: Plain text, Web pages, PDF documents, EPUB books, HTML content
- - [sitbon/magg](https://github.com/sitbon/magg) 🍎 🪟 🐧 ☁️ 🏠 🐍 - Magg: A meta-MCP server that acts as a universal hub, allowing LLMs to autonomously discover, install, and orchestrate multiple MCP servers - essentially giving AI assistants the power to extend their own capabilities on-demand.
- - [TheLunarCompany/lunar#mcpx](https://github.com/TheLunarCompany/lunar/tree/main/mcpx) 📇 🏠  ☁️ 🍎 🪟 🐧 - MCPX is a production-ready, open-source gateway to manage MCP servers at scale—centralize tool discovery, access controls, call prioritization, and usage tracking to simplify agent workflows.
- - [julien040/anyquery](https://github.com/julien040/anyquery) 🏎️ 🏠 ☁️ - Query more than 40 apps with one binary using SQL. It can also connect to your PostgreSQL, MySQL, or SQLite compatible database. Local-first and private by design.
- - [glenngillen/mcpmcp-server](https://github.com/glenngillen/mcpmcp-server) ☁️ 📇 🍎 🪟 🐧 - A list of MCP servers so you can ask your client which servers you can use to improve your daily workflow.
- - [wegotdocs/open-mcp](https://github.com/wegotdocs/open-mcp) 📇 🏠 🍎 🪟 🐧 - Turn a web API into an MCP server in 10 seconds and add it to the open source registry: https://open-mcp.org
- - [VeriTeknik/pluggedin-mcp-proxy](https://github.com/VeriTeknik/pluggedin-mcp-proxy)  📇 🏠 - A comprehensive proxy server that combines multiple MCP servers into a single interface with extensive visibility features. It provides discovery and management of tools, prompts, resources, and templates across servers, plus a playground for debugging when building MCP servers.
- - [sxhxliang/mcp-access-point](https://github.com/sxhxliang/mcp-access-point) 📇 ☁️ 🏠 🍎 🪟 🐧 - Turn a web service into an MCP server in one click without making any code changes.
- - [hamflx/imagen3-mcp](https://github.com/hamflx/imagen3-mcp) 📇 🏠 🪟 🍎 🐧 - A powerful image generation tool using Google's Imagen 3.0 API through MCP. Generate high-quality images from text prompts with advanced photography, artistic, and photorealistic controls.
- - [SureScaleAI/openai-gpt-image-mcp](https://github.com/SureScaleAI/openai-gpt-image-mcp) 📇 ☁️ - OpenAI GPT image generation/editing MCP server.
- - [r-huijts/rijksmuseum-mcp](https://github.com/r-huijts/rijksmuseum-mcp) 📇 ☁️ - Rijksmuseum API integration for artwork search, details, and collections
- - [diivi/aseprite-mcp](https://github.com/diivi/aseprite-mcp) 🐍 🏠 - MCP server using the Aseprite API to create pixel art
- - [omni-mcp/isaac-sim-mcp](https://github.com/omni-mcp/isaac-sim-mcp) 📇 ☁️ - A MCP Server and an extension enables natural language control of NVIDIA Isaac Sim, Lab, OpenUSD and etc.
- - [8enSmith/mcp-open-library](https://github.com/8enSmith/mcp-open-library) 📇 ☁️ - A MCP server for the Open Library API that enables AI assistants to search for book information.
- - [PatrickPalmer/MayaMCP](https://github.com/PatrickPalmer/MayaMCP) 🐍 🏠 - MCP server for Autodesk Maya
- - [ahujasid/blender-mcp](https://github.com/ahujasid/blender-mcp) 🐍 - MCP server for working with Blender
- - [cantian-ai/bazi-mcp](https://github.com/cantian-ai/bazi-mcp) 📇 🏠 ☁️ 🍎 🪟 - Provides comprehensive and accurate Bazi (Chinese Astrology) charting and analysis
- - [antonkulaga/pharmacology-mcp](https://github.com/antonkulaga/pharmacology-mcp) 🐍 🏠 ☁️ - MCP server for accessing the Guide to PHARMACOLOGY database for drug, target, and ligand information.
- - [xspadex/bilibili-mcp](https://github.com/xspadex/bilibili-mcp.git) 📇 🏠 - A FastMCP-based tool that fetches Bilibili's trending videos and exposes them via a standard MCP interface.
- - [operative_sh/web-eval-agent](https://github.com/Operative-Sh/web-eval-agent) 🐍 🏠 🍎 - An MCP Server that autonomously debugs web applications with browser-use browser agents
- - [agent-infra/mcp-server-browser](https://github.com/bytedance/UI-TARS-desktop/tree/main/packages/agent-infra/mcp-servers/browser) 📇 🏠 - Browser automation capabilities using Puppeteer, both support local and remote browser connection.
- - [lightpanda-io/gomcp](https://github.com/lightpanda-io/gomcp) 🏎 🏠/☁️ 🐧/🍎 - An MCP server in Go for Lightpanda, the ultra fast headless browser designed for web automation
- - [Nebula-Block-Data/nebulablock-mcp-server](https://github.com/Nebula-Block-Data/nebulablock-mcp-server) 📇 🏠 - integrates with the fastmcp library to expose the full range of NebulaBlock API functionalities as accessible tools
- - [awslabs/mcp](https://github.com/awslabs/mcp) 🎖️ ☁️ - AWS MCP servers for seamless integration with AWS services and resources.
- - [qiniu/qiniu-mcp-server](https://github.com/qiniu/qiniu-mcp-server) 🐍 ☁️ - A MCP built on Qiniu Cloud products, supporting access to Qiniu Cloud Storage, media processing services, etc.
- - [alexbakers/mcp-ipfs](https://github.com/alexbakers/mcp-ipfs) 📇 ☁️ - upload and manipulation of IPFS storage
- - [reza-gholizade/k8s-mcp-server](https://github.com/reza-gholizade/k8s-mcp-server) 🏎️ ☁️/🏠 - A Kubernetes Model Context Protocol (MCP) server that provides tools for interacting with Kubernetes clusters through a standardized interface, including API resource discovery, resource management, pod logs, metrics, and events.
- - [VmLia/books-mcp-server](https://github.com/VmLia/books-mcp-server) 📇 ☁️ - This is an MCP server used for querying books, and it can be applied in common MCP clients, such as Cherry Studio.
- - [jedisct1/fastly-mcp-server](https://github.com/jedisct1/fastly-openapi-schema) 🎖️ 📇 ☁️ - Integration with h Fastly services
- - [nwiizo/tfmcp](https://github.com/nwiizo/tfmcp) - 🦀 🏠 - A Terraform MCP server allowing AI assistants to manage and operate Terraform environments, enabling reading configurations, analyzing plans, applying configurations, and managing Terraform state.
- - [StacklokLabs/mkp](https://github.com/StacklokLabs/mkp) 🏎️ ☁️ - MKP is a Model Context Protocol (MCP) server for Kubernetes that allows LLM-powered applications to interact with Kubernetes clusters. It provides tools for listing and applying Kubernetes resources through the MCP protocol.
- - [StacklokLabs/ocireg-mcp](https://github.com/StacklokLabs/ocireg-mcp) 🏎️ ☁️ - An SSE-based MCP server that allows LLM-powered applications to interact with OCI registries. It provides tools for retrieving information about container images, listing tags, and more.
- - [StacklokLabs/mkp](https://github.com/StacklokLabs/mkp) 🏎️ ☁️/🏠 - Model Kontext Protocol Server for Kubernetes that allows LLM-powered applications to interact with Kubernetes clusters through native Go implementation with direct API integration and comprehensive resource management
- - [erikhoward/adls-mcp-server](https://github.com/erikhoward/adls-mcp-server) 🐍 ☁️/🏠 - MCP Server for Azure Data Lake Storage. It can perform manage containers, read/write/upload/download operations on container files and manage file metadata.
- - [silenceper/mcp-k8s](https://github.com/silenceper/mcp-k8s) 🏎️ ☁️/🏠 - MCP-K8S is an AI-driven Kubernetes resource management tool that allows users to operate any resources in Kubernetes clusters through natural language interaction, including native resources (like Deployment, Service) and custom resources (CRD). No need to memorize complex commands - just describe your needs, and AI will accurately execute the corresponding cluster operations, greatly enhancing the usability of Kubernetes.
- - [redis/mcp-redis-cloud](https://github.com/redis/mcp-redis-cloud) 📇 ☁️ - Manage your Redis Cloud resources effortlessly using natural language. Create databases, monitor subscriptions, and configure cloud deployments with simple commands.
- - [portainer/portainer-mcp](https://github.com/portainer/portainer-mcp) 🏎️ ☁️/🏠 - A powerful MCP server that enables AI assistants to seamlessly interact with Portainer instances, providing natural language access to container management, deployment operations, and infrastructure monitoring capabilities.
- - [elementfm/mcp](https://gitlab.com/elementfm/mcp) 🎖️ 🐍 📇 🏠 ☁️ - Open source podcast hosting platform
- - [pydantic/pydantic-ai/mcp-run-python](https://github.com/pydantic/pydantic-ai/tree/main/mcp-run-python) 🐍 🏠 - Run Python code in a secure sandbox via MCP tool calls
- - [yepcode/mcp-server-js](https://github.com/yepcode/mcp-server-js) 🎖️ 📇 ☁️ - Execute any LLM-generated code in a secure and scalable sandbox environment and create your own MCP tools using JavaScript or Python, with full support for NPM and PyPI packages
- - [alfonsograziano/node-code-sandbox-mcp](https://github.com/alfonsograziano/node-code-sandbox-mcp) 📇 🏠 – A Node.js MCP server that spins up isolated Docker-based sandboxes for executing JavaScript snippets with on-the-fly npm dependency installation and clean teardown
- - [gwbischof/outsource-mcp](https://github.com/gwbischof/outsource-mcp) 🐍 ☁️ - Give your AI assistant its own AI assistants. For example: "Could you ask openai to generate an image of a dog?"
- - [oraios/serena](https://github.com/oraios/serena) 🐍 🏠 - A fully-featured coding agent that relies on symbolic code operations by using language servers.
- - [ezyang/codemcp](https://github.com/ezyang/codemcp) 🐍 🏠 - Coding agent with basic read, write and command line tools.
- - [stippi/code-assistant](https://github.com/stippi/code-assistant) 🦀 🏠 - Coding agent with basic list, read, replace_in_file, write, execute_command and web search tools. Supports multiple projects concurrently.
- - [rinadelph/Agent-MCP](https://github.com/rinadelph/Agent-MCP) 🐍 🏠 - A framework for creating multi-agent systems using MCP for coordinated AI collaboration, featuring task management, shared context, and RAG capabilities.
- - [tiianhk/MaxMSP-MCP-Server](https://github.com/tiianhk/MaxMSP-MCP-Server) 🐍 🏠 🎵 🎥 - A coding agent for Max (Max/MSP/Jitter), which is a visual programming language for music and multimedia.
- ... (273 more deletions)
+ - [0xshellming/mcp-summarizer](https://github.com/0xshellming/mcp-summarizer) 📕 ☁️ - AI Summarization MCP Server, Support for multiple content types: Plain text, Web pages, PDF documents, EPUB books, HTML content
+ - [glenngillen/mcpmcp-server](https://github.com/glenngillen/mcpmcp-server) ☁️ 📇 🍎 🪟 🐧 - A list of MCP servers so you can ask your client which servers you can use to improve your daily workflow.
+ - [hamflx/imagen3-mcp](https://github.com/hamflx/imagen3-mcp) 📇 🏠 🪟 🍎 🐧 - A powerful image generation tool using Google's Imagen 3.0 API through MCP. Generate high-quality images from text prompts with advanced photography, artistic, and photorealistic controls.
+ - [julien040/anyquery](https://github.com/julien040/anyquery) 🏎️ 🏠 ☁️ - Query more than 40 apps with one binary using SQL. It can also connect to your PostgreSQL, MySQL, or SQLite compatible database. Local-first and private by design.
+ - [sitbon/magg](https://github.com/sitbon/magg) 🍎 🪟 🐧 ☁️ 🏠 🐍 - Magg: A meta-MCP server that acts as a universal hub, allowing LLMs to autonomously discover, install, and orchestrate multiple MCP servers - essentially giving AI assistants the power to extend their own capabilities on-demand.
+ - [SureScaleAI/openai-gpt-image-mcp](https://github.com/SureScaleAI/openai-gpt-image-mcp) 📇 ☁️ - OpenAI GPT image generation/editing MCP server.
+ - [sxhxliang/mcp-access-point](https://github.com/sxhxliang/mcp-access-point) 📇 ☁️ 🏠 🍎 🪟 🐧 - Turn a web service into an MCP server in one click without making any code changes.
+ - [TheLunarCompany/lunar#mcpx](https://github.com/TheLunarCompany/lunar/tree/main/mcpx) 📇 🏠  ☁️ 🍎 🪟 🐧 - MCPX is a production-ready, open-source gateway to manage MCP servers at scale—centralize tool discovery, access controls, call prioritization, and usage tracking to simplify agent workflows.
+ - [VeriTeknik/pluggedin-mcp-proxy](https://github.com/VeriTeknik/pluggedin-mcp-proxy)  📇 🏠 - A comprehensive proxy server that combines multiple MCP servers into a single interface with extensive visibility features. It provides discovery and management of tools, prompts, resources, and templates across servers, plus a playground for debugging when building MCP servers.
+ - [wegotdocs/open-mcp](https://github.com/wegotdocs/open-mcp) 📇 🏠 🍎 🪟 🐧 - Turn a web API into an MCP server in 10 seconds and add it to the open source registry: https://open-mcp.org
+ - [8enSmith/mcp-open-library](https://github.com/8enSmith/mcp-open-library) 📇 ☁️ - A MCP server for the Open Library API that enables AI assistants to search for book information.
+ - [ahujasid/blender-mcp](https://github.com/ahujasid/blender-mcp) 🐍 - MCP server for working with Blender
+ - [cantian-ai/bazi-mcp](https://github.com/cantian-ai/bazi-mcp) 📇 🏠 ☁️ 🍎 🪟 - Provides comprehensive and accurate Bazi (Chinese Astrology) charting and analysis
+ - [diivi/aseprite-mcp](https://github.com/diivi/aseprite-mcp) 🐍 🏠 - MCP server using the Aseprite API to create pixel art
+ - [omni-mcp/isaac-sim-mcp](https://github.com/omni-mcp/isaac-sim-mcp) 📇 ☁️ - A MCP Server and an extension enables natural language control of NVIDIA Isaac Sim, Lab, OpenUSD and etc.
+ - [PatrickPalmer/MayaMCP](https://github.com/PatrickPalmer/MayaMCP) 🐍 🏠 - MCP server for Autodesk Maya
+ - [r-huijts/rijksmuseum-mcp](https://github.com/r-huijts/rijksmuseum-mcp) 📇 ☁️ - Rijksmuseum API integration for artwork search, details, and collections
+ - [antonkulaga/pharmacology-mcp](https://github.com/antonkulaga/pharmacology-mcp) 🐍 🏠 ☁️ - MCP server for accessing the Guide to PHARMACOLOGY database for drug, target, and ligand information.
+ - [agent-infra/mcp-server-browser](https://github.com/bytedance/UI-TARS-desktop/tree/main/packages/agent-infra/mcp-servers/browser) 📇 🏠 - Browser automation capabilities using Puppeteer, both support local and remote browser connection.
+ - [lightpanda-io/gomcp](https://github.com/lightpanda-io/gomcp) 🏎 🏠/☁️ 🐧/🍎 - An MCP server in Go for Lightpanda, the ultra fast headless browser designed for web automation
+ - [operative_sh/web-eval-agent](https://github.com/Operative-Sh/web-eval-agent) 🐍 🏠 🍎 - An MCP Server that autonomously debugs web applications with browser-use browser agents
+ - [xspadex/bilibili-mcp](https://github.com/xspadex/bilibili-mcp.git) 📇 🏠 - A FastMCP-based tool that fetches Bilibili's trending videos and exposes them via a standard MCP interface.
+ - [alexbakers/mcp-ipfs](https://github.com/alexbakers/mcp-ipfs) 📇 ☁️ - upload and manipulation of IPFS storage
+ - [awslabs/mcp](https://github.com/awslabs/mcp) 🎖️ ☁️ - AWS MCP servers for seamless integration with AWS services and resources.
+ - [elementfm/mcp](https://gitlab.com/elementfm/mcp) 🎖️ 🐍 📇 🏠 ☁️ - Open source podcast hosting platform
+ - [erikhoward/adls-mcp-server](https://github.com/erikhoward/adls-mcp-server) 🐍 ☁️/🏠 - MCP Server for Azure Data Lake Storage. It can perform manage containers, read/write/upload/download operations on container files and manage file metadata.
+ - [jedisct1/fastly-mcp-server](https://github.com/jedisct1/fastly-openapi-schema) 🎖️ 📇 ☁️ - Integration with h Fastly services
+ - [Nebula-Block-Data/nebulablock-mcp-server](https://github.com/Nebula-Block-Data/nebulablock-mcp-server) 📇 🏠 - integrates with the fastmcp library to expose the full range of NebulaBlock API functionalities as accessible tools
+ - [nwiizo/tfmcp](https://github.com/nwiizo/tfmcp) - 🦀 🏠 - A Terraform MCP server allowing AI assistants to manage and operate Terraform environments, enabling reading configurations, analyzing plans, applying configurations, and managing Terraform state.
+ - [portainer/portainer-mcp](https://github.com/portainer/portainer-mcp) 🏎️ ☁️/🏠 - A powerful MCP server that enables AI assistants to seamlessly interact with Portainer instances, providing natural language access to container management, deployment operations, and infrastructure monitoring capabilities.
+ - [qiniu/qiniu-mcp-server](https://github.com/qiniu/qiniu-mcp-server) 🐍 ☁️ - A MCP built on Qiniu Cloud products, supporting access to Qiniu Cloud Storage, media processing services, etc.
+ - [redis/mcp-redis-cloud](https://github.com/redis/mcp-redis-cloud) 📇 ☁️ - Manage your Redis Cloud resources effortlessly using natural language. Create databases, monitor subscriptions, and configure cloud deployments with simple commands.
+ - [reza-gholizade/k8s-mcp-server](https://github.com/reza-gholizade/k8s-mcp-server) 🏎️ ☁️/🏠 - A Kubernetes Model Context Protocol (MCP) server that provides tools for interacting with Kubernetes clusters through a standardized interface, including API resource discovery, resource management, pod logs, metrics, and events.
+ - [silenceper/mcp-k8s](https://github.com/silenceper/mcp-k8s) 🏎️ ☁️/🏠 - MCP-K8S is an AI-driven Kubernetes resource management tool that allows users to operate any resources in Kubernetes clusters through natural language interaction, including native resources (like Deployment, Service) and custom resources (CRD). No need to memorize complex commands - just describe your needs, and AI will accurately execute the corresponding cluster operations, greatly enhancing the usability of Kubernetes.
+ - [StacklokLabs/mkp](https://github.com/StacklokLabs/mkp) 🏎️ ☁️ - MKP is a Model Context Protocol (MCP) server for Kubernetes that allows LLM-powered applications to interact with Kubernetes clusters. It provides tools for listing and applying Kubernetes resources through the MCP protocol.
+ - [StacklokLabs/mkp](https://github.com/StacklokLabs/mkp) 🏎️ ☁️/🏠 - Model Kontext Protocol Server for Kubernetes that allows LLM-powered applications to interact with Kubernetes clusters through native Go implementation with direct API integration and comprehensive resource management
+ - [StacklokLabs/ocireg-mcp](https://github.com/StacklokLabs/ocireg-mcp) 🏎️ ☁️ - An SSE-based MCP server that allows LLM-powered applications to interact with OCI registries. It provides tools for retrieving information about container images, listing tags, and more.
+ - [VmLia/books-mcp-server](https://github.com/VmLia/books-mcp-server) 📇 ☁️ - This is an MCP server used for querying books, and it can be applied in common MCP clients, such as Cherry Studio.
+ - [alfonsograziano/node-code-sandbox-mcp](https://github.com/alfonsograziano/node-code-sandbox-mcp) 📇 🏠 – A Node.js MCP server that spins up isolated Docker-based sandboxes for executing JavaScript snippets with on-the-fly npm dependency installation and clean teardown
+ - [gwbischof/outsource-mcp](https://github.com/gwbischof/outsource-mcp) 🐍 ☁️ - Give your AI assistant its own AI assistants. For example: "Could you ask openai to generate an image of a dog?"
+ - [pydantic/pydantic-ai/mcp-run-python](https://github.com/pydantic/pydantic-ai/tree/main/mcp-run-python) 🐍 🏠 - Run Python code in a secure sandbox via MCP tool calls
+ - [yepcode/mcp-server-js](https://github.com/yepcode/mcp-server-js) 🎖️ 📇 ☁️ - Execute any LLM-generated code in a secure and scalable sandbox environment and create your own MCP tools using JavaScript or Python, with full support for NPM and PyPI packages
+ - [ezyang/codemcp](https://github.com/ezyang/codemcp) 🐍 🏠 - Coding agent with basic read, write and command line tools.
+ - [gabrielmaialva33/winx-code-agent](https://github.com/gabrielmaialva33/winx-code-agent) 🦀 🏠 - A high-performance Rust reimplementation of WCGW for code agents, providing shell execution and advanced file management capabilities for LLMs via MCP.
+ - [oraios/serena](https://github.com/oraios/serena) 🐍 🏠 - A fully-featured coding agent that relies on symbolic code operations by using language servers.
+ - [rinadelph/Agent-MCP](https://github.com/rinadelph/Agent-MCP) 🐍 🏠 - A framework for creating multi-agent systems using MCP for coordinated AI collaboration, featuring task management, shared context, and RAG capabilities.
+ - [stippi/code-assistant](https://github.com/stippi/code-assistant) 🦀 🏠 - Coding agent with basic list, read, replace_in_file, write, execute_command and web search tools. Supports multiple projects concurrently.
+ - [tiianhk/MaxMSP-MCP-Server](https://github.com/tiianhk/MaxMSP-MCP-Server) 🐍 🏠 🎵 🎥 - A coding agent for Max (Max/MSP/Jitter), which is a visual programming language for music and multimedia.
+ - [VertexStudio/developer](https://github.com/VertexStudio/developer) 🦀 🏠 🍎 🪟 🐧 - Comprehensive developer tools for file editing, shell command execution, and screen capture capabilities
+ - [automateyournetwork/pyATS_MCP](https://github.com/automateyournetwork/pyATS_MCP) - Cisco pyATS server enabling structured, model-driven interaction with network devices.
+ ... (505 more additions)
```



#### [Awesome-Dify-Workflow](https://github.com/svcvit/Awesome-Dify-Workflow)

##### Commit Changes

No file changes detected.

#### [system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools)

##### Commit Changes

- [9a42317](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools/commit/9a42317870443d6ba70d6b1d67faf9a602fa6f83) Update README.md - Lucas Valbuena


##### File Content Changes

**README.md** (Modified, +1 -1 lines):

```diff
- > **Latest Update:** 30/06/2025
+ > **Latest Update:** 02/07/2025
```



