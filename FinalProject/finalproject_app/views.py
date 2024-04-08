from django.shortcuts import render, redirect
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


def modify_recipe(request, recipe_id):
    recipe = Recipe.objects.get(pk=recipe_id)
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('recipe_detail', recipe_id)
    else:
        form = RecipeForm(instance=recipe)
    return render(request, 'finalproject_app/modify_recipe.html', {'form': form})

def add_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('recipe_list')  
    else:
        form = RecipeForm()
    return render(request, 'finalproject_app/add_recipe.html', {'form': form})

def delete_recipe_view(request, recipe_id):
    recipe = Recipe.objects.get(pk=recipe_id)
    if request.method == 'POST':
        recipe.delete()
        return redirect('recipe_list')  
    return render(request, 'finalproject_app/confirm_delete_recipe.html', {'recipe': recipe})