from fastmcp import FastMCP
from fastmcp.server.auth.providers.jwt import StaticTokenVerifier

# Define development tokens and their associated claims
verifier = StaticTokenVerifier(
    tokens={
        "dev-girish-token": {
            "client_id": "girish12n@gmail.com",
            "scopes": ["read:data", "write:data", "admin:users"]
        },
        "dev-guest-token": {
            "client_id": "guest-user",
            "scopes": ["read:data"]
        }
    },
    required_scopes=["read:data"]
)

mcp = FastMCP(name="onBoardingServer", auth=verifier)

