from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib import messages
from owners.models import Owner
from .forms import OwnerProfileForm
from django.http import JsonResponse


# Create your views here.
def owner_profile(request):
    """A view that displays the profile page"""
    owner = get_object_or_404(Owner, user=request.user)
    context = {
        'owner': owner,
    }
    return render(request, 'owners/owner_profile.html', context)


class ownerProfileView(View):
    """A view that displays the owner profile page"""
    def get(self, request):
        return render(request, 'owners/owner_profile.html')


def save_profile(request):
    """A view that saves the owner profile page"""
    if request.method == 'POST':
        print(request)
        print(request.POST)
        form = OwnerProfileForm(request.POST, request.FILES, instance=request.user.owner)
        print(request.user.owner)
    
        if form.is_valid():
            print('form is valid')
            form.save()
            return redirect('profile')
        else:
            print()
            messages.error(request, 'Please correct the error below.')
            return redirect('profile')
    else:
        form = OwnerProfileForm(instance=request.user.owner)
    return render(request, 'owners/owner_profile.html', {'form': form})

