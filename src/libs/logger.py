import logging
import json
from pythonjsonlogger import jsonlogger


def setup_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    log_handler = logging.StreamHandler()
    formatter = jsonlogger.JsonFormatter()
    log_handler.setFormatter(formatter)
    logger.addHandler(log_handler)

    return logger
