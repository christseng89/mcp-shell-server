# MCP Resources

## MCP Server Primitives

---

### TOOLS

- https://modelcontextprotocol.io/docs/concepts/tools

* Model **controlled functions** that can be invoked and does something
* **API** requests, **CRUD** operations, computations
* …

---

### RESOURCES

- https://modelcontextprotocol.io/docs/concepts/resources

* Application **controlled data** to provide contextual data to the host / client
* File contents, user data
* …

---

### PROMPTS

- https://modelcontextprotocol.io/docs/concepts/prompts

* User **controlled prompt** templates to provide LLMs with custom prompts
* Prompts to draft a research report in a specific way
* …

---

### MCP Popular Clients

- https://modelcontextprotocol.io/clients

* Most popular MCP clients support Tools ONLY

---

## Awesome MCP Servers

- https://github.com/punkpeye/awesome-mcp-servers
- https://mcp.so/
- https://glama.ai/mcp/servers

### MCP Server Examples

- Playwright 
```json
{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": [
        "@playwright/mcp@latest"
      ]
    }
  }
}
```

- Cursor Settings => Tools & Integration => Add MCP Server => Paste Playwright MCP Server configuration.
- Chat
    I want to get official MCP servers
    Visit cursor.directory and give me here 5 mcp servers examples
