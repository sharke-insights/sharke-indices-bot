import logging

from telegram.ext import Updater, CommandHandler
from .handlers import start, now, setup_daily_jobs
from .database import Database
from .envs import FILE_IDS_PATH, WEBHOOK_TOKEN

logger = logger = logging.getLogger(__name__)


def setup_log():
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


def start_polling(updater):
    updater.start_polling()
    updater.idle()


def start_webhook(updater, host='0.0.0.0', port=80, webhook_url=None):
    if webhook_url is None:
        raise('Webhook URL can not be None')

    updater.start_webhook(listen=host, port=port, url_path=WEBHOOK_TOKEN)
    updater.bot.set_webhook(webhook_url + WEBHOOK_TOKEN)
    updater.idle()


def run(token, execution_type='polling', host='localhost', port=80,
        webhook_url=None):
    setup_log()

    db = Database(FILE_IDS_PATH)
    chat_ids = db.data().get("chat_ids", [])

    updater = Updater(token, use_context=True)

    setup_daily_jobs(updater, chat_ids)

    updater.dispatcher.add_handler(CommandHandler('start', start,
                                   pass_args=True,
                                   pass_job_queue=True,
                                   pass_chat_data=True))

    updater.dispatcher.add_handler(CommandHandler('now', now,
                                   pass_args=True,
                                   pass_chat_data=True))
    if execution_type == 'webhook':
        start_webhook(updater, host, port, webhook_url)
    elif execution_type == 'polling':
        start_polling(updater)
