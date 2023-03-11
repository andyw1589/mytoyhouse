from django.urls import path 
from characters.views import *

app_name = "characters"
urlpatterns = [
    path("<int:folder>/add/", AddCharacterView.as_view(), name="add"),
    path("<int:pk>/view/", DisplayCharacterView.as_view(), name="view"),
    path("<int:pk>/edit/", EditCharacterView.as_view(), name="edit"),
    path('<int:pk>/delete/', DeleteCharacterView.as_view(), name="delete")
]