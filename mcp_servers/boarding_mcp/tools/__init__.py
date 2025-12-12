from fastmcp import FastMCP

mcp = FastMCP(
    name="OnboardingAssistant",
    instructions="""...""",
    version="0.0.1"
)


from .get_tools import *
from .post_tools import *
from .patch_tools import *