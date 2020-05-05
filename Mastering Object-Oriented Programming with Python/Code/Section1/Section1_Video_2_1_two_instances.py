'''
Created on May 20, 2019
@author: Burkhard A. Meier
'''





#--------------------------------------------------
# Create class 'blue print'
#--------------------------------------------------

class PythonClass(object):
    
    def __init__(self):             # initializer - automatically runs when class gets created
        print(self)                 # print instance (self)


#--------------------------------------------------
# Create instance(s) of class
#--------------------------------------------------

first_instance = PythonClass()
second_instance = PythonClass()


#=====================================================================
# Result - two distinct objects located at different memory addresses:
# 
# <__main__.PythonClass object at 0x0000014314A456D8>
# <__main__.PythonClass object at 0x0000014314A45780>
#=====================================================================



