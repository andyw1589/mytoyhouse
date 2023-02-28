from django.views.generic.edit import CreateView
from folders.models import Folder
from characters.forms import CharacterForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.http import HttpResponseForbidden

class AddCharacterView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy("accounts:login")
    template_name = "characters/add.html"
    form_class = CharacterForm

    def get(self, request, folder):
        # user must be the owner of the target folder
        if folder != 0:
            folder = Folder.objects.get(id=folder)
            if folder.owner != request.user:
                return HttpResponseForbidden()
        return super().get(request, folder)
    
    def post(self, request, folder):
        # user must be the owner
        if folder != 0:
            folder = Folder.objects.get(id=folder)
            if folder.owner != request.user:
                return HttpResponseForbidden()
        return super().post(request, folder)

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data["folder"] = self.kwargs["folder"]
        return data

    def get_success_url(self) -> str:
        return  reverse_lazy("folders:view", kwargs={"pk": self.kwargs["folder"]})

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
    
    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)
        # exclude the root folder; no characters in the root folder
        form.fields["folder"].queryset = self.request.user.folder_set.exclude(parent=None)
        form.fields["folder"].initial = self.request.user.folder_set.get(id=self.kwargs["folder"])
        return form