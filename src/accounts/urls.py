from django.urls import path

from . import views

app_name = "Accounts app"
urlpatterns = [
    path(
        "login/",
        views.LoginView.as_view(),
        name="login",
    ),
    path(
        "create/",
        views.CreateUserView.as_view(),
        name="create",
    ),
    path(
        "logout/",
        views.LogoutView.as_view(),
        name="logout",
    ),
]
