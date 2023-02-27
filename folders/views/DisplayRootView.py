from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.http import HttpResponseNotAllowed
from django.shortcuts import render

class DisplayRootView(LoginRequiredMixin, View):
    login_url = reverse_lazy("accounts:login")

    def get(self, request):
        root = request.user.rootfolder
        return render(request, "folders/root.html", {"root": root})

    def post(self, request):
        return HttpResponseNotAllowed(("GET"))