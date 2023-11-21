"""Forms for the owners/profile app."""
from django import forms
from allauth.account.forms import SignupForm
from .models import owner


class CustomSignupForm(SignupForm):
    """Form for the owner signup page"""
    first_name = forms.CharField(max_length=30, label='First Name', required=True, help_text='Required.', widget=forms.TextInput(attrs={'placeholder': 'First Name'}) )
    last_name = forms.CharField(max_length=30, label='Last Name', required=True, help_text='Required.', widget=forms.TextInput(attrs={'placeholder': 'Last Name'}) )
    business_name = forms.CharField(max_length=50, label='Business Name', required=True, help_text='Required.', widget=forms.TextInput(attrs={'placeholder': 'Business Name'}) )

    def __init__(self, *args, **kwargs):
       super(CustomSignupForm, self).__init__(*args, **kwargs)
       del self.fields['username']

    def save(self, request):
       user = super(CustomSignupForm, self).save(request)

       user.first_name = self.cleaned_data['first_name']
       user.last_name = self.cleaned_data['last_name']
       user.business_name = self.cleaned_data['business_name']
       user.save()

       return user


class ownerProfileForm(forms.ModelForm):
  """Form for owner profile"""
  class Meta():
    model = owner
    fields = ('profile_pic', 'first_name', 'last_name', 'business_name', 'email', 'bio', 'website')
    widgets = {
      'profile_pic': forms.FileInput(attrs={'class': 'form-control'}),
      'first_name': forms.TextInput(attrs={'class': 'form-control'}),
      'last_name': forms.TextInput(attrs={'class': 'form-control'}),
      'business_name': forms.TextInput(attrs={'class': 'form-control'}),
      'email': forms.TextInput(attrs={'class': 'form-control'}),
      'bio': forms.Textarea(attrs={'class': 'form-control'}),
      'website': forms.URLInput(attrs={'class': 'form-control'}),
    }

