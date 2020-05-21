import logging

from extensions.market_indexes import get_ibovespa, get_sandp, get_ifix, get_dolar_to_brl

logger = logger = logging.getLogger(__name__)


def daily_indexes(context):
    logger.debug("Executing Job `daily_indexes`")
    job = context.job

    ibov_time, ibov_price = get_ibovespa()
    sandp_time, sandp_price = get_sandp()
    ifix_time, ifix_price = get_ifix()
    dolar_time, dolar_price = get_dolar_to_brl()

    message = """
IBOVESPA: {ibov_price} - {ibov_time}
S&P 500: {sandp_price} - {sandp_time}
IFIX: {ifix_price} - {ifix_time}
Dólar: {dolar_price} - {dolar_time}
    """.format(ibov_price=ibov_price, ibov_time=ibov_time,
               sandp_price=sandp_price, sandp_time=sandp_time,
               ifix_price=ifix_price, ifix_time=ifix_time,
               dolar_price=dolar_price, dolar_time=dolar_time)

    context.bot.send_message(chat_id=job.context, text=message)
