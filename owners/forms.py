"""Forms for the owners/profile app."""
from django import forms
from allauth.account.forms import SignupForm
from .models import owner


class CustomSignupForm(SignupForm):
    # Add additional fields from your 'owner' model
    first_name = forms.CharField(max_length=30, label='First Name')
    last_name = forms.CharField(max_length=30, label='Last Name')
    business_name = forms.CharField(max_length=50, label='Business Name')

    def save(self, request):
        # Call the parent class method to save the user
        user = super().save(request)

        # Save additional fields to the 'owner' model
        owner = owner.objects.create(
            user=user,  
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            business_name=self.cleaned_data['business_name'],
            # Add other fields as needed
        )

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

