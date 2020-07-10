import os

TOKEN = os.environ.get('TELEGRAM_KEY')
FILE_IDS_PATH = os.environ.get("FILE_IDS_PATH", "ids.json")
HOUR = int(os.environ.get('HOUR_JOB', 0))
MINUTE = int(os.environ.get('MINUTE_JOB', 0))
TIMEZONE = "America/Sao_Paulo"
WEBHOOK_URL = os.environ.get('WEBHOOK_URL')
HOST = os.environ.get('HOST', '0.0.0.0')
PORT = int(os.environ.get('PORT', 80))
WEBHOOK_TOKEN = os.environ.get('WEBHOOK_TOKEN')
EXECUTION_TYPE = os.environ.get('EXECUTION_TYPE', 'polling')
