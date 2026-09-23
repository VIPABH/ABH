import os
import sys
import asyncio
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from ABHS import *
async def run_react():
    print("⏳ جاري تشغيل بوت التفاعلات والـ 15 عميل...")
    await init_clients()    
    await REACTBOT.start()
    if isinstance(ABHS, list):
        tasks = [client.start() for client in ABHS if client and not client.is_connected()]
        if tasks:
            await asyncio.gather(*tasks)
    print("🚀 جميع الحسابات وبوت التفاعلات شغالين بنجاح!")
