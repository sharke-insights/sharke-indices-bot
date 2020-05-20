import logging

from extensions.market_indexes import get_ibovespa, get_sandp

logger = logger = logging.getLogger(__name__)


def daily_indexes(context):
    logger.debug("Executing Job `daily_indexes`")
    job = context.job

    ibov_time, ibov_price = get_ibovespa()
    sandp_time, sandp_price = get_sandp()

    message = """
IBOVESPA: {ibov_price} - {ibov_time}
S&P 500: {sandp_price} - {sandp_time}
    """.format(ibov_price=ibov_price, ibov_time=ibov_time,
               sandp_price=sandp_price, sandp_time=sandp_time)

    context.bot.send_message(chat_id=job.context, text=message)
