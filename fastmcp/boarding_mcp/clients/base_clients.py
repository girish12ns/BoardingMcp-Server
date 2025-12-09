import aiohttp
import logging
from typing import Dict, Any, Optional
from app.config.logging import logger
from dataclasses import dataclass
from app.config.setting import settings


@dataclass
class AiSensyBaseClient:
    """Base client with shared functionality."""
    
    api_key: str
    timeout: int = 30
    BASE_URL: str = field(default_factory=lambda: settings.BASE_URL)
    _session: Optional[aiohttp.ClientSession] = field(default=None, init=False, repr=False)
    
    async def _get_session(self) -> aiohttp.ClientSession:
        """Get or create HTTP session."""
        if self._session is None or self._session.closed:
            self._session = aiohttp.ClientSession(
                timeout=aiohttp.ClientTimeout(total=self.timeout),
                headers={
                    "Accept": "application/json",
                    "Content-Type": "application/json",
                    "X-AiSensy-Partner-API-Key": self.api_key,
                }
            )
        return self._session
    
    async def close(self) -> None:
        """Close HTTP session."""
        if self._session and not self._session.closed:
            await self._session.close()
            self._session = None
            logger.debug("Session closed")
    
    def _handle_error(self, status: int, error_text: str) -> Dict[str, Any]:
        """Handle error response."""
        error_map = {
            400: "Bad request",
            401: "Invalid API key",
            404: "Not found",
            409: "Already exists",
            422: "Validation error",
            429: "Rate limit exceeded",
            500: "Server error",
        }
        return {
            "success": False,
            "error": error_map.get(status, f"HTTP {status}"),
            "status_code": status,
            "details": error_text,
        }