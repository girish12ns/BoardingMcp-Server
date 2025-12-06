import logging import setup_logging
from app.config.logging import 
from app.config.settings import settings
import requests


#intialize the log
logger = setup_logging()
module_logger = logging.getLogger(__name__)



#creating Business Profile
def create_business(payload: dict) -> dict:
    """Create WhatsApp Business for  Client"""
    
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



# Creating Project for a Business
def create_project_business(payload: dict) -> dict:
    """Create WhatsApp Business for  Client"""
    

    module_logger.info(f"Creating project for Business")
    
    url = f"https://apis.aisensy.com/partner-apis/v1/partner/{settings.PARTNER_ID}/business/{settings.BUSINESS_ID}/project"
    
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


#create Generated Embedded Signup Url
def create_generated_embedded_signup_url(payload: dict) -> dict:
    """Create the embedde_signup_url """ 

    module_logger.info(f"Creating embbeded url")
    
    url = f"https://apis.aisensy.com/partner-apis/v1/partner/{settings.PARTNER_ID}/generate-waba-link"
    
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
        module_logger.error(f"Failed to embbeding_url for:{company}:{e}")
        return {"error": True, "message": str(e)}








