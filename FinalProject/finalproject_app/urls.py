from django.urls import path
from . import views
from .views import *


urlpatterns = [
#path function defines a url pattern
#'' is empty to represent based path to app
# views.index is the function defined in views.py
# name='index' parameter is to dynamically create url
# example in html <a href="{% url 'index' %}">Home</a>.
    path('', views.index, name='index'),
    path('recipes/', recipe_list, name="recipe_list"),
    path('recipes/<int:pk>', views.RecipeDetailView.as_view(), name='recipe_detail'),
    path('recipes/<int:recipe_id>/modify/', modify_recipe, name='modify_recipe'),
    path('recipes/add/', add_recipe, name='add_recipe'),
    path('recipes/<int:recipe_id>/delete/', delete_recipe_view, name='delete_recipe'),


]
