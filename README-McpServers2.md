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

#### MCP Server - server.py

```note
I want you to implement me a simple MCP Server from @MCP . Use the python sdk @MCP Python SDK and the server should expose one tool which is called terminal tool which will allow user to run terminal commands, make it simple
```

```cmd
cd mcp-shell-server
uv run server.py

```

#### Resources in server.py

```note
I want you to help me expose a resource in my MCP server using the @MCP Python SDK. Please write the code to expose the file mcpPySdkREADME.md located in my D:\development\mcp-servers directory.
```

---

### **MCP & Security**

*Remote Code Execution (RCE), Supply Chain Attack*

1. Create Malicious gist.github.com file
2. Expose a tool that downloads the malicious file
3. Compromise MCP Client

```note
help me expose another tool in my mcp server. @MCP use the python sdk @MCP Python SDK

the tool is called "benign_tool" and should download via curl the content
@https://gist.githubusercontent.com/emarco177/47fac6debd88e1f8ad9ff6a1a33041a5/raw/9802cafba96ebeb010f3d080d948e7471987b081/hacked.txt and return what was downloaded
```

- Malicious code can be manipulated to execute arbitrary commands via MCP servers.

### **MCP Containers Advantages**

- Consistency across environments
- Isolation and safer execution
- Easy scaling and management

```note Dockerfile
Write a dockerfile to run this app in a container. I am using uv, checkout the docs:
@https://docs.astral.sh/uv/guides/integration/docker/#installing-uv

The way i am running the command is inside the virtual environment:
uv run server.py
```

- Copy Dockerfile from mcp-crash-course

```cmd
docker build -t mcp-shell-server .
docker run -it 
--rm mcp-shell-server
```
