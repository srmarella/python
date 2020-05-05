'''
Created on May 20, 2019
@author: Burkhard A. Meier
'''





#--------------------------------------------------
# Create class 'blue print'
#--------------------------------------------------

class PythonClass(object):
    
    def __init__(self):             # initializer - automatically runs when class gets created
        self.new_method()           # call new method using self and dot notation

    def new_method(self):
        print('Hello')
        
        
#--------------------------------------------------
# Create instance(s) of class
#--------------------------------------------------

first_instance = PythonClass()





