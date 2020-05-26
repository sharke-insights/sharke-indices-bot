import os
from datetime import datetime

import requests

YAHOO_BASE_URL = os.environ.get('YAHOO_BASE_URL')
BCB_BASE_URL = os.environ.get('BCB_BASE_URL')


def profitability(curr_price, prev_price):
    return ((curr_price - prev_price) / prev_price) * 100


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
    profit = profitability(data['meta']['regularMarketPrice'], data['meta']['chartPreviousClose'])

    return timestamp.strftime("%d/%m/%Y - %H:%M"), market_price, round(profit, 2)


def get_dolar_to_brl():
    """
    Retrieve last dolar to brl quotation from Central Bank of Brazil API
    """
    usd_brl_symbol = "BRL=X"
    return get_yahoo_finance(usd_brl_symbol)


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


def market_indexes_message():
    ibov_time, ibov_price, ibov_profit = get_ibovespa()
    sandp_time, sandp_price, sandp_profit = get_sandp()
    ifix_time, ifix_price, ifix_profit = get_ifix()
    dolar_time, dolar_price, dolar_profit = get_dolar_to_brl()

    message = """
IBOVESPA 💲 `{ibov_price}`  📈 `{ibov_profit}`  🕠 `{ibov_time}`

S&P 500 💲 `{sandp_price}`  📈 `{sandp_profit}`  🕠 `{sandp_time}`

IFIX 💲 `{ifix_price}`  📈 `{ifix_profit}`  🕠 `{ifix_time}`

Dólar 💲 `{dolar_price}`  📈 `{dolar_profit}`  🕠 `{dolar_time}`
    """.format(ibov_price=ibov_price, ibov_time=ibov_time, ibov_profit=ibov_profit,
               sandp_price=sandp_price, sandp_time=sandp_time, sandp_profit=sandp_profit,
               ifix_price=ifix_price, ifix_time=ifix_time, ifix_profit=ifix_profit,
               dolar_price=dolar_price, dolar_time=dolar_time, dolar_profit=dolar_profit)

    return message


