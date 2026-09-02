from buttonbot.button_bot import *
from react import *
from client  import *
BUTTON_BOT.start(bot_token=os.getenv("BUTTON_BOT"))
print("BUTTON_BOT is running!")
REACTBOT.start(bot_token=os.getenv("REACTBOT"))
print("REACTBOT is running!")
REACTBOT.run_until_disconnected()
