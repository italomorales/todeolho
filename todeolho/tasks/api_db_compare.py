from typing import Any, Optional
import requests
from sqlalchemy import create_engine, text
from tenacity import retry, stop_after_attempt, wait_fixed

from ..logging import get_logger
from ..registry import register_task


@register_task("api_db_compare")
def api_db_compare(
    api_url: str,
    db_conn: str,
    db_query: str,
    timeout: int = 5,
    auth: Optional[tuple] = None,
) -> None:
    logger = get_logger()

    @retry(stop=stop_after_attempt(3), wait=wait_fixed(2))
    def _call_api() -> Any:
        logger.info("Calling API", extra={"url": api_url})
        response = requests.get(api_url, timeout=timeout, auth=auth)
        response.raise_for_status()
        return response.json()

    api_result = _call_api()
    engine = create_engine(db_conn)
    with engine.connect() as conn:
        result = conn.execute(text(db_query))
        db_rows = [dict(row) for row in result.fetchall()]

    logger.info(
        "Comparison", extra={"api_rows": len(api_result), "db_rows": len(db_rows)}
    )
    if api_result != db_rows:
        logger.error("Mismatch between API and DB result")
    else:
        logger.info("API and DB results match")
