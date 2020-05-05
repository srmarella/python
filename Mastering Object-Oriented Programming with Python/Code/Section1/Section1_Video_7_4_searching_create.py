'''
Created on May 23, 2019
@author: Burkhard A. Meier
'''






import os

module_dir = os.path.dirname(__file__)
class_modules_folder = os.path.join(module_dir, 'class_modules')
os.makedirs(class_modules_folder, exist_ok=True)

template_class_module = '''
class PythonClass(object):
    def __init__(self, name):      
        self.name = name                            

    def get_name(self):
        return self.name                

if __name__== '__main__': 
    inst = PythonClass('A Name')
    print(inst.get_name())
'''

for idx in range(1, 6):
    new_file = os.path.join(class_modules_folder, 'ClassModule' + str(idx) + '.py')
    with open(new_file, 'w') as file:                                                   # overwrite file if exists
        file.writelines(template_class_module)


print(os.listdir(class_modules_folder))








    
    
    
    