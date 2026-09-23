import os
import asyncio
import sys
import logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.ERROR
)
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from client import BUTTON_BOT, REACTBOT
import buttonbot
import react
from react.run import run_react
from react.ABHS import *
async def main():
    token_button = os.getenv("BUTTON_BOT")
    token_react = os.getenv("REACTBOT")
    if not token_button or not token_react:
        logging.error("❌ تعذر العثور على توكنات البوتات في متغيرات البيئة (Environment Variables)!")
        return
    print("⏳ جاري تشغيل البوتين والحسابات...")
    await BUTTON_BOT.start(bot_token=token_button)
    print("✅ BUTTON_BOT is running!")
    await run_react()
    print("⚡ جميع البوتات والحسابات تعمل الآن بنجاح ضمن Event Loop واحدة.")
    try:
        await asyncio.Event().wait()
    except (KeyboardInterrupt, SystemExit):
        pass
    finally:
        print("\n🛑 جاري إغلاق الجلسات بأمان...")
        all_clients = [BUTTON_BOT, REACTBOT, mainABH, bot]
        if isinstance(ABHS, list):
            all_clients.extend(ABHS)
        for c in set(all_clients):
            if c:
                try:
                    if c.is_connected():
                        await c.disconnect()
                except Exception as e:
                    print(f"تنبيه أثناء فصل جلسة: {e}")
if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print("\n🛑 تم إيقاف تشغيل المشاري.")
