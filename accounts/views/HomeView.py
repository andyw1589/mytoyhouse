from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View 
from django.urls import reverse_lazy
from django.shortcuts import render
from django.http import HttpResponseNotAllowed

class HomeView(LoginRequiredMixin, View):
    login_url = reverse_lazy("accounts:login")
    
    def get(self, request):
        return render(request, "accounts/home.html")
    
    def post(self, request):
        return HttpResponseNotAllowed(("GET"))