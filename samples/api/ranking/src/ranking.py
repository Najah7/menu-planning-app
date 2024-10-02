import requests
import json

SEARCH_URL = 'https://app.rakuten.co.jp/services/api/IchibaItem/Ranking/20170628'

# maybe we can use genre search for recommendation
# python api/ichiba/ranking/src/ranking.py > api/ichiba/ranking/outputs/grocery.json

def get_api_data(params):
    api = requests.get(SEARCH_URL, params=params).text
    return json.loads(api)

GENRE_LIST = 0
GROCERY = 100227
COOKWARE = 558944

params = {
    "applicationId": "1003118371091832102",
    "format": "json",
    'genreId': GROCERY,
    'hits': 10,
}
items = get_api_data(params)
print(json.dumps(items, indent=2, ensure_ascii=False))