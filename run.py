import os
import asyncio
from buttonbot.button_bot import *
from react import *
from client import *
async def main():
    print("Starting bots...")
    await asyncio.gather(
        BUTTON_BOT.start(bot_token=os.getenv("BUTTON_BOT")),
        REACTBOT.start(bot_token=os.getenv("REACTBOT"))
    )
    print("BUTTON_BOT and REACTBOT are now running!")
    await asyncio.gather(
        BUTTON_BOT.run_until_disconnected(),
        REACTBOT.run_until_disconnected()
    )
if __name__ == "__main__":
    asyncio.run(main())
