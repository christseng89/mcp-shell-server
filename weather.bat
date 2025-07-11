@echo off
REM Change drive and directory in one step
cd /D D:\development\mcp-servers\quickstart-resources\weather-server-python

REM Activate your virtual environment
call venv\Scripts\activate.bat

REM Start the MCP server via uvicorn
uv run weather.py
