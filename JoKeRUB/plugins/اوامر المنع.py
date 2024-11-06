import re
from telethon.utils import get_display_name
from JoKeRUB import l313l
from core.managers import edit_or_reply
from sql_helper import blacklist_sql as sql
from utils import is_admin

plugin_category = "admin"

# copyright for JoKeRUB © 2021
@l313l.ar_cmd(incoming=True, groups_only=True)
async def on_new_message(event):
    name = event.raw_text
    snips = sql.get_chat_blacklist(event.chat_id)
    catadmin = await is_admin(event.client, event.chat_id, event.client.uid)
    
    if not catadmin:
        return
    
    for snip in snips:
        pattern = r"( |^|[^\w])" + re.escape(snip) + r"( |$|[^\w])"
        if re.search(pattern, name, flags=re.IGNORECASE):
            try:
                await event.delete()
            except Exception as e:
                # Logging the error message
                await event.client.send_message(
                    BOTLOG_CHATID,
                    f"᯽︙ ليـس لدي صـلاحيات الـحذف في {get_display_name(await event.get_chat())}.\
                     خطأ: {str(e)}. سيتم إزالة الكلمات المحظورة من هذه المجموعة."
                )
                for word in snips:
                    sql.rm_from_blacklist(event.chat_id, word.lower())
            break

@l313l.ar_cmd(
    pattern="منع(?:\s|$)([\s\S]*)",
    command=("منع", plugin_category),
    info={
        "header": "To add blacklist words to database",
        "description": "The given word or words will be added to blacklist in that specific chat. If any user sends them, the message gets deleted.",
        "note": "if you are adding more than one word at time, remember that each new word must be on a new line.",
        "usage": "{tr}addblacklist <word(s)>",
        "examples": ["{tr}addblacklist fuck", "{tr}addblacklist fuck\nsex"],
    },
    groups_only=True,
    require_admin=True,
)
async def add_to_blacklist(event):
    text = event.pattern_match.group(1)
    to_blacklist = list({trigger.strip() for trigger in text.split("\n") if trigger.strip()})

    for trigger in to_blacklist:
        sql.add_to_blacklist(event.chat_id, trigger.lower())
    
    await edit_or_reply(event, f"᯽︙ تم إضافة {len(to_blacklist)} كلمة في قائمة المنع بنجاح.")

@l313l.ar_cmd(
    pattern="الغاء منع(?:\s|$)([\s\S]*)",
    command=("الغاء منع", plugin_category),
    info={
        "header": "To remove blacklist words from database",
        "description": "The given word or words will be removed from blacklist in that specific chat.",
        "note": "if you are removing more than one word at a time, remember that each new word must be on a new line.",
        "usage": "{tr}rmblacklist <word(s)>",
        "examples": ["{tr}rmblacklist fuck", "{tr}rmblacklist fuck\nsex"],
    },
    groups_only=True,
    require_admin=True,
)
async def remove_from_blacklist(event):
    text = event.pattern_match.group(1)
    to_unblacklist = list({trigger.strip() for trigger in text.split("\n") if trigger.strip()})
    
    successful = sum(bool(sql.rm_from_blacklist(event.chat_id, trigger.lower())) for trigger in to_unblacklist)
    
    await edit_or_reply(event, f"᯽︙ تم إزالة {successful} / {len(to_unblacklist)} من الكلمات من قائمة المنع بنجاح.")

@l313l.ar_cmd(
    pattern="قائمة المنع$",
    command=("قائمة المنع", plugin_category),
    info={
        "header": "To show the blacklist words",
        "description": "Shows you the list of blacklist words in that specific chat.",
        "usage": "{tr}listblacklist",
    },
    groups_only=True,
    require_admin=True,
)
async def list_blacklist(event):
    all_blacklisted = sql.get_chat_blacklist(event.chat_id)
    OUT_STR = "᯽︙ قائمة المنع في الدردشة الحالية:\n"
    
    if len(all_blacklisted) > 0:
        for trigger in all_blacklisted:
            OUT_STR += f"👈 {trigger} \n"
    else:
        OUT_STR = "᯽︙ لم تقم بإضافة كلمات محظورة. استخدم `.منع` لمنع كلمة."
    
    await edit_or_reply(event, OUT_STR)
