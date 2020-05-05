'''
Created on May 21, 2019
@author: Burkhard A. Meier
'''




from os import path, makedirs

class Logger(object):   
    def __init__(self, full_name):
        module_name = path.splitext(path.basename(full_name))[0]    # save name w/out extension
        self.log_name = module_name + '.log'                        # append new extension

        logs_folder = 'logs'          
        if not path.exists(logs_folder):                     
            makedirs(logs_folder, exist_ok = True)                  # create new folder if it does not exist  

        self.log = path.join(logs_folder, self.log_name)            # add Logs folder to full path         
        self.create_log()

    def create_log(self):    
        with open(self.log, mode='w', encoding='utf-8') as log_file:
            log_file.write('\t\t*** Starting Log ***\n')
        log_file.close()                                            # should not be necessary

               
if __name__== '__main__':   
    logger = Logger(__file__)           # pass in the full name of this Python module
    print(path.basename(__file__))             
    print(logger.log_name)
        
        
        


        
        
        
        
        
        
        
             