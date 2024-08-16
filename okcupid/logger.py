import logging
from pythonjsonlogger import jsonlogger
import sys
import time
from pathlib import Path
from okcupid import consts


def setup_logger(logger_name: str, log_dir: Path | str) -> logging.Logger:
    formatter = jsonlogger.JsonFormatter(timestamp=True)

    stdout_handler = logging.StreamHandler(sys.stdout)
    stdout_handler.setFormatter(formatter)

    if isinstance(log_dir, str):
        log_dir = Path(log_dir)

    if not log_dir.is_absolute():
        log_dir = consts.PROJECT_DIR / log_dir
    log_dir.mkdir(exist_ok=True)

    file_handler = logging.FileHandler(
        log_dir / time.strftime("%Y_%m_%d-%H_%M_%S-okcupid.json")
    )
    file_handler.setFormatter(formatter)

    logger = logging.getLogger(logger_name)
    logger.addHandler(stdout_handler)
    logger.addHandler(file_handler)

    return logger
