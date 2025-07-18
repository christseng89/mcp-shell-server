# Secure MCP Server with Auth0 - for Todos API

## References Info for Todos API

- https://auth0.com/
- https://www.cloudflare.com/
- https://auth0.com/blog/secure-and-deploy-remote-mcp-servers-with-auth0-and-cloudflare/
- https://github.com/cloudflare/ai/tree/main/demos/remote-mcp-auth0

## Setup Accounts

- Create an Auth0 Account.
- Create a Cloudflare Account.

## Auth0 Setup for Todos API

### Get the Todo API and Remote Auth0 MCP server samples

```cmd
md auth0
cd auth0
npm i -D wrangler@latest
npx wrangler --version
    ⛅️ wrangler 4.24.3 (update available 4.24.4)

npm i -D wrangler@latest
npx wrangler --version  

    ⛅️ wrangler 4.24.4

```

```cmd
git clone https://github.com/cloudflare/ai.git
cd ai/demos/remote-mcp-auth0/todos-api
npm i
npm run dev
    ...
    ⎔ Starting local server...
    [wrangler:info] Ready on http://127.0.0.1:8789
```

### Configure the Todos API with Auth0

- https://manage.auth0.com/dashboard/us/dev-18kjovdn/

Applications => APIs => Create API

---

**Name**\*
`Todo API`

**Identifier**\*
`urn:todos-api`

**Allow Offline Access**\*
ON

=> Create

---

#### Todo API Settings

APIs => Todo API => QuickStart
    - Select Node.js
        issuerBaseURL: 'https://dev-18kjovdn.auth0.com/'

- Todos API project, **CREATE** a .dev.vars file. With the following format:

```dotenv
AUTH0_DOMAIN=dev-18kjovdn.auth0.com
AUTH0_AUDIENCE=urn:todos-api
```

---

APIs => Todo API => Permissions

```note
Permission         Description
──────────────     ─────────────────
read:todos         read todos
read:billing       read biling
```

```cmd
npm run dev
http://127.0.0.1:8789/
    Unauthorized
```

---

APIs => Todo API => Test

```cmd
curl --request POST \
  --url https://dev-18kjovdn.auth0.com/oauth/token \
  --header 'content-type: application/json' \
  --data '{
    "client_id":"JjK0kreOPlmX0GbiR...",
    "client_secret":"WyV_6j-AAsGTw0l-J...",
    "audience":"urn:todos-api",
    "grant_type":"client_credentials"
  }'

```

```note
{"access_token":"eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVC...","expires_in":86400,"token_type":"Bearer"}

```

```Sending
curl --request GET \
  --url http://127.0.0.1:8789/api/todos \
  --header 'authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVC...'

    Unauthorized

curl --request GET \
  --url http://127.0.0.1:8789/api/me \
  --header 'authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVC...'  

  {"iss":"https://dev-18kjovdn.auth0.com/","sub":"JjK0kreO...@clients","aud":"urn:todos-api","iat":1752736981,"exp":1752823381,"gty":"client-credentials","azp":"JjK0kre..."}
```

---

#### Deploy the Todos API to Cloudflare

```cmd
cd auth0\ai\demos\remote-mcp-auth0\todos-api
npx wrangler secret put AUTH0_DOMAIN
    ...
    Successfully logged in.
    √ Enter a secret value: ... *dev-18kjovdn.auth0.com*
    🌀 Creating the secret for the Worker "todos-api"
    √ There doesn't seem to be a Worker called "todos-api". Do you want to create a new Worker with that name and add secrets to it? ... yes
    🌀 Creating new Worker "todos-api"...
    ✨ Success! Uploaded secret AUTH0_DOMAIN

npx wrangler secret put AUTH0_AUDIENCE

    √ Enter a secret value: ... urn:todos-api
    🌀 Creating the secret for the Worker "todos-api"
    ✨ Success! Uploaded secret AUTH0_AUDIENCE

npx wrangler deploy
    ...
    Uploaded todos-api (4.69 sec)
    Deployed todos-api triggers (0.79 sec)
    https://todos-api.samfire5200.workers.dev
    Current Version ID: 8cbeba2f-b0bc-491e-93d0-bc336fff6d75

```

- https://dash.cloudflare.com/

Computer (Workers) => Todos API => Settings =>

- Domains & Routes
- Variables and Secrets

```cmd
curl --request GET \
  --url https://todos-api.samfire5200.workers.dev/api/me \
  --header 'authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVC...'  

    {"iss":"https://dev-18kjovdn.auth0.com/","sub":"JjK0kreOPlmX0G...@clients","aud":"urn:todos-api","iat":1752736981,"exp":1752823381,"gty":"client-credentials","azp":"JjK0kreOPlmX0Gbi..."}

```
