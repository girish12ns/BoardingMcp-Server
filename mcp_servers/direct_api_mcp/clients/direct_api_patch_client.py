"""
PATCH client for AiSensy Direct APIs
"""
from typing import Dict, Any, Optional, List
import aiohttp

from .base_client import AiSensyDirectApiClient
from app import logger


class AiSensyDirectApiPatchClient(AiSensyDirectApiClient):
    """Client for all PATCH operations on Direct APIs."""

    # ==================== 1. UPDATE PROFILE PICTURE ====================

    async def update_profile_picture(self, whatsapp_display_image: str) -> Dict[str, Any]:
        """
        Update WhatsApp profile picture via the AiSensy Direct API.

        Args:
            whatsapp_display_image: URL of the new profile picture.

        Returns:
            Dict[str, Any]: A dictionary containing the response
            as returned by the AiSensy API.
        """
        if not whatsapp_display_image:
            logger.error("Missing whatsapp_display_image parameter")
            return {
                "success": False,
                "error": "Missing required field: whatsapp_display_image"
            }

        url = f"{self.BASE_URL}/update-profile-picture"
        payload = {"whatsAppDisplayImage": whatsapp_display_image}
        logger.debug(f"Updating profile picture at: {url}")

        try:
            session = await self._get_session()
            async with session.patch(url, json=payload) as response:
                if response.status == 200:
                    data = await response.json()
                    logger.info("Successfully updated profile picture")
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

    # ==================== 2. UPDATE PROFILE ====================

    async def update_profile(
        self,
        whatsapp_about: Optional[str] = None,
        address: Optional[str] = None,
        description: Optional[str] = None,
        vertical: Optional[str] = None,
        email: Optional[str] = None,
        websites: Optional[List[str]] = None,
        whatsapp_display_image: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Update WhatsApp business profile via the AiSensy Direct API.

        Args:
            whatsapp_about: WhatsApp about/status text.
            address: Business address.
            description: Business description.
            vertical: Business vertical (e.g., "HEALTH", "RETAIL").
            email: Business email.
            websites: List of business website URLs.
            whatsapp_display_image: URL of the profile picture.

        Returns:
            Dict[str, Any]: A dictionary containing the response
            as returned by the AiSensy API.
        """
        url = f"{self.BASE_URL}/update-profile"
        payload = {}

        if whatsapp_about is not None:
            payload["whatsAppAbout"] = whatsapp_about
        if address is not None:
            payload["address"] = address
        if description is not None:
            payload["description"] = description
        if vertical is not None:
            payload["vertical"] = vertical
        if email is not None:
            payload["email"] = email
        if websites is not None:
            payload["websites"] = websites
        if whatsapp_display_image is not None:
            payload["whatsAppDisplayImage"] = whatsapp_display_image

        if not payload:
            logger.error("No fields provided to update")
            return {
                "success": False,
                "error": "At least one field is required to update"
            }

        logger.debug(f"Updating profile at: {url}")

        try:
            session = await self._get_session()
            async with session.patch(url, json=payload) as response:
                if response.status == 200:
                    data = await response.json()
                    logger.info("Successfully updated profile")
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

    # ==================== 3. UPDATE QR CODE ====================

    async def update_qr_code(
        self,
        qr_code_id: str,
        prefilled_message: str
    ) -> Dict[str, Any]:
        """
        Update a QR code via the AiSensy Direct API.

        Args:
            qr_code_id: The QR code ID to update.
            prefilled_message: The new prefilled message for the QR code.

        Returns:
            Dict[str, Any]: A dictionary containing the response
            as returned by the AiSensy API.
        """
        if not qr_code_id or not prefilled_message:
            logger.error("Missing required parameters")
            return {
                "success": False,
                "error": "Missing required fields: qr_code_id and prefilled_message"
            }

        url = f"{self.BASE_URL}/qr-codes"
        payload = {
            "qrCodeId": qr_code_id,
            "prefilledMessage": prefilled_message
        }
        logger.debug(f"Updating QR code: {qr_code_id}")

        try:
            session = await self._get_session()
            async with session.patch(url, json=payload) as response:
                if response.status == 200:
                    data = await response.json()
                    logger.info(f"Successfully updated QR code: {qr_code_id}")
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

    # ==================== 4. UPDATE FLOW ====================

    async def update_flow(
        self,
        flow_id: str,
        name: Optional[str] = None,
        categories: Optional[List[str]] = None
    ) -> Dict[str, Any]:
        """
        Update a flow via the AiSensy Direct API.

        Args:
            flow_id: The flow ID to update.
            name: New flow name.
            categories: New list of flow categories (e.g., ["APPOINTMENT_BOOKING", "LEAD_GENERATION"]).

        Returns:
            Dict[str, Any]: A dictionary containing the response
            as returned by the AiSensy API.
        """
        if not flow_id:
            logger.error("Missing flow_id parameter")
            return {
                "success": False,
                "error": "Missing required field: flow_id"
            }

        url = f"{self.BASE_URL}/flows/{flow_id}"
        payload = {}

        if name is not None:
            payload["name"] = name
        if categories is not None:
            payload["categories"] = categories

        if not payload:
            logger.error("No fields provided to update")
            return {
                "success": False,
                "error": "At least one field (name or categories) is required to update"
            }

        logger.debug(f"Updating flow: {flow_id}")

        try:
            session = await self._get_session()
            async with session.patch(url, json=payload) as response:
                if response.status == 200:
                    data = await response.json()
                    logger.info(f"Successfully updated flow: {flow_id}")
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