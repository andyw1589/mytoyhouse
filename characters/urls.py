from django.urls import path 
from characters.views import *

app_name = "characters"
urlpatterns = [
    path("add/<int:folder>/", AddCharacterView.as_view(), name="add")
]