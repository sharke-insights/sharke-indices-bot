import os

from core.bot import run
from core.envs import TOKEN, WEBHOOK_URL, HOST, PORT, EXECUTION_TYPE

if __name__ == '__main__':
    run(TOKEN, EXECUTION_TYPE, HOST, PORT, WEBHOOK_URL)

