import logging import setup_logging
from app.config.logging import 
from app.config.settings import settings
import requests



#intialize the log
logger = setup_logging()
module_logger = logging.getLogger(__name__)


# Generating the Token 
def _send_messages(payload: dict) -> dict:
    """creating new token"""

    company = payload.get('company', 'Unknown')
    module_logger.info(f"send the message: {company}")
    
    url = f"https://backend.aisensy.com/direct-apis/t1/users/{regenrate_token}"
    
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": "Bearer f"{username}:True:{Token}
    }
    
    try:
        response = requests.post(url, headers=headers, json=payload, timeout=30)
        response.raise_for_status()
        
        module_logger.info(f"Succesfully token created:{company}")
        return response.json()
        
    except Exception as e:
        module_logger.error(f"Failed to created token:{company}:{e}")
        return {"error": True, "message": str(e)}