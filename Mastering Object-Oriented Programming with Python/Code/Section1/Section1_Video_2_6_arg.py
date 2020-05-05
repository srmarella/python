'''
Created on May 20, 2019
@author: Burkhard A. Meier
'''





#--------------------------------------------------
# Create class 'blue print'
#--------------------------------------------------

class PythonClass(object):
    
    def __init__(self, name='default'):             # initializer - now accepts args
        self.name = name                            # save name

    def new_method(self):
        print('Hello ' + self.name)                 # use class attribute via self
        
        
#--------------------------------------------------
# Create instance(s) of class
#--------------------------------------------------

first_instance = PythonClass()
first_instance.new_method()         # call method using instance











