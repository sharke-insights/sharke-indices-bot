import os
import logging
from datetime import time

import pytz

from .jobs import daily_indexes

HOUR = int(os.environ.get('HOUR_JOB', 0))
MINUTE = int(os.environ.get('MINUTE_JOB', 0))
TIMEZONE = "America/Sao_Paulo"

logger = logger = logging.getLogger(__name__)


def create_daily_job(context, callback, execution_time, days, job_context):
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

    update.message.reply_text(message_start)

    timezone = pytz.timezone(TIMEZONE)
    e_time = time(hour=HOUR, minute=MINUTE, tzinfo=timezone)

    context.chat_data['job'] = create_daily_job(context, daily_indexes,
                                                e_time, tuple(range(1, 5)),
                                                update.message.chat_id)

    update.message.reply_text("Todas as configurações foram feitas com sucesso, te manterei atualizado de Segunda a Sexta!")



