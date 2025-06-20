from typing import Any
from sqlalchemy import create_engine, text
from ..logging import get_logger
from ..registry import register_task


@register_task("db_monitor")
def db_monitor(conn_str: str, query: str) -> None:
    logger = get_logger()
    logger.info("Executing query", extra={"query": query})
    engine = create_engine(conn_str)
    with engine.connect() as conn:
        result = conn.execute(text(query))
        rows = result.fetchall()
        logger.info("Query result", extra={"rows": len(rows)})
