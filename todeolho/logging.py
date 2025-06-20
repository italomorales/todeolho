import logging
from json_log_formatter import JSONFormatter


def get_logger(name: str = "todeolho") -> logging.Logger:
    """Return a logger configured with JSON formatting."""
    logger = logging.getLogger(name)
    if not logger.handlers:
        handler = logging.StreamHandler()
        handler.setFormatter(JSONFormatter())
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)
    return logger
