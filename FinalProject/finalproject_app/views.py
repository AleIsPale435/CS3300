from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import ChefForm, RecipeForm, RegisterForm
from django.views import generic
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decorators import allowed_users

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

@login_required(login_url='login')
def modify_recipe(request, recipe_id):
    recipe = Recipe.objects.get(pk=recipe_id)
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('chef_profile')
    else:
        form = RecipeForm(instance=recipe)
    return render(request, 'finalproject_app/modify_recipe.html', {'form': form})

@login_required(login_url='login')
@allowed_users(allowed_roles=['Chefs'])
def add_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('chef_profile')  
    else:
        form = RecipeForm()
    return render(request, 'finalproject_app/add_recipe.html', {'form': form})

@login_required(login_url='login')
def delete_recipe_view(request, recipe_id):
    recipe = Recipe.objects.get(pk=recipe_id)
    if request.method == 'POST':
        recipe.delete()
        return redirect('chef_profile')  
    return render(request, 'finalproject_app/delete_recipe.html', {'recipe': recipe})

def registerPage(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('login')
    context = {'form': form}
    return render(request, 'registration/register.html', context)

def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password1')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, username)
            return redirect('index.html')

    context = {}
    return render(request, 'registration/login.html', context)

def logoutPage(request):
    logout(request)
    return redirect('logout.html')

@login_required(login_url='login')
def chef_profile(request):

    recipes = request.user.chef.recipe
    context = {'recipes': recipes}
    return render(request, 'finalproject_app/chef_profile.html', context)