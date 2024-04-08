from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import ChefForm, RecipeForm
from django.views import generic

# Create your views here.
def index(request):

    return render(request, 'finalproject_app/index.html')

def recipe_list(request):
    recipes = Recipe.objects.filter(visibility=True)
    return render(request, 'finalproject_app/recipe_list.html', {'recipes': recipes})

class RecipeListView(generic.ListView):
    model = Recipe

class RecipeDetailView(generic.DetailView):
    model = Recipe

class ChefDetailView(generic.DetailView):
    model = Chef