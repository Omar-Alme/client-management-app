from django.shortcuts import render

# Create your views here.
def dashboard(request):
    """A view that displays the add client page"""
    return render(request, 'clients/dashboard.html')