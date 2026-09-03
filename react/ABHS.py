import os
import asyncio
from telethon import TelegramClient
api_id = int(os.getenv("API_ID", 0))
api_hash = os.getenv("API_HASH")
bot_token = os.getenv("bot_token")
bot = TelegramClient("botcode", api_id, api_hash)
wfffp = 1910015590
mainABH = TelegramClient("wfffp", api_id, api_hash)
clients = {
    'wfffp': mainABH
}
MAX = 15
async def start_client(session_name, api_id_val, api_hash_val):
    try:
        client = TelegramClient(session_name, int(api_id_val), api_hash_val)
        await client.start()
        print(f"✅ {session_name} is working!")
        return session_name, client
    except Exception as e:
        print(f"❌ Error starting {session_name}: {e}")
        return session_name, None
async def main():
    await bot.start(bot_token=bot_token)
    print("✅ Bot is working!")
    await mainABH.start()
    print("✅ mainABH (wfffp) is working!")
    tasks = []
    for i in range(1, MAX):
        session = f'code{i}'
        api_id_i = os.getenv(f"API_ID{i}")
        api_hash_i = os.getenv(f"API_HASH{i}")
        curr_api_id = api_id_i if api_id_i else api_id
        curr_api_hash = api_hash_i if api_hash_i else api_hash
        if curr_api_id and curr_api_hash:
            print(f"Starting {session}...")
            tasks.append(start_client(session, curr_api_id, curr_api_hash))
        else:
            print(f"⚠️ Skipping {session} due to missing API_ID/API_HASH.")
    results = await asyncio.gather(*tasks)
    for session_name, client_obj in results:
        if client_obj:
            clients[session_name] = client_obj
    await asyncio.gather(
        bot.run_until_disconnected(),
        mainABH.run_until_disconnected(),
        *[c.run_until_disconnected() for c in ABHS]
    )
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
if __name__ == "__main__":
    asyncio.run(main())
