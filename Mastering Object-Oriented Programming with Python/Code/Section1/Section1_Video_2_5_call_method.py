'''
Created on May 20, 2019
@author: Burkhard A. Meier
'''





#--------------------------------------------------
# Create class 'blue print'
#--------------------------------------------------

class PythonClass(object):
    
    def __init__(self):             # initializer - automatically runs when class gets created
        pass

    def new_method(self):
        print('Hello')
        
        
#--------------------------------------------------
# Create instance(s) of class
#--------------------------------------------------

first_instance = PythonClass()
first_instance.new_method()         # call method using instance











