from django.urls import path
from folders.views import *

app_name = "folders"
urlpatterns = [
    path("add/<int:parent>", AddFolderView.as_view(), name="add"),
    path("list/<int:parent>", ListFolderView.as_view(), name="list")
]