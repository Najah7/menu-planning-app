from django.contrib.auth.decorators import login_required
from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = "Recipe Home"
urlpatterns = [
    path(
        "",
        login_required(TemplateView.as_view(template_name="home/home.html")),
        name="home",
    ),
    path(
        "recipes/",
        login_required(views.RecipeListView.as_view()),
        name="recipe_list",
    ),
    path(
        "recipes/<int:pk>",
        login_required(views.RecipeDetailView.as_view()),
        name="recipe_detail",
    ),
    path(
        "personal/",
        login_required(login_required(views.PersonalView.as_view())),
        name="personal",
    ),
    path(
        "weekly_recipe_list/",
        views.WeeklyRecipeListView.as_view(),
        name='weekly_recipe_list',
    ),
]
