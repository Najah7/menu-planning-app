from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views

app_name = "Recipe Home"
urlpatterns = [
    path(
        "",
        views.RecipeListView.as_view(),
        name="recipe_list",
    ),
    path(
        "<int:pk>",
        views.RecipeDetailView.as_view(),
        name="recipe_detail",
    ),
    path(
        "personal/",
        login_required(views.PersonalView.as_view()),
        name="personal",
    ),
]
