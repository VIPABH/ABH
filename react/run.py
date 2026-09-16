import os
import sys
import asyncio
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from ABHS import *
import الحماية
async def run_react():
    print("⏳ جاري تشغيل بوت التفاعلات والـ 15 عميل...")
    await init_clients()
    await REACTBOT.start()
    print("🚀 جميع الحسابات وبوت التفاعلات شغالين بنجاح!")
    try:
        await REACTBOT.run_until_disconnected()
        await asyncio.Event().wait()
    except (KeyboardInterrupt, SystemExit):
        pass
    finally:
        print("\n🛑 جاري إغلاق الجلسات بأمان...")        
        raw_clients = [c for c in [REACTBOT, mainABH, bot] + (ABHS if isinstance(ABHS, list) else []) if c]        
        for client in raw_clients:
            try:
                if client and client.is_connected():
                    await client.disconnect()
            except Exception as e:
                print(f"تنبيه أثناء فصل جلسة: {e}")
