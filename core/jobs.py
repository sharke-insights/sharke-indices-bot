import logging

logger = logger = logging.getLogger(__name__)


def daily_indexes(context):
    logger.debug("Executing Job `daily_indexes`")
    job = context.job
    context.bot.send_message(chat_id=job.context, text="Teste")
