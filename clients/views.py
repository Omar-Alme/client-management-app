from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from .models import Client
from dashboard.forms import ClientForm



def client_form(request):
    """A view that displays the client form"""

    form = ClientForm()
    clients = Client.objects.all()
    if request.method == 'POST':
        # print('Printing Post' ,request.POST)
        form = ClientForm(request.POST)
        if form.is_valid():
            new_client = form.save()
            return redirect('add_client')


    context = {
        'form': form,
        'clients': clients,
        }
    return render(request, 'clients/client_form.html', context)

def add_client(request):
    """A view that displays the client form"""
    clients = Client.objects.all()

    context = {
        'clients': clients,
        }

    return render(request, 'clients/add_client.html', context)

def edit_client(request, pk):
    """A view that displays the client form"""
    client = get_object_or_404(Client,pk=pk)

    # form = ClientForm(instance=client)
    if request.method == 'POST':
        # print('Printing Post' ,request.POST)
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('add_client')
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
        return redirect('add_client')

    context = {
        'client': client,
        }
    return render(request, 'clients/delete_client.html', context)