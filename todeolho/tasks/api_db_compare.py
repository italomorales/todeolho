"""Task to compare API and PostgreSQL results."""

from __future__ import annotations

import os
from typing import Any, Optional

import requests
from sqlalchemy import create_engine, text
from tenacity import retry, stop_after_attempt, wait_fixed

from ..alerts import send_alert
from ..logging import get_logger
from ..registry import register_task


@register_task("api_db_compare")
def api_db_compare() -> None:
    """Compare results from an API and a Postgres query.

    Configuration is read from environment variables:
    ``API_URL``, ``DB_CONN``, ``DB_QUERY`` and optional ``API_TIMEOUT``.
    ``API_USER``/``API_PASS`` can be used for basic auth.
    """

    api_url = os.getenv("API_URL", "http://localhost/api")
    db_conn = os.getenv("DB_CONN", "postgresql://user:pass@localhost/db")
    db_query = os.getenv("DB_QUERY", "SELECT 1")
    timeout = int(os.getenv("API_TIMEOUT", "5"))
    auth: Optional[tuple[str, str]] = None
    if os.getenv("API_USER") and os.getenv("API_PASS"):
        auth = (os.environ["API_USER"], os.environ["API_PASS"])

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
        message = "Mismatch between API and DB result"
        logger.error(message)
        send_alert(message)
    else:
        logger.info("API and DB results match")
