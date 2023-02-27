from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from accounts.forms import UserForm
from django.contrib.auth.models import User
from folders.models import Folder

class SignUpView(FormView):
    template_name = "accounts/signup.html"
    success_url = reverse_lazy("accounts:login")
    form_class = UserForm

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data["title"] = "Sign Up"
        return data
    
    def form_valid(self, form):
        # create the user
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("pass1")
        user = User.objects.create_user(username=username, password=password)
        user.save()

        # automatically create the user's root folder
        folder = Folder.objects.create(owner=user, name="default")
        folder.save()
        
        return super().form_valid(form)