"""PostgreSQL monitor task."""

from __future__ import annotations

import os
from typing import Any

from sqlalchemy import create_engine, text
from ..logging import get_logger
from ..registry import register_task


@register_task("db_monitor")
def db_monitor() -> None:
    """Run a SQL query on a Postgres database defined by environment variables."""

    conn_str = os.getenv("DB_CONN", "postgresql://user:pass@localhost/db")
    query = os.getenv("DB_QUERY", "SELECT 1")
    logger = get_logger()
    logger.info("Executing query", extra={"query": query})
    engine = create_engine(conn_str)
    with engine.connect() as conn:
        result = conn.execute(text(query))
        rows = result.fetchall()
        logger.info("Query result", extra={"rows": len(rows)})
