"""Forms for the owners/profile app."""
from django import forms
from allauth.account.forms import SignupForm, LoginForm
from allauth.account.views import SignupView
from .models import Owner
from django.contrib.auth import login


class CustomSignupForm(SignupForm):
    """Form for the owner signup page"""

    def __init__(self, *args, **kwargs):
        super(CustomSignupForm, self).__init__(*args, **kwargs)
        del self.fields['username']

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.email = self.cleaned_data['email']
        user.save()

        return user


class CustomLoginForm(LoginForm):
    login = forms.EmailField(
            label='Email',
            required=True,
            widget=forms.TextInput(attrs={'placeholder': 'Email'})
            )


class OwnerProfileForm(forms.ModelForm):
    """Form for owner profile"""
    class Meta():
        model = Owner
        fields = (
            'first_name', 'last_name',
            'business_name', 'email', 
            'bio', 'website'
            )
        widgets = {
          'first_name': forms.TextInput(attrs={'class': 'form-control'}),
          'last_name': forms.TextInput(attrs={'class': 'form-control'}),
          'business_name': forms.TextInput(attrs={'class': 'form-control'}),
          'email': forms.TextInput(attrs={'class': 'form-control'}),
          'bio': forms.Textarea(attrs={'class': 'form-control'}),
          'website': forms.URLInput(attrs={'class': 'form-control'}),
        }


class SignupView(SignupView):
    """A view that displays the signup page"""
    form_class = CustomSignupForm
    
    def form_valid(self, form):
      response = super().form_valid(form)

      login(self.request, self.user)
      return response






