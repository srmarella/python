'''
Created on May 19, 2019
@author: Burkhard A. Meier
'''





import logging

logger = logging.getLogger(__name__)    # recommended to use __name__

logging.basicConfig(filename='Application.log', level=logging.DEBUG,
                    format='%(asctime)s:%(name)s:%(levelname)s:%(message)s')

logger.debug('log debug message')
logger.info('log info message')
logger.warning('log warning message')
logger.error('log error message')
logger.critical('log critical message')















