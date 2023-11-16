from django.shortcuts import render

# Create your views here.
def profile(request):
    """A view that displays the profile page"""
    return render(request, 'owners/profile.html')