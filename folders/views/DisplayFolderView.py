from django.views.generic.detail import DetailView
from folders.models import Folder 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.http import HttpResponseForbidden

class DisplayFolderView(LoginRequiredMixin, DetailView):
    login_url = reverse_lazy("accounts:login")
    template_name = "folders/details.html"
    context_object_name = "folder"
    model = Folder

    def get(self, request, pk):
        # user must be the owner
        folder = Folder.objects.get(id=pk)
        if folder.owner != request.user:
            return HttpResponseForbidden()
        return super().get(request, pk)
    
    def post(self, request, pk):
        # user must be the owner
        folder = Folder.objects.get(id=pk)
        if folder.owner != request.user:
            return HttpResponseForbidden()
        return super().post(request, pk)