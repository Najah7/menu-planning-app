import requests
import json

# This is from the sample app
# python api/ichiba/item/src/item_search.py > api/ichiba/item/outputs/items.json

SEARCH_URL = 'https://app.rakuten.co.jp/services/api/Recipe/CategoryList/20170426'

def get_api_data(params):
    api = requests.get(SEARCH_URL, params=params).text
    return json.loads(api)

params = {
    "applicationId": "1003118371091832102",
    "format": "json",
    'categoryType':'large',
}

result = get_api_data(params)
print(json.dumps(result, indent=2, ensure_ascii=False))