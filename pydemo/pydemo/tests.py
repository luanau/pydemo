from django.test import TestCase
from django.core.urlresolvers import resolve
from django.http import HttpRequest

from pydemo.views import home_page
from boto.beanstalk.response import Response

class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page,)
        


        
    def test_home_page_returns_correct_html(self):
        request = HttpRequest
        response = home_page(request)
        self.assertTrue(response.content.startswith('<html>'))
#        self.assertIn('<title>pydemo</title>',response.content)
        self.assertIn('<title>Master of the universe</title>',response.content)
        self.assertTrue(response.content.endswith('</html>'))