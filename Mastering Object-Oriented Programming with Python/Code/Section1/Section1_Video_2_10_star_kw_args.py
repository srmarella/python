'''
Created on May 20, 2019
@author: Burkhard A. Meier
'''





#--------------------------------------------------
# Create class 'blue print'
#--------------------------------------------------

class PythonClass(object):
    
    def __init__(self, name='default', *args, **kw):    # unpack extra positional and keyword args 
        self.name = name                                # save name
        print('extra positional args:', args)
        print('extra keyword args:', kw)

    def new_method(self):
        print('Hello ' + self.name)                 # use class attribute via self
        
        
#--------------------------------------------------
# Create instance(s) of class
#--------------------------------------------------

first_instance = PythonClass('Python', 'more', 1, 23, 'another',
                             keyword1='one', keyword2=2)            # pass in many positional and keyword args
first_instance.new_method()                                         # call method using instance











