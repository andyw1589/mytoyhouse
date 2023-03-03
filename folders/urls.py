from django.urls import path
from folders.views import *

app_name = "folders"
urlpatterns = [
    path("add/<int:parent>/", AddFolderView.as_view(), name="add"),
    path("view/<int:pk>/", DisplayFolderView.as_view(), name="view"),
    path("edit/<int:pk>/", EditFolderView.as_view(), name="edit")
]