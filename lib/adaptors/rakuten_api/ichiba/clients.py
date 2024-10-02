import enum
import json

import requests

from .responses import ErrorResponse, ItemResponse
from .values import RakutenIchibaGenreIDs


class RakutenIchibaItemClient:
    def __init__(self):
        # TODO: get app_id from config
        self.app_id = "1003118371091832102"
        self.SEARCH_URL = (
            "https://app.rakuten.co.jp/services/api/IchibaItem/Search/20220601"
        )
        self.HITS = 10

    def fetch_groceries(self, ingredient):
        # NOTE: return a grocery item or grocery items?
        params = self._create_params(ingredient, RakutenIchibaGenreIDs.GROCERY.value)
        return self._get_api_data(params)

    def fetch_recommend_cookwares(self, recipe_title):
        params = self._create_params(recipe_title, RakutenIchibaGenreIDs.COOKWARE.value)
        return self._get_api_data(params)

    def _get_api_data(self, params) -> ItemResponse | ErrorResponse:
        res = requests.get(self.SEARCH_URL, params=params)
        data = json.loads(res.text)
        if res.status_code != 200:
            return ErrorResponse(**data)
        return ItemResponse(**data)

    def _create_params(self, keyword, genre_id):
        return {
            "applicationId": self.app_id,
            "format": "json",
            "keyword": keyword,
            "hits": self.HITS,
            "genreId": genre_id,
        }
