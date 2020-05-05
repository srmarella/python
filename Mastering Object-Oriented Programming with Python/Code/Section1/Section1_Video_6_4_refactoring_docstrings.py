#Created on May 23, 2019
#@author: Burkhard A. Meier






class PythonClass(object):
    '''This class expects a name being passed in as an argument'''
    def __init__(self, name=None):      
        self.name = name                            

    def get_name(self):
        '''Returns the passed-in name'''
        if self.name:
            return self.name 
        else:
            return '*** Check your code: name is None!\n'\
                    + PythonClass.__doc__              

if __name__== '__main__': 
    inst = PythonClass()
    print(inst.get_name())

    









    
    
    
    