"""
Views
"""
from django.shortcuts import render
from .models import Project, Pro


def home(request):
    """
    home
    """
    # pylint: disable=no-member
    projects = Project.objects.all()
    pros = Pro.objects.all()

    # total_pros = pros.count()

    total_projects = projects.count()
    completed = projects.filter(status='Completed').count()
    pending = projects.filter(status='Pending').count()

    context = {'projects': projects, 'pros': pros,
               'total_projects': total_projects, 'completed': completed,
               'pending': pending}

    return render(request, 'accounts/dashboard.html', context)


def project(request):
    """
    project
    """
    # pylint: disable=no-member
    projects = Project.objects.all()
    return render(request, 'accounts/projects.html', {'projects': projects})


def pro(request):
    """
    pro
    """
    return render(request, 'accounts/pro.html')
