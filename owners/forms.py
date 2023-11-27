"""Forms for the owners/profile app."""
from django import forms
from allauth.account.forms import SignupForm, LoginForm
from .models import Owner


class CustomSignupForm(SignupForm):
    """Form for the owner signup page"""
    first_name = forms.CharField(max_length=30, label='First Name', required=True, widget=forms.TextInput(attrs={'placeholder': 'First Name'}) )
    last_name = forms.CharField(max_length=30, label='Last Name', required=True,  widget=forms.TextInput(attrs={'placeholder': 'Last Name'}) )
   
    

    def __init__(self, *args, **kwargs):
       super(CustomSignupForm, self).__init__(*args, **kwargs)
       del self.fields['username']

    def save(self, request):
       user = super(CustomSignupForm, self).save(request)

      #  user.first_name = self.cleaned_data['first_name']
      #  user.last_name = self.cleaned_data['last_name']
       user.email = self.cleaned_data['email']
       user.save()

       return user

class CustomLoginForm(LoginForm):
      login = forms.EmailField(label='Email', required=True, widget=forms.TextInput(attrs={'placeholder': 'Email'}) )

class OwnerProfileForm(forms.ModelForm):
  """Form for owner profile"""
  class Meta():
    model = Owner
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

  profile_pic = forms.ImageField(widget=forms.ClearableFileInput(attrs={'class': 'form-control'}), required=False)



