'''
Created on May 21, 2019
@author: Burkhard A. Meier
'''






import unittest 

class PythonClassTests(unittest.TestCase):
    def setUp(self):
        self.name = 'Bob'                                   # have to use self.
        self.inst = PythonClass(self.name)                  # create class instance, passing in name        
        self.name_returned = self.inst.get_name()
        
    def test_exception(self):
        self.assertRaises(TypeError, PythonClass)

    def test_name(self):
        self.assertEqual(self.name, self.name_returned)          # test for correct answer

    def test_name_wrong(self):
        name_wrong = 'Bill'
        self.assertNotEqual(name_wrong, self.name_returned)      # assertNotEqual


class PythonClass(object):
    def __init__(self, name):      
        self.name = name                            

    def get_name(self):
        return self.name                

if __name__ == '__main__': 
    unittest.main() 
    



    
    
    
    