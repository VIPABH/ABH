import os
import sys
import asyncio
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from ABHS import init_clients, ABHS, REACTBOT
async def run_react():
    print("⏳ جاري تشغيل بوت التفاعلات والـ 15 عميل...")
    await init_clients()
    print(f"🚀 تم تشغيل بوت التفاعلات و ({len(ABHS)}) حساب بنجاح!")
