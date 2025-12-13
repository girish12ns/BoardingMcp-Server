"""
POST client for AiSensy Direct APIs
"""
from typing import Dict, Any, Optional, List
import aiohttp

from .base_client import AiSensyDirectApiClient
from app import logger


class AiSensyDirectApiPostClient(AiSensyDirectApiClient):
    """Client for all POST operations on Direct APIs."""

    # ==================== 1. USERS ====================

    async def regenerate_token(self, direct_api: bool = True) -> Dict[str, Any]:
        """
        Regenerate API token from the AiSensy Direct API.

        Args:
            direct_api: Whether to use direct API. Defaults to True.

        Returns:
            Dict[str, Any]: A dictionary containing the new token details
            as returned by the AiSensy API.
        """
        url = f"{self.BASE_URL}/users/regenrate-token"
        payload = {"direct_api": direct_api}
        logger.debug(f"Regenerating token at: {url}")

        try:
            session = await self._get_session()
            async with session.post(url, json=payload) as response:
                if response.status == 200:
                    data = await response.json()
                    logger.info("Successfully regenerated token")
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

    # ==================== 2. ANALYTICS ====================

    async def get_waba_analytics(
        self,
        fields: str,
        start: int,
        end: int,
        granularity: str,
        country_codes: Optional[List[str]] = None
    ) -> Dict[str, Any]:
        """
        Fetch WABA analytics from the AiSensy Direct API.

        Args:
            fields: Analytics fields to fetch (e.g., "analytics").
            start: Start timestamp (Unix epoch).
            end: End timestamp (Unix epoch).
            granularity: Data granularity (e.g., "DAY", "MONTH").
            country_codes: Optional list of country codes to filter.

        Returns:
            Dict[str, Any]: A dictionary containing the WABA analytics
            as returned by the AiSensy API.
        """
        url = f"{self.BASE_URL}/waba-analytics"
        payload = {
            "fields": fields,
            "start": start,
            "end": end,
            "granularity": granularity
        }
        if country_codes:
            payload["country_codes"] = country_codes

        logger.debug(f"Fetching WABA analytics from: {url}")

        try:
            session = await self._get_session()
            async with session.post(url, json=payload) as response:
                if response.status == 200:
                    data = await response.json()
                    logger.info("Successfully fetched WABA analytics")
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

    # ==================== 3. HEALTH STATUS ====================

    async def get_health_status(self, node_id: str) -> Dict[str, Any]:
        """
        Fetch health status from the AiSensy Direct API.

        Args:
            node_id: The node ID to check health status for.

        Returns:
            Dict[str, Any]: A dictionary containing the health status
            as returned by the AiSensy API.
        """
        if not node_id:
            logger.error("Missing node_id parameter")
            return {
                "success": False,
                "error": "Missing required field: node_id"
            }

        url = f"{self.BASE_URL}/health-status"
        payload = {"nodeId": node_id}
        logger.debug(f"Fetching health status from: {url}")

        try:
            session = await self._get_session()
            async with session.post(url, json=payload) as response:
                if response.status == 200:
                    data = await response.json()
                    logger.info("Successfully fetched health status")
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

    # ==================== 4. MESSAGES ====================

    async def send_message(
        self,
        to: str,
        message_type: str,
        text_body: str,
        recipient_type: str = "individual"
    ) -> Dict[str, Any]:
        """
        Send a message via the AiSensy Direct API.

        Args:
            to: Recipient phone number (e.g., "917089379345").
            message_type: Type of message (e.g., "text").
            text_body: The message body text.
            recipient_type: Type of recipient. Defaults to "individual".

        Returns:
            Dict[str, Any]: A dictionary containing the message response
            as returned by the AiSensy API.
        """
        if not to or not text_body:
            logger.error("Missing required parameters")
            return {
                "success": False,
                "error": "Missing required fields: to and text_body"
            }

        url = f"{self.BASE_URL}/messages"
        payload = {
            "to": to,
            "type": message_type,
            "recipient_type": recipient_type,
            "text": {
                "body": text_body
            }
        }
        logger.debug(f"Sending message to: {to}")

        try:
            session = await self._get_session()
            async with session.post(url, json=payload) as response:
                if response.status == 200:
                    data = await response.json()
                    logger.info(f"Successfully sent message to: {to}")
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

    # ==================== 5. MARKETING MESSAGES ====================

    async def send_marketing_message(
        self,
        to: str,
        message_type: str,
        text_body: str,
        recipient_type: str = "individual"
    ) -> Dict[str, Any]:
        """
        Send a marketing message via the AiSensy Direct API.

        Args:
            to: Recipient phone number (e.g., "917089379345").
            message_type: Type of message (e.g., "text").
            text_body: The message body text.
            recipient_type: Type of recipient. Defaults to "individual".

        Returns:
            Dict[str, Any]: A dictionary containing the message response
            as returned by the AiSensy API.
        """
        if not to or not text_body:
            logger.error("Missing required parameters")
            return {
                "success": False,
                "error": "Missing required fields: to and text_body"
            }

        url = f"{self.BASE_URL}/marketing_messages"
        payload = {
            "to": to,
            "type": message_type,
            "recipient_type": recipient_type,
            "text": {
                "body": text_body
            }
        }
        logger.debug(f"Sending marketing message to: {to}")

        try:
            session = await self._get_session()
            async with session.post(url, json=payload) as response:
                if response.status == 200:
                    data = await response.json()
                    logger.info(f"Successfully sent marketing message to: {to}")
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

    # ==================== 6. MARK READ ====================

    async def mark_message_read(self, message_id: str) -> Dict[str, Any]:
        """
        Mark a message as read via the AiSensy Direct API.

        Args:
            message_id: The message ID to mark as read.

        Returns:
            Dict[str, Any]: A dictionary containing the response
            as returned by the AiSensy API.
        """
        if not message_id:
            logger.error("Missing message_id parameter")
            return {
                "success": False,
                "error": "Missing required field: message_id"
            }

        url = f"{self.BASE_URL}/mark-read"
        payload = {"messageId": message_id}
        logger.debug(f"Marking message as read: {message_id}")

        try:
            session = await self._get_session()
            async with session.post(url, json=payload) as response:
                if response.status == 200:
                    data = await response.json()
                    logger.info(f"Successfully marked message as read: {message_id}")
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

    # ==================== 7. CREATE TEMPLATE ====================

    async def create_template(
        self,
        name: str,
        category: str,
        language: str,
        components: List[Dict[str, Any]]
    ) -> Dict[str, Any]:
        """
        Create a WhatsApp template via the AiSensy Direct API.

        Args:
            name: Template name.
            category: Template category (e.g., "MARKETING").
            language: Template language (e.g., "en").
            components: List of template components (HEADER, BODY, FOOTER, BUTTONS).

        Returns:
            Dict[str, Any]: A dictionary containing the created template
            as returned by the AiSensy API.
        """
        if not name or not category or not language or not components:
            logger.error("Missing required parameters")
            return {
                "success": False,
                "error": "Missing required fields: name, category, language, and components"
            }

        url = f"{self.BASE_URL}/wa_template"
        payload = {
            "name": name,
            "category": category,
            "language": language,
            "components": components
        }
        logger.debug(f"Creating template: {name}")

        try:
            session = await self._get_session()
            async with session.post(url, json=payload) as response:
                if response.status == 200:
                    data = await response.json()
                    logger.info(f"Successfully created template: {name}")
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

    # ==================== 8. EDIT TEMPLATE ====================

    async def edit_template(
        self,
        template_id: str,
        category: str,
        components: List[Dict[str, Any]]
    ) -> Dict[str, Any]:
        """
        Edit a WhatsApp template via the AiSensy Direct API.

        Args:
            template_id: The template ID to edit.
            category: Template category (e.g., "MARKETING").
            components: List of template components (HEADER, BODY, FOOTER, BUTTONS).

        Returns:
            Dict[str, Any]: A dictionary containing the updated template
            as returned by the AiSensy API.
        """
        if not template_id or not category or not components:
            logger.error("Missing required parameters")
            return {
                "success": False,
                "error": "Missing required fields: template_id, category, and components"
            }

        url = f"{self.BASE_URL}/edit-template/{template_id}"
        payload = {
            "category": category,
            "components": components
        }
        logger.debug(f"Editing template: {template_id}")

        try:
            session = await self._get_session()
            async with session.post(url, json=payload) as response:
                if response.status == 200:
                    data = await response.json()
                    logger.info(f"Successfully edited template: {template_id}")
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

    # ==================== 9. COMPARE TEMPLATE ====================

    async def compare_template(
        self,
        template_id: str,
        template_ids: List[int],
        start: int,
        end: int
    ) -> Dict[str, Any]:
        """
        Compare templates via the AiSensy Direct API.

        Args:
            template_id: The primary template ID for comparison.
            template_ids: List of template IDs to compare.
            start: Start timestamp (Unix epoch).
            end: End timestamp (Unix epoch).

        Returns:
            Dict[str, Any]: A dictionary containing the comparison results
            as returned by the AiSensy API.
        """
        if not template_id or not template_ids:
            logger.error("Missing required parameters")
            return {
                "success": False,
                "error": "Missing required fields: template_id and template_ids"
            }

        url = f"{self.BASE_URL}/compare-template/{template_id}"
        payload = {
            "templateIds": template_ids,
            "start": start,
            "end": end
        }
        logger.debug(f"Comparing template: {template_id}")

        try:
            session = await self._get_session()
            async with session.post(url, json=payload) as response:
                if response.status == 200:
                    data = await response.json()
                    logger.info(f"Successfully compared template: {template_id}")
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

    # ==================== 10. UPLOAD MEDIA ====================

    async def upload_media(self, file_path: str) -> Dict[str, Any]:
        """
        Upload media via the AiSensy Direct API (multipart/form-data).

        Args:
            file_path: Path to the file to upload.

        Returns:
            Dict[str, Any]: A dictionary containing the upload response
            as returned by the AiSensy API.
        """
        if not file_path:
            logger.error("Missing file_path parameter")
            return {
                "success": False,
                "error": "Missing required field: file_path"
            }

        url = f"{self.BASE_URL}/media"
        logger.debug(f"Uploading media from: {file_path}")

        try:
            session = await self._get_session()
            data = aiohttp.FormData()
            data.add_field('file', open(file_path, 'rb'))

            async with session.post(url, data=data) as response:
                if response.status == 200:
                    resp_data = await response.json()
                    logger.info("Successfully uploaded media")
                    return {"success": True, "data": resp_data}

                error_text = await response.text()
                return self._handle_error(response.status, error_text)

        except FileNotFoundError:
            logger.error(f"File not found: {file_path}")
            return {"success": False, "error": f"File not found: {file_path}"}
        except aiohttp.ClientConnectorError:
            logger.error("Network connection error")
            return {"success": False, "error": "Network connection error"}
        except aiohttp.ClientTimeout:
            logger.error("Request timeout")
            return {"success": False, "error": "Request timeout"}
        except Exception as e:
            logger.exception("Unexpected error")
            return {"success": False, "error": str(e)}

    # ==================== 11. GET MEDIA ====================

    async def get_media(self, media_id: str) -> Dict[str, Any]:
        """
        Get media by ID via the AiSensy Direct API.

        Args:
            media_id: The media ID to fetch.

        Returns:
            Dict[str, Any]: A dictionary containing the media details
            as returned by the AiSensy API.
        """
        if not media_id:
            logger.error("Missing media_id parameter")
            return {
                "success": False,
                "error": "Missing required field: media_id"
            }

        url = f"{self.BASE_URL}/get-media"
        payload = {"id": media_id}
        logger.debug(f"Fetching media: {media_id}")

        try:
            session = await self._get_session()
            async with session.post(url, json=payload) as response:
                if response.status == 200:
                    data = await response.json()
                    logger.info(f"Successfully fetched media: {media_id}")
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

    # ==================== 12. CREATE MEDIA SESSION ====================

    async def create_media_session(
        self,
        file_name: str,
        file_length: str,
        file_type: str
    ) -> Dict[str, Any]:
        """
        Create a media upload session via the AiSensy Direct API.

        Args:
            file_name: Name of the file to upload.
            file_length: Size of the file in bytes.
            file_type: MIME type of the file (e.g., "image/jpg").

        Returns:
            Dict[str, Any]: A dictionary containing the session details
            as returned by the AiSensy API.
        """
        if not file_name or not file_length or not file_type:
            logger.error("Missing required parameters")
            return {
                "success": False,
                "error": "Missing required fields: file_name, file_length, and file_type"
            }

        url = f"{self.BASE_URL}/media/session"
        payload = {
            "fileName": file_name,
            "fileLength": file_length,
            "fileType": file_type
        }
        logger.debug(f"Creating media session for: {file_name}")

        try:
            session = await self._get_session()
            async with session.post(url, json=payload) as response:
                if response.status == 200:
                    data = await response.json()
                    logger.info(f"Successfully created media session for: {file_name}")
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

    # ==================== 13. UPLOAD MEDIA TO SESSION ====================

    async def upload_media_to_session(
        self,
        upload_session_id: str,
        file_path: str,
        file_offset: int = 0
    ) -> Dict[str, Any]:
        """
        Upload media to an existing session via the AiSensy Direct API.

        Args:
            upload_session_id: The upload session ID.
            file_path: Path to the file to upload.
            file_offset: Byte offset for resumable uploads. Defaults to 0.

        Returns:
            Dict[str, Any]: A dictionary containing the upload response
            as returned by the AiSensy API.
        """
        if not upload_session_id or not file_path:
            logger.error("Missing required parameters")
            return {
                "success": False,
                "error": "Missing required fields: upload_session_id and file_path"
            }

        url = f"{self.BASE_URL}/media/session/{upload_session_id}"
        logger.debug(f"Uploading media to session: {upload_session_id}")

        try:
            session = await self._get_session()
            data = aiohttp.FormData()
            data.add_field('file', open(file_path, 'rb'))
            data.add_field('fileOffset', str(file_offset))

            async with session.post(url, data=data) as response:
                if response.status == 200:
                    resp_data = await response.json()
                    logger.info(f"Successfully uploaded media to session: {upload_session_id}")
                    return {"success": True, "data": resp_data}

                error_text = await response.text()
                return self._handle_error(response.status, error_text)

        except FileNotFoundError:
            logger.error(f"File not found: {file_path}")
            return {"success": False, "error": f"File not found: {file_path}"}
        except aiohttp.ClientConnectorError:
            logger.error("Network connection error")
            return {"success": False, "error": "Network connection error"}
        except aiohttp.ClientTimeout:
            logger.error("Request timeout")
            return {"success": False, "error": "Request timeout"}
        except Exception as e:
            logger.exception("Unexpected error")
            return {"success": False, "error": str(e)}

    # ==================== 14. CREATE CATALOG ====================

    async def create_catalog(
        self,
        name: str,
        vertical: str = "commerce",
        product_count: int = 0,
        feed_count: int = 1,
        default_image_url: Optional[str] = None,
        fallback_image_url: Optional[List[str]] = None,
        is_catalog_segment: bool = False,
        da_display_settings: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """
        Create a catalog via the AiSensy Direct API.

        Args:
            name: Catalog name.
            vertical: Catalog vertical. Defaults to "commerce".
            product_count: Number of products. Defaults to 0.
            feed_count: Number of feeds. Defaults to 1.
            default_image_url: Default image URL.
            fallback_image_url: List of fallback image URLs.
            is_catalog_segment: Whether catalog is a segment. Defaults to False.
            da_display_settings: Display settings for dynamic ads.

        Returns:
            Dict[str, Any]: A dictionary containing the created catalog
            as returned by the AiSensy API.
        """
        if not name:
            logger.error("Missing name parameter")
            return {
                "success": False,
                "error": "Missing required field: name"
            }

        url = f"{self.BASE_URL}/catalog"
        payload = {
            "vertical": vertical,
            "name": name,
            "product_count": product_count,
            "feed_count": feed_count,
            "is_catalog_segment": is_catalog_segment
        }
        if default_image_url:
            payload["default_image_url"] = default_image_url
        if fallback_image_url:
            payload["fallback_image_url"] = fallback_image_url
        if da_display_settings:
            payload["da_display_settings"] = da_display_settings

        logger.debug(f"Creating catalog: {name}")

        try:
            session = await self._get_session()
            async with session.post(url, json=payload) as response:
                if response.status == 200:
                    data = await response.json()
                    logger.info(f"Successfully created catalog: {name}")
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

    # ==================== 15. CONNECT CATALOG ====================

    async def connect_catalog(self, catalog_id: str) -> Dict[str, Any]:
        """
        Connect a catalog via the AiSensy Direct API.

        Args:
            catalog_id: The catalog ID to connect.

        Returns:
            Dict[str, Any]: A dictionary containing the response
            as returned by the AiSensy API.
        """
        if not catalog_id:
            logger.error("Missing catalog_id parameter")
            return {
                "success": False,
                "error": "Missing required field: catalog_id"
            }

        url = f"{self.BASE_URL}/connect-catalog"
        payload = {"catalogId": catalog_id}
        logger.debug(f"Connecting catalog: {catalog_id}")

        try:
            session = await self._get_session()
            async with session.post(url, json=payload) as response:
                if response.status == 200:
                    data = await response.json()
                    logger.info(f"Successfully connected catalog: {catalog_id}")
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

    # ==================== 16. CREATE PRODUCT ====================

    async def create_product(
        self,
        catalog_id: str,
        name: str,
        category: str,
        currency: str,
        image_url: str,
        price: str,
        retailer_id: str,
        description: Optional[str] = None,
        url: Optional[str] = None,
        brand: Optional[str] = None,
        sale_price: Optional[str] = None,
        sale_price_start_date: Optional[str] = None,
        sale_price_end_date: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Create a product via the AiSensy Direct API.

        Args:
            catalog_id: The catalog ID to add product to.
            name: Product name.
            category: Product category.
            currency: Currency code (e.g., "INR").
            image_url: Product image URL.
            price: Product price.
            retailer_id: Retailer ID.
            description: Product description.
            url: Product URL.
            brand: Product brand.
            sale_price: Sale price.
            sale_price_start_date: Sale start date.
            sale_price_end_date: Sale end date.

        Returns:
            Dict[str, Any]: A dictionary containing the created product
            as returned by the AiSensy API.
        """
        if not catalog_id or not name or not category or not currency or not image_url or not price or not retailer_id:
            logger.error("Missing required parameters")
            return {
                "success": False,
                "error": "Missing required fields: catalog_id, name, category, currency, image_url, price, retailer_id"
            }

        url_endpoint = f"{self.BASE_URL}/product"
        payload = {
            "catalogId": catalog_id,
            "name": name,
            "category": category,
            "currency": currency,
            "image_url": image_url,
            "price": price,
            "retailer_id": retailer_id
        }
        if description:
            payload["description"] = description
        if url:
            payload["url"] = url
        if brand:
            payload["brand"] = brand
        if sale_price:
            payload["sale_price"] = sale_price
        if sale_price_start_date:
            payload["sale_price_start_date"] = sale_price_start_date
        if sale_price_end_date:
            payload["sale_price_end_date"] = sale_price_end_date

        logger.debug(f"Creating product: {name}")

        try:
            session = await self._get_session()
            async with session.post(url_endpoint, json=payload) as response:
                if response.status == 200:
                    data = await response.json()
                    logger.info(f"Successfully created product: {name}")
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

    # ==================== 17. UPDATE WHATSAPP COMMERCE SETTINGS ====================

    async def update_whatsapp_commerce_settings(
        self,
        enable_catalog: bool,
        enable_cart: bool
    ) -> Dict[str, Any]:
        """
        Update WhatsApp commerce settings via the AiSensy Direct API.

        Args:
            enable_catalog: Whether to enable catalog.
            enable_cart: Whether to enable cart.

        Returns:
            Dict[str, Any]: A dictionary containing the updated settings
            as returned by the AiSensy API.
        """
        url = f"{self.BASE_URL}/whatsapp-commerce-settings"
        payload = {
            "enableCatalog": enable_catalog,
            "enableCart": enable_cart
        }
        logger.debug("Updating WhatsApp commerce settings")

        try:
            session = await self._get_session()
            async with session.post(url, json=payload) as response:
                if response.status == 200:
                    data = await response.json()
                    logger.info("Successfully updated WhatsApp commerce settings")
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

    # ==================== 18. CREATE QR CODE ====================

    async def create_qr_code(
        self,
        prefilled_message: str,
        generate_qr_image: str = "SVG"
    ) -> Dict[str, Any]:
        """
        Create a QR code via the AiSensy Direct API.

        Args:
            prefilled_message: The prefilled message for the QR code.
            generate_qr_image: QR image format. Defaults to "SVG".

        Returns:
            Dict[str, Any]: A dictionary containing the created QR code
            as returned by the AiSensy API.
        """
        if not prefilled_message:
            logger.error("Missing prefilled_message parameter")
            return {
                "success": False,
                "error": "Missing required field: prefilled_message"
            }

        url = f"{self.BASE_URL}/qr-codes"
        payload = {
            "prefilledMessage": prefilled_message,
            "generateQrImage": generate_qr_image
        }
        logger.debug("Creating QR code")

        try:
            session = await self._get_session()
            async with session.post(url, json=payload) as response:
                if response.status == 200:
                    data = await response.json()
                    logger.info("Successfully created QR code")
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

    # ==================== 19. SET WHATSAPP BUSINESS ENCRYPTION ====================

    async def set_whatsapp_business_encryption(self, business_public_key: str) -> Dict[str, Any]:
        """
        Set WhatsApp business encryption via the AiSensy Direct API.

        Args:
            business_public_key: The business public key (PEM format).

        Returns:
            Dict[str, Any]: A dictionary containing the response
            as returned by the AiSensy API.
        """
        if not business_public_key:
            logger.error("Missing business_public_key parameter")
            return {
                "success": False,
                "error": "Missing required field: business_public_key"
            }

        url = f"{self.BASE_URL}/whatsapp-business-encryption"
        payload = {"businessPublicKey": business_public_key}
        logger.debug("Setting WhatsApp business encryption")

        try:
            session = await self._get_session()
            async with session.post(url, json=payload) as response:
                if response.status == 200:
                    data = await response.json()
                    logger.info("Successfully set WhatsApp business encryption")
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

    # ==================== 20. CREATE FLOW ====================

    async def create_flow(
        self,
        name: str,
        categories: List[str]
    ) -> Dict[str, Any]:
        """
        Create a flow via the AiSensy Direct API.

        Args:
            name: Flow name.
            categories: List of flow categories (e.g., ["APPOINTMENT_BOOKING"]).

        Returns:
            Dict[str, Any]: A dictionary containing the created flow
            as returned by the AiSensy API.
        """
        if not name or not categories:
            logger.error("Missing required parameters")
            return {
                "success": False,
                "error": "Missing required fields: name and categories"
            }

        url = f"{self.BASE_URL}/flows"
        payload = {
            "name": name,
            "categories": categories
        }
        logger.debug(f"Creating flow: {name}")

        try:
            session = await self._get_session()
            async with session.post(url, json=payload) as response:
                if response.status == 200:
                    data = await response.json()
                    logger.info(f"Successfully created flow: {name}")
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

    # ==================== 21. UPLOAD FLOW ASSETS ====================

    async def upload_flow_assets(self, flow_id: str, file_path: str) -> Dict[str, Any]:
        """
        Upload assets to a flow via the AiSensy Direct API.

        Args:
            flow_id: The flow ID to upload assets to.
            file_path: Path to the file to upload.

        Returns:
            Dict[str, Any]: A dictionary containing the upload response
            as returned by the AiSensy API.
        """
        if not flow_id or not file_path:
            logger.error("Missing required parameters")
            return {
                "success": False,
                "error": "Missing required fields: flow_id and file_path"
            }

        url = f"{self.BASE_URL}/flows/{flow_id}/assets"
        logger.debug(f"Uploading assets to flow: {flow_id}")

        try:
            session = await self._get_session()
            data = aiohttp.FormData()
            data.add_field('file', open(file_path, 'rb'))

            async with session.post(url, data=data) as response:
                if response.status == 200:
                    resp_data = await response.json()
                    logger.info(f"Successfully uploaded assets to flow: {flow_id}")
                    return {"success": True, "data": resp_data}

                error_text = await response.text()
                return self._handle_error(response.status, error_text)

        except FileNotFoundError:
            logger.error(f"File not found: {file_path}")
            return {"success": False, "error": f"File not found: {file_path}"}
        except aiohttp.ClientConnectorError:
            logger.error("Network connection error")
            return {"success": False, "error": "Network connection error"}
        except aiohttp.ClientTimeout:
            logger.error("Request timeout")
            return {"success": False, "error": "Request timeout"}
        except Exception as e:
            logger.exception("Unexpected error")
            return {"success": False, "error": str(e)}

    # ==================== 22. PUBLISH FLOW ====================

    async def publish_flow(self, flow_id: str) -> Dict[str, Any]:
        """
        Publish a flow via the AiSensy Direct API.

        Args:
            flow_id: The flow ID to publish.

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

        url = f"{self.BASE_URL}/flows/{flow_id}/publish"
        logger.debug(f"Publishing flow: {flow_id}")

        try:
            session = await self._get_session()
            async with session.post(url) as response:
                if response.status == 200:
                    data = await response.json()
                    logger.info(f"Successfully published flow: {flow_id}")
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

    # ==================== 23. DEPRECATE FLOW ====================

    async def deprecate_flow(self, flow_id: str) -> Dict[str, Any]:
        """
        Deprecate a flow via the AiSensy Direct API.

        Args:
            flow_id: The flow ID to deprecate.

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

        url = f"{self.BASE_URL}/flows/{flow_id}/deprecate"
        logger.debug(f"Deprecating flow: {flow_id}")

        try:
            session = await self._get_session()
            async with session.post(url) as response:
                if response.status == 200:
                    data = await response.json()
                    logger.info(f"Successfully deprecated flow: {flow_id}")
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

    # ==================== 24. CREATE PAYMENT CONFIGURATION ====================

    async def create_payment_configuration(
        self,
        configuration_name: str,
        purpose_code: str,
        merchant_category_code: str,
        provider_name: str,
        redirect_url: str
    ) -> Dict[str, Any]:
        """
        Create a payment configuration via the AiSensy Direct API.

        Args:
            configuration_name: Name of the payment configuration.
            purpose_code: Purpose code (e.g., "00").
            merchant_category_code: Merchant category code (e.g., "0000").
            provider_name: Payment provider name (e.g., "razorpay").
            redirect_url: Redirect URL after payment.

        Returns:
            Dict[str, Any]: A dictionary containing the created configuration
            as returned by the AiSensy API.
        """
        if not configuration_name or not purpose_code or not merchant_category_code or not provider_name or not redirect_url:
            logger.error("Missing required parameters")
            return {
                "success": False,
                "error": "Missing required fields: configuration_name, purpose_code, merchant_category_code, provider_name, redirect_url"
            }

        url = f"{self.BASE_URL}/payment_configuration"
        payload = {
            "configuration_name": configuration_name,
            "purpose_code": purpose_code,
            "merchant_category_code": merchant_category_code,
            "provider_name": provider_name,
            "redirect_url": redirect_url
        }
        logger.debug(f"Creating payment configuration: {configuration_name}")

        try:
            session = await self._get_session()
            async with session.post(url, json=payload) as response:
                if response.status == 200:
                    data = await response.json()
                    logger.info(f"Successfully created payment configuration: {configuration_name}")
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

    # ==================== 25. GENERATE PAYMENT CONFIGURATION OAUTH LINK ====================

    async def generate_payment_configuration_oauth_link(
        self,
        configuration_name: str,
        redirect_url: str
    ) -> Dict[str, Any]:
        """
        Generate OAuth link for payment configuration via the AiSensy Direct API.

        Args:
            configuration_name: Name of the payment configuration.
            redirect_url: Redirect URL after OAuth.

        Returns:
            Dict[str, Any]: A dictionary containing the OAuth link
            as returned by the AiSensy API.
        """
        if not configuration_name or not redirect_url:
            logger.error("Missing required parameters")
            return {
                "success": False,
                "error": "Missing required fields: configuration_name and redirect_url"
            }

        url = f"{self.BASE_URL}/generate_payment_configuration_oauth_link"
        payload = {
            "configuration_name": configuration_name,
            "redirect_url": redirect_url
        }
        logger.debug(f"Generating OAuth link for: {configuration_name}")

        try:
            session = await self._get_session()
            async with session.post(url, json=payload) as response:
                if response.status == 200:
                    data = await response.json()
                    logger.info(f"Successfully generated OAuth link for: {configuration_name}")
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