'''
Created on May 23, 2019
@author: Burkhard A. Meier
'''





import os
import shutil

module_dir = os.path.dirname(__file__)                  # full path to parent directory
backup_folder = os.path.join(module_dir, 'backup')      # append backup folder

module_file = os.path.basename(__file__)                # this is the current Python module we are running

shutil.copy(module_file, backup_folder)                 # copy the current module to the backup folder

print(os.listdir(backup_folder))                        # list all files in the backup folder

    









    
    
    
    