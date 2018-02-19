from django.urls import resolve
from django.test import TestCase
from letter.views import homepage
from django.http import HttpRequest
from django.template.loader import render_to_string
# from letter.models import 

# Create your tests here.

class Homepage_test(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, homepage)

