cat << 'EOF' > /root/ABH/buttonbot/run.py
import os
import sys
import asyncio

# 1. إضافة المسار الرئيسي (/root/ABH) أولاً قبل أي import آخر
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# 2. الاستيراد الآن سيتعرف على helpers.py و client.py بدون أي أخطاء
from client import BUTTON_BOT, r
from button_bot import *

async def main():
    print("⏳ جاري تشغيل بوت الأزرار...")
    
    button_token = os.getenv("BUTTON_BOT")
    if not button_token:
        print("❌ خطأ: لم يتم العثور على توكن BUTTON_BOT في المتغيرات البيئية!")
        return

    await BUTTON_BOT.start(bot_token=button_token)
    print("✅ BUTTON_BOT يعمل الآن بنجاح وبشكل منفصل!")

    try:
        await BUTTON_BOT.run_until_disconnected()
    except (KeyboardInterrupt, SystemExit):
        pass
    finally:
        print("\n🛑 جاري إغلاق بوت الأزرار...")
        if BUTTON_BOT.is_connected():
            await BUTTON_BOT.disconnect()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print("\n🛑 تم إيقاف التشغيل.")
EOF
