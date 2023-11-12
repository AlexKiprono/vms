from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from .models import Visitor

# Handles authentication

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "password1", "password2"]
        widgets = {
            
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        }

class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ["username", "password1", "password2"]
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
        }

# Handles visitors
class VisitorForm(forms.ModelForm):
    class Meta:
        model = Visitor
        fields = ["image", "title", "firstname", "lastname", "email", "host", "date"]
        widgets = {
            'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'title': forms.Select(attrs={'class': 'form-control'}),
            'firstname': forms.TextInput(attrs={'class': 'form-control'}),
            'lastname': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'host': forms.Select(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control'}),
        }

# Form to handle editing
class EditVisitorForm(forms.ModelForm):
    class Meta:
        model = Visitor
        fields = ["image", "title", "firstname", "lastname", "email", "host", "date"]
        widgets = {
            'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'title': forms.Select(attrs={'class': 'form-select form-select-sm'}),
            'firstname': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'lastname': forms.TextInput(attrs={'class': 'form-control form-control-sm'}),
            'email': forms.EmailInput(attrs={'class': 'form-control form-control-sm'}),
            'host': forms.Select(attrs={'class': 'form-select form-select-sm'}),
            'date': forms.DateInput(attrs={'class': 'form-control'}),
        }
