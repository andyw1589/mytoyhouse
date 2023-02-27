from django.views import View 
from django.http import HttpResponseNotAllowed
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import redirect

class LogoutView(LoginRequiredMixin, View):
    login_url = reverse_lazy("accounts:login")
    def get(self, request):
        logout(request)
        return redirect("accounts:login")
    
    def post(self, request):
        return HttpResponseNotAllowed(("GET"))
