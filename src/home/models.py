from django.contrib.auth.models import User
from django.db import models


class RecipeBook(models.Model):
    recipeName = models.CharField("recipe name", max_length=100)
    img = models.URLField("image")
    ingredients = models.TextField("ingredients")
    link = models.URLField("link")

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


class WeeklyMenu(models.Model):
    created_at = models.DateTimeField("creation_date", auto_now_add=True)
    modified_at = models.DateTimeField("modification_date", auto_now=True)
    day1 = models.ForeignKey(
        RecipeBook,
        on_delete=models.CASCADE,
        null=True,
        related_name="day1",
    )
    day2 = models.ForeignKey(
        RecipeBook,
        on_delete=models.CASCADE,
        null=True,
        related_name="day2",
    )
    day3 = models.ForeignKey(
        RecipeBook,
        on_delete=models.CASCADE,
        null=True,
        related_name="day3",
    )
    day4 = models.ForeignKey(
        RecipeBook,
        on_delete=models.CASCADE,
        null=True,
        related_name="day4",
    )
    day5 = models.ForeignKey(
        RecipeBook,
        on_delete=models.CASCADE,
        null=True,
        related_name="day5",
    )
    day6 = models.ForeignKey(
        RecipeBook,
        on_delete=models.CASCADE,
        null=True,
        related_name="day6",
    )
    day7 = models.ForeignKey(
        RecipeBook,
        on_delete=models.CASCADE,
        null=True,
        related_name="day7",
    )

    owner = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.owner.username} - {self.created_at} | {self.modified_at}"
