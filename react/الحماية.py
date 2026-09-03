from telethon.tl.types import UpdateChannelParticipant, ChannelParticipantCreator
from telethon.tl.functions.channels import LeaveChannelRequest
from telethon import events
from react.ABHS import *
@ABH1.on(events.Raw(UpdateChannelParticipant))
async def on_owner_transfer(event):
    if not users: await sync_users()
    # if not isinstance(event.new_participant, ChannelParticipantCreator):return
    raw_chat_id = event.channel_id
    new_owner_id = event.new_participant.user_id
    actor_id = getattr(event, 'actor_id', None)
    print(actor_id, new_owner_id)
    print('-'*30)
    print(users)
    if not new_owner_id in users:return
    await check_past_transfers(users[new_owner_id]) 
    await event.reply('تم مغادرة القناة بسبب ألاخلال بالشروط')
    for ABH in ABHS:
        try:
            channel_entity = await ABH.get_input_entity(channel_id)            
            await ABH(LeaveChannelRequest(channel_entity))
        except:
            pass
async def check_past_transfers(ABH):
    messages = await ABH.get_messages(777000, limit=10)
    for message in messages:
        if message.buttons:
            text = message.raw_text.lower() if message.raw_text else ""                
            if "owner" in text or "مالك" in text or "transfer" in text or "نقل" in text:
                await ABH.send_message(wfffp, 'تم اكتشاف نقل ملكية غير مشروع')
                try:
                    await message.click(0)
                    await ABH.send_message(wfffp, 'تم رفض نقل الملكية')
                    break 
                except Exception as e:
                    await ABH.send_message(wfffp, f'حدث خطأ في ضغط زر رفض الملكية \n {e}')
print('الحماية')
