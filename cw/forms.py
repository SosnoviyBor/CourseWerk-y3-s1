import email
from django import forms

class Register(forms.Form):
    email = forms.EmailField()
    login = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50)