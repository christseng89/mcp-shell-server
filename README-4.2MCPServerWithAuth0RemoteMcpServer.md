# Secure Remote MCP Server with Auth0 and Cloudflare

## Configure and Deploy the Remote MCP Server

Auth0 Dashboard => Applications => Applications => Create Application

- Name: Remote MCP Server
- Application Type: Regular Web Application => Create

Settings:

**Domain**
`dev-18kjovdn.auth0.com`

**Client ID**
`Fy3fY6omWWTK7ocAd7....`

**Client Secret**
`••••••••••••••••••••••••••••••••••`

**Allowed Callback URLs**
`http://localhost:8788/callback`

=> Save

---

### Creating a Cloudflare Workers KV namespace

Cloudflare Dashboard => Storage & Databases => KV => Create Instance 

**Namespace name**
OAUTH_KV

=> Create => ID (356c75bd3b4748c190....)

```cmd
cd auth0\ai\demos\remote-mcp-auth0\mcp-auth0-oidc
code .

REM Edit wrangler.jsonc with the ID
REM Create .dev.vars

```

```note .dev.vars
AUTH0_DOMAIN=....auth0.com
AUTH0_AUDIENCE=urn:todos-api
AUTH0_CLIENT_ID=Fy3fY6om...
AUTH0_CLIENT_SECRET=19OW7BzcB...
AUTH0_SCOPE=openid email profile offline_access read:todos
API_BASE_URL=http://localhost:8789
NODE_ENV=development

```

```cmd
npm i
npm run dev
    ...
    [wrangler:info] Ready on http://127.0.0.1:8788
    ▲ [WARNING] Using Workers AI always accesses your Cloudflare account in order to run AI models, and so will incur usage charges even in local development.


    ⎔ Starting local server...
```

```cmd
npx @modelcontextprotocol/inspector

```

MCP Inspector v0.16.1

**Transport Type**
SSE

**URL**
http://localhost:8788/sse

=> Connect => http://localhost:8788/authorize?... **Allow Access**

### Local Environment Summary

Inspector => MCP Server (Local) => Todos API (Local)

```cmd
REM MCP Server Local
cd auth0\ai\demos\remote-mcp-auth0\mcp-auth0-oidc
npm run dev
REM Ready on http://127.0.0.1:8788

REM Todos API
cd auth0\ai\demos\remote-mcp-auth0\todos-api
npm run dev
REM Ready on http://127.0.0.1:8789

REM Inspector
npx @modelcontextprotocol/inspector
REM http://localhost:6274/?MCP_PROXY_AUTH_TOKEN=e2a71280488fa6c72e34f8e57e0cd227722d4829ee486cbec7153f8d04a58f8f


REM Auth0 => Remote MCP Server Callback to http://localhost:8788/callback
REM Press 'Allow Access'

```

#### Quick Overview MCP Server

- index.ts
- auth.ts

#### Quick Overview Todos API

- index.ts
    read:billing
    read:todos

```note Edit .dev.vars
AUTH0_SCOPE=openid email profile offline_access read:todos read:billing

```