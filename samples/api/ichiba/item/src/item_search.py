import requests
import json

# This is from the sample app
# python api/ichiba/item/src/item_search.py > api/ichiba/item/outputs/items.json

SEARCH_URL = 'https://app.rakuten.co.jp/services/api/IchibaItem/Search/20220601'

def get_api_data(params):
    api = requests.get(SEARCH_URL, params=params).text
    return json.loads(api)

GENRE_LIST = 0
GROCERY = 100227
COOKWARE = 558944

params = {
    "applicationId": "1003118371091832102",
    "format": "json",
    'keyword':'唐揚げ',
    'hits':10,
    "genreId": COOKWARE,
}

result = get_api_data(params)
print(json.dumps(result, indent=2, ensure_ascii=False))