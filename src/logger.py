import logging
import os
from datetime import datetime

# Create a unique log file name based on the current date and time
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Create a path to store the log files in a "logs" folder within your project directory
logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)

# Create the "logs" folder if it doesn't already exist
os.makedirs(logs_path, exist_ok=True)

# Define the full path to the log file
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Configure the logging module
logging.basicConfig(
    filename=LOG_FILE_PATH,  # Use the defined log file path
    format="[ %(asctime)s]  %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO  # Set the logging level to INFO (captures informational messages)
)

'''
#testing if logger.py is working
if __name__=="__main__":
    logging.info("Logging has started")

    '''