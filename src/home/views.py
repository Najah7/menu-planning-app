import random
import re
from datetime import datetime
from typing import Any

from django.db.models.query import QuerySet
from django.http import HttpRequest, HttpResponseRedirect
from django.http.response import HttpResponse as HttpResponse
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, TemplateView

from .models import RecipeBook, WeeklyMenu


class RecipeListView(ListView):
    model = RecipeBook
    template_name = "home/recipe_list.html"
    context_object_name = "recipes"


class RecipeDetailView(DetailView):
    model = RecipeBook
    context_object_name = "recipe"
    template_name = "home/recipe_detail.html"


class PersonalView(ListView):
    model = WeeklyMenu
    template_name = "home/personal.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        book = RecipeBook.objects
        menu = WeeklyMenu.objects.filter(owner=self.request.user).values()
        context["exists"] = True

        if len(menu) == 0:
            context["exists"] = False
            return context

        for idx in range(7):
            if menu[0][f"day{idx+1}_id"] != None:
                context[f"item{idx+1}"] = book.filter(
                    id=menu[0][f"day{idx+1}_id"]
                ).values()[0]["recipeName"]
                context[f"link{idx+1}"] = book.filter(
                    id=menu[0][f"day{idx+1}_id"]
                ).values()[0]["link"]
                context[f"img{idx+1}"] = book.filter(
                    id=menu[0][f"day{idx+1}_id"]
                ).values()[0]["img"]

        ingredients = list()
        for idx in range(7):
            if menu[0][f"day{idx+1}_id"] != None:
                ingredients.extend(
                    book.filter(id=menu[0][f"day{idx+1}_id"])
                    .values()[0]["ingredients"]
                    .strip()
                    .split("、")
                )
        context["ingredients"] = set([self._clean_text(item) for item in ingredients])

        return context

    def _clean_text(self, text):
        if text == "":
            return ""

        HIRAGANA = r"\u3041-\u3096"
        KATAKANA = r"\u30A1-\u30F6"
        PROLONGED_SOUND_MARK = r"\u30FC"
        KANJI = r"\u3006\u4E00-\u9FFF"  # U+3006: 〆
        REPEATING_MARK = r"\u3005"

        WHITELIST_PTN = re.compile(
            rf"[a-zA-Z0-9!?()「」、。{HIRAGANA}{KATAKANA}{PROLONGED_SOUND_MARK}{KANJI}{REPEATING_MARK}]"
        )
        JP_PTN = re.compile(rf"[{HIRAGANA}{KATAKANA}{PROLONGED_SOUND_MARK}{KANJI}]")

        clean_text = str()
        for character in text:
            if JP_PTN.match(character):
                clean_text += character

        return clean_text


def ApplyWeeklyList(request):
    items = RecipeBook.objects.filter(
        id__in=sorted([int(idx) for idx in request.GET["q"].split("-")])
    )

    menu = WeeklyMenu.objects
    try:
        menu.get(owner=request.user).delete()
    except:
        ...
    finally:
        menu.create(
            day1=items[0],
            day2=items[1],
            day3=items[2],
            day4=items[3],
            day5=items[4],
            day6=items[5],
            day7=items[6],
            owner=request.user,
        )

    return HttpResponseRedirect(reverse_lazy("home:personal"))


def AddRecipeToList(request):
    item = RecipeBook.objects.get(id=int(request.GET["q"]))
    menu = WeeklyMenu.objects.filter(owner=request.user).values()

    if len(menu) == 0:
        WeeklyMenu.objects.create(
            day1=item,
            owner=request.user,
        )
        return HttpResponseRedirect(reverse_lazy("home:personal"))

    if menu[0][f"day1_id"] == None:
        WeeklyMenu.objects.filter(id=menu[0]["id"]).update(day1_id=item)
    elif menu[0][f"day2_id"] == None:
        WeeklyMenu.objects.filter(id=menu[0]["id"]).update(day2_id=item)
    elif menu[0][f"day3_id"] == None:
        WeeklyMenu.objects.filter(id=menu[0]["id"]).update(day3_id=item)
    elif menu[0][f"day4_id"] == None:
        WeeklyMenu.objects.filter(id=menu[0]["id"]).update(day4_id=item)
    elif menu[0][f"day5_id"] == None:
        WeeklyMenu.objects.filter(id=menu[0]["id"]).update(day5_id=item)
    elif menu[0][f"day6_id"] == None:
        WeeklyMenu.objects.filter(id=menu[0]["id"]).update(day6_id=item)
    elif menu[0][f"day7_id"] == None:
        WeeklyMenu.objects.filter(id=menu[0]["id"]).update(day7_id=item)

    return HttpResponseRedirect(reverse_lazy("home:personal"))


def ClearPersonal(request):
    WeeklyMenu.objects.filter(owner=request.user).delete()
    return HttpResponseRedirect(reverse_lazy("home:personal"))


class WeeklyRecipeListView(TemplateView):
    template_name = "home/weeklyrecipe_list.html"

    def get_weekly_recipe(self, seed):
        random.seed(seed)
        random_numbers = random.sample(range(1, RecipeBook.objects.count() + 1), 7)
        weekly_recipes = []
        for random_number in random_numbers:
            recipe = RecipeBook.objects.get(id=random_number)
            weekly_recipes.append(
                {
                    "id": random_number,
                    "recipeName": recipe.recipeName,
                    "img": recipe.img,
                    "ingredients": recipe.ingredients,
                }
            )

        return weekly_recipes

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        if "s" not in self.request.GET:
            timestamp = datetime.today().timestamp()
            weekStart = int(timestamp - (timestamp % 604800))
            return HttpResponseRedirect(
                reverse_lazy("home:weekly_recipe_list") + f"?s={weekStart}"
            )
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        s = self.request.GET.get("s")
        items = self.get_weekly_recipe(seed=int(s))
        context["weekly_recipes"] = items
        context["item_list"] = "-".join([str(item["id"]) for item in items])

        return context
