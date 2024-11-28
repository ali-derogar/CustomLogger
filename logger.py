import logging
import logging.handlers
import os
from datetime import datetime
import json

def init_logger(file_name: str = None, log_level: str = "DEBUG", use_json: bool = False) -> logging.Logger:
    """
    Initialize a logger with an optional file_name for log output.

    Args:
        file_name (str, optional): The name of the log file. If None, the logger name is used as the file name.
        log_level (str, optional): The logging level (e.g., DEBUG, INFO, WARNING, ERROR, CRITICAL).
        use_json (bool, optional): Whether to format logs as JSON.

    Returns:
        logging.Logger: Initialized logger object.

    This function initializes a logger, allowing you to log messages to both the console and a daily log file.

    Example:
    >>> logger = init_logger(__name__)
    >>> logger.debug("This is a debug message")
    """

    logger = logging.getLogger(file_name or __name__)
    logger.setLevel(log_level.upper())

    if use_json:
        logger_format = logging.Formatter(
            json.dumps({
                "process": "%(process)d",
                "asctime": "%(asctime)s",
                "name": "%(name)s",
                "levelname": "%(levelname)s",
                "message": "%(message)s"
            })
        )
    else:
        logger_format = logging.Formatter(
            "#%(process)d | %(asctime)s - %(name)s : %(levelname)s => %(message)s"
        )

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(logger_format)
    logger.addHandler(console_handler)

    current_time = datetime.now().strftime("%Y-%m-%d")
    logs_location = os.getenv('LOG_DIRECTORY', os.path.join(os.getcwd(), "logs"))

    try:
        if not os.path.exists(logs_location):
            os.makedirs(logs_location)
    except OSError as e:
        logger.error(f"Failed to create log directory: {e}")
        return logger

    file_handler = logging.handlers.RotatingFileHandler(
        os.path.join(logs_location, f"{current_time}.log"),
        maxBytes=10*1024*1024,  # 10 MB
        backupCount=2
    )
    file_handler.setFormatter(logger_format)
    logger.addHandler(file_handler)

    # Uncomment and configure the Logstash handler if needed
    # host = "***.***.***.***"
    # elk_handler = logstash.TCPLogstashHandler(host, 8300, version=1)
    # logger.addHandler(elk_handler)

    return logger

# ------------- How to use ------------- #
if __name__ == "__main__":
    logger = init_logger(__name__, log_level="INFO", use_json=False)
    logger.debug("This is a debug message")
    logger.info("This is an info message")
    logger.warning("This is a warning message")
    logger.error("This is an error message")
    logger.critical("This is a critical message")
