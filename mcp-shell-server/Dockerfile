FROM python:3.12-slim

# Install curl and build dependencies
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

# Install uv (official method)
RUN pip install --upgrade pip && pip install uv

# Set workdir
WORKDIR /app

# Copy only the files needed for install first (for better caching)
COPY mcp-shell-server/pyproject.toml mcp-shell-server/uv.lock ./

# Create virtual environment and install dependencies
RUN uv venv .venv && \
    .venv/bin/uv pip install mcp && \
    .venv/bin/uv pip install --no-deps .

# Copy the rest of the app
COPY mcp-shell-server/ .

# Set environment variables for uv venv
ENV VIRTUAL_ENV="/app/.venv"
ENV PATH="/app/.venv/bin:$PATH"

# Expose no ports (stdio transport)

# Entrypoint: run the server using uv in the venv
ENTRYPOINT ["uv", "run", "server.py"]
