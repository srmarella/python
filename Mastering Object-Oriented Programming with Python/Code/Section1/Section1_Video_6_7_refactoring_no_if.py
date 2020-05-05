#Created on May 23, 2019
#@author: Burkhard A. Meier






class NameClass(object):
    '''This class expects a name being passed in as an argument'''
    def __init__(self, name=None):   
        if not isinstance(name, str):   # check if str
            name = str(name) 
        self.name = name                            

    def return_name(self):
        '''Returns the passed-in name'''
        return self.name 
             

if __name__== '__main__': 
    arg = [1, 'bob', None]
    nameClass = NameClass(arg)          
    print(nameClass.return_name())

    









    
    
    
    