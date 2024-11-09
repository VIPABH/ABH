from telethon import events
import asyncio
from telethon.tl.types import Message
from module_name import admin_cmd, edit_or_reply

@l313l.on(admin_cmd(pattern="ع(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    await edit_or_reply(mention, f"عليكم السلام , اهلا")
