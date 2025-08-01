import logging
import os

def configure_logger():
    logger = logging.getLogger("accent_translator")
    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter('[%(asctime)s] %(levelname)s in %(module)s: %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    # Set logging level from environment variable or default to DEBUG
    log_level = os.getenv("LOG_LEVEL", "DEBUG").upper()
    logger.setLevel(getattr(logging, log_level, logging.DEBUG))

    return logger

logger = configure_logger()
