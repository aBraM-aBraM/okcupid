import json
import logging
import sys
from datetime import datetime


class JsonFormatter(logging.Formatter):
    def format(self, record):
        log_record = {
            'message': record.getMessage(),
            'timestamp': self.formatTime(record),
            'extras': record.__dict__.get('extra', {})
        }
        return json.dumps(log_record)


def setup_logger(logger_name: str) -> logging.Logger:
    stdout_handler = logging.StreamHandler(sys.stdout)
    file_handler = logging.FileHandler(datetime.now().strftime("%d_%m_%y-%H:%M:%S-okcupid.json"))

    stdout_handler.setFormatter(logging.Formatter('%(message)s'))
    file_handler.setFormatter(JsonFormatter())

    logger = logging.getLogger(logger_name)
    logger.addHandler(stdout_handler)
    logger.addHandler(file_handler)

    return logger
