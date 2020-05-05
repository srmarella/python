#Created on May 23, 2019
#@author: Burkhard A. Meier



class BaseNameClass(object):
    '''This class expects a name being passed in as an argument'''
    def __init__(self, name=None):   
        if not isinstance(name, str):   # check if str
            name = str(name) 
        self.name = name 

class NameClass(BaseNameClass):
    '''This class expects a name being passed in as an argument'''
    def __init__(self, name=None):   
        super().__init__(name)

    def return_name(self):
        '''Returns the passed-in name'''
        return self.name 
             

if __name__== '__main__': 
    arg = 'First name, last name'
    nameClass = NameClass(arg)          
    print(nameClass.return_name())

    









    
    
    
    