'''
Created on May 21, 2019
@author: Burkhard A. Meier
'''






import unittest 

class PythonClassTests(unittest.TestCase):
    def test_exception(self):
        self.assertRaises(TypeError, PythonClass)

    def test_name(self):
        name = 'Bob'
        inst = PythonClass(name)                    # create class instance, passing in name
        name_returned = inst.get_name()             # call class method
        self.assertEqual(name, name_returned)       # test for correct answer

    def test_name_wrong(self):
        name = 'Bob'
        inst = PythonClass(name)                            # create class instance, passing in name
        name_returned = inst.get_name()                     # call class method
        name_wrong = 'Bill'
        self.assertEqual(name_wrong, name_returned)         # should cause AssertionError


class PythonClass(object):
    def __init__(self, name):      
        self.name = name                            

    def get_name(self):
        return self.name                

if __name__ == '__main__': 
    unittest.main() 
    



    
    
    
    