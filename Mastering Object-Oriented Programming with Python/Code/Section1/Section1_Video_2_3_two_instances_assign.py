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

first_instance_copy = first_instance            # assign class instance to another variable

print(first_instance == first_instance_copy)
print(first_instance is first_instance_copy)

print(first_instance)
print(first_instance_copy)




