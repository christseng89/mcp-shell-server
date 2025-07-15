# MCP Clients

## LangChain MCP Adapter 

- https://github.com/langchain-ai/langchain-mcp-adapters

---

### ✅ MCP Process Flow

```markdown

| Step  | User               | App                           | LLM                           | MCP Server                      |
|-------|--------------------|-------------------------------|-------------------------------|---------------------------------|
| 1     |                    | Initializes connection →      |                               | #                               |
| 2     |                    | #                             |                               | ← Responds w available tools    |
| 3     | Sends query →      | #                             |                               |                                 |
| 4     |                    | Sends query (w MCP Tools) →   | #                             |                                 |
| 5     |                    | #                             | ← Responds with Tool Call     |                                 |
| 6     |                    | Sends Tool Call →             |                               | #                               |
| 7     |                    | #                             |                               | ← Responds with tool response   |
| 8     |                    | Sends Tool Response →         | #                             |                                 |
| 9     |                    | #                             | ← Responds w Final Answer     |                                 |
| 10    | #                  | ← Responds w Final Answer     |                               |                                 |
```

---

#### Flow Steps Description

| Step | Description                                                                                    |
| ---- | ---------------------------------------------------------------------------------------------- |
| 1    | **App → MCP Server**: Initializes connection (handshake, requests manifest of available tools) |
| 2    | **MCP Server → App**: Responds with available tools and descriptions                           |
| 3    | **User → App**: Sends a query (the original user question)                                     |
| 4    | **App → LLM**: Sends user query, including list of MCP tools                                   |
| 5    | **LLM → App**: Responds with a tool call decision (which MCP tool to invoke + its parameters)  |
| 6    | **App → MCP Server**: Sends the tool call                                                      |
| 7    | **MCP Server → App**: Responds with the tool’s output                                          |
| 8    | **App → LLM**: Sends the tool result back to the LLM                                           |
| 9    | **LLM → App**: Returns either the final answer or requests another tool call                   |
| 10   | **App → User**: Sends the final answer to the user         

✅ Note on Step 5–8

> *Step 5 to 8 are repeated until the final answer is reached.*

---

## Hands-on

```cmd for Reference ONLY
git clone -b project/langchain-mcp-adapters https://github.com/emarco177/mcp-crash-course.git langchain-mcp-adapters
cd langchain-mcp-adapters
git checkout f3567e5babb9bc91e8406d41ee82f2331f5641fe
git status

uv sync

```

### Create a new MCP Adapters Folder

- https://github.com/langchain-ai/langchain-mcp-adapters
- https://modelcontextprotocol.io/clients
- https://github.com/modelcontextprotocol/python-sdk?tab=readme-ov-file#completions

```cmd
cd ..
md mcp-adapters
cd mcp-adapters
uv init
uv venv
.venv\Scripts\activate

uv add langchain-mcp-adapters langgraph "langchain[openai]"
uv add python-dotenv
uv run main.py

REM Part II
uv run servers\math_server.py
uv run servers\weather_server.py
    INFO:     Started server process [10168]
    INFO:     Waiting for application startup.
    StreamableHTTP session manager started
    INFO:     Application startup complete.
    INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```

#### Using Postman to test Weather MCP SSE server

- http://localhost:8000/mcp/

```cmd
REM *Modify Main.py*
uv run main.py
    Hello from mcp-adapters!
```
