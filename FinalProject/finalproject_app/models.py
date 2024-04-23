from django.db import models
from django.urls import reverse

# Create your models here.

class Recipe(models.Model):
    title = models.CharField(max_length=200)
    ingredients = models.TextField()
    pictures = models.ImageField(upload_to='recipe_images/', null=True)
    number_of_steps = models.IntegerField()
    steps = models.TextField()
    author = models.CharField(max_length=200, null=True)
    visibility = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("recipe_detail", args=[str(self.id)])
    

class Chef(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20, null=True)
    recipe = models.OneToOneField(Recipe, null=True, on_delete=models.CASCADE, unique=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("chef_detail", args=[str(self.id)])
    