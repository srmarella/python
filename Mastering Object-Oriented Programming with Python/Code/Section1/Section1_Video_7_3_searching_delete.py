'''
Created on May 23, 2019
@author: Burkhard A. Meier
'''






import os

module_dir = os.path.dirname(__file__)                  # full path to parent directory
backup_folder = os.path.join(module_dir, 'backup')      # append backup folder
backup_files = os.listdir(backup_folder)                # files in backup folder
    
backup_files_path = [os.path.join(backup_folder, file) for file in backup_files]        # full path to files in backup folder

try:
    for file in backup_files_path:
        os.remove(file)                                 # try to delete all files in backup folder
except Exception as ex:                                 # catch any exceptions
    print(ex)









    
    
    
    