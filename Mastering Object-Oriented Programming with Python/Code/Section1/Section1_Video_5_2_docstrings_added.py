# Created on May 22, 2019
# @author: Burkhard A. Meier







class PythonClass(object):
    '''A class used for examples in our video course.
    
    :param name: Used in the get_name method.
    :type name: str.
    '''
    def __init__(self, name):    
        self.name = name                            

    def get_name(self):
        '''Getter for the name class instance attribute
        
        :returns: self.name.
        '''
        return self.name                

if __name__== '__main__': 
    pass
#     help()                      # prints how to use help()
#     help(PythonClass)           # prints class and method signatures

#     print(__doc__)                # prints the module docstring
#     print(PythonClass.__doc__)    # prints the docstring of the class

#     help(PythonClass.get_name)            # prints method name, signature and docstring
#     print(PythonClass.get_name.__doc__)   # prints docstring

    









    
    
    
    