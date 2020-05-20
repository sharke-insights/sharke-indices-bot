import logging
from datetime import datetime, time
import pytz

logger = logger = logging.getLogger(__name__)


def job_response(context):
    logger.warning("Executing Job")
    job = context.job
    context.bot.send_message(chat_id=job.context, text="Teste")


def start(update, context):
    logger.debug("Entrando no start")
    message_start = "Olá %s, eu faço parte a equipe Sharke Insights e vou te manter atualizado com os principais índices do mercado financeiro" % update.message.from_user.first_name

    update.message.reply_text(message_start)

    timezone = pytz.timezone("America/Sao_Paulo")
    date = time(hour=16, minute=5, second=0, tzinfo=timezone)

    if 'job' in context.chat_data:
        logger.debug("Deletando old job")
        old_job = context.chat_data['job']
        old_job.schedule_removal()

    new_job = context.job_queue.run_daily(job_response, date, days=(1, 2, 3, 4, 5), context=update.message.chat_id)

    logger.debug("Job is enabled: %s" % new_job.enabled)
    logger.debug("Job next time: %s" % new_job.next_t)
    logger.debug("Job tz info: %s" % new_job.tzinfo)

    context.chat_data['job'] = new_job

    update.message.reply_text("Todas as configurações foram feitas com sucesso, te manterei atualizado de Segunda a Sexta!")



