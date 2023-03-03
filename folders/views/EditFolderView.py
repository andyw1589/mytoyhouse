from django.views.generic.edit import UpdateView
from folders.models import Folder
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.http import HttpResponseForbidden, HttpResponseNotAllowed

class EditFolderView(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy("accounts:login")
    template_name="folders/edit.html"
    context_object_name = "folder"
    model = Folder
    fields = ["parent", "name", "description", "private"]

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

    def get_success_url(self) -> str:
        # open details of the new folder
        return reverse_lazy("folders:view", kwargs={"pk": self.object.id})
    
    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)
        form.fields["parent"].queryset = self.request.user.folder_set.all().exclude(id=self.kwargs["pk"])
        form.fields["parent"].queryset = form.fields["parent"].queryset.exclude(id__in=self.get_object().folder_set.all())
        return form