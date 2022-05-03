import json

import requests
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

# Create your views here.

class DataView(View):
    def get(self, request, *args, **kwargs):
        symbol = request.GET["symbol"]
        outputsize = request.GET["outputsize"]
        url = 'https://www.alphavantage.co/query'
        params = {"function": "TIME_SERIES_DAILY", "apikey":"MRYEV0BP5ROJORBJ", "symbol": symbol, "outputsize": outputsize}
        r = requests.get(url, params=params)
        response = HttpResponse(r.text, r.headers)
        response.status_code = r.status_code
        return response

