"""
Models
"""

from django.db import models


class Category(models.Model):
    """
    Category
    """
    category_name = models.CharField(max_length=200)


class Wiki(models.Model):
    """
    Wiki
    """
    wiki_title = models.CharField(max_length=200)
    wiki_text = models.CharField(max_length=10000)
    pub_date = models.DateTimeField('date published')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)  # many to many (fix me)
