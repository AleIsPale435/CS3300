from django.test import SimpleTestCase
from django.urls import reverse, resolve
from finalproject_app.views import *

class TestUrls(SimpleTestCase):

    def test_url_resolves(self):
        url = reverse('index')
        print(resolve(url))
        self.assertEquals(resolve(url).func, index)

    def test_url_resolves(self):
        url = reverse('recipe_list')
        print(resolve(url))
        self.assertEquals(resolve(url).func, recipe_list)

    def test_url_resolves(self):
        url = reverse('add_recipe', args=['params'])
        print(resolve(url))
        self.assertEquals(resolve(url).func, add_recipe)

    def test_url_resolves(self):
        url = reverse('chef_profile')
        print(resolve(url))
        self.assertEquals(resolve(url).func, chef_profile)
