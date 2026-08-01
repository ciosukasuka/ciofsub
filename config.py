import os

API_ID = int(os.environ.get("API_ID", 0))
API_HASH = os.environ.get("API_HASH", "")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

CHANNEL_ID = int(os.environ.get("CHANNEL_ID", 0))
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", 0))
ADMINS = [int(x) for x in os.environ.get("ADMINS", "").split()]

DB_URI = os.environ.get("DB_URI", "")
DB_NAME = os.environ.get("DB_NAME", "fsub")
