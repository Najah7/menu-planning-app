from django.views.generic import DetailView, ListView, TemplateView

from .models import RecipeBook


class RecipeListView(ListView):
    model = RecipeBook
    template_name = "home/recipe_list.html"
    context_object_name = "recipes"


class RecipeDetailView(DetailView):
    model = RecipeBook
    context_object_name = "recipe"
    template_name = "home/recipe_detail.html"


class PersonalView(TemplateView):
    template_name = "home/personal.html"
