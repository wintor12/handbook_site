"""
Admin
"""

from django.contrib import admin

from .models import Project, Category, Pro

admin.site.register(Project)
admin.site.register(Category)
admin.site.register(Pro)
