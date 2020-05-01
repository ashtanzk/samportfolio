from django.shortcuts import render
from django.http import HttpResponse
from django.core import exceptions
from .models import Project, ProjectPhoto


def home(request):
    projects=Project.objects
    return render(request, "projects/home.html", {'projects':projects})

def project(request, project_id):
    projectphoto = ProjectPhoto.objects.get(pk=project_id)
    project_photos = ProjectPhoto.objects.filter(project_id=projectphoto.id)
    return render(request, 'projects/project.html', {"project_photos":project_photos, "projectphoto":projectphoto})

def aboutme(request):
    return render(request, "projects/aboutme.html")