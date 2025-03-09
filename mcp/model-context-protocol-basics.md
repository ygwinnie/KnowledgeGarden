# Model Context Protocol (MCP) 基础知识

## 什么是 MCP？

Model Context Protocol (MCP) 是一个协议框架，为 AI 模型（如 Claude）提供了与外部系统和服务进行交互的能力。它允许 AI 助手进行文件操作、代码执行、联网查询等操作，大大拓展了 AI 的应用场景和能力边界。

## MCP 的核心概念

1. **MCP 服务器**：实现特定功能的独立服务，如文件系统访问、Git 仓库操作等
2. **协议通信**：AI 模型与 MCP 服务器之间通过标准化的协议进行通信
3. **权限控制**：每个 MCP 服务器有明确的权限范围，确保安全性

## Claude 桌面应用中的 MCP 配置

Claude 桌面应用使用 `claude_desktop_config.json` 文件来配置 MCP 服务器。这个文件通常位于用户的应用配置目录中。

### 配置文件结构

```json
{
  "mcpServers": {
    "服务器名称": {
      "command": "执行命令",
      "args": ["参数列表"],
      "env": {
        "环境变量名": "环境变量值"
      }
    },
    // 其他服务器配置...
  }
}
```

## 常用 MCP 服务器

### 1. 文件系统服务器

允许 Claude 读取和写入本地文件系统中的文件。

```json
"filesystem": {
  "command": "npx",
  "args": [
    "-y",
    "@modelcontextprotocol/server-filesystem",
    "/Users/username/Documents/",
    "/Users/username/Downloads/"
  ]
}
```

**功能**：
- 读取指定目录中的文件
- 写入或修改文件
- 列出目录内容

### 2. GitHub 服务器

允许 Claude 与 GitHub 仓库进行交互。

```json
"github": {
  "command": "npx",
  "args": [
    "-y",
    "@modelcontextprotocol/server-github"
  ],
  "env": {
    "GITHUB_PERSONAL_ACCESS_TOKEN": "your_github_token"
  }
}
```

**功能**：
- 克隆仓库
- 读取仓库中的文件
- 提交更改
- 创建分支
- 推送更改到远程仓库

### 3. WCGW (Web Content Generator for Web) 服务器

提供网页内容生成和处理能力。

```json
"wcgw": {
  "command": "uv",
  "args": [
    "tool",
    "run",
    "--from",
    "wcgw@latest",
    "--python",
    "3.12",
    "wcgw_mcp"
  ]
}
```

**功能**：
- 网页内容生成
- 网页数据处理
- 内容分析

## 配置 MCP 的步骤

1. **找到配置文件位置**：
   - macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
   - Windows: `%APPDATA%\Claude\claude_desktop_config.json`

2. **编辑配置文件**：
   - 确保 JSON 格式正确
   - 添加或修改需要的 MCP 服务器配置

3. **设置必要的权限**：
   - 对于 GitHub，需要创建有适当权限的个人访问令牌
   - 对于文件系统，确保指定的路径是可访问的

4. **重启 Claude 桌面应用**：
   - 配置更改后需要重启应用才能生效

## GitHub 令牌配置

要配置 GitHub 集成，您需要：

1. **生成 GitHub 个人访问令牌**：
   - 访问 GitHub 设置 -> 开发者设置 -> 个人访问令牌
   - 创建新的令牌，赋予适当的权限（通常需要 `repo` 权限）
   - 复制生成的令牌

2. **在 MCP 配置中添加令牌**：
   ```json
   "env": {
     "GITHUB_PERSONAL_ACCESS_TOKEN": "粘贴您的令牌"
   }
   ```

3. **可选配置**：
   - `GITHUB_REPOSITORY`: 指定默认仓库，格式为 "用户名/仓库名"
   - `GITHUB_BRANCH`: 指定默认分支

## 安全注意事项

1. **令牌安全**：
   - 个人访问令牌等同于密码，应妥善保护
   - 如果怀疑令牌泄露，立即在 GitHub 中撤销并创建新令牌

2. **路径限制**：
   - 文件系统 MCP 只能访问配置中明确指定的路径
   - 尽量限制为特定工作目录，避免暴露整个系统

3. **权限最小化**：
   - 为 GitHub 令牌分配最小必要的权限
   - 可以创建专用于 Claude 的仓库或组织

## 常见问题排查

1. **MCP 服务器无法启动**：
   - 检查命令和参数是否正确
   - 确认所需工具（如 npx, uv）已安装

2. **GitHub 认证失败**：
   - 验证令牌是否有效且未过期
   - 确认令牌具有适当的权限范围

3. **文件访问错误**：
   - 检查指定的路径是否存在且可访问
   - 验证文件权限设置

## 结论

MCP 极大地扩展了 Claude 等 AI 助手的能力，使其能够与外部系统和服务交互。通过正确配置 MCP 服务器，您可以让 Claude 直接操作文件、与 GitHub 仓库协作，以及执行其他复杂任务，从而提高工作效率。