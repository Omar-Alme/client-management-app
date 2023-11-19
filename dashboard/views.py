from django.shortcuts import render


"""A view that displays the dashboard page"""
def dashboard(request):
    """A view that displays the index page"""
    return render(request, 'dashboard/dashboard.html')