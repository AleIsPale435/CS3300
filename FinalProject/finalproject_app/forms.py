from django.forms import ModelForm
from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = ('title', 'ingredients', 'pictures', 'number_of_steps', 'steps', 'author', 'visibility')

class ChefForm(ModelForm):
    class Meta:
        model = Chef
        fields = '__all__'
        exclude =['user', 'recipe']

class RegisterForm(UserCreationForm):
    class meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')