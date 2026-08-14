from telethon import events, TelegramClient, connection
api_id = int(os.getenv("API_ID") or config['anymous'].get('api_id'))
api_hash = os.getenv("API_HASH") or config['anymous'].get('api_hash')
bot_token = os.getenv("BOT_TOKEN") or config['anymous'].get('bot_token')
BUTTON_BOT = TelegramClient(
    "BUTTON_BOT", 
    api_id, 
    api_hash,
    connection=connection.ConnectionTcpFull,
    sequential_updates=False,
    auto_reconnect=True,
    connection_retries=None
)
