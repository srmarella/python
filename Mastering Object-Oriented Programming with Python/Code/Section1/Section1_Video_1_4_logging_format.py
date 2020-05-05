'''
Created on May 19, 2019
@author: Burkhard A. Meier
'''





import logging

# see: https://docs.python.org/3/library/logging.html#logrecord-attributes 
# for format options and explanations

logging.basicConfig(filename='Application.log', level=logging.DEBUG,
                    format='%(asctime)s:%(name)s:%(levelname)s:%(message)s')

logging.debug('log debug message')
logging.info('log info message')
logging.warning('log warning message')
logging.error('log error message')
logging.critical('log critical message')















