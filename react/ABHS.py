import os
from telethon import TelegramClient, events
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
print(BASE_DIR
api_id_env = os.getenv("API_ID")
api_id = int(api_id_env) if api_id_env else None
api_hash = os.getenv("API_HASH")
bot_token = os.getenv("bot_token")
bot_session = os.path.join(BASE_DIR, "botcode")
bot = TelegramClient(bot_session, api_id, api_hash).start(bot_token=bot_token)
wfffp = 1910015590
print("setting wfffp")
wfffp_session = os.path.join(BASE_DIR, "wfffp")
mainABH = TelegramClient(wfffp_session, api_id, api_hash).start()
print("wfffp is on!")
clients = {}
clients['wfffp'] = mainABH
MAX = 16
sessions = [f'code{num}' for num in range(1, MAX)]
for i, session_name in enumerate(sessions, start=1):
    api_id_i = os.getenv(f"API_ID{i}") or os.getenv("API_ID")
    api_hash_i = os.getenv(f"API_HASH{i}") or os.getenv("API_HASH")
    if api_id_i and api_hash_i:
        print(f"Starting {session_name}...")
        session_path = os.path.join(BASE_DIR, session_name)
        clients[session_name] = TelegramClient(session_path, int(api_id_i), api_hash_i).start()
        print(f"{session_name} is working!")
    else:
        print(f"Skipping {session_name} due to missing environment variables.")
ABH1 = clients.get("code1")
ABH2 = clients.get("code2")
ABH3 = clients.get("code3")
ABH4 = clients.get("code4")
ABH5 = clients.get("code5")
ABH6 = clients.get("code6")
ABH7 = clients.get("code7")
ABH8 = clients.get("code8")
ABH9 = clients.get("code9")
ABH10 = clients.get("code10")
ABH11 = clients.get("code11")
ABH12 = clients.get("code12")
ABH13 = clients.get("code13")
ABH14 = clients.get("code14")
ABH15 = clients.get("code15")
ABHS = [ABH1, ABH2, ABH3, ABH4, ABH5, ABH6, ABH7, ABH8, ABH9, ABH10, ABH11, ABH12, ABH13, ABH14, ABH15]
users = {}
async def sync_users():
    users.clear()
    for ABH in ABHS:
        if ABH and ABH.is_connected():
            try:
                me = await ABH.get_me()
                if me:
                    users[me.id] = ABH
            except Exception as e:
                print(f"خطأ بمزامنة حساب: {e}")
