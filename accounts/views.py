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


def pro(request, pro_id):
    """
    pro
    """
    # pylint: disable=no-member
    pro_item = Pro.objects.get(id=pro_id)

    projects = pro_item.project_set.all()
    # for project in projects:
    #     print("=====", project.name)
    #     print("=====", project.category.all())
    #     for x in project.category.all():
    #         print(x.name)
    project_count = projects.count()

    context = {'pro': pro_item, 'projects': projects, 'project_count': project_count}
    return render(request, 'accounts/pro.html', context)
