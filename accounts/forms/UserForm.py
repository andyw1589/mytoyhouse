from django import forms
from django.contrib.auth.models import User

class UserForm(forms.Form):
    username = forms.CharField(max_length=100, required=True, error_messages={"required": "Please provide a username."})
    pass1 = forms.CharField(min_length=8, required=True)
    pass2 = forms.CharField(min_length=8, required=True, error_messages={"required": "You must confirm your password."})
    
    def clean_username(self):
        username = self.cleaned_data.get("username").strip()
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("That username is taken.")
        return username

    def clean_pass2(self):
        pass1 = self.cleaned_data.get("pass1")
        pass2 = self.cleaned_data.get("pass2")

        if pass1 != pass2:
            raise forms.ValidationError("Your passwords do not match.")
        return pass2
