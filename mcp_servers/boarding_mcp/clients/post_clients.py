"""This is POST Aisensy Client"""

from typing import Dict, Any, Optional
import aiohttp
import asyncio

from .base_client import AiSensyBaseClient
from app import settings, logger


class AiSensyPostClient(AiSensyBaseClient):
    """Client for all POST operations."""

    async def create_business_profile(
        self,
        display_name: str,
        email: str,
        company: str,
        contact: str,
        timezone: str,
        currency: str,
        company_size: str,
        password: str
    ) -> Dict[str, Any]:
        """
        Create a new business profile in the AiSensy API.

        Args:
            display_name: Display name for the business.
            email: Business email address.
            company: Company name.
            contact: Contact number.
            timezone: Timezone (e.g., "Asia/Calcutta GMT+05:30").
            currency: Currency code (e.g., "INR").
            company_size: Size of the company (e.g., "10 - 20").
            password: Password for the business account.

        Returns:
            Dict[str, Any]: A dictionary containing the created business profile 
            as returned by the AiSensy API.
        """
        if not settings.PARTNER_ID:
            logger.error("Missing PARTNER_ID in settings")
            return {
                "success": False,
                "error": "Missing required field: partner_id"
            }

        url = f"{self.BASE_URL}/partner/{settings.PARTNER_ID}/business"
        payload = {
            "display_name": display_name,
            "email": email,
            "company": company,
            "contact": contact,
            "timezone": timezone,
            "currency": currency,
            "companySize": company_size,
            "password": password
        }
        logger.debug(f"Creating business profile at: {url}")

        try:
            session = await self._get_session()
            async with session.post(url, json=payload) as response:
                if response.status in (200, 201):
                    data = await response.json()
                    logger.info("Successfully created business profile")
                    return {"success": True, "data": data}

                error_text = await response.text()
                return self._handle_error(response.status, error_text)

        except aiohttp.ClientConnectorError:
            logger.error("Network connection error")
            return {"success": False, "error": "Network connection error"}
        except aiohttp.ClientTimeout:
            logger.error("Request timeout")
            return {"success": False, "error": "Request timeout"}
        except Exception as e:
            logger.exception("Unexpected error")
            return {"success": False, "error": str(e)}

    async def create_project(self, name: str) -> Dict[str, Any]:
        """
        Create a new project in the AiSensy API.

        Args:
            name: Name for the project.

        Returns:
            Dict[str, Any]: A dictionary containing the created project 
            as returned by the AiSensy API.
        """
        if not settings.PARTNER_ID or not settings.BUSINESS_ID:
            logger.error("Missing PARTNER_ID or BUSINESS_ID in settings")
            return {
                "success": False,
                "error": "Missing required fields: partner_id and business_id"
            }

        if not name:
            logger.error("Missing name parameter")
            return {
                "success": False,
                "error": "Missing required field: name"
            }

        url = f"{self.BASE_URL}/partner/{settings.PARTNER_ID}/business/{settings.BUSINESS_ID}/project"
        payload = {"name": name}
        logger.debug(f"Creating project at: {url}")

        try:
            session = await self._get_session()
            async with session.post(url, json=payload) as response:
                if response.status in (200, 201):
                    data = await response.json()
                    logger.info("Successfully created project")
                    return {"success": True, "data": data}

                error_text = await response.text()
                return self._handle_error(response.status, error_text)

        except aiohttp.ClientConnectorError:
            logger.error("Network connection error")
            return {"success": False, "error": "Network connection error"}
        except aiohttp.ClientTimeout:
            logger.error("Request timeout")
            return {"success": False, "error": "Request timeout"}
        except Exception as e:
            logger.exception("Unexpected error")
            return {"success": False, "error": str(e)}

    async def generate_embedded_signup_url(
        self,
        business_id: str,
        assistant_id: str,
        business_name: str,
        business_email: str,
        phone_code: int,
        phone_number: str,
        website: str,
        street_address: str,
        city: str,
        state: str,
        zip_postal: str,
        country: str,
        timezone: str,
        display_name: str,
        category: str,
        description: Optional[str] = ""
    ) -> Dict[str, Any]:
        """
        Generate an embedded signup URL for WhatsApp Business API (WABA).

        Args:
            business_id: The business ID.
            assistant_id: The assistant ID.
            business_name: Name of the business.
            business_email: Email of the business.
            phone_code: Phone country code (e.g., 1 for US).
            phone_number: Phone number.
            website: Business website URL.
            street_address: Street address.
            city: City name.
            state: State/Province code.
            zip_postal: ZIP/Postal code.
            country: Country code (e.g., "US").
            timezone: Timezone (e.g., "UTC-08:00").
            display_name: Display name for the phone.
            category: Business category (e.g., "ENTERTAIN").
            description: Optional description.

        Returns:
            Dict[str, Any]: A dictionary containing the generated signup URL 
            as returned by the AiSensy API.
        """
        if not settings.PARTNER_ID:
            logger.error("Missing PARTNER_ID in settings")
            return {
                "success": False,
                "error": "Missing required field: partner_id"
            }

        url = f"{self.BASE_URL}/partner/{settings.PARTNER_ID}/generate-waba-link"
        payload = {
            "businessId": business_id,
            "assistantId": assistant_id,
            "setup": {
                "business": {
                    "name": business_name,
                    "email": business_email,
                    "phone": {
                        "code": phone_code,
                        "number": phone_number
                    },
                    "website": website,
                    "address": {
                        "streetAddress1": street_address,
                        "city": city,
                        "state": state,
                        "zipPostal": zip_postal,
                        "country": country
                    },
                    "timezone": timezone
                },
                "phone": {
                    "displayName": display_name,
                    "category": category,
                    "description": description
                }
            }
        }
        logger.debug(f"Generating embedded signup URL at: {url}")

        try:
            session = await self._get_session()
            async with session.post(url, json=payload) as response:
                if response.status in (200, 201):
                    data = await response.json()
                    logger.info("Successfully generated embedded signup URL")
                    return {"success": True, "data": data}

                error_text = await response.text()
                return self._handle_error(response.status, error_text)

        except aiohttp.ClientConnectorError:
            logger.error("Network connection error")
            return {"success": False, "error": "Network connection error"}
        except aiohttp.ClientTimeout:
            logger.error("Request timeout")
            return {"success": False, "error": "Request timeout"}
        except Exception as e:
            logger.exception("Unexpected error")
            return {"success": False, "error": str(e)}

    async def submit_waba_app_id(
        self,
        assistant_id: str,
        waba_app_id: str
    ) -> Dict[str, Any]:
        """
        Submit WABA App ID (Facebook Access Token) to the AiSensy API.

        Args:
            assistant_id: The assistant ID.
            waba_app_id: The WABA App ID.

        Returns:
            Dict[str, Any]: A dictionary containing the response 
            as returned by the AiSensy API.
        """
        if not settings.PARTNER_ID:
            logger.error("Missing PARTNER_ID in settings")
            return {
                "success": False,
                "error": "Missing required field: partner_id"
            }

        if not assistant_id or not waba_app_id:
            logger.error("Missing assistant_id or waba_app_id parameter")
            return {
                "success": False,
                "error": "Missing required fields: assistant_id and waba_app_id"
            }

        url = f"{self.BASE_URL}/partner/{settings.PARTNER_ID}/submit-facebook-access-token"
        payload = {
            "assistantId": assistant_id,
            "wabaAppId": waba_app_id
        }
        logger.debug(f"Submitting WABA App ID at: {url}")

        try:
            session = await self._get_session()
            async with session.post(url, json=payload) as response:
                if response.status in (200, 201):
                    data = await response.json()
                    logger.info("Successfully submitted WABA App ID")
                    return {"success": True, "data": data}

                error_text = await response.text()
                return self._handle_error(response.status, error_text)

        except aiohttp.ClientConnectorError:
            logger.error("Network connection error")
            return {"success": False, "error": "Network connection error"}
        except aiohttp.ClientTimeout:
            logger.error("Request timeout")
            return {"success": False, "error": "Request timeout"}
        except Exception as e:
            logger.exception("Unexpected error")
            return {"success": False, "error": str(e)}

    async def start_migration(
        self,
        assistant_id: str,
        target_id: str,
        country_code: str,
        phone_number: str
    ) -> Dict[str, Any]:
        """
        Start migration by submitting Facebook access token for migration to partner.

        Args:
            assistant_id: The assistant ID.
            target_id: The target ID for migration.
            country_code: Country code (e.g., "91").
            phone_number: Phone number to migrate.

        Returns:
            Dict[str, Any]: A dictionary containing the migration response 
            as returned by the AiSensy API.
        """
        if not settings.PARTNER_ID:
            logger.error("Missing PARTNER_ID in settings")
            return {
                "success": False,
                "error": "Missing required field: partner_id"
            }

        if not assistant_id or not target_id or not country_code or not phone_number:
            logger.error("Missing required parameters for migration")
            return {
                "success": False,
                "error": "Missing required fields: assistant_id, target_id, country_code, phone_number"
            }

        url = f"{self.BASE_URL}/partner/{settings.PARTNER_ID}/submit-facebook-access-token-for-migration-to-partner"
        payload = {
            "assistantId": assistant_id,
            "targetId": target_id,
            "countryCode": country_code,
            "phoneNumber": phone_number
        }
        logger.debug(f"Starting migration at: {url}")

        try:
            session = await self._get_session()
            async with session.post(url, json=payload) as response:
                if response.status in (200, 201):
                    data = await response.json()
                    logger.info("Successfully started migration")
                    return {"success": True, "data": data}

                error_text = await response.text()
                return self._handle_error(response.status, error_text)

        except aiohttp.ClientConnectorError:
            logger.error("Network connection error")
            return {"success": False, "error": "Network connection error"}
        except aiohttp.ClientTimeout:
            logger.error("Request timeout")
            return {"success": False, "error": "Request timeout"}
        except Exception as e:
            logger.exception("Unexpected error")
            return {"success": False, "error": str(e)}

    async def request_otp_for_verification(
        self,
        assistant_id: str,
        mode: str = "sms"
    ) -> Dict[str, Any]:
        """
        Request OTP for verification during migration.

        Args:
            assistant_id: The assistant ID.
            mode: OTP delivery mode (e.g., "sms" or "voice").

        Returns:
            Dict[str, Any]: A dictionary containing the OTP request response 
            as returned by the AiSensy API.
        """
        if not settings.PARTNER_ID:
            logger.error("Missing PARTNER_ID in settings")
            return {
                "success": False,
                "error": "Missing required field: partner_id"
            }

        if not assistant_id:
            logger.error("Missing assistant_id parameter")
            return {
                "success": False,
                "error": "Missing required field: assistant_id"
            }

        url = f"{self.BASE_URL}/partner/{settings.PARTNER_ID}/request-otp-for-migration-to-partner"
        payload = {
            "assistantId": assistant_id,
            "mode": mode
        }
        logger.debug(f"Requesting OTP for verification at: {url}")

        try:
            session = await self._get_session()
            async with session.post(url, json=payload) as response:
                if response.status in (200, 201):
                    data = await response.json()
                    logger.info("Successfully requested OTP for verification")
                    return {"success": True, "data": data}

                error_text = await response.text()
                return self._handle_error(response.status, error_text)

        except aiohttp.ClientConnectorError:
            logger.error("Network connection error")
            return {"success": False, "error": "Network connection error"}
        except aiohttp.ClientTimeout:
            logger.error("Request timeout")
            return {"success": False, "error": "Request timeout"}
        except Exception as e:
            logger.exception("Unexpected error")
            return {"success": False, "error": str(e)}

    async def verify_otp(
        self,
        assistant_id: str,
        otp: str
    ) -> Dict[str, Any]:
        """
        Verify OTP for migration to partner.

        Args:
            assistant_id: The assistant ID.
            otp: The OTP code to verify.

        Returns:
            Dict[str, Any]: A dictionary containing the OTP verification response 
            as returned by the AiSensy API.
        """
        if not settings.PARTNER_ID:
            logger.error("Missing PARTNER_ID in settings")
            return {
                "success": False,
                "error": "Missing required field: partner_id"
            }

        if not assistant_id or not otp:
            logger.error("Missing assistant_id or otp parameter")
            return {
                "success": False,
                "error": "Missing required fields: assistant_id and otp"
            }

        url = f"{self.BASE_URL}/partner/{settings.PARTNER_ID}/validate-otp-for-migration-to-partner"
        payload = {
            "assistantId": assistant_id,
            "otp": otp
        }
        logger.debug(f"Verifying OTP at: {url}")

        try:
            session = await self._get_session()
            async with session.post(url, json=payload) as response:
                if response.status in (200, 201):
                    data = await response.json()
                    logger.info("Successfully verified OTP")
                    return {"success": True, "data": data}

                error_text = await response.text()
                return self._handle_error(response.status, error_text)

        except aiohttp.ClientConnectorError:
            logger.error("Network connection error")
            return {"success": False, "error": "Network connection error"}
        except aiohttp.ClientTimeout:
            logger.error("Request timeout")
            return {"success": False, "error": "Request timeout"}
        except Exception as e:
            logger.exception("Unexpected error")
            return {"success": False, "error": str(e)}

    async def generate_embedded_fb_catalog_url(
        self,
        business_id: str,
        assistant_id: str
    ) -> Dict[str, Any]:
        """
        Generate an embedded Facebook Catalog connect URL.

        Args:
            business_id: The business ID.
            assistant_id: The assistant ID.

        Returns:
            Dict[str, Any]: A dictionary containing the generated catalog connect URL 
            as returned by the AiSensy API.
        """
        if not settings.PARTNER_ID:
            logger.error("Missing PARTNER_ID in settings")
            return {
                "success": False,
                "error": "Missing required field: partner_id"
            }

        if not business_id or not assistant_id:
            logger.error("Missing business_id or assistant_id parameter")
            return {
                "success": False,
                "error": "Missing required fields: business_id and assistant_id"
            }

        url = f"{self.BASE_URL}/partner/{settings.PARTNER_ID}/generate-catalog-connect-link"
        payload = {
            "businessId": business_id,
            "assistantId": assistant_id
        }
        logger.debug(f"Generating embedded FB catalog URL at: {url}")

        try:
            session = await self._get_session()
            async with session.post(url, json=payload) as response:
                if response.status in (200, 201):
                    data = await response.json()
                    logger.info("Successfully generated embedded FB catalog URL")
                    return {"success": True, "data": data}

                error_text = await response.text()
                return self._handle_error(response.status, error_text)

        except aiohttp.ClientConnectorError:
            logger.error("Network connection error")
            return {"success": False, "error": "Network connection error"}
        except aiohttp.ClientTimeout:
            logger.error("Request timeout")
            return {"success": False, "error": "Request timeout"}
        except Exception as e:
            logger.exception("Unexpected error")
            return {"success": False, "error": str(e)}

    async def generate_ctwa_ads_manager_dashboard_url(
        self,
        business_id: str,
        assistant_id: str,
        expires_in: int = 150000
    ) -> Dict[str, Any]:
        """
        Generate CTWA (Click-to-WhatsApp) Ads Manager Dashboard URL.

        Args:
            business_id: The business ID.
            assistant_id: The assistant ID.
            expires_in: URL expiration time in milliseconds (default: 150000).

        Returns:
            Dict[str, Any]: A dictionary containing the generated dashboard URL 
            as returned by the AiSensy API.
        """
        if not settings.PARTNER_ID:
            logger.error("Missing PARTNER_ID in settings")
            return {
                "success": False,
                "error": "Missing required field: partner_id"
            }

        if not business_id or not assistant_id:
            logger.error("Missing business_id or assistant_id parameter")
            return {
                "success": False,
                "error": "Missing required fields: business_id and assistant_id"
            }

        url = f"{self.BASE_URL}/partner/{settings.PARTNER_ID}/ads/generate-dashboard-link"
        payload = {
            "businessId": business_id,
            "assistantId": assistant_id,
            "expiresIn": expires_in
        }
        logger.debug(f"Generating CTWA Ads Manager Dashboard URL at: {url}")

        try:
            session = await self._get_session()
            async with session.post(url, json=payload) as response:
                if response.status in (200, 201):
                    data = await response.json()
                    logger.info("Successfully generated CTWA Ads Manager Dashboard URL")
                    return {"success": True, "data": data}

                error_text = await response.text()
                return self._handle_error(response.status, error_text)

        except aiohttp.ClientConnectorError:
            logger.error("Network connection error")
            return {"success": False, "error": "Network connection error"}
        except aiohttp.ClientTimeout:
            logger.error("Request timeout")
            return {"success": False, "error": "Request timeout"}
        except Exception as e:
            logger.exception("Unexpected error")
            return {"success": False, "error": str(e)}



