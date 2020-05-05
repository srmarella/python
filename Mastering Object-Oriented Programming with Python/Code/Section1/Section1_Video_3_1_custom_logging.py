'''
Created on May 21, 2019
@author: Burkhard A. Meier
'''




from os import path

class Logger(object):   
    def __init__(self, full_name):
        module_name = path.splitext(path.basename(full_name))[0]   # save name w/out extension
        self.log_name = module_name + '.log'                       # append new extension
        
               
if __name__== '__main__':   
    logger = Logger(__file__)           # pass in the full name of this Python module
    print(__file__)  
    print(path.basename(__file__))             
    print(logger.log_name)
        
        
        


        
        
        
        
        
        
        
             