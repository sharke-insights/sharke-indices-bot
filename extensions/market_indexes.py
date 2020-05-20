import os
from datetime import datetime

import requests

YAHOO_BASE_URL = os.environ.get('YAHOO_BASE_URL')


def get_yahoo_finance(symbol):
    url = "{}?symbols={}&range=1d&interval=1d&indicators=close".format(YAHOO_BASE_URL, symbol)

    response = requests.get(url)

    if response.status_code != 200:
        raise Exception("Error retrieving ibovespa data code: {}".format(response.status_code))

    data = response.json()['spark']['result'][0]['response'][0]

    timestamp = datetime.fromtimestamp(data['meta']['regularMarketTime'])
    market_price = data['meta']['regularMarketPrice']

    return timestamp.strftime("%d/%m/%Y - %H:%M"), market_price


def get_ibovespa():
    ibov_symbol = "^BVSP"
    return get_yahoo_finance(ibov_symbol)


def get_sandp():
    sandp_symbol = "^GSPC"
    return get_yahoo_finance(sandp_symbol)
