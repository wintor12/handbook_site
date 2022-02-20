"""
Views
"""
from django.shortcuts import render
# from django.http import HttpResponse


def home(request):
    return render(request, 'accounts/dashboard.html')


def project(request):
    return render(request, 'accounts/projects.html')


def pro(request):
    return render(request, 'accounts/pro.html')
