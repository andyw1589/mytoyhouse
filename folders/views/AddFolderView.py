from django.views.generic.edit import CreateView
from folders.models import Folder
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.http import HttpResponseForbidden

class AddFolderView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy("accounts:login")
    model = Folder
    template_name = "folders/add.html"
    fields = ["parent", "name"]

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
        return data

    def get_success_url(self) -> str:
        return  reverse_lazy("folders:list", kwargs={"parent": self.kwargs["parent"]})

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
    
    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)
        form.fields["parent"].queryset = self.request.user.folder_set.all()
        if self.kwargs["parent"] != 0:
            form.fields["parent"].initial = self.request.user.folder_set.get(id=self.kwargs["parent"])
        return form