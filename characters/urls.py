from django.urls import path 
from characters.views import *

app_name = "characters"
urlpatterns = [
    path("add/<int:folder>/", AddCharacterView.as_view(), name="add"),
    path("view/<int:pk>", DisplayCharacterView.as_view(), name="view")
]