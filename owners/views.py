from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from owners.models import owner


# Create your views here.
def profile(request):
    """A view that displays the profile page"""
    return render(request, 'owners/profile.html')

def edit_profile(request):
    """A view that displays the edit profile page"""
    return render(request, 'owners/edit_profile.html')

class ownerProfileView(View):
    """A view that displays the owner profile page"""
    def get(self, request):
        profile = owner.objects.all()
        return render(request, 'owners/profile.html')