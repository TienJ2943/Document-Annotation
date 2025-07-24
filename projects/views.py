from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from django.http import Http404
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import ProjectsForm
from .models import Projects

class ProjectsDeleteView(DeleteView):
    model = Projects
    success_url = '/projectslist/projects'
    template_name = 'projects/projects_delete.html'
    login_url = "/admin"

class ProjectsUpdateView(UpdateView):
    model = Projects
    success_url = '/projectslist/projects'
    form_class = ProjectsForm
    login_url = "/admin"

class ProjectsCreateView(CreateView):
    model = Projects
    success_url = '/projectslist/projects'
    form_class = ProjectsForm
    login_url = "/admin"

    def form_valid(self, form):
        self.object= form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

class ProjectsListView(LoginRequiredMixin, ListView):
    model = Projects
    context_object_name = "projects"
    template_name = "projects/projects_list.html"
    login_url = "/admin"

    def get_queryset(self):
        return self.request.user.projects.all()

class ProjectsDetailView(DetailView):
    model = Projects
    context_object_name = "project"

def detail(request, pk):
    try:
        project = Projects.objects.get(pk=pk)
    except Projects.DoesNotExist:
        raise Http404('Project does not exist')
    return render(request, 'projects/projects_detail.html', {'project':project})