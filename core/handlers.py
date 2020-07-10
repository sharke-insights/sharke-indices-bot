import logging
from datetime import time

import pytz
from telegram.ext import Updater

from .jobs import daily_indexes
from .database import Database
from .envs import TIMEZONE, HOUR, MINUTE, FILE_IDS_PATH
from extensions.market_indexes import market_indexes_message

logger = logger = logging.getLogger(__name__)


def setup_daily_jobs(context, chat_ids):
    logger.info("Setting up daily jobs for registred chats, total: %s" % len(chat_ids))

    timezone = pytz.timezone(TIMEZONE)
    e_time = time(hour=HOUR, minute=MINUTE, tzinfo=timezone)

    for chat_id in chat_ids:
        create_daily_job(context, daily_indexes, e_time,
                         tuple(range(1, 5)), chat_id)

    logger.info("Jobs added with success!")


def create_daily_job(context, callback, execution_time, days, job_context):

    # When setting up bot jobs on boot context is an instance of Updater,
    # so there is no .chat_data attr
    if not isinstance(context, Updater):
        if 'job' in context.chat_data:
            old_job = context.chat_data['job']
            old_job.schedule_removal()

    new_job = context.job_queue.run_daily(callback, execution_time,
                                          days=days, context=job_context)

    logger.debug("Job is enabled: %s" % new_job.enabled)
    logger.debug("Job next time: %s" % new_job.next_t)
    logger.debug("Job tz info: %s" % new_job.tzinfo)

    return new_job


def start(update, context):
    message_start = "Olá %s, eu faço parte a equipe Sharke Insights e vou te manter atualizado com os principais índices do mercado financeiro" % update.message.from_user.first_name
    db = Database(FILE_IDS_PATH)

    update.message.reply_text(message_start)

    timezone = pytz.timezone(TIMEZONE)
    e_time = time(hour=HOUR, minute=MINUTE, tzinfo=timezone)
    chat_id = update.message.chat_id

    context.chat_data['job'] = create_daily_job(context, daily_indexes,
                                                e_time, tuple(range(1, 5)),
                                                chat_id)

    db.save(chat_id)

    update.message.reply_text("Todas as configurações foram feitas com sucesso, te manterei atualizado de Segunda a Sexta!")


def now(update, context):
    message = "Buscando cotações..."
    update.message.reply_text(message)
    update.message.reply_markdown(market_indexes_message())


def add_to_channel(update, context):
    db = Database(FILE_IDS_PATH)
    try:
        channel_id = context.args[0]
    except IndexError:
        update.message.reply_text("É necessário passar o @ do canal!")

    db.save(channel_id)
    user = update.message.from_user.username

    message = "Olá, eu faço parte a equipe Sharke Insights e vou manter esse grupo atualizado com os principais índices do mercado financeiro. Fui adicionado pelo usuário %s." % user

    context.bot.send_message(chat_id=channel_id, text=message)
