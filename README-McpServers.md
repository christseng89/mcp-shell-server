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
- An **MCP Server** serves as a lightweight program that specifically **exposes** capabilities, such as **tools** or **data**, through the MCP protocol. 
- The MCP Server is designed to be **language-agnostic**, meaning it can be implemented in any programming language, allowing for flexibility and adaptability in various development environments.
- The MCP Server is intended to be **lightweight** and **stateless**, ensuring that it can run efficiently without minimal resource overhead. This lightweight nature ensures that the server can be easily deployed and maintained, making it suitable for a wide range of applications and environments.

```
                   +---------------------+
                   |      MCP Host       |
                   |                     |
                   |  Claude / Desktop   |
                   |     IDE / AI Tools  |
                   +----------+----------+
                              |
                         MCP Protocol
                              |
                       +------+-------+ 
                       | MCP Clients  | 
                       | (invoke      |
                       |  tools on    |
                       |  Servers)    |
                       +------+-------+ 
                              |
              +---------------+---------------+
              |               |               |
      +-------v-----+  +------v------+  +-----v------+
      | MCP Server  |  | MCP Server  |  | MCP Server |
      |     A       |  |     B       |  |     C      |
      +-------+-----+  +------+------|  +-----+------+
              |               |               |
      +-------v-----+  +------v------+  +-----v------+
      | Google      |  | PostgreSQL  |  | Web APIs   |
      | Drive       |  | DB          |  | (Internet, |
      |             |  |             |  |  GitHub,   |
      |             |  |             |  |  Slack)    |
      +-------------+  +-------------+  +------------+
    minimal resource overhead. This lightweight nature ensures that the server can be easily deployed and maintained, making it suitable for a wide range of applications and environments.
    
```

## The Theory of MCP Servers

MCP Client:    <----------------->  MCP Server:
- invokes Tools,                    - exposes Tools,
- queries for Resources,            - exposes Resources,
- interpolates Prompts              - exposes Prompts

---

### Tools *(Model-Controlled)*

Functions invoked by the model:

* Retrieve / Search
* Send Message
* Update DB

---

### Resources *(Application-Controlled)*

Data exposed to the application:

* Files
* DB Records
* API Responses

---

### Prompts *(User-Controlled)*

Pre-defined templates for AI interactions:

* Documentation Q\&A
* Transcript Summary
* Output as JSON

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

## ✅ 實例說明

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
