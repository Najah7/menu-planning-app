from django.urls import path

from . import views

app_name = "Recipe Home"
urlpatterns = [
    path(
        "rakuten/ichiba/item-search/",
        views.RakutenIchibaRedirectView.as_view(),
    ),
]
