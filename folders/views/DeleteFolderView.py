from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404
from folders.models import Folder


class DeleteFolderView(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy("accounts:login")
    model = Folder
    template_name = "folders/view.html"
    context_object_name = "folder"

    def get_success_url(self):
        return reverse_lazy("folders:view", kwargs={"pk": self.get_object().parent.id})

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data["delete_confirmation"] = True
        return data

    def get(self, request, pk):
        folder = get_object_or_404(Folder, id=pk)

        # cannot delete root folder
        if folder.owner is None:
            return HttpResponseForbidden()

        # check ownership
        if folder.owner != request.user:
            return HttpResponseForbidden()
        return super().get(request, pk)

    def post(self, request, pk):
        folder = get_object_or_404(Folder, id=pk)

        # cannot delete root folder
        if folder.owner is None:
            return HttpResponseForbidden()

        # check ownership
        if folder.owner != request.user:
            return HttpResponseForbidden()
        return super().post(request, pk)
