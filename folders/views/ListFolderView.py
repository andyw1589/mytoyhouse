from django.views.generic.list import ListView
from folders.models import Folder 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.http import HttpResponseForbidden

class ListFolderView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy("accounts:login")
    template_name = "folders/list.html"
    context_object_name = "folders"

    def get(self, request, parent):
        # user must be the owner
        if parent != 0:
            parent = Folder.objects.get(id=parent)
            if parent.owner != request.user:
                return HttpResponseForbidden()
        return super().get(request, parent)
    
    def post(self, request, parent):
        # user must be the owner
        if parent != 0:
            parent = Folder.objects.get(id=parent)
            if parent.owner != request.user:
                return HttpResponseForbidden()
        return super().post(request, parent)

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data["parent"] = self.kwargs["parent"]
        if data["parent"] != 0:
            parent = Folder.objects.get(id=data["parent"])
            data["parent_folder_name"] = parent.name
            
            if parent.parent is None:
                data["back_id"] = 0
            else:
                data["back_id"] = parent.parent.id
        return data
    
    def get_queryset(self):
        user_folders = self.request.user.folder_set
        if self.kwargs["parent"] == 0:
            # root folders
            return user_folders.filter(parent=None)
        else:
            return user_folders.filter(parent__id=self.kwargs["parent"])