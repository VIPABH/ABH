import asyncio
from telethon.tl.types import Message
from JoKeRUB import l313l
from JoKeRUB.core.logger import logging
from telethon.errors.rpcerrorlist import MessageNotModifiedError
from ..Config import Config
from ..core.managers import edit_delete
from ..helpers.tools import media_type
from ..helpers.utils import _format
from ..sql_helper import no_log_pms_sql
from ..sql_helper.globals import addgvar, gvarstatus
from . import BOTLOG, BOTLOG_CHATID

LOGS = logging.getLogger(__name__)

plugin_category = "البوت"


@l313l.ar_cmd(incoming=True, func=lambda e: e.is_private, edited=True)
async def handle_edited_messages(event):
    if Config.PM_LOGGER_GROUP_ID == -100:
        return
    if gvarstatus("PMLOG") and gvarstatus("PMLOG") == "false":
        return

    sender = await event.get_sender()
    if not sender.bot:
        chat = await event.get_chat()
        if not no_log_pms_sql.is_approved(chat.id) and chat.id != 777000:
            if LOG_CHATS_.NEWPM:
                try:
                    # تحديث النص المعدل في الرسالة المسجلة
                    new_text = f"**🛂┊المستخدم :** {_format.mentionuser(sender.first_name, sender.id)}\n"
                    new_text += f"**🎟┊الايـدي :** `{chat.id}`\n\n"
                    new_text += f"**الرسالة المعدلة:** {event.message.text}"
                    await LOG_CHATS_.NEWPM.edit(new_text)
                except Exception as e:
                    # إذا لم يكن بالإمكان تعديل الرسالة المسجلة، سجل الرسالة المعدلة من جديد
                    LOGS.warn(f"لم يتم تعديل الرسالة: {str(e)}")
                    LOG_CHATS_.NEWPM = await event.client.send_message(
                        Config.PM_LOGGER_GROUP_ID,
                        f"**🛂┊المستخدم :** {_format.mentionuser(sender.first_name, sender.id)}\n"
                        f"**🎟┊الايـدي :** `{chat.id}`\n\n"
                        f"**الرسالة المعدلة:** {event.message.text}",
                    )



me = "me" 
@l313l.ar_cmd(
    pattern="خاص(?:\s|$)([\s\S]*)",
    command=("خاص", plugin_category),
    info={
        "header": "لحفظ الرسائل المردود عليها أو نصوص في الخاص فقط.",
        "الاسـتخـدام": [
            "{tr}خزن",
        ],
    },
)
async def log(log_text):
    """لحفظ الرسائل المردود عليها أو نصوص في الخاص فقط."""
    if log_text.reply_to_msg_id: 
        reply_msg = await log_text.get_reply_message()
        await reply_msg.forward_to(me) 
    elif log_text.pattern_match.group(1):  
        user = f"#التخــزين / ايـدي الدردشــه : {log_text.chat_id}\n\n"
        textx = user + log_text.pattern_match.group(1)
        await log_text.client.send_message(me, textx) 
    else:  
        await log_text.edit("**⌔┊يرجى الرد على رسالة لحفظها أو إدخال نص لتخزينه.**")
        return
    await log_text.edit("**⌔┊تم الحفظ في الخاص بنجاح ✓**")
    await asyncio.sleep(2)
    await log_text.delete()


@l313l.ar_cmd(
    pattern="تفعيل التخزين$",
    command=("تفعيل التخزين", plugin_category),
    info={
        "header": "To turn on logging of messages from that chat.",
        "الاسـتخـدام": [
            "{tr}log",
        ],
    },
)
async def set_no_log_p_m(event):
    "To turn on logging of messages from that chat."
    if Config.PM_LOGGER_GROUP_ID != -100:
        chat = await event.get_chat()
        if no_log_pms_sql.is_approved(chat.id):
            no_log_pms_sql.disapprove(chat.id)
            await edit_delete(
                event, "**⌔┊تـم تفعيـل التخـزين لهـذه الدردشـه .. بنجـاح ✓**", 5
            )


@l313l.ar_cmd(
    pattern="تعطيل التخزين$",
    command=("تعطيل التخزين", plugin_category),
    info={
        "header": "To turn off logging of messages from that chat.",
        "الاسـتخـدام": [
            "{tr}nolog",
        ],
    },
)
async def set_no_log_p_m(event):
    "To turn off logging of messages from that chat."
    if Config.PM_LOGGER_GROUP_ID != -100:
        chat = await event.get_chat()
        if not no_log_pms_sql.is_approved(chat.id):
            no_log_pms_sql.approve(chat.id)
            await edit_delete(
                event, "**⌔┊تـم تعطيـل التخـزين لهـذه الدردشـه .. بنجـاح ✓**", 5
            )


@l313l.ar_cmd(
    pattern="تخزين الخاص (تفعيل|تعطيل)$",
    command=("تخزين الخاص", plugin_category),
    info={
        "header": "To turn on or turn off logging of Private messages in pmlogger group.",
        "الاسـتخـدام": [
            "{tr}pmlog on",
            "{tr}pmlog off",
        ],
    },
)
async def set_pmlog(event):
    "To turn on or turn off logging of Private messages"
    if Config.PM_LOGGER_GROUP_ID == -100:
        return await edit_delete(
            event,
            "__For functioning of this you need to set PM_LOGGER_GROUP_ID in config vars__",
            10,
        )
    input_str = event.pattern_match.group(1)
    if input_str == "تعطيل":
        h_type = False
    elif input_str == "تفعيل":
        h_type = True
    PMLOG = not gvarstatus("PMLOG") or gvarstatus("PMLOG") != "false"
    if PMLOG:
        if h_type:
            await event.edit("**- تخزين الخاص بالفعـل ممكـن ✓**")
        else:
            addgvar("PMLOG", h_type)
            await event.edit("**- تـم تعطيـل تخـزين رسـائل الخـاص .. بنجـاح✓**")
    elif h_type:
        addgvar("PMLOG", h_type)
        await event.edit("**- تـم تفعيـل تخـزين رسـائل الخـاص .. بنجـاح✓**")
    else:
        await event.edit("**- تخزين الخاص بالفعـل معطـل ✓**")


@l313l.ar_cmd(
    pattern="تخزين الكروبات (تفعيل|تعطيل)$",
    command=("تخزين الكروبات", plugin_category),
    info={
        "header": "To turn on or turn off group tags logging in pmlogger group.",
        "الاسـتخـدام": [
            "{tr}grplog on",
            "{tr}grplog off",
        ],
    },
)
async def set_grplog(event):
    "To turn on or turn off group tags logging"
    if Config.PM_LOGGER_GROUP_ID == -100:
        return await edit_delete(
            event,
            "__For functioning of this you need to set PM_LOGGER_GROUP_ID in config vars__",
            10,
        )
    input_str = event.pattern_match.group(1)
    if input_str == "تعطيل":
        h_type = False
    elif input_str == "تفعيل":
        h_type = True
    GRPLOG = not gvarstatus("GRPLOG") or gvarstatus("GRPLOG") != "false"
    if GRPLOG:
        if h_type:
            await event.edit("**- تخزين الكـروبات بالفعـل ممكـن ✓**")
        else:
            addgvar("GRPLOG", h_type)
            await event.edit("**- تـم تعطيـل تخـزين تاكـات الكـروبات .. بنجـاح✓**")
    elif h_type:
        addgvar("GRPLOG", h_type)
        await event.edit("**- تـم تفعيـل تخـزين تاكـات الكـروبات .. بنجـاح✓**")
    else:
        await event.edit("**- تخزين الكـروبات بالفعـل معطـل ✓**")
