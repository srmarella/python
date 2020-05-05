'''
Created on May 20, 2019
@author: Burkhard A. Meier
'''





#--------------------------------------------------
# Create class 'blue print'
#--------------------------------------------------

class PythonClass(object):
    
    def __init__(self, name='default', *args):      # unpack extra args using *
        self.name = name                            # save name
        print('extra *args:', args)

    def new_method(self):
        print('Hello ' + self.name)                 # use class attribute via self
        
        
#--------------------------------------------------
# Create instance(s) of class
#--------------------------------------------------

first_instance = PythonClass('Python', 'more', 1, 23, 'another')    # pass in many args
first_instance.new_method()                                         # call method using instance











