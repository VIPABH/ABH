import os
import asyncio
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from buttonbot.client import BUTTON_BOT
from react.client import REACTBOT
import buttonbot.run
import react.run
async def main():
    print("⏳ جاري تشغيل البوتين...")
    await BUTTON_BOT.start(bot_token=os.getenv("BUTTON_BOT"))
    print("✅ BUTTON_BOT is running!")
    await REACTBOT.start(bot_token=os.getenv("REACTBOT"))
    print("✅ REACTBOT is running!")
    await asyncio.gather(
        BUTTON_BOT.run_until_disconnected(),
        REACTBOT.run_until_disconnected()
    )
if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print("\n🛑 تم إيقاف تشغيل البوتين.")
