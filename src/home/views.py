from django.views.generic import ListView

from .models import RecipeBook


class RecipeListHome(ListView):
    model = RecipeBook
    template_name = "home/recipe_list.html"
    context_object_name = "recipes"
