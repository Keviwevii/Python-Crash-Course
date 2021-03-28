#Test for employee.py

import unittest
from employee import Employee

class EmployeeTestCase(unittest.TestCase):
    '''A test for methdos in Employee Class'''
    
    def setUp(self):
        '''Set up for testing methods so I dont multiple instances'''
        self.me = Employee('Kevin', 'Floyd', 5000)
        
    def test_give_default_raise(self):
        '''Test that default raise works.'''
        self.assertEqual(self.me.give_raise(), 10000)
        
    def test_give_custom_raise(self):
        '''Testing a custom raise.'''
        self.assertEqual(self.me.give_raise(6000), 11000)
if __name__ == '__main__':
    unittest.main()