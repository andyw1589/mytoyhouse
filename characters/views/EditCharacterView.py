from django.views.generic.edit import UpdateView
from characters.models import Tag, Character
from characters.forms import CharacterForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.http import HttpResponseForbidden

class EditCharacterView(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy("accounts:login")
    template_name = "characters/edit.html"
    form_class = CharacterForm
    model = Character
    context_object_name = "char"

    def get(self, request, pk):
        # user must be the owner of the character
        char = self.get_object()
        if char.owner != request.user:
            return HttpResponseForbidden()
        
        return super().get(request, pk)
    
    def post(self, request, pk):
        # user must be the owner of the character
        char = self.get_object()
        if char.owner != request.user:
            return HttpResponseForbidden()
        
        return super().post(request, pk)

    def get_success_url(self) -> str:
        return reverse_lazy("characters:view", kwargs={"pk": self.get_form().instance.id})

    def form_valid(self, form):
        form.instance.owner = self.request.user
        data = super().form_valid(form)  # save the character
        
        # process the tags
        new_tags = list(map(str.strip, form.cleaned_data["tags"].split(',')))  # tags in form
        current_tags = form.instance.list_tags()  # current tags already applied

        # find tags to delete (in current_tags but not tags)
        to_delete = [tag for tag in current_tags if tag not in new_tags]

        # find tags to add (in tags but not current_tags)
        to_add = [tag.strip() for tag in new_tags if (tag not in current_tags) and (tag != '')]

        for tag in to_add:
            new_tag = Tag.objects.create(character=form.instance, tag=tag)
            new_tag.save()

        for tag in to_delete:
            old_tag = Tag.objects.get(character=form.instance, tag=tag)
            old_tag.delete()

        return data
    
    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)
        # exclude the root folder; no characters in the root folder
        form.fields["folder"].queryset = self.request.user.folder_set.exclude(parent=None)
        form.fields["folder"].initial = form.instance.folder

        # get all the character's current tags
        tags = form.instance.list_tags()
        form.fields["tags"].initial = ", ".join(tags)

        return form