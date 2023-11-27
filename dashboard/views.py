from django.shortcuts import render
from owners.models import Owner
from django.contrib.auth.decorators import login_required 
from django.http import HttpResponse, JsonResponse
from clients.models import Client
from .forms import ClientForm


"""A view that displays the dashboard page only when logged in"""
@login_required
def dashboard(request):
    """Retrieve the user's profile information"""

    return render(request, 'dashboard/dashboard.html')

def client_form(request):
    """A view that displays the client form"""
   

    return render(request, 'clients/client_form.html')


           

    
    