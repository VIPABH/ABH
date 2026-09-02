from client import *
import asyncio, os
import buttonbot
import react
async def main():
    print("Starting both bots...")
    await asyncio.gather(
        BUTTON_BOT.start(bot_token=os.getenv("BUTTON_BOT")),
        REACTBOT.start(bot_token=os.getenv("REACTBOT"))
    )
    print("Both bots are online and handlers registered!")
    await asyncio.gather(
        BUTTON_BOT.run_until_disconnected(),
        REACTBOT.run_until_disconnected()
    )
if __name__ == "__main__":
    asyncio.run(main())
