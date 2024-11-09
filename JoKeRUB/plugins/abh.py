from telethon import events
import asyncio

@l313l.on(admin_cmd(pattern="ع(?:\s|$)([\s\S]*)"))
async def permalink(mention):
    await edit_or_reply(mention, f"عليكم السلام , اهلا")
