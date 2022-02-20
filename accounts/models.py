"""
Models
"""

from django.db import models


class Category(models.Model):
    """
    Category
    """
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1000, blank=True)

    def __str__(self):
        return str(self.name)


class Pro(models.Model):
    """
    Pro
    """
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return str(self.name)


class Project(models.Model):
    """
    Project
    """
    STATUS = (
        ('Open', 'Open'),
        ('Assigned', 'Assigned'),
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
    )
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1000, blank=True)
    pro = models.ForeignKey(Pro, null=True, blank=True, on_delete=models.SET_NULL)
    category = models.ManyToManyField(Category, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    status = models.CharField(max_length=200, null=True, blank=True, choices=STATUS)

    def __str__(self):
        return str(self.name)
