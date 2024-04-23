from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm

class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = ('title', 'ingredients', 'pictures', 'number_of_steps', 'steps', 'author', 'visibility')

class ChefForm(ModelForm):
    class Meta:
        model = Chef
        fields = ('name', 'email', 'phone_number', 'recipe')