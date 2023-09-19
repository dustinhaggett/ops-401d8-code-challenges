import logging
from logging.handlers import RotatingFileHandler

# Set up the logger
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# Create a rotating file handler which rotates the log files when they reach 5MB in size
# and keeps 3 backup versions of the log files.
file_handler = RotatingFileHandler('example.log', maxBytes=5*1024*1024, backupCount=3)

# Create a stream handler to output logs to the terminal
stream_handler = logging.StreamHandler()

# Create a formatter and set it for both handlers
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
stream_handler.setFormatter(formatter)

# Add the handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(stream_handler)

# Different levels of log messages
logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')



# Attribution to chatgpt4 code interpreter and codefellows github