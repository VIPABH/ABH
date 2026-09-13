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
    await check_past_transfers(event)



    # 4. مغادرة الحسابات للقناة
    for ABH in ABHS:
        if ABH and ABH.is_connected():
            try:
                channel_entity = await ABH.get_input_entity(raw_chat_id)
                await ABH(LeaveChannelRequest(channel_entity))
            except Exception as e:
                print(f"خطأ بمغادرة القناة: {e}")
import asyncio
from telethon import events
from telethon.tl.functions.messages import GetBotCallbackAnswerRequest

@REACTBOT.on(events.NewMessage(pattern="اضغط"))
async def check_past_transfers(event):
    if not users:
        await sync_users()
    
    # جلب الحساب المطلوب من القائمة
    ABH = users.get(7278066500)
    if not ABH:
        await event.reply("لم يتم العثور على الحساب المطلوب في القائمة!")
        return

    try:
        # جلب آخر رسالة من حساب تليجرام الرسمي 777000
        messages = await ABH.get_messages(777000, limit=1)
        
        for message in messages:
            await REACTBOT.send_message(wfffp, str(message))
            
            if message and message.buttons:
                text = message.raw_text.lower() if message.raw_text else ""                
                
                if any(word in text for word in ["owner", "مالك", "transfer", "نقل"]):
                    await asyncio.sleep(2)
                    await ABH.send_message(wfffp, '⚠️ تم اكتشاف نقل ملكية، جاري الرفض...')
                    
                    try:
                        # 1. محاولة الضغط على الزر الأول واستلام الاستجابة
                        res = await message.click(0)
                        
                        # 2. الانتظار ثانية ثم إعادة جلب الرسالة للتحقق من اختفاء الزر
                        await asyncio.sleep(1.5)
                        updated_msg = await ABH.get_messages(777000, ids=message.id)
                        
                        # إذا اختفت الأزرار أو رجعت استجابة مؤكدة
                        if not updated_msg.reply_markup:
                            await ABH.send_message(wfffp, '✅ تم رفض نقل الملكية بنجاح واختفى الزر.')
                        else:
                            # في حال كانت هناك رسالة توضيحية من السيرفر
                            pop_text = getattr(res, 'message', 'لا تزال الأزرار موجودة')
                            await ABH.send_message(wfffp, f'ℹ️ نتيجة الضغط: {pop_text}')
                            
                        break 
                        
                    except Exception as err:
                        await ABH.send_message(wfffp, f'❌ حدث خطأ أثناء ضغط الزر: {err}')

    except Exception as err:
        print(f"خطأ في فحص الرسائل: {err}")

print('الحماية شغالة')
