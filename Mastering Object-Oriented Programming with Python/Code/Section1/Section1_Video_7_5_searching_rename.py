'''
Created on May 23, 2019
@author: Burkhard A. Meier
'''







import os
from os.path import dirname, join, splitext


module_dir = dirname(__file__)
class_modules_folder = join(module_dir, 'class_modules')

for cur_dir, sub_dirs, files_in_dir in os.walk(class_modules_folder):
    for cur_file in files_in_dir:
        module_num = splitext(cur_file)[0][-1]

        cur_file_path = join(cur_dir, cur_file)
        with open(cur_file_path, 'r') as file:                          # open existing file    
            code = file.read()                                          # read entire file
        
        # replace code in memory, chaining calls to replace()    
        new_code = code.replace('PythonClass', 'NameClass').replace('inst', 'nameClass').replace('get_name', 'return_name')        

        with open(cur_file_path, 'w') as file:                          # overwrite existing file with new code
            file.write(new_code)







    
    
    
    