import os

from core.bot import run
from core.envs import TOKEN, WEBHOOK_URL, HOST, PORT

if __name__ == '__main__':
    run(TOKEN, 'webhook', HOST, PORT, WEBHOOK_URL)

