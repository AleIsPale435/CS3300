from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import *
from .forms import ProjectForm, PortfolioForm, StudentForm
from django.views import generic


# Create your views here.
def index(request):

# Render the HTML template index.html with the data in the context variable.
    studentActivePortfolios = Student.objects.select_related('portfolio').all().filter(portfolio__is_active=True)
    print("active portfolio query set", studentActivePortfolios)
    return render(request, 'portfolio_app/index.html', {'studentActivePortfolios': studentActivePortfolios})
  # return render( request, 'portfolio_app/index.html')

class StudentListView(generic.ListView):
    model = Student

class StudentDetailView(generic.DetailView):
    model = Student

class PortfolioDetailView(generic.DetailView):
    model = Portfolio

class ProjectListView(generic.ListView):
    model = Project

class ProjectDetailView(generic.DetailView):
    model = Project

def createProject(request, portfolio_id):
    form = ProjectForm()
    portfolio = Portfolio.objects.get(pk=portfolio_id)

    if request.method == 'POST':
        project_data = request.POST.copy()
        project_data['portfolio_id'] = portfolio_id
        form = ProjectForm(project_data)
        if form.is_valid():
            project = form.save(commit=False)
            project.portfolio = portfolio
            project.save()

            return redirect('portfolio-detail', portfolio_id)
    
    context = {'form': form}
    return render(request, 'portfolio_app/project_form.html', context)

def editProject(request, project_id):
    try:
        project = Project.objects.get(pk=project_id)
    except:
        print("FAILED")

    portfolio_id = project.portfolio.id
    form = ProjectForm(instance=project)

    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('portfolio-detail', portfolio_id=portfolio_id)
    
    context = {'form': form}
    return render(request, 'portfolio_app/edit_project.html', context)