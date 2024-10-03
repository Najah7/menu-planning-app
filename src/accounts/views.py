from django.contrib.auth import models, views
from django.urls import reverse_lazy
from django.views.generic import CreateView

from . import forms


class LoginView(views.LoginView):
    template_name = "accounts/login.html"


class CreateUserView(CreateView):
    model = models.User
    form_class = forms.UserCreationForm
    template_name = "accounts/create.html"
    success_url = reverse_lazy("home:personal")


class LogoutView(views.LogoutView):
    next_page = reverse_lazy("accounts:login")
