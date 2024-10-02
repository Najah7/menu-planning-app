from os import path

from conf.settings import BASE_DIR
from django.core.management.base import BaseCommand, CommandError
from home.models import RecipeBook


class Command(BaseCommand):
    help = "Populates DB"

    def handle(self, *args, **options):
        book = RecipeBook.objects
        book.all().delete()

        with open(
            path.join(BASE_DIR.parent, "recipe_info.csv"),
            "r",
            encoding="utf-8",
        ) as file:
            for line in file.readlines()[1:]:
                name, img, ingredients = line.split(",")
                book.create(
                    recipeName=name,
                    img=img,
                    ingredients=ingredients,
                )

        print(book.all())
