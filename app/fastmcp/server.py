from fastmcp import FastMCP

mcp=FastMCP(name="OnboardingServer")


mcp_with_instructions = = FastMCP(
    name="onboardingAssistant",
    instructions= """
        This server provides onboardingTools.
    """,
    version=0.1
)


@mcp.tool
def multiply(a: float, b: float) -> float:
    """Multiplies two numbers together."""
    return a * b



@mcp.resource("data://config")
def get_config() -> dict:
    """Provides the application configuration."""
    return {"theme": "dark", "version": "1.0"}


from fastmcp import FastMCP
from fastmcp.prompts.prompt import Message, PromptMessage, TextContent

mcp = FastMCP(name="PromptServer")

# Basic prompt returning a string (converted to user message automatically)
@mcp.prompt
def ask_about_topic(topic: str) -> str:
    """Generates a user message asking for an explanation of a topic."""
    return f"Can you please explain the concept of '{topic}'?"

# Prompt returning a specific message type
@mcp.prompt
def generate_code_request(language: str, task_description: str) -> PromptMessage:
    """Generates a user message requesting code generation."""
    content = f"Write a {language} function that performs the following task: {task_description}"
    return PromptMessage(role="user", content=TextContent(type="text", text=content))


@mcp.prompt(
    name="analyze_data_request",          # Custom prompt name
    description="Creates a request to analyze data with specific parameters",  # Custom description
    tags={"analysis", "data"},            # Optional categorization tags
    meta={"version": "1.1", "author": "data-team"}  # Custom metadata
)
def data_analysis_prompt(
    data_uri: str = Field(description="The URI of the resource containing the data."),
    analysis_type: str = Field(default="summary", description="Type of analysis.")
) -> str:
    """This docstring is ignored when description is provided."""
    return f"Please perform a '{analysis_type}' analysis on the data found at {data_uri}."


@mcp.tool(tags={"public", "utility"})
def public_tool() -> str:
    return "This tool is public"

@mcp.tool(tags={"internal", "admin"})
def admin_tool() -> str:
    return "This tool is for admins only"


from fastmcp import FastMCP
from fastmcp.server.auth.providers.auth0 import Auth0Provider

# The Auth0Provider utilizes Auth0 OIDC configuration
auth_provider = Auth0Provider(
    config_url="https://.../.well-known/openid-configuration",  # Your Auth0 configuration URL
    client_id="tv2ObNgaZAWWhhycr7Bz1LU2mxlnsmsB",               # Your Auth0 application Client ID
    client_secret="vPYqbjemq...",                               # Your Auth0 application Client Secret
    audience="https://...",                                     # Your Auth0 API audience
    base_url="http://localhost:8000",                           # Must match your application configuration
    # redirect_path="/auth/callback"                            # Default value, customize if needed
)

mcp = FastMCP(name="Auth0 Secured App", auth=auth_provider)

# Add a protected tool to test authentication
@mcp.tool
async def get_token_info() -> dict:
    """Returns information about the Auth0 token."""
    from fastmcp.server.dependencies import get_access_token

    token = get_access_token()

    return {
        "issuer": token.claims.get("iss"),
        "audience": token.claims.get("aud"),
        "scope": token.claims.get("scope")
    }