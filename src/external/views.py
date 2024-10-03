from django.shortcuts import render
from django.views.generic import RedirectView

from lib.adaptors.rakuten_api.ichiba.clients import RakutenIchibaItemClient


class RakutenIchibaRedirectView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        grocery = self.request.GET.get("grocery_name")
        if not grocery:
            return "No grocery found in query parameter"
        client = RakutenIchibaItemClient()
        response = client.fetch_grocery(grocery)
        return response.Item.itemUrl
