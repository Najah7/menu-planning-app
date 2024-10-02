from django.urls import path

from . import views

app_name = "Recipe Home"
urlpatterns = [
    path(
        "",
        views.RecipeListHome.as_view(),
        name="recipe_list",
    ),
]
