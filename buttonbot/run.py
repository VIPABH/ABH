import os
import sys
import asyncio
from client import *
from button_bot import *
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
async def main():
    print("⏳ جاري تشغيل بوت الأزرار...")
    button_token = os.getenv("BUTTON_BOT")
    if not button_token:
        print("❌ خطأ: لم يتم العثور على توكن BUTTON_BOT في المتغيرات البيئية (os.getenv)!")
        return
    await BUTTON_BOT.start(bot_token=button_token)
    print("✅ BUTTON_BOT يعمل الآن بنجاح وبشكل منفصل!")
    try:
        await BUTTON_BOT.run_until_disconnected()
    except (KeyboardInterrupt, SystemExit):
        pass
    finally:
        print("\n🛑 جاري إغلاق بوت الأزرار بنظافة...")
        if BUTTON_BOT.is_connected():
            await BUTTON_BOT.disconnect()
        print("✅ تم إغلاق البوت بسلام.")
if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print("\n🛑 تم إيقاف التشغيل.")
