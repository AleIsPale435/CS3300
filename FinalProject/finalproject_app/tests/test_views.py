from django.test import TestCase, Client
from django.urls import reverse
from finalproject_app.models import *
import json


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.recipe_list_url = reverse('recipe_list')
        self.recipe_detail_url = reverse('recipe_detail')

    def test_project_list_GET(self):

        response = self.client.get(reverse('recipe_list'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'finalproject_app/recipe_list.html')

    def test_project_detail_GET(self):
        response = self.client.get(reverse('recipe_list'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'finalproject_app/recipe_detail.html')
