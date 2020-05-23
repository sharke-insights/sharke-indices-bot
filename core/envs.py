import os

FILE_IDS_PATH = os.environ.get("FILE_IDS_PATH", "ids.json")
HOUR = int(os.environ.get('HOUR_JOB', 0))
MINUTE = int(os.environ.get('MINUTE_JOB', 0))
TIMEZONE = "America/Sao_Paulo"
