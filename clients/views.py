from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.models import User
from django.views import generic
from .models import Client
from owners.models import Owner
from .forms import ClientForm


@login_required
def dashboard(request):
    """Retrieve the user's profile information"""
    user_clients = Client.objects.filter(user=request.user)

    context = {
        'clients': user_clients,
        }

    return render(request, 'clients/dashboard.html', context)


def client_form(request):
    """A view that displays the client form"""

    form = ClientForm()

    if request.method == 'POST':

        form = ClientForm(request.POST)
        if form.is_valid():
            new_client = form.save(commit=False)
            new_client.user = request.user
            new_client.save()

            return redirect('clients:dashboard')

    clients = Client.objects.filter(user=request.user)


    context = {
        'form': form,
        'clients': clients,
        }
    return render(request, 'clients/client_form.html', context)


def edit_client(request, pk):
    """A view that displays the client form"""
    client = get_object_or_404(Client,pk=pk)

    # form = ClientForm(instance=client)
    if request.method == 'POST':
        # print('Printing Post' ,request.POST)
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('clients:dashboard')
    else:
        form = ClientForm(instance=client)


    context = {
        'form': form,
        'client': client,
        }
    return render(request, 'clients/edit_client.html', context)


def delete_client(request, pk):
    """A view that displays the client form"""
    client = get_object_or_404(Client,pk=pk)

    if request.method == 'POST':
        client.delete()
        return redirect('clients:dashboard')

    context = {
        'client': client,
        }
    return render(request, 'clients/delete_client.html', context)