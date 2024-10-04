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
        views.RecipeListView.as_view(),
        name="recipe_list",
    ),
    path(
        "ingredients_list/",
        views.IngredientsListView.as_view(),
        name="ingredients_list",
    ),
    path(
        "recipes/<int:pk>",
        views.RecipeDetailView.as_view(),
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
        name="weekly_recipe_list",
    ),
    path(
        "add_weekly_list/",
        login_required(views.ApplyWeeklyList),
        name="add_weekly_list",
    ),
    path(
        "add_recipe/",
        login_required(views.AddRecipeToList),
        name="add_recipe",
    ),
    path(
        "clear_personal/",
        login_required(views.ClearPersonal),
        name="clear_personal",
    ),
]
