from django.views.generic import DetailView, ListView, TemplateView

from .models import RecipeBook

import random


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

class WeeklyRecipeListView(TemplateView):
    template_name = "home/weeklyrecipe_list.html"

    def get_weekly_recipe(self, seed):
        random.seed(seed)
        random_numbers = random.sample(range(1, RecipeBook.objects.count()+1), 7)
        weekly_recipes = []
        for random_number in random_numbers:
            recipe = RecipeBook.objects.get(id=random_number)
            weekly_recipes.append(
            {
                "id": random_number,
                "recipeName": recipe.recipeName,
                "img": recipe.img,
                "ingredients": recipe.ingredients
            }
            )

        return weekly_recipes
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        s = self.request.GET.get("s")
        if s is None:  
            context['weekly_recipes'] = self.get_weekly_recipe()
        context['weekly_recipes'] = self.get_weekly_recipe(seed = s)
        return context
