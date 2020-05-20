import logging

from telegram.ext import Updater, CommandHandler, Filters
from .handlers import start


def setup_log():
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


def start_polling(updater):
    updater.start_polling()
    updater.idle()


def start_webhook(updater, host='0.0.0.0', port=80, webhook_url=None):
    if webhook_url is None:
        raise('Webhook URL can not be None')

    updater.start_webhook(listen=host, port=port)
    updater.bot.set_webhook(webhook_url)
    updater.idle()


def run(token, execution_type='polling', host='localhost', port=80,
        webhook_url='/'):
    setup_log()

    updater = Updater(token, use_context=True)
    updater.dispatcher.add_handler(CommandHandler('start', start,
                                   pass_args=True,
                                   pass_job_queue=True,
                                   pass_chat_data=True))

    if execution_type == 'webhook':
        start_webhook(updater, host, port, webhook_url)
    elif execution_type == 'polling':
        start_polling(updater)