# async def main():
#     """Test all POST client methods."""
    
#     async with AiSensyPostClient() as client:
        
#         # 1. Create Business Profile
#         print("=" * 50)
#         print("1. Create Business Profile")
#         print("=" * 50)
#         result = await client.create_business_profile(
#             display_name="CallHippo Support",
#             email="support@callhippo.com",
#             company="CallHippo",
#             contact="918116856153",
#             timezone="Asia/Calcutta GMT+05:30",
#             currency="INR",
#             company_size="10 - 20",
#             password="somerandompassword"
#         )
#         print(result)
#         print()

#         # 2. Create Project
#         print("=" * 50)
#         print("2. Create Project")
#         print("=" * 50)
#         result = await client.create_project(name="API TEST PROJECT 1")
#         print(result)
#         print()

#         # 3. Generate Embedded Signup URL
#         print("=" * 50)
#         print("3. Generate Embedded Signup URL")
#         print("=" * 50)
#         result = await client.generate_embedded_signup_url(
#             business_id="63bbe4c2cd10ea720a532ez0",
#             assistant_id="63bbe4c256be217200ad1b5b",
#             business_name="Acme Inc.",
#             business_email="johndoe@acme.com",
#             phone_code=1,
#             phone_number="6505551234",
#             website="https://www.acme.com",
#             street_address="1 Acme Way",
#             city="Acme Town",
#             state="CA",
#             zip_postal="94000",
#             country="US",
#             timezone="UTC-08:00",
#             display_name="Acme Inc.",
#             category="ENTERTAIN",
#             description=""
#         )
#         print(result)
#         print()

