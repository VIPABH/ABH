import random
from telethon import events
import random, re

from JoKeRUB.utils import admin_cmd

import asyncio
from JoKeRUB import l313l

from ..core.managers import edit_or_reply

plugin_category = "extra"

@l313l.ar_cmd(incoming=True, func=lambda e: "rich" in e.text.lower(), edited=False)
async def reply_salam(event):
    # الرد بـ "عليكم السلام"
    await event.reply("غني")

@l313l.ar_cmd(incoming=True, func=lambda e: "calm" in e.text.lower(), edited=False)
async def reply_salam(event):
    # الرد بـ "عليكم السلام"
    await event.reply("هدوء")

@l313l.ar_cmd(incoming=True, func=lambda e: "joke" in e.text.lower(), edited=False)
async def reply_salam(event):
    # الرد بـ "عليكم السلام"
    await event.reply("نكتة")

@l313l.ar_cmd(incoming=True, func=lambda e: "law" in e.text.lower(), edited=False)
async def reply_salam(event):
    # الرد بـ "عليكم السلام"
    await event.reply("قانون")

@l313l.ar_cmd(incoming=True, func=lambda e: "young" in e.text.lower(), edited=False)
async def reply_salam(event):
    # الرد بـ "عليكم السلام"
    await event.reply("صغير")

@l313l.ar_cmd(incoming=True, func=lambda e: "hotel" in e.text.lower(), edited=False)
async def reply_salam(event):
    # الرد بـ "عليكم السلام"
    await event.reply("فندق")

@l313l.ar_cmd(incoming=True, func=lambda e: "coat" in e.text.lower(), edited=False)
async def reply_salam(event):
    # الرد بـ "عليكم السلام"
    await event.reply("معطف")

@l313l.ar_cmd(incoming=True, func=lambda e: "how" in e.text.lower(), edited=False)
async def reply_salam(event):
    # الرد بـ "عليكم السلام"
    await event.reply("كيف")

@l313l.ar_cmd(incoming=True, func=lambda e: "donate" in e.text.lower(), edited=False)
async def reply_salam(event):
    # الرد بـ "عليكم السلام"
    await event.reply("تبرع")

@l313l.ar_cmd(incoming=True, func=lambda e: "angry" in e.text.lower(), edited=False)
async def reply_salam(event):
    # الرد بـ "عليكم السلام"
    await event.reply("غاضب")
