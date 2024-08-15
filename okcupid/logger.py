import json
import logging
import sys
import time


class JsonFormatter(logging.Formatter):
    def format(self, record):
        log_record = {
            'message': record.getMessage(),
            'timestamp': self.formatTime(record),
        }
        return json.dumps(log_record)


def setup_logger(logger_name: str) -> logging.Logger:
    stdout_handler = logging.StreamHandler(sys.stdout)
    file_handler = logging.FileHandler(time.strftime("%Y_%m_%d-%H_%M_%S-okcupid.json"))

    stdout_handler.setFormatter(logging.Formatter("%(message)s"))
    file_handler.setFormatter(JsonFormatter())

    logger = logging.getLogger(logger_name)
    logger.addHandler(stdout_handler)
    logger.addHandler(file_handler)

    return logger
