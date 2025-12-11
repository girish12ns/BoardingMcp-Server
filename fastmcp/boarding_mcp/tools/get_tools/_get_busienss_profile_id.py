"""
MCP Tool: Get Business Profile by ID

Fetches the business profile details for the configured business ID.
"""
from typing import Dict, Any

from . import mcp
from ..client_manager import get_aisensy_get_client
from app import logger


@mcp.tool(
    name="get_business_profile_by_id",
    description=(
        "Fetches the business profile details for the configured business ID. "
        "Returns business information including name, status, and configuration. "
        "Requires PARTNER_ID and BUSINESS_ID to be configured in settings."
    ),
    tags={
        "business",
        "profile",
        "get",
        "business-profile",
        "aisensy"
    },
    meta={
        "version": "1.0.0",
        "author": "AiSensy Team",
        "category": "Business Management"
    }
)
async def get_business_profile_by_id() -> Dict[str, Any]:
    """
    Fetch the business profile by configured business ID.
    
    Returns:
        Dict containing:
        - success (bool): Whether the operation was successful
        - data (dict): Business profile details if successful
        - error (str): Error message if unsuccessful
    """
    try:
        async with get_aisensy_get_client() as client:
            response = await client.get_business_profile_by_id()
            
            if response.get("success"):
                logger.info("Successfully retrieved business profile by ID")
            else:
                logger.warning(
                    f"Failed to retrieve business profile: {response.get('error')}"
                )
            
            return response
        
    except Exception as e:
        error_msg = f"Unexpected error fetching business profile: {str(e)}"
        logger.exception(error_msg)
        return {
            "success": False,
            "error": error_msg
        }