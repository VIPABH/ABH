import random
from telethon import events
import random, re

from JoKeRUB.utils import admin_cmd

import asyncio
from JoKeRUB import l313l

from ..core.managers import edit_or_reply

plugin_category = "extra"

@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( Shoes )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("حذاء")
    else:
        pass
