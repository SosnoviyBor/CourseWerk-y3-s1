import email
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

# class Login(forms.Form):
#     login = forms.CharField(max_length=50)
#     password = forms.CharField(max_length=50)