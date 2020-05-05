'''
Created on May 19, 2019
@author: Burkhard A. Meier
'''





import logging

logger = logging.getLogger(__name__)    # recommended to use __name__
logger.setLevel(logging.DEBUG)

# compare handlers and formatter to basicConfig below

file_handler = logging.FileHandler('Application.log')
 
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.WARNING)   # set different log level

formatter = logging.Formatter('%(asctime)s:%(name)s:%(levelname)s:%(message)s')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(console_handler)

# Advanced logger replaces basicConfig
# logging.basicConfig(filename='Application.log', level=logging.DEBUG,
#                     format='%(asctime)s:%(name)s:%(levelname)s:%(message)s')

logger.debug('log debug message')
logger.info('log info message')
logger.warning('log warning message')
logger.error('log error message')
logger.critical('log critical message')















