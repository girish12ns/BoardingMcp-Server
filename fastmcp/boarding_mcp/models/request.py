from pydantic import BaseModel, EmailStr, HttpUrl, Field
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


#Project creation for the whatsp Business
class Project_creation(BaseModel):
    name:str=Field(..., description="Name of the project")

        class Config:
        json_schema_extra = {
            "example": {
               "name":"API TEST PROJECT 1"
            }
        }






class PhoneNumber(BaseModel):
    code: int = Field(..., ge=1, le=999, description="Country calling code")
    number: str = Field(..., pattern=r'^\d{7,15}$', description="Phone number without country code")

class Address(BaseModel):
    streetAddress1: str
    streetAddress2: Optional[str] = None  # Consider adding this
    city: str
    state: str
    zipPostal: str
    country: str = Field(..., pattern=r'^[A-Z]{2}$', description="Two-letter country code")

class Business(BaseModel):
    name: str
    email: EmailStr
    phone: PhoneNumber
    website: Optional[HttpUrl] = None
    address: Address
    timezone: str = Field(..., pattern=r'^UTC[+-]\d{2}:\d{2}$', description="Timezone in UTC offset format")

class AssistantPhone(BaseModel):
    displayName: str
    category: str = Field(..., description="Category like ENTERTAIN, BUSINESS, etc.")
    description: Optional[str] = ""

class Setup(BaseModel):
    business: Business
    phone: AssistantPhone

#Generating EmbeddingURLGeneration
class EmbeddingURLGeneration(BaseModel):
    businessId: str = Field(..., min_length=24, max_length=24, description="24-character business ID")
    assistantId: str = Field(..., min_length=24, max_length=24, description="24-character assistant ID")
    setup: Setup
    
    model_config = {
        "json_schema_extra": {
            "example": {
                "businessId": "63bbe4c2cd10ea720a532ez0",
                "assistantId": "63bbe4c256be217200ad1b5b",
                "setup": {
                    "business": {
                        "name": "Acme Inc.",
                        "email": "johndoe@acme.com",
                        "phone": {
                            "code": 1,
                            "number": "6505551234"
                        },
                        "website": "https://www.acme.com",
                        "address": {
                            "streetAddress1": "1 Acme Way",
                            "city": "Acme Town",
                            "state": "CA",
                            "zipPostal": "94000",
                            "country": "US"
                        },
                        "timezone": "UTC-08:00"
                    },
                    "phone": {
                        "displayName": "Acme Inc.",
                        "category": "ENTERTAIN",
                        "description": ""
                    }
                }
            }
        }
    }