from django.urls import path
from . import views

urlpatterns = [
    path('projects', views.ProjectsListView.as_view(), name="projects.list"),
    path('projects/<int:pk>', views.ProjectsDetailView.as_view(), name="projects.detail"), 
    path('projects/<int:pk>/edit', views.ProjectsUpdateView.as_view(), name="projects.update"), 
    path('projects/<int:pk>/delete', views.ProjectsDeleteView.as_view(), name="projects.delete"), 
    path('projects/new', views.ProjectsCreateView.as_view(), name="projects.new"),

]
