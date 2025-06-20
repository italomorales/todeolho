"""Simple alerting utilities."""

from __future__ import annotations

from ..logging import get_logger


def send_alert(message: str) -> None:
    """Send an alert message.

    This demo implementation just logs with level ERROR. In a real
    system you could integrate with e-mail, Teams or WhatsApp here.
    """

    logger = get_logger("alert")
    logger.error(message)
