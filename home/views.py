"""Views for the home page of the app"""
from django.shortcuts import render
from django.contrib import messages


def index(request):
    """A view that displays the index page"""

    return render(request, 'home/index.html')