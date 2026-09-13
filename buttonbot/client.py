import os
import redis
from telethon import TelegramClient, connection
api_id_env = os.getenv("API_ID")
api_id = int(api_id_env) if api_id_env else None
api_hash = os.getenv("API_HASH")
r = redis.Redis(
    host="localhost",
    port=6379,
    db=0,
    decode_responses=True
)
BUTTON_BOT = TelegramClient(
    "BUTTON_BOT",
    api_id,
    api_hash,
    connection=connection.ConnectionTcpFull,
    sequential_updates=False,
    auto_reconnect=True,
    connection_retries=None
)
