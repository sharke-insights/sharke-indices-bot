import logging

from extensions.market_indexes import get_ibovespa, get_sandp, get_ifix, get_dolar_to_brl

logger = logger = logging.getLogger(__name__)


def daily_indexes(context):
    logger.debug("Executing Job `daily_indexes`")
    job = context.job

    ibov_time, ibov_price, ibov_profit = get_ibovespa()
    sandp_time, sandp_price, sandp_profit = get_sandp()
    ifix_time, ifix_price, ifix_profit = get_ifix()
    dolar_time, dolar_price, dolar_profit = get_dolar_to_brl()

    message = """
IBOVESPA: {ibov_price} - {ibov_time} * {ibov_profit}
S&P 500: {sandp_price} - {sandp_time} * {sandp_profit}
IFIX: {ifix_price} - {ifix_time} * {ifix_profit}
Dólar: {dolar_price} - {dolar_time} * {dolar_profit}
    """.format(ibov_price=ibov_price, ibov_time=ibov_time, ibov_profit=ibov_profit,
               sandp_price=sandp_price, sandp_time=sandp_time, sandp_profit=sandp_profit,
               ifix_price=ifix_price, ifix_time=ifix_time, ifix_profit=ifix_profit,
               dolar_price=dolar_price, dolar_time=dolar_time, dolar_profit=dolar_profit)

    context.bot.send_message(chat_id=job.context, text=message)
