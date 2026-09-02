import os
import asyncio
from buttonbot.button_bot import *
from react import *
from client import *
async def main():
    await BUTTON_BOT.start(bot_token=os.getenv("BUTTON_BOT"))
    print("BUTTON_BOT is running!")
    await REACTBOT.start(bot_token=os.getenv("REACTBOT"))
    print("REACTBOT is running!")
    await asyncio.gather(
        BUTTON_BOT.run_until_disconnected(),
        REACTBOT.run_until_disconnected()
    )
if __name__ == "__main__":
    asyncio.run(main())
