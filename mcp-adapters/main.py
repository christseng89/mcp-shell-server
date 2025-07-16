import asyncio
from dotenv import load_dotenv

from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain_core.messages import HumanMessage
# from langchain_mcp_adapters.tools import load_mcp_tools
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent
# from mcp import ClientSession, StdioServerParameters
# from mcp.client.stdio import stdio_client

load_dotenv()


llm = ChatOpenAI(model='gpt-4o-mini')

# stdio_server_params = StdioServerParameters(
#     command="python",
#     args=["D:/development/mcp-servers/mcp-adapters/servers/math_server.py"],
# )

client = MultiServerMCPClient(
    {
        "math": {
            "command": "python",
            # Make sure to update to the full absolute path to your math_server.py file
            "args": ["D:/development/mcp-servers/mcp-adapters/servers/math_server.py"],
            "transport": "stdio",
        },
        "weather": {
            # Make sure you start your weather server on port 8000
            "url": "http://localhost:8000/mcp/",
            "transport": "streamable_http",
        }
    }
)
async def main():
    # print("Hello from mcp-adapters!")
    # async with stdio_client(stdio_server_params) as (read,write):    
    #     async with ClientSession(read_stream=read, write_stream=write) as session:
    #         await session.initialize()
    #         print("Session initialized")
    #         tools = await load_mcp_tools(session)
    tools = await client.get_tools()
    print (f"Loaded {len(tools)} tools")
    for tool in tools:
        print(f"Tool: {tool.name}, Description: {tool.description}")
    
    print("\nCreating react agent")
    agent = create_react_agent(llm,tools)
    math_response = await agent.ainvoke({"messages": [HumanMessage(content="What is 54 + 2 * 3?")]})
    print(math_response["messages"][-1].content)

    weather_response = await agent.ainvoke({"messages": "what is the weather in nyc?"})
    print(weather_response["messages"][-1].content)


if __name__ == "__main__":
    asyncio.run(main())
    #main()
