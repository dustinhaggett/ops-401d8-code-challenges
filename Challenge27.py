import logging
from logging.handlers import RotatingFileHandler

# Set up the logger
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# Create a rotating file handler which rotates the log files when they reach 5MB in size
# and keeps 3 backup versions of the log files.
handler = RotatingFileHandler('example.log', maxBytes=5*1024*1024, backupCount=3)

# Create a formatter and set it for the handler
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# Add the handler to the logger
logger.addHandler(handler)

# Different levels of log messages
logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')


# Attribution to chatgpt4 code interpreter and codefellows github