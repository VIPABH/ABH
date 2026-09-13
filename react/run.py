import os
import sys
import asyncio
from ABHS import init_clients, REACTBOT, mainABH, bot, ABHS
import الحماية
async def main():
    # print("⏳ جاري تشغيل بوت التفاعلات والـ 15 عميل...")
    # await init_clients()
    # print("🚀 جميع الحسابات وبوت التفاعلات شغالين بنجاح!")
    all_clients = [c for c in [REACTBOT, mainABH, bot] + ABHS if c and c.is_connected()]
    try:
        if REACTBOT.is_connected():
            await REACTBOT.run_until_disconnected()
        else:
            await asyncio.Event().wait()
    except (KeyboardInterrupt, SystemExit):
        pass
    finally:
        print("\n🛑 جاري إغلاق الجلسات...")
        tasks = [c.disconnect() for c in all_clients if c.is_connected()]
        if tasks:
            await asyncio.gather(*tasks, return_exceptions=True)
        print("✅ تم الإغلاق بسلام.")
if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print("\n🛑 تم الإيقاف.")
