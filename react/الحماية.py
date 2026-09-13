import os
import sys
from telethon import events
from telethon.tl.types import UpdateChannelParticipant, ChannelParticipantCreator, ChatAdminRights
from telethon.tl.functions.channels import LeaveChannelRequest, EditAdminRequest

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from ABHS import *
from client import REACTBOT
TWO_STEP_PASSWORD = os.getenv("TWO_STEP_PASSWORD", "00")
async def revert_ownership(current_owner_client, raw_chat_id, target_user_id):
    try:
        channel_entity = await current_owner_client.get_input_entity(raw_chat_id)
        target_user_entity = await current_owner_client.get_input_entity(target_user_id)
        pwd_check = None
        if TWO_STEP_PASSWORD:
            pwd_info = await current_owner_client(GetInputPasswordRequest())
            pwd_check = compute_check(pwd_info, TWO_STEP_PASSWORD)
        await current_owner_client(EditCreatorRequest(
            channel=channel_entity,
            user_id=target_user_entity,
            password=pwd_check
        ))
        return True
    except Exception as e:
        print(f"خطأ أثناء إعادة نقل الملكية: {e}")
        return False
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
    current_owner_client = users[new_owner_id]
    await check_past_transfers(current_owner_client)
    target_revert_id = wfffp if isinstance(wfffp, int) else getattr(mainABH, 'id', wfffp)
    reverted = await revert_ownership(current_owner_client, raw_chat_id, target_revert_id)
    try:
        msg = 'تم إعادة نقل الملكية ومغادرة القناة بسبب الإخلال بالشروط' if reverted else 'تم مغادرة القناة بسبب الإخلال بالشروط'
        await current_owner_client.send_message(raw_chat_id, msg)
    except Exception as e:
        print(f"خطأ في إرسال الرسالة: {e}")
    for ABH in ABHS:
        if ABH and ABH.is_connected():
            try:
                channel_entity = await ABH.get_input_entity(raw_chat_id)
                await ABH(LeaveChannelRequest(channel_entity))
            except Exception as e:
                print(f"خطأ بمغادرة القناة: {e}")
async def check_past_transfers(ABH):
    try:
        messages = await ABH.get_messages(777000, limit=10)
        for message in messages:
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
