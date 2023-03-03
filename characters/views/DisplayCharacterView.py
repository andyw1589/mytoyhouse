from django.views.generic.detail import DetailView
from characters.models import Character
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.http import HttpResponseForbidden, HttpResponseNotAllowed

class DisplayCharacterView(LoginRequiredMixin, DetailView):
    login_url = reverse_lazy("accounts:login")
    template_name = "characters/view.html"
    context_object_name = "char"
    model = Character

    def get(self, request, pk):
        # private?
        char = self.get_object()
        if char.owner != request.user and char.private:
            return HttpResponseForbidden()
        
        return super().get(request, pk)
    
    def post(self, request, pk):
        return HttpResponseNotAllowed(("GET"))