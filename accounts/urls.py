"""
Urls
"""

from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('projects/', views.project, name='project'),
    path('pro/<int:pro_id>/', views.pro, name='pro'),
]
