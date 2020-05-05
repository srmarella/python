'''
Created on May 23, 2019
@author: Burkhard A. Meier
'''





class PythonClass(object):
    def __init__(self, name=None):      
        self.name = name                            

    def get_name(self):
        if self.name:
            return self.name 
        else:
            return '*** Check your code: name is None!'               

if __name__== '__main__': 
    inst = PythonClass()
    print(inst.get_name())

    









    
    
    
    