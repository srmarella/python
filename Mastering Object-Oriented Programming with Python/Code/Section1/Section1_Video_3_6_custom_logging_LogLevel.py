'''
Created on May 21, 2019
@author: Burkhard A. Meier
'''




from os import path, makedirs
from datetime import datetime
from enum import Enum

class LogLevel(Enum):
    OFF     = 1
    MINIMUM = 2
    NORMAL  = 3
    DEBUG   = 4
    

class Logger(object):   
    def __init__(self, full_name, log_level=LogLevel.DEBUG):
        module_name = path.splitext(path.basename(full_name))[0]    # save name w/out extension
        self.log_name = module_name + '.log'                        # append new extension

        logs_folder = 'logs'          
        if not path.exists(logs_folder):                     
            makedirs(logs_folder, exist_ok = True)                  # create new folder if it does not exist  

        self.log = path.join(logs_folder, self.log_name)            # add Logs folder to full path         
        self.create_log()
        
        self.logging_level = log_level

    def create_log(self):    
        with open(self.log, mode='w', encoding='utf-8') as log_file:                # write mode
            log_file.write(self.get_date_time() + '\t\t*** Starting Log ***\n')
        log_file.close()                                            

    def get_date_time(self):
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    def write_to_log(self, msg='', log_level=LogLevel.DEBUG): 
        if log_level.value > self.logging_level.value:                      # control how much gets logged
            return

        with open(self.log, mode='a', encoding='utf-8') as log_file:        # open the log attribute; append mode
            if msg.startswith('\n'):
                msg = msg[1:]                                               # remove leading newline                                        
                log_file.write(self.get_date_time() + '\n')
            
            msg = f'{log_level.name}: {msg}'                                # add logging level to msg
            if msg.endswith('\n'):
                log_file.write(self.get_date_time() + '\t\t' + msg)
                log_file.write(self.get_date_time() + '\n')                 # append trailing newline
            else: 
                log_file.write(self.get_date_time() + '\t\t' + msg + '\n')       
        log_file.close()            
        
                      
if __name__== '__main__':   
    logger = Logger(__file__, log_level=LogLevel.NORMAL)                    # set logging level
    
    logger.write_to_log('regular log message', log_level=LogLevel.MINIMUM)
    logger.write_to_log('\nlog message with leading newline', log_level=LogLevel.NORMAL)
    logger.write_to_log('log message with trailing newline\n', log_level=LogLevel.NORMAL)
    logger.write_to_log('The final message', log_level=LogLevel.DEBUG)
        
        


        
        
        
        
        
        
        
             