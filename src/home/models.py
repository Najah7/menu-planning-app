from typing import Any

from django.db import models


class RecipeBook(models.Model):
    recipeName = models.CharField("recipe name", max_length=100)
    img = models.URLField("image")
    ingredients = models.TextField("ingredients")

    def __str__(self) -> str:
        return self.recipeName
