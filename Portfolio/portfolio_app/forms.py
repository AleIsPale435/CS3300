from django.forms import ModelForm
from .models import Project, Portfolio, Student
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ('title', 'description',)

class PortfolioForm(ModelForm):
    class Meta:
        model = Portfolio
        fields = ('title', 'contact_email', 'is_active', 'about')

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        exclude =['user', 'portfolio']

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
