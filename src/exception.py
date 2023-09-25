import sys
from src.logger import logging

# Function to get error details
def error_message_detail(error, error_detail):
    exc_type, exc_obj, exc_tb = sys.exc_info()
    
    # Get the file name and line number where the error occurred
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = f"Error occurred in Python script name [{file_name}] line number [{exc_tb.tb_lineno}] error message [{error}]"

    return error_message

# Custom Exception class
class CustomException(Exception):
    def __init__(self, error_message, error_detail):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail)

    def __str__(self):
        return self.error_message
    


# Testing if exception.py is working
if __name__ == "__main__":
    try:
        a = 1 / 0
    except Exception as e:
        logging.info("Division by zero error")
        raise CustomException(str(e), sys.exc_info())
