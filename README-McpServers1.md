# MCP Servers

## Install environments

MCP User's Guide => Quickstart => For Server Developers
https://modelcontextprotocol.io/quickstart/server

### Node.js Weather MCP Server
```
git clone https://github.com/modelcontextprotocol/quickstart-resources.git
cd quickstart-resources
cd weather-server-typescript
npm install
npm run build
node build/index.js
    Weather MCP Server running on stdio

node d:\development\mcp-servers\quickstart-resources\weather-server-typescript\build\index.js
    Weather MCP Server running on stdio

cd ..
```

### Python Weather MCP Server
```cmd
cd weather-server-python
uv sync
uv run weather.py
    Weather MCP Server running on stdio

cd c:\Users\samfi
weather.bat
    Weather MCP Server running on stdio

REM wsl --cd ~/projects/mcp-servers/quickstart-resources/weather-server-python -- /home/samfire5200/.local/bin/uv run weather.py
```

### MCP Servers architecture

- The Model Context Protocol (**MCP**) is explicitly designed to facilitate smooth connections between **LLM applications** and **external data sources** and **tools**, as stated in the documentation. This seamless integration allows LLMs to effectively interact with various resources, enhancing their capabilities and utility.
- An **MCP Server** serves as a lightweight program that specifically **

---

### Model Context Protocol Architecture Overview

| MCP Client | ↔ | MCP Server |
|------------|---|------------|
| - Invoke **Tools** |   | - Exposes **Tools** |
| - Queries for **Resources** |   | - Exposes **Resources** |
| - Interpolates **Prompts** |   | - Exposes **Prompts** |

| **Tools**                | **Resources**               | **Prompts**                    |
|--------------------------|-----------------------------|--------------------------------|
| *Model-Controlled*       | *Application-Controlled*    | *User-Controlled*              |
| Functions invoked by the model | Data exposed to the application | Pre-defined templates for AI interactions |
| - Retrieve / Search      | - Files                     | - Documentation Q&A            |
| - Send Message           | - DB Records                | - Transcript Summary           |
| - Update DB              | - API Responses             | - Output as JSON               |

---

## MCP 架構的兩個角色說明

### **MCP Client**

* 負責：

  * 呼叫 **Tools**（工具）
  * 查詢 **Resources**（資源）
  * 使用 **Prompts**（提示模板）去填充互動內容

→ 它相當於**AI 模型端**，或是「**使用者的代理人**」。

---

### **MCP Server**

* 負責：

  * 提供（expose）**Tools**
  * 提供 **Resources**
  * 提供 **Prompts**

→ 它相當於**後端服務端**，或是「**工具箱**、**資料庫**或 **API** 來源」。

---

## MCP 架構的三個核心概念說明

### **Tools** *(模型控制)*

* 是模型能直接呼叫的函式，例如：

  * Retrieve/Search → 搜尋資料
  * Send Message → 傳送訊息
  * Update DB → 更新資料庫

---

### **Resources** *(應用程式控制)*

* 是 MCP Server 提供的資料，例如：

  * Files → 檔案
  * DB Records → 資料庫紀錄
  * API Responses → API 回傳結果

---

### **Prompts** *(使用者控制)*

* 是已定義好的提示模板，例如：

  * Documentation Q\&A → 文件問答
  * Transcript Summary → 摘要逐字稿
  * Output as JSON → 以 JSON 格式輸出

---

### ✅ 實例說明

**例子 1 — 撰寫技術文件問答機器人**

* **場景**：

  * 使用者想建立一個 AI 助理，可以回答公司技術文件的問題。

* **MCP Server**：

  * 暴露：

    * **Tools** → 搜尋技術文件
    * **Resources** → 技術文件檔案
    * **Prompts** → Documentation Q\&A 模板

* **MCP Client**：

  * 模型收到問題：

    > 「請問產品 X 支援哪些作業系統？」
  * 呼叫 Tool → `Retrieve/Search` 技術文件
  * 查到內容 → 從 Resource `Files` 中撈資料
  * 用 Prompt `Documentation Q&A` 格式，生成回答：

    > 「產品 X 支援 Windows、Linux、macOS 系統。」

---

**例子 2 — 客服聊天機器人**

* **場景**：

  * 使用者想建立客服機器人，能回覆客戶訊息，並更新客戶資料。

* **MCP Server**：

  * 暴露：

    * **Tools** → Send Message、Update DB
    * **Resources** → 客戶紀錄 (DB Records)
    * **Prompts** → Transcript Summary (自動生成對話紀錄摘要)

* **MCP Client**：

  * 模型：

    * 收到客戶訊息 → 呼叫 `Send Message`
    * 客戶要求更新聯絡資訊 → 呼叫 `Update DB`
    * 產出摘要 → 使用 `Transcript Summary` Prompt

結果：

> 「已更新您的電話號碼。以下是本次對話摘要：…」

---

**簡單一句話**：

> 這張圖就是在說：**Client 負責請求，Server 負責提供工具、資料和提示，讓 AI 模型能完成各種任務。**

---

## MCP Inspector

- https://modelcontextprotocol.io/docs/tools/inspector

> **MCP Inspector** 是一個圖形化的除錯與測試工具，幫助開發者探索和驗證 MCP Server 的 Tools、Resources 和 Prompts，確保它們在連接到客戶端或 LLM 之前正常運作。

### ✅ MCP Inspector 使用方式

```
cd quickstart-resources\weather-server-typescript
node build\index.js
```

```
cd quickstart-resources\weather-server-typescript
npx @modelcontextprotocol/inspector

```

