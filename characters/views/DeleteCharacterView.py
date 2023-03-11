from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404
from characters.models import Character


class DeleteCharacterView(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy("accounts:login")
    model = Character
    template_name = "characters/view.html"
    context_object_name = "char"

    def get_success_url(self):
        return reverse_lazy("folders:view", kwargs={"pk": self.get_object().folder.id})

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data["delete_confirmation"] = True
        return data

    def get(self, request, pk):
        char = get_object_or_404(Character, id=pk)

        # check ownership
        if char.owner != request.user:
            return HttpResponseForbidden()
        return super().get(request, pk)

    def post(self, request, pk):
        char = get_object_or_404(Character, id=pk)

        # check ownership
        if char.owner != request.user:
            return HttpResponseForbidden()
        return super().post(request, pk)
