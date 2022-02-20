"""
Views
"""
from django.shortcuts import render
# from django.http import HttpResponse


def home(request):
    """
    home
    """
    return render(request, 'accounts/dashboard.html')


def project(request):
    """
    project
    """
    return render(request, 'accounts/projects.html')


def pro(request):
    """
    pro
    """
    return render(request, 'accounts/pro.html')
