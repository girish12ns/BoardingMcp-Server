"""
MCP Tool: Get WABA Information

Fetches WhatsApp Business Account (WABA) information from the AiSensy Direct API.
"""
from typing import Dict, Any

from .... import mcp
from ....clients import get_direct_api_get_client
from app import logger


@mcp.tool(
    name="get_waba_information",
    description=(
        "Fetches WhatsApp Business Account (WABA) information from the AiSensy Direct API. "
        "Returns comprehensive business details including account status, phone numbers, "
        "business verification status, and other WABA-related information associated "
        "with the authenticated account."
    ),
    tags={
        "waba",
        "whatsapp",
        "business",
        "account",
        "info",
        "get",
        "direct-api",
        "aisensy"
    },
    meta={
        "version": "1.0.0",
        "author": "AiSensy Team",
        "category": "WABA Management"
    }
)
async def get_waba_information() -> Dict[str, Any]:
    """
    Fetch WhatsApp Business Account (WABA) information.
    
    Returns:
        Dict containing:
        - success (bool): Whether the operation was successful
        - data (dict): WABA information if successful
        - error (str): Error message if unsuccessful
    """
    try:
        async with get_direct_api_get_client() as client:
            response = await client.get_business_info()
            
            if response.get("success"):
                logger.info("Successfully retrieved WABA information")
            else:
                logger.warning(
                    f"Failed to retrieve WABA information: {response.get('error')}"
                )
            
            return response
        
    except Exception as e:
        error_msg = f"Unexpected error fetching WABA information: {str(e)}"
        logger.exception(error_msg)
        return {
            "success": False,
            "error": error_msg
        }