from django.urls import path
from folders.views import *

app_name = "folders"
urlpatterns = [
    path("<int:parent>/add/", AddFolderView.as_view(), name="add"),
    path("<int:pk>/view/", DisplayFolderView.as_view(), name="view"),
    path("<int:pk>/edit/", EditFolderView.as_view(), name="edit"),
    path("<int:pk>/delete/", DeleteFolderView.as_view(), name="delete")
]