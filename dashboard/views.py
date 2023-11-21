from django.shortcuts import render
from owners.models import owner
from django.contrib.auth.decorators import login_required 


"""A view that displays the dashboard page only when logged in"""
@login_required
def dashboard(request):
    """Retrieve the user's profile information"""

    return render(request, 'dashboard/dashboard.html')