#         # 4. Submit WABA App ID
#         print("=" * 50)
#         print("4. Submit WABA App ID")
#         print("=" * 50)
#         result = await client.submit_waba_app_id(
#             assistant_id="66a73a246f969d0b5dbb6903",
#             waba_app_id="100375269493439"
#         )
#         print(result)
#         print()

#         # 5. Start Migration
#         print("=" * 50)
#         print("5. Start Migration")
#         print("=" * 50)
#         result = await client.start_migration(
#             assistant_id="66a73a246f969d0b5dbb6903",
#             target_id="107945432259014",
#             country_code="91",
#             phone_number="8645614148"
#         )
#         print(result)
#         print()

#         # 6. Request OTP for Verification
#         print("=" * 50)
#         print("6. Request OTP for Verification")
#         print("=" * 50)
#         result = await client.request_otp_for_verification(
#             assistant_id="66a73a246f969d0b5dbb6903",
#             mode="sms"
#         )
#         print(result)
#         print()

#         # 7. Verify OTP
#         print("=" * 50)
#         print("7. Verify OTP")
#         print("=" * 50)
#         result = await client.verify_otp(
#             assistant_id="66a73a246f969d0b5dbb6903",
#             otp="123456"
#         )
#         print(result)
#         print()

#         # 8. Generate Embedded FB Catalog URL
#         print("=" * 50)
#         print("8. Generate Embedded FB Catalog URL")
#         print("=" * 50)
#         result = await client.generate_embedded_fb_catalog_url(
#             business_id="67482a210fa2703716c11a4e",
#             assistant_id="66a73a246f969d0b5dbb6903"
#         )
#         print(result)
#         print()

#         # 9. Generate CTWA Ads Manager Dashboard URL
#         print("=" * 50)
#         print("9. Generate CTWA Ads Manager Dashboard URL")
#         print("=" * 50)
#         result = await client.generate_ctwa_ads_manager_dashboard_url(
#             business_id="6880aa4c61c4b97902d4c1ce",
#             assistant_id="6880aa4c61c4b97902d4c1d5",
#             expires_in=150000
#         )
#         print(result)
#         print()


# if __name__ == "__main__":
#     asyncio.run(main())