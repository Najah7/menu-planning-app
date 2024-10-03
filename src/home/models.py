from typing import Any

from django.db import models


class RecipeBook(models.Model):
    recipeName = models.CharField("recipe name", max_length=100)
    img = models.URLField("image")
    ingredients = models.TextField("ingredients")

    def __str__(self) -> str:
        return self.recipeName


class IngredientCategory(models.Model):
    name = models.CharField("name", max_length=100)
    description = models.TextField("description")

    def __str__(self) -> str:
        return f"{self.name}: {self.description}"


class IngredientsToRecipe(models.Model):
    recipe = models.ForeignKey(RecipeBook, on_delete=models.CASCADE)
    category = models.ForeignKey(IngredientCategory, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.recipe} {self.category}"
