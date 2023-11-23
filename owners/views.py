from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from owners.models import Owner


# Create your views here.
def profile(request):
    """A view that displays the profile page"""
    owner = get_object_or_404(Owner, user=request.user)
    context = {
        'owner': owner,
    }
    return render(request, 'owners/profile.html', context)


class ownerProfileView(View):
    """A view that displays the owner profile page"""
    def get(self, request):
        return render(request, 'owners/profile.html')