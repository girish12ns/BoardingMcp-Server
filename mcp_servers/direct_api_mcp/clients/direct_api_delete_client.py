"""
DELETE client for AiSensy Direct APIs
"""
from typing import Dict, Any
import aiohttp

from .base_client import AiSensyDirectApiClient
from app import logger


class AiSensyDirectApiDeleteClient(AiSensyDirectApiClient):
    """Client for all DELETE operations on Direct APIs."""

    # ==================== 1. DELETE ALL TEMPLATES ====================

    async def delete_all_templates(self) -> Dict[str, Any]:
        """
        Delete all WhatsApp templates via the AiSensy Direct API.

        Returns:
            Dict[str, Any]: A dictionary containing the response
            as returned by the AiSensy API.
        """
        url = f"{self.BASE_URL}/wa_template"
        logger.debug(f"Deleting all templates at: {url}")

        try:
            session = await self._get_session()
            async with session.delete(url) as response:
                if response.status == 200:
                    data = await response.json()
                    logger.info("Successfully deleted all templates")
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

    # ==================== 2. DELETE TEMPLATE BY NAME ====================

    async def delete_template_by_name(self, template_name: str) -> Dict[str, Any]:
        """
        Delete a specific WhatsApp template by name via the AiSensy Direct API.

        Args:
            template_name: The template name to delete.

        Returns:
            Dict[str, Any]: A dictionary containing the response
            as returned by the AiSensy API.
        """
        if not template_name:
            logger.error("Missing template_name parameter")
            return {
                "success": False,
                "error": "Missing required field: template_name"
            }

        url = f"{self.BASE_URL}/wa_template/{template_name}"
        logger.debug(f"Deleting template: {template_name}")

        try:
            session = await self._get_session()
            async with session.delete(url) as response:
                if response.status == 200:
                    data = await response.json()
                    logger.info(f"Successfully deleted template: {template_name}")
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

    # ==================== 3. DELETE MEDIA ====================

    async def delete_media(self) -> Dict[str, Any]:
        """
        Delete media via the AiSensy Direct API.

        Returns:
            Dict[str, Any]: A dictionary containing the response
            as returned by the AiSensy API.
        """
        url = f"{self.BASE_URL}/media"
        logger.debug(f"Deleting media at: {url}")

        try:
            session = await self._get_session()
            async with session.delete(url) as response:
                if response.status == 200:
                    data = await response.json()
                    logger.info("Successfully deleted media")
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

    # ==================== 4. DISCONNECT CATALOG ====================

    async def disconnect_catalog(self) -> Dict[str, Any]:
        """
        Disconnect catalog via the AiSensy Direct API.

        Returns:
            Dict[str, Any]: A dictionary containing the response
            as returned by the AiSensy API.
        """
        url = f"{self.BASE_URL}/disconnect-catalog"
        logger.debug(f"Disconnecting catalog at: {url}")

        try:
            session = await self._get_session()
            async with session.delete(url) as response:
                if response.status == 200:
                    data = await response.json()
                    logger.info("Successfully disconnected catalog")
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

    # ==================== 5. DELETE FLOW ====================

    async def delete_flow(self, flow_id: str) -> Dict[str, Any]:
        """
        Delete a flow via the AiSensy Direct API.

        Args:
            flow_id: The flow ID to delete.

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
        logger.debug(f"Deleting flow: {flow_id}")

        try:
            session = await self._get_session()
            async with session.delete(url) as response:
                if response.status == 200:
                    data = await response.json()
                    logger.info(f"Successfully deleted flow: {flow_id}")
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