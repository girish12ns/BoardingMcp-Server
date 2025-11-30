
import logging import setup_logging
from app.config.logging import 
from app.config.settings import settings
import requests



#intialize the log
logger = setup_logging()
module_logger = logging.getLogger(__name__)


def create_business(payload: dict) -> dict:
    """Create WhatsApp Business profile."""
    
    company = payload.get('company', 'Unknown')
    module_logger.info(f"Creating profile for: {company}")
    
    url = f"https://apis.aisensy.com/partner-apis/v1/partner/{settings.PARTNER_ID}/business"
    
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "X-AiSensy-Partner-API-Key": settings.AiSensy_API_Key
    }
    
    try:
        response = requests.post(url, headers=headers, json=payload, timeout=30)
        response.raise_for_status()
        
        module_logger.info(f"Success for:{company}")
        return response.json()
        
    except Exception as e:
        module_logger.error(f"Failed to create:{company}:{e}")
        return {"error": True, "message": str(e)}









