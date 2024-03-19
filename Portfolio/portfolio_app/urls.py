from django.urls import include, path

from portfolio_app import admin
from . import views

urlpatterns = [
#path function defines a url pattern
#'' is empty to represent based path to app
# views.index is the function defined in views.py
# name='index' parameter is to dynamically create url
# example in html <a href="{% url 'index' %}">Home</a>.
    path('', views.index, name='index'),
    path('students/', views.StudentListView.as_view(), name='student'),
    path('student/<int:pk>', views.StudentDetailView.as_view(), name='student-detail'),
    path('projects/', views.ProjectListView.as_view(), name='projects'),
    path('portfolio/<int:pk>', views.PortfolioDetailView.as_view(), name='portfolio-detail'),
    path('project/<int:pk>/', views.ProjectDetailView.as_view(), name='project-detail'),
    path('portfolio/<int:portfolio_id>/create_project', views.createProject, name='create_project'),
    path('project/<int:project_id>/edit_project', views.editProject, name='edit_project'),
    path('portfolio/<int:portfolio_id>/update_portfolio', views.update_portfolio, name='update_portfolio'),
    path('project/int:<project_id>/delete_project', views.delete_project, name='delete_project')
]