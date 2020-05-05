'''
Created on May 23, 2019
@author: Burkhard A. Meier
'''





import os
from pprint import pprint

module_dir = os.path.dirname(__file__)      # full path to parent directory of this Python module
pprint(os.listdir(module_dir))              # print out all files located in the parent directory

backup_folder = os.path.join(module_dir, 'backup')      # append/join backup folder to parent directory

os.makedirs(backup_folder, exist_ok=True)               # create the new backup folder if it does not exist




    









    
    
    
    