```
Starting MCP inspector...
⚙️ Proxy server listening on 127.0.0.1:6277
🔑 Session token: a70e7d7d79cea9f735ee7237f0e5b3df9c867b8eea1e431cb9783e746263908e
Use this token to authenticate requests or set DANGEROUSLY_OMIT_AUTH=true to disable auth

🔗 Open inspector with token pre-filled:
   http://localhost:6274/?MCP_PROXY_AUTH_TOKEN=a70e7d7d79cea9f735ee7237f0e5b3df9c867b8eea1e431cb9783e746263908e

🔍 MCP Inspector is up and running at http://127.0.0.1:6274 🚀

```

- http://localhost:6274/?MCP_PROXY_AUTH_TOKEN=a70e7d7d79cea9f735ee7237f0e5b3df9c867b8eea1e431cb9783e746263908e#resources

- **Transport Type** (STDIO)
- **Command** (node)
- **Arguments** (build/index.js)
=> Connect

---

## McpDoc

- https://langchain-ai.github.io/langgraph/llms-txt-overview/
- https://github.com/langchain-ai/mcpdoc

非常棒！你的理解 **幾乎完全正確**，但可以再更精確一點。以下用中文詳細說明：

---

### ✅ MCPDoc 是什麼？

✅ MCPDoc 是一個 **MCP Server**，專門用來即時獲取最新的 **LLM 相關官方文件或技術說明**。

> MCPDoc 就是用來「抓官方文件」的 MCP Server，幫助 AI 工具即時讀到最新 LLM 技術文件與說明，而不是抓模型內部參數。
> MCPDoc 幫 AI 工具把官方文件變成即時知識，確保回答基於最新資料。

---

### ✅ LLMs.txt 是什麼？

LLMs.txt 並 **不是直接用來獲取最新 LLM 訊息**。

- 它的真正用途是： **告訴 MCP Server：**

   * 哪些 LLM 要用（如 GPT-4、Claude 3）
   * 使用什麼參數（例如溫度、top\_p）
   * 哪些網址包含相關文件或資源（例如官方文件）

---

### ✅ MCP Server 如何用到 LLMs.txt？

→ MCP Server **根據 LLMs.txt 裡的網址 (URL)**

* 去抓取最新的文件內容
* 把抓到的內容，提供給像 Claude、Cursor 等 AI 工具
* 讓 AI 回答時，根據最新的官方文件，而不是舊的模型知識

---

#### llms.txt 長這樣：

```
[openai]
model = "gpt-4"
temperature = 0.3
docs_url = "https://platform.openai.com/docs"

[langgraph]
docs_url = "https://langchain-ai.github.io/langgraph/llms.txt"
```

---

### ✅ 總結

* ❌ LLMs.txt **不是**直接保存最新的 LLM 訊息
* ✅ 它是 MCP Server 的「導航圖」：

  * 告訴 Server 要去哪裡抓最新資料
  * 管理 LLM 設定（模型名、參數）
* MCP Server **才是真正負責去抓最新文件的角色**

---

### ✅ 安裝與啟動 MCPDoc

```cmd
git colon https://github.com/langchain-ai/mcpdoc.git
cd mcpdoc

uvx --from mcpdoc mcpdoc --urls "LangGraph:https://langchain-ai.github.io/langgraph/llms.txt" "LangChain:https://python.langchain.com/llms.txt" --transport sse --port 8087 --host localhost
```

```note
  ...
  INFO:     Waiting for application startup.
  INFO:     Application startup complete.
  INFO:     Uvicorn running on http://localhost:8087 (Press CTRL+C to quit)    
```

### 使用 MCP Inspector 檢查 MCPDoc

```cmd
cd mcpdoc
npx @modelcontextprotocol/inspector uvx --from mcpdoc mcpdoc --urls "LangGraph:https://langchain-ai.github.io/langgraph/llms.txt" "LangChain:https://python.langchain.com/llms.txt" --transport sse --port 8087 --host localhost
```

```note
Starting MCP inspector...
⚙️ Proxy server listening on 127.0.0.1:6277
🔑 Session token: 69f0505c3cb65501ab26bac0e445d6f381f4320d7dc0918544881b521d0cb531
Use this token to authenticate requests or set DANGEROUSLY_OMIT_AUTH=true to disable auth

🔗 Open inspector with token pre-filled:
   http://localhost:6274/?MCP_PROXY_AUTH_TOKEN=69f0505c3cb65501ab26bac0e445d6f381f4320d7dc0918544881b521d0cb531

🔍 MCP Inspector is up and running at http://127.0.0.1:6274 🚀
```

#### Inspector connect to MCPDoc
http://localhost:6274/?MCP_PROXY_AUTH_TOKEN=69f0505c3cb65501ab26bac0e445d6f381f4320d7dc0918544881b521d0cb531

- **Transport Type** (SSE)
- **URL** (http://localhost:8087/sse)
=> Connect -> Tools -> List Tools -> 
  - list_doc_sources => Run Tools 
  - fetch_docs => url (https://langchain-ai.github.io/langgraph/llms.txt) => Run Tools

#### Claude to work with MCPDoc

Edit claude_desktop_config.json

```
...
{
  "mcpServers": {
    ...,
    "langgraph-docs-mcp": {
    "command": "C:/Users/samfi/.local/bin/uvx",
    "args": [
      "--from",
      "D:/development/mcp-servers/mcpdoc",
      "mcpdoc",
      "--urls",
      "LangGraph:https://langchain-ai.github.io/langgraph/llms.txt LangChain:https://python.langchain.com/llms.txt",
      "--transport",
      "stdio"
      ]
    }
  }
}

```
What is LangGraph memory?
