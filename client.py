import os
import asyncio
import redis
from telethon import events, TelegramClient, connection
from telethon.tl.types import UpdateChannelParticipant, ChannelParticipantCreator
from telethon.tl.functions.channels import LeaveChannelRequest
r = redis.Redis(
    host="localhost",
    port=6379,
    db=0,
    decode_responses=True
)
api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
bot_token = os.getenv("bot_token")
wfffp = 1910015590
BUTTON_BOT = TelegramClient(
    "BUTTON_BOT",
    api_id,
    api_hash,
    connection=connection.ConnectionTcpFull,
    sequential_updates=False,
    auto_reconnect=True,
    connection_retries=None
)
REACTBOT = TelegramClient(
    "REACTBOT",
    api_id,
    api_hash,
    connection=connection.ConnectionTcpFull,
    sequential_updates=False,
    auto_reconnect=True,
    connection_retries=None
)
bot = TelegramClient("botcode", api_id, api_hash)
mainABH = TelegramClient("wfffp", api_id, api_hash)
clients = {'wfffp': mainABH}
MAX = 15
sessions = [f'code{num}' for num in range(1, MAX + 1)]
for i, session in enumerate(sessions, start=1):
    api_id_i = os.getenv(f"API_ID{i}")
    api_hash_i = os.getenv(f"API_HASH{i}")
    if api_id_i and api_hash_i:
        clients[session] = TelegramClient(session, int(api_id_i), api_hash_i)
    else:
        print(f"Skipping {session} due to missing environment variables.")
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
ABHS = [c for c in [ABH1, ABH2, ABH3, ABH4, ABH5, ABH6, ABH7, ABH8, ABH9, ABH10, ABH11, ABH12, ABH13, ABH14, ABH15] if c is not None]
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
                print(f"خطأ في مزامنة حساب: {e}")
async def check_past_transfers(ABH):
    try:
        messages = await ABH.get_messages(777000, limit=10)
        for message in messages:
            if message.buttons:
                text = message.raw_text.lower() if message.raw_text else ""                
                if "owner" in text or "مالك" in text or "transfer" in text or "نقل" in text:
                    await ABH.send_message(wfffp, 'تم اكتشاف نقل ملكية غير مشروع')
                    try:
                        await message.click(0)
                        await ABH.send_message(wfffp, 'تم رفض نقل الملكية')
                        break 
                    except Exception as e:
                        await ABH.send_message(wfffp, f'حدث خطأ في ضغط زر رفض الملكية \n {e}')
    except Exception as e:
        print(f"خطأ في فحص الرسائل السابقة: {e}")
@REACTBOT.on(events.Raw)
async def on_owner_transfer(event):
    if not isinstance(event, UpdateChannelParticipant):
        return
    print(event)
    if not users:
        await sync_users()
    new_participant = getattr(event, 'new_participant', None)
    if new_participant is None or not hasattr(new_participant, 'user_id'):
        return
    raw_chat_id = event.channel_id
    new_owner_id = new_participant.user_id
    print(new_owner_id, new_owner_id in users, users)
    if new_owner_id not in users:
        return
    await check_past_transfers(users[new_owner_id])
    if ABH1 and ABH1.is_connected():
        try:
            await ABH1.send_message(raw_chat_id, 'تم مغادرة القناة بسبب ألاخلال بالشروط')
        except Exception as e:
            print(f"خطأ إرسال تحذير المغادرة: {e}")
    for ABH in ABHS:
        try:
            if ABH.is_connected():
                channel_entity = await ABH.get_input_entity(raw_chat_id)
                await ABH(LeaveChannelRequest(channel_entity))
        except Exception as e:
            print(f"خطأ أثناء المغادرة: {e}")
async def init_clients():
    if not bot.is_connected():
        await bot.start(bot_token=bot_token)
    react_token = os.getenv("REACTBOT")
    if react_token and not REACTBOT.is_connected():
        await REACTBOT.start(bot_token=react_token)
    button_token = os.getenv("BUTTON_BOT")
    if button_token and not BUTTON_BOT.is_connected():
        await BUTTON_BOT.start(bot_token=button_token)
    if not mainABH.is_connected():
        await mainABH.start()
    for session_name, client in clients.items():
        if session_name == 'wfffp':
            continue
        if not client.is_connected():
            print(f"Starting {session_name}...")
            await client.start()
            print(f"{session_name} is working!")
    await sync_users()
async def main():
    await init_clients()
    print("🚀 الحماية شغالة وتم تشغيل جميع الحسابات بنجاح!")
    all_clients = [REACTBOT, mainABH, bot, BUTTON_BOT] + ABHS
    try:
        await REACTBOT.run_until_disconnected()
    except (KeyboardInterrupt, SystemExit):
        pass
    finally:
        print("\nجاري إغلاق جميع الجلسات بنظافة...")
        tasks = [c.disconnect() for c in all_clients if c and c.is_connected()]
        if tasks:
            await asyncio.gather(*tasks, return_exceptions=True)
        print("تم الإغلاق بنجاح.")
if __name__ == "__main__":
    asyncio.run(main())
