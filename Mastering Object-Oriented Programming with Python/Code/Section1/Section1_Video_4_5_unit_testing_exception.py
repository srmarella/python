'''
Created on May 21, 2019
@author: Burkhard A. Meier
'''






import unittest 

class PythonClassTests(unittest.TestCase):
    def test_exception(self):
        self.assertRaises(TypeError, PythonClass)



class PythonClass(object):
    def __init__(self, name):      
        self.name = name                            

    def get_name(self):
        return self.name                

if __name__ == '__main__': 
    unittest.main() 
    



    
    
    
    