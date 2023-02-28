from django import forms
from characters.models import Character 

class CharacterForm(forms.ModelForm):
    tags = forms.CharField(max_length=2000, required=False)  # comma-separated string of tags that will be processed
    class Meta:
        model = Character 
        exclude = ["owner", "created"]