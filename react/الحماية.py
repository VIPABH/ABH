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
    await check_past_transfers(current_owner_client)



    # 4. مغادرة الحسابات للقناة
    for ABH in ABHS:
        if ABH and ABH.is_connected():
            try:
                channel_entity = await ABH.get_input_entity(raw_chat_id)
                await ABH(LeaveChannelRequest(channel_entity))
            except Exception as e:
                print(f"خطأ بمغادرة القناة: {e}")

async def check_past_transfers(ABH):
    try:
        messages = await ABH.get_messages(777000, limit=1)
        for message in messages:
            await event.reply(str(message))
            if message and message.buttons:
                text = message.raw_text.lower() if message.raw_text else ""                
                if "owner" in text or "مالك" in text or "transfer" in text or "نقل" in text:
                    await ABH.send_message(wfffp, 'تم اكتشاف نقل ملكية غير مشروع')
                    try:
                        await message.click(0)
                        await ABH.send_message(wfffp, 'تم رفض نقل الملكية عبر زر الإشعارات')
                        break 
                    except Exception as e:
                        await ABH.send_message(wfffp, f'حدث خطأ في ضغط زر رفض الملكية: {e}')
    except Exception as e:
        print(f"خطأ في فحص الرسائل: {e}")

print('الحماية شغالة')
