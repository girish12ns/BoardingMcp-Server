from pydantic import BaseModel, Field, EmailStr
from typing import Optional

#business_profile_creation
class Business_Profile_creation(BaseModel):
    display_name: str = Field(..., description="Display name for the business")
    email: EmailStr = Field(..., description="Business email address")
    company: str = Field(..., description="Company name")
    contact: str = Field(..., description="Contact phone number with country code")
    timezone: str = Field(default="Asia/Calcutta GMT+05:30", description="Timezone (default: Asia/Calcutta)")
    currency: str = Field(default="INR", description="Currency code (default: INR)")
    companySize: str = Field(..., description="Company size range (e.g., '20 - 50')")
    password: str = Field(..., min_length=8, description="Password (minimum 8 characters)")
    
    class Config:
        json_schema_extra = {
            "example": {
                "display_name": "TestAceSoft Support",
                "email": "support@acesoft.io",
                "company": "TestAceSoft Technologies",
                "contact": "919076543710",
                "timezone": "Asia/Calcutta GMT+05:30",
                "currency": "INR",
                "companySize": "20 - 50",
                "password": "Test@123458900"
            }
        }



