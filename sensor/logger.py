import logging
import os
import sys
from datetime import datetime

# Correctly close the f-string literal
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Define the log path
log_path = os.path.join(os.getcwd(), 'logs', LOG_FILE)

# Create the directory if it doesn't exist
os.makedirs(log_path, exist_ok=True)

# Full log file path
LOG_FILE_PATH = os.path.join(log_path,LOG_FILE)

# Configure the logging settings
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format='[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
)

# Example usage of logging
#logging.info("Logging setup completed successfully.")
