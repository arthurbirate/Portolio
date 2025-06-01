from django.shortcuts import render, redirect
from .forms import ProjectForm
from .models import Project

def projects(request):
    projects = Project.objects.all()
    return render(request, 'projects/projects.html', {'projects': projects})


def add_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('projects')  # Change to your project list URL name
    else:
        form = ProjectForm()
    return render(request, 'projects/add_project.html', {'form': form})