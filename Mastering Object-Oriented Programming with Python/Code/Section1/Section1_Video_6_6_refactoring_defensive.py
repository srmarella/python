#Created on May 23, 2019
#@author: Burkhard A. Meier







class NameClass(object):
    '''This class expects a name being passed in as an argument'''
    def __init__(self, name=None):   
        print(type(name)) 
        if not isinstance(name, str):   # check if str
            name = str(name) 
        print(type(name))
        self.name = name                            

    def return_name(self):
        '''Returns the passed-in name'''
        if self.name:
            return self.name 
        else:
            return '*** Check your code: name is None!\n'\
                    + NameClass.__doc__              

if __name__== '__main__': 
    nameClass = NameClass(123)          # <-- pass in int
    print(nameClass.return_name())

    









    
    
    
    