import os
import sys, asyncio
from telethon import events
from telethon.tl.types import UpdateChannelParticipant, ChannelParticipantCreator, ChatAdminRights
from telethon.tl.functions.channels import LeaveChannelRequest, EditAdminRequest

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from ABHS import *
from client import REACTBOT

@REACTBOT.on(events.Raw(UpdateChannelParticipant))
async def on_owner_transfer(event):
    if not users:
        await sync_users()
        
    new_participant = getattr(event, 'new_participant', None)
    if new_participant is None or not hasattr(new_participant, 'user_id'):
        return

    if not isinstance(new_participant, ChannelParticipantCreator):
        return

    raw_chat_id = getattr(event, 'channel_id', None)
    new_owner_id = new_participant.user_id

    if new_owner_id not in users or not raw_chat_id:
        return

    msg = 'تم رفض نقل الملكية ومغادرة القناة بسبب الإخلال بالشروط' 
    current_owner_client = users[new_owner_id]
    await current_owner_client.send_message(raw_chat_id, msg)
    await asyncio.sleep(1)
    # await check_past_transfers(event)
    #for ABH in ABHS:
        #if ABH and ABH.is_connected():
            #try:
                #channel_entity = await ABH.get_input_entity(raw_chat_id)
                #await ABH(LeaveChannelRequest(channel_entity))
            #except Exception as e:
                #print(f"خطأ بمغادرة القناة: {import asyncio

import asyncio
import logging
from telethon import TelegramClient, events
OFFICIAL_NOTICE_ID = 777000  # حساب تليجرام الرسمي للتنبيهات

# نصوص الزر التي قد تظهر (عربي/إنجليزي) — يبحث عن أي منها
REJECT_BUTTON_TEXTS = [
    "رفض نقل القناة",
    "Reject channel transfer",
]

logging.basicConfig(level=logging.INFO)
log = logging.getLogger("reject-transfer-bot")



@ABH1.on(events.NewMessage(chats=OFFICIAL_NOTICE_ID))
async def handle_official_notice(event):
    message = event.message

    if not message.buttons:
        return

    # ابحث عن زر الرفض تحديداً بالنص، بدل الاعتماد على ترتيبه (index)
    for row_index, row in enumerate(message.buttons):
        for col_index, button in enumerate(row):
            button_text = getattr(button, "text", "") or ""
            if any(reject_text in button_text for reject_text in REJECT_BUTTON_TEXTS):
                try:
                    await message.click(row_index, col_index)
                    log.info("تم رفض نقل ملكية القناة بنجاح.")
                except Exception as e:
                    log.error(f"فشل الضغط على زر الرفض: {e}")
                return

    log.info("رسالة من 777000 لكنها ليست تنبيه نقل ملكية قناة، تم تجاهلها.")

print('الحماية شغالة')
