# src/logger.py

import logging

# Create a logger object
logger = logging.getLogger("mlproject_logger")

# Set log level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
logger.setLevel(logging.INFO)

# Create a console handler to write logs to stdout
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# Define log message format
formatter = logging.Formatter(
    "[%(asctime)s] %(name)s - %(levelname)s - %(message)s"
)
console_handler.setFormatter(formatter)

# Add the console handler to the logger
if not logger.hasHandlers():
    logger.addHandler(console_handler)

# Example usage:
# logger.info("App started")
# logger.error("An error occurred")
