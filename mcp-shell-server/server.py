from mcp.server.fastmcp import FastMCP
import asyncio
import subprocess
from typing import Dict, Any

# Create the MCP server
mcp = FastMCP("Terminal Tool Server")

@mcp.tool(name="terminal_tool")
async def terminal_tool(command: str) -> Dict[str, Any]:
    """
    Run a terminal command and return the output.
    Args:
        command: The command to execute in the terminal
    Returns:
        A dictionary containing stdout, stderr, and return code
    """
    try:
        process = await asyncio.create_subprocess_shell(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        stdout, stderr = await process.communicate()
        return {
            "stdout": stdout.decode() if stdout else "",
            "stderr": stderr.decode() if stderr else "",
            "return_code": process.returncode
        }
    except Exception as e:
        return {
            "stdout": "",
            "stderr": f"Error executing command: {str(e)}",
            "return_code": -1
        }

if __name__ == "__main__":
    print("Starting MCP server...")
    mcp.run("stdio") 
