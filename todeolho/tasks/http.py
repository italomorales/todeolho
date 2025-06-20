from typing import Optional
import requests
from tenacity import retry, stop_after_attempt, wait_fixed

from ..logging import get_logger
from ..registry import register_task


@register_task("http_monitor")
def http_monitor(url: str, timeout: int = 5, auth: Optional[tuple] = None) -> None:
    logger = get_logger()

    @retry(stop=stop_after_attempt(3), wait=wait_fixed(2))
    def _request() -> None:
        logger.info("Calling API", extra={"url": url})
        response = requests.get(url, timeout=timeout, auth=auth)
        logger.info("API response", extra={"status": response.status_code})
        response.raise_for_status()

    _request()
