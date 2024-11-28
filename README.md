# Logger Initialization Example

This example demonstrates how to initialize and configure a logger in Python for logging messages to both the console and a log file. The logger supports various features such as log rotation, dynamic log level configuration, JSON formatting, and optional Logstash integration.

## Features

- **Log Rotation**: Automatically rotates log files to manage size.
- **Dynamic Log Level**: Set the log level dynamically.
- **JSON Formatting**: Optionally format logs in JSON for easier parsing.
- **Environment Variable for Log Directory**: Set the log directory via an environment variable.
- **Error Handling**: Robust error handling for file operations.
- **Logstash Integration**: Optional integration with Logstash for centralized logging.

## Usage

1. Import the `init_logger` function from this module.
2. Call the `init_logger` function to obtain a configured logger instance.
3. Use the logger to log messages with different severity levels, such as debug, info, warning, error, and critical.

## Parameters

- `file_name` (str, optional): The name of the log file. If None, the logger name is used as the file name.
- `log_level` (str, optional): The logging level (e.g., DEBUG, INFO, WARNING, ERROR, CRITICAL). Default is "DEBUG".
- `use_json` (bool, optional): Whether to format logs as JSON. Default is False.

## Example

```python
from logger_initializer import init_logger

# Initialize the logger with default settings
logger = init_logger(__name__)
logger.debug("This is a debug message")
logger.info("This is an info message")
logger.warning("This is a warning message")
logger.error("This is an error message")
logger.critical("This is a critical message")

# Initialize the logger with JSON formatting
json_logger = init_logger(__name__, use_json=True)
json_logger.info("This is an info message in JSON format")

# Initialize the logger with a specific log level
info_logger = init_logger(__name__, log_level="INFO")
info_logger.debug("This debug message will not be logged")
info_logger.info("This i
