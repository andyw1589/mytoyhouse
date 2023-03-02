from django.views.generic.detail import DetailView
from folders.models import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.http import HttpResponseForbidden, HttpResponseNotAllowed

class DisplayFolderView(LoginRequiredMixin, DetailView):
    login_url = reverse_lazy("accounts:login")
    template_name = "folders/view.html"
    context_object_name = "folder"
    model = Folder

    def get(self, request, pk):
        # if folder is actually a root folder (root folders are always viewable)
        if self.get_object().parent is None:
            self.template_name = "folders/root.html"
            self.context_object_name = "root"

        if request.user != self.get_object().owner and self.get_object().private:
            return HttpResponseForbidden()
        
        return super().get(request, pk)
    
    def post(self, request, pk):
        return HttpResponseNotAllowed(("GET"))