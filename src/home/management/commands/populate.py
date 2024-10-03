from os import path
from wsgiref.util import request_uri

from conf.settings import BASE_DIR
from django.core.management.base import BaseCommand, CommandError
from home.models import IngredientCategory, IngredientsToRecipe, RecipeBook


class Command(BaseCommand):
    help = "Populates DB"

    def handle(self, *args, **options):
        self._make_categories()

        book = RecipeBook.objects
        ingredientLookup = IngredientsToRecipe.objects

        book.all().delete()
        ingredientLookup.all().delete()

        with open(
            path.join(BASE_DIR.parent, "recipe_info.csv"),
            "r",
            encoding="utf-8",
        ) as file:
            for line in file.readlines()[1:]:
                name, img, ingredients, link = line.split(",")
                item = book.create(
                    recipeName=name,
                    img=img,
                    ingredients=ingredients,
                    link=link,
                )

                for category in IngredientCategory.objects.all():
                    if self._find_ingredient(category, ingredients):
                        ingredientLookup.create(recipe=item, category=category)

    def _find_ingredient(self, category, ingredients):
        filter_list = category.description.split(", ")
        for item in filter_list:
            if item in ingredients:
                return True

        return False

    def _make_categories(self):
        categories = IngredientCategory.objects

        categories.all().delete()

        categories.create(
            name="肉",
            description="肉, 豚, 鳥, ロース, ハム, ささみ, 手羽先",
        )
        categories.create(
            name="玉ねぎ",
            description="タマネギ, 玉ねぎ, たまねぎ",
        )
        categories.create(
            name="ナス",
            description="ナス, 茄子, なすび, なす",
        )
        categories.create(
            name="じゃが芋",
            description="じゃが芋, じゃがいも, ジャガイモ, 里芋",
        )
        categories.create(
            name="れんこん",
            description="れんこん",
        )
        categories.create(
            name="きゅうり",
            description="きゅうり",
        )
        categories.create(
            name="卵",
            description="卵",
        )
        categories.create(
            name="にら",
            description="にら, ニラ",
        )
        categories.create(
            name="キノコ",
            description="しめじ, えのき",
        )
        categories.create(
            name="キャベツ",
            description="キャベツ, きゃべつ",
        )
        categories.create(
            name="ゴーヤー",
            description="ゴーヤー",
        )
        categories.create(
            name="かぼちゃ",
            description="かぼちゃ",
        )
        categories.create(
            name="栗",
            description="栗",
        )
        categories.create(
            name="小松菜",
            description="小松菜",
        )
        categories.create(
            name="ネギ",
            description="ネギ, ねぎ, 青ねぎ",
        )
        categories.create(
            name="ピーマン",
            description="ピーマン",
        )
        categories.create(
            name="大根",
            description="大根",
        )
        categories.create(
            name="冬瓜(とうがん)",
            description="冬瓜, とうがん",
        )
        categories.create(
            name="にんじん",
            description="にんじん, ニンジン, 人参",
        )
        categories.create(
            name="ごぼう",
            description="ごぼう",
        )
        categories.create(
            name="オクラ",
            description="オクラ",
        )
        categories.create(
            name="こんにゃく",
            description="こんにゃく",
        )
