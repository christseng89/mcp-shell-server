import asyncio
from dotenv import load_dotenv

from dotenv import load_dotenv
from langchain_mcp_adapters.tools import load_mcp_tools
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

load_dotenv()


llm = ChatOpenAI()

stdio_server_params = StdioServerParameters(
    command="python",
    args=["D:/development/mcp-servers/mcp-adapters/servers/math_server.py"],
)

async def main():
    print("Hello from mcp-adapters!")


if __name__ == "__main__":
    asyncio.run(main())
    #main()
