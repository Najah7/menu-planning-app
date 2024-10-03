import json

import requests
from typing import List

from .responses import ErrorResponse, ItemResponse, Item
from .values import RakutenIchibaGenreIDs
from .errors import RakutenAPIError


class RakutenIchibaItemClient:
    def __init__(self):
        # TODO: get app_id from config
        self.app_id = "1003118371091832102"
        self.SEARCH_URL = (
            "https://app.rakuten.co.jp/services/api/IchibaItem/Search/20220601"
        )
        self.HITS = 10

    def fetch_grocery(self, grocery_name: str)-> Item:
        """
        Fetch groceries for the ingredient.

        @raises RakutenAPIError
        """
        params = self._create_params(grocery_name, RakutenIchibaGenreIDs.GROCERY.value)
        data = self._get_api_data(params)
        response = ItemResponse(**data)
        return self._pick_one(response)

    def fetch_recommend_cookwares(self, recipe_title: str) -> List[Item]:
        """
        Fetch recommended cookwares for the recipe title.

        @raises RakutenAPIError
        """
        params = self._create_params(recipe_title, RakutenIchibaGenreIDs.COOKWARE.value)
        data = self._get_api_data(params)
        return ItemResponse(**data).Items

    def _get_api_data(self, params):
        res = requests.get(self.SEARCH_URL, params=params)
        data = json.loads(res.text)
        if res.status_code != 200:
            raise RakutenAPIError(
                "something went wrong when calling Outer API",
                ErrorResponse(**data))
        return data

    def _create_params(self, keyword, genre_id):
        return {
            "applicationId": self.app_id,
            "format": "json",
            "keyword": keyword,
            "hits": self.HITS,
            "genreId": genre_id,
        }
    
    def _pick_one(self, items: ItemResponse) -> ItemResponse:
        # HACK: how should I pick one item?
        return items.Items[0]
