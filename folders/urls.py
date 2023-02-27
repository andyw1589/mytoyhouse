from django.urls import path
from folders.views import *

app_name = "folders"
urlpatterns = [
    path("add/<int:parent>/", AddFolderView.as_view(), name="add"),
    path("details/<int:pk>/", DisplayFolderView.as_view(), name="details"),
    path("root/", DisplayRootView.as_view(), name="root")
]