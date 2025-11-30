from fastmcp import FastMCP

# Create a basic server instance
mcp = FastMCP(name="OnboardingServer")

# You can also add instructions for how to interact with the server
mcp_with_instructions = FastMCP(
    name="onBordingAssistant",
    instructions="""This provides assistnt to on onboarding the Customer""",
    version=0.01,
    auth=None

)
