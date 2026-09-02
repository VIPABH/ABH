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
    global ABHS
    ABHS = [clients.get(f"code{i}") for i in range(1, MAX) if clients.get(f"code{i}")]
    print(f"\n🚀 Total active userbots running: {len(ABHS)}")
    await asyncio.gather(
        bot.run_until_disconnected(),
        mainABH.run_until_disconnected(),
        *[c.run_until_disconnected() for c in ABHS]
    )
if __name__ == "__main__":
    asyncio.run(main())
