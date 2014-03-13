#from django.test import TestCase
#from django.test.simple.DjangoTestSuiteRunner import 
import unittest

def my_func(a, index):
    return a[index]

# Create your tests here.
class MyFuncTestCase(unittest.TestCase):
    def testBasic(self):
        a = ['larry', 'curly', 'moe']
        self.assertEqual(my_func(a, 0), 'larry')
        self.assertEqual(my_func(a, 1), 'curly')