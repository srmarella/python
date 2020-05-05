'''
Created on May 21, 2019
@author: Burkhard A. Meier
'''






import unittest 

class PythonClassTests(unittest.TestCase):
    def no_test_(self):
        print('hello')


class PythonClass(object):
    def __init__(self, name):      
        self.name = name                            

    def get_name(self):
        return self.name                

if __name__ == '__main__': 
    unittest.main() 
    



    
    
    
    