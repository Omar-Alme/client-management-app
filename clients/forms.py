from django import forms
from clients.models import Client
from django.forms import ModelForm

class ClientForm(forms.ModelForm):
  class Meta:
    model = Client
    fields = ('client_name', 'industry', 'email', 'bio', 'online_presence', )
    widgets = {
      'client_name': forms.TextInput(attrs={'class': 'form-control'}),
      'industry': forms.TextInput(attrs={'class': 'form-control'}),
      'email': forms.EmailInput(attrs={'class': 'form-control'}),
      'bio': forms.Textarea(attrs={'class': 'form-control'}),
      'online_presence': forms.URLInput(attrs={'class': 'form-control'}),
    }


