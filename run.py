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
from react import *
async def main():
    token_button = os.getenv("BUTTON_BOT")
    token_react = os.getenv("REACTBOT")
    if not token_button or not token_react:
        logging.error("❌ تعذر العثور على توكنات البوتات في متغيرات البيئة (Environment Variables)!")
        return
    print("⏳ جاري تشغيل البوتين...")
    await BUTTON_BOT.start(bot_token=token_button)
    print("✅ BUTTON_BOT is running!")
    await REACTBOT.start(bot_token=token_react)
    print("✅ REACTBOT is running!")
    await asyncio.gather(
        BUTTON_BOT.run_until_disconnected(),
        run_react()
        # REACTBOT.run_until_disconnected()
    )
if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print("\n🛑 تم إيقاف تشغيل البوتين.")
