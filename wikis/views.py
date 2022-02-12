"""
Views
"""

from django.http import HttpResponse


def index(request):
    """
    index
    """
    print(request)
    return HttpResponse("Hello, world. You're at the wikis index.")
