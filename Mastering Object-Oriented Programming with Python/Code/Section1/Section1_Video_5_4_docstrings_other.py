# Created on May 22, 2019
# @author: Burkhard A. Meier







class AnotherPythonClass(object):
    '''Another class used for examples in our video course.
    
    :param name: Used in the get_other_name method.
    :type name: str.
    '''
    def __init__(self, other_name):    
        self.other_name = other_name                            

    def print_other_name(self):
        '''Getter for the name class instance attribute
        
        :returns: self.other_name.
        '''
        print(self.other_name)               

if __name__== '__main__': 
    pass

    









    
    
    
    