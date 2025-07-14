# Build MCP Server

## Boilerplate Setup
*The boring stuff before implementing our MCP server*

1. Initialize project with UV
2. Create virtual environment with UV
3. Install dependencies (MCP\[CLI])
4. Index Official MCP Documentation with Cursor
5. Update Project with Cursor rules

```bash
uv init mcp-shell-server
cd mcp-shell-server
uv venv
.venv\Scripts\activate # Windows
uv add mcp[cli]
del main.py # Remove default main.py
echo. > server.py # Create new server.py

cursor .
```

### Setting Up Cursor

#### Add Documentations
- Indexing & Docs => Add Doc
    1. MCP => https://modelcontextprotocol.io/introduction
    2. MCP Python SDK => https://github.com/modelcontextprotocol/python-sdk

#### Add Rules for Python
- Rules => Add Rule, from Cursor Directory (https://cursor.directory/rules/python)
    1. md .cursor & cd .cursor
    2. md rules
    3. Create python.mdc file in .cursor/rules/

### Git Clone

```bash
git clone https://github.com/emarco177/mcp-crash-course.git

cd mcp-crash-course
uv sync
```

```note
I want you to implement me a simple MCP Server from @MCP . Use the python sdk @MCP Python SDK and the server should expose one tool which is called terminal tool which will allow user to run terminal commands, make it simple
```

```
cd mcp-shell-server
uv run server.py

```
