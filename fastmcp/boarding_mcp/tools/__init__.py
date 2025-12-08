from fastmcp import FastMCP

# Create a basic server instance
mcp = FastMCP(name="OnboardingServer")

# You can also add instructions for how to interact with the server
mcp_with_instructions = FastMCP(
    name="onboardingAssistant",
    instructions="""
    This server helps to assist the user onboarding whatsp business account """,
    version="0.01"
)