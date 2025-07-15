## Model Context Protocol

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
