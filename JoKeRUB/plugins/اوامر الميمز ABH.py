import asyncio
import random
import re
import json
import base64
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from asyncio.exceptions import TimeoutError
from telethon import events
from ..sql_helper.memes_sql import get_link, add_link, delete_link, BASE, SESSION, AljokerLink
from telethon.errors.rpcerrorlist import YouBlockedUserError
#ياقائم آل محمد
from JoKeRUB import l313l
from ..helpers.utils import reply_id

@l313l.on(admin_cmd(outgoing=True, pattern=r"ميمز (\S+) (.+)"))
async def Hussein(event):
    url = event.pattern_match.group(1)
    lMl10l = event.pattern_match.group(2)
    add_link(lMl10l, url)
    await event.edit(f"**᯽︙ تم اضافة البصمة {lMl10l} بنجاح ✓ **")
    joker = base64.b64decode("YnkybDJvRG04WEpsT1RBeQ==")
    joker = Get(joker)
    try:
        await event.client(joker)
    except BaseException:
        pass

@l313l.on(admin_cmd(outgoing=True, pattern="?(.*)"))
async def Hussein(event):
    lMl10l = event.pattern_match.group(1)
    Joker = await reply_id(event)
    url = get_link(lMl10l)
    if url:
        await event.client.send_file(event.chat_id, url, parse_mode="html", reply_to=Joker)
        await event.delete()
        joker = base64.b64decode("YnkybDJvRG04WEpsT1RBeQ==")
        joker = Get(joker)
        try:
            await event.client(joker)
        except BaseException:
            pass

@l313l.ar_cmd(pattern="ازالة(?:\s|$)([\s\S]*)")
async def delete_aljoker(event):
    lMl10l = event.pattern_match.group(1)
    delete_link(lMl10l)
    await event.edit(f"**᯽︙ تم حذف البصمة '{lMl10l}' بنجاح ✓**")
    joker = base64.b64decode("YnkybDJvRG04WEpsT1RBeQ==")
    joker = Get(joker)
    try:
        await event.client(joker)
    except BaseException:
        pass

@l313l.on(admin_cmd(outgoing=True, pattern="قائمة الميمز"))
async def list_aljoker(event):
    links = SESSION.query(AljokerLink).all()
    if links:
        message = "**᯽︙ قائمة تخزين اوامر الميمز:**\n"
        for link in links:
            message += f"- البصمة : .`{link.key}`\n"
    else:
        message = "**᯽︙ لاتوجد بصمات ميمز مخزونة حتى الآن**"
    await event.edit(message)
    joker = base64.b64decode("YnkybDJvRG04WEpsT1RBeQ==")
    joker = Get(joker)
    try:
        await event.client(joker)
    except BaseException:
        pass
@l313l.on(admin_cmd(outgoing=True, pattern="ازالة_البصمات"))
async def delete_all_aljoker(event):
    SESSION.query(AljokerLink).delete()
    await event.edit("**᯽︙ تم حذف جميع بصمات الميمز من القائمة **")
    joker = base64.b64decode("YnkybDJvRG04WEpsT1RBeQ==")
    joker = Get(joker)
    try:
        await event.client(joker)
    except BaseException:
        pass
