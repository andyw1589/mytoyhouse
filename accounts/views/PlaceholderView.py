from django.views import View
from django.shortcuts import render

class PlaceholderView(View):
    def get(self, request):
        return render(request, "accounts/base.html")