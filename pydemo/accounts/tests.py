#from django.test import TestCase
#from django.test.simple.DjangoTestSuiteRunner import 

from django.http import HttpRequest, HttpResponse
from accounts.views import my_view

import unittest

def my_func(a, index):
    return a[index]

# Create your tests here.
class MyFuncTestCase(unittest.TestCase):
    def testBasic(self):
        a = ['larry', 'curly', 'moe']
        self.assertEqual(my_func(a, 0), 'larry')
        self.assertEqual(my_func(a, 1), 'curly')
        
    def test_view_page_returns_correct_html(self):
        request = HttpRequest
        response = my_view(request)
        self.assertTrue(response.content.startswith('<html>'))
#        self.assertIn('<title>pydemo</title>',response.content)
        self.assertIn('<title>Master of the universe</title>',response.content)
        self.assertTrue(response.content.endswith('</html>'))