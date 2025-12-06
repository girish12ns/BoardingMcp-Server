from fastmcp import FastMCP
from fastmcp.server.auth.providers.jwt import StaticTokenVerifier
from fastmcp.boarding_mcp.tools.boarding_tools import (
    create_business,
    create_project_business,
    create_generated_embedded_signup_url
)
from model.request import (
    Business_Profile_creation,
    Project_creation,
    embedde_signup_url  
)

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

#business profile creation
@mcp.tool(
    name="whatsapp_business_profile_creation",
    description="Creates a new WhatsApp Business profile with company information including display name, email, contact details, timezone, currency preferences, company size, and secure password. This tool sets up the foundational business account for WhatsApp Business API integration, enabling businesses to communicate with customers professionally through the WhatsApp platform.",
    tags={"Business profile", "whatsapp business", "profile creation",},
    meta={"version": "0.01", "author": "Girish"}
)
def creating_business_profile(payload:Business_Profile_creation)->dict:
    """Creation of whatsp Business profile Creation"""
    return create_business(payload)
    
# project creation for Business
@mcp.tool(
    name="whatsap project creation for Business",
    description="Creates the project for whatsp for Business",
    tags={"project creation", "project creation for whatsapp business"},
    meta={"version": "0.01", "author": "Girish"}
)
def creating_project_business(payload:Project_creation)->dict:
    """Creation of whatsp Business profile Creation"""
    return reate_project_business(payload)


#Generating embbeding url link
@mcp.tool(
    name="generating Embedding url for company ",
    description="Creating the embbeding url",
    tags={"creation embbeding url", "embbeding url"},
    meta={"version": "0.01", "author": "Girish"}
)
def embedded_signup_url(payload:EmbeddingURLGeneration)->dict:
    """Creation of whatsp Business profile Creation"""
    return create_generated_embedded_signup_url(payload)
    
    


















