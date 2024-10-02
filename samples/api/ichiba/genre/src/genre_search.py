import requests
import json

SEARCH_URL = 'https://app.rakuten.co.jp/services/api/IchibaItem/Search/20220601?format=json&applicationId=1003118371091832102'

SEARCH_URL = "https://app.rakuten.co.jp/services/api/IchibaGenre/Search/20120723?format=json&applicationId=1003118371091832102"

# maybe we can use genre search for recommendation

def get_api_data(params):
    api = requests.get(SEARCH_URL, params=params).text
    return json.loads(api)

GENRE_LIST = 0
GROCERY = 100227
COOKWARE = 558944

params = {
    'genreId': COOKWARE,
}
items = get_api_data(params)
print({json.dumps(items, indent=2, ensure_ascii=False)})