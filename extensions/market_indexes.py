import os
from datetime import datetime

import requests

YAHOO_BASE_URL = os.environ.get('YAHOO_BASE_URL')
BCB_BASE_URL = os.environ.get('BCB_BASE_URL')


def get_yahoo_finance(symbol):
    """
    Retrieve last price data of the given symbol from
    Yahoo Finance API
    """

    url = "{}?symbols={}&range=1d&interval=1d&indicators=close".format(YAHOO_BASE_URL, symbol)

    response = requests.get(url)

    if response.status_code != 200:
        raise Exception("Error retrieving ibovespa data. Code: {}".format(response.status_code))

    data = response.json()['spark']['result'][0]['response'][0]

    timestamp = datetime.fromtimestamp(data['meta']['regularMarketTime'])
    market_price = data['meta']['regularMarketPrice']

    return timestamp.strftime("%d/%m/%Y - %H:%M"), market_price


def get_dolar_to_brl():
    """
    Retrieve last dolar to brl quotation from Central Bank of Brazil API
    """

    dolar_code = 1
    url = "{}/bcdata.sgs.{}/dados/ultimos/1?formato=json".format(BCB_BASE_URL,
                                                                 dolar_code)

    response = requests.get(url)

    if response.status_code != 200:
        raise Exception("Error retrieving Dolar data. Code: {}".format(response.status_code))

    data = response.json()[0]

    return data['data'], data['valor']


def get_ibovespa():
    """
    Retrive IBOVESPA price from Yahoo Finance API
    """

    ibov_symbol = "^BVSP"
    return get_yahoo_finance(ibov_symbol)


def get_sandp():
    """
    Retrive S&P 500 price from Yahoo Finance API
    """

    sandp_symbol = "^GSPC"
    return get_yahoo_finance(sandp_symbol)


def get_ifix():
    """
    Retrive IFIX price from Yahoo Finance API
    """
    ifix_symbol = "IFIX.SA"
    return get_yahoo_finance(ifix_symbol)
