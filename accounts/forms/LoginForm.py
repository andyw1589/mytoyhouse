from django import forms
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, required=True, error_messages={"required": "Please provide a username."})
    password = forms.CharField(min_length=8, required=True, error_messages={"required": "Please provide a password."})
