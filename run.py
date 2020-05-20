import os

from core.bot import run

TOKEN = os.environ.get('TELEGRAM_KEY')

if __name__ == '__main__':
    run(TOKEN)

