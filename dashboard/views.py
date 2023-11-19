from django.shortcuts import render
from django.contrib.auth.decorators import login_required 


"""A view that displays the dashboard page only when logged in"""
@login_required
def dashboard(request):
    return render(request, 'dashboard/dashboard.html')