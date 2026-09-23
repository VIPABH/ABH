import os
import asyncio
from telethon import TelegramClient
from client import REACTBOT, r
api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
bot_token = os.getenv("bot_token")
wfffp = 1910015590
bot = TelegramClient("botcode", api_id, api_hash)
mainABH = TelegramClient("wfffp", api_id, api_hash)
clients = {'wfffp': mainABH}
MAX = 2
sessions = [f'code{num}' for num in range(1, MAX + 1)]
for i, session in enumerate(sessions, start=1):
    api_id_i = os.getenv(f"API_ID{i}")
    api_hash_i = os.getenv(f"API_HASH{i}")
    if api_id_i and api_hash_i:
        clients[session] = TelegramClient(session, int(api_id_i), api_hash_i)
ABH1 = clients.get("code1")
ABH2 = clients.get("code2")
ABHS = [c for session_name, c in clients.items() if session_name != 'wfffp' and c is not None]
users = {}
async def sync_users():
    users.clear()
    for ABH in ABHS:
        try:
            if ABH.is_connected() and await ABH.is_user_authorized():
                me = await ABH.get_me()
                if me:
                    users[me.id] = ABH
            else:
                print(f"⚠️ الحساب {ABH.session.filename} غير متصل أو غير مصرح.")
        except Exception as e:
            print(f"❌ خطأ أثناء جلب بيانات الحساب {ABH.session.filename}: {e}")
async def init_clients():
    if not bot.is_connected():
        await bot.start(bot_token=bot_token)    
    react_token = os.getenv("REACTBOT")
    if react_token and not REACTBOT.is_connected():
        await REACTBOT.start(bot_token=react_token)
    if not mainABH.is_connected():
        await mainABH.start()
    valid_clients = []
    for session_name, client in clients.items():
        if session_name == 'wfffp':
            continue
        try:
            if not client.is_connected():
                print(f"⏳ جاري تشغيل الجلسة {session_name}...")
                await client.start()
                
            if await client.is_user_authorized():
                print(f"✅ تم تفعيل الجلسة {session_name} بنجاح.")
                valid_clients.append(client)
            else:
                print(f"❌ الجلسة {session_name}.session غير مسجلة دخول!")
        except Exception as e:
            print(f"❌ تعذر الاتصال بالجلسة {session_name}: {e}")
    global ABHS
    ABHS = valid_clients
    await sync_users()
