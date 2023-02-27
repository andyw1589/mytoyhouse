from django.views.generic.edit import FormView
from accounts.forms import LoginForm
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect

class LoginView(FormView):
    form_class = LoginForm
    template_name = "accounts/login.html"
    success_url = reverse_lazy("accounts:home")

    def get(self, request):
        if request.user.is_authenticated:
            return redirect("accounts:home")
        return super().get(request)

    def form_valid(self, form):
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]

        user = authenticate(self.request, username=username, password=password)
        if user is None:
            print("bruh")
            form.add_error("username", "Username/password combination is not correct")
            return super().form_invalid(form)
        else:
            login(self.request, user)
            return super().form_valid(form)
