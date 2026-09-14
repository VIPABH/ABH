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
    #for ABH in ABHS:
        #if ABH and ABH.is_connected():
            #try:
                #channel_entity = await ABH.get_input_entity(raw_chat_id)
                #await ABH(LeaveChannelRequest(channel_entity))
            #except Exception as e:
                #print(f"خطأ بمغادرة القناة: {e}")
import asyncio
from telethon import events
from telethon.tl.functions.messages import GetBotCallbackAnswerRequest


import re
import pyotp  # تأكد من تثبيت المكتبة: pip install pyotp
@REACTBOT.on(events.NewMessage(pattern="اضغط"))
async def check_past_transfers(event):
    if not users:
        await sync_users()
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
                    
                    button_success = False
                    
                    # --- 1. محاولة الرفض عبر ضغط الزر تلقائياً ---
                    try:
                        res = await message.click(0)
                        await asyncio.sleep(1.5)
                        updated_msg = await ABH.get_messages(777000, ids=message.id)
                        
                        # إذا اختفت الأزرار تعتبر العملية نجحت
                        if not updated_msg or not updated_msg.reply_markup:
                            await ABH.send_message(wfffp, '✅ تم رفض نقل الملكية بنجاح عبر الزر.')
                            button_success = True
                        else:
                            pop_text = getattr(res, 'message', 'لا تزال الأزرار موجودة')
                            await ABH.send_message(wfffp, f'⚠️ فشل الضغط الآلي: {pop_text}، جاري المحاولة يدوياً...')
                    except Exception as err:
                        await ABH.send_message(wfffp, f'❌ حدث خطأ أثناء ضغط الزر: {err}، جاري المحاولة يدوياً...')

                    # --- 2. المحاولة اليدوية عبر استخراج الكود/رمز 2FA إذا فشل الزر ---
                    if not button_success:
                        try:
                            # استخراج أي رمز أرقام من نص الرسالة (مثل كود التأكيد/الرفض)
                            code_match = re.search(r'\b\d{5,6}\b', message.raw_text)
                            
                            # إذا كان لديك مفتاح 2FA سري مخزن للحساب
                            two_factor_secret = "00" # ضع مفتاح الـ 2FA الخاص بالحساب هنا
                            totp_code = None
                            if two_factor_secret and two_factor_secret != "YOUR_2FA_SECRET_HERE":
                                totp = pyotp.TOTP(two_factor_secret)
                                totp_code = totp.now()

                            # إرسال رد يدوي على رسالة 777000
                            if code_match:
                                extracted_code = code_match.group(0)
                                await ABH.send_message(777000, f"CANCEL {extracted_code}")
                                await ABH.send_message(wfffp, f'🔄 تم إرسال أمر الإلغاء اليدوي باستخدام الكود المستخرج: {extracted_code}')
                            elif totp_code:
                                await ABH.send_message(777000, totp_code)
                                await ABH.send_message(wfffp, f'🔑 تم إرسال رمز 2FA اليدوي من المكتبة: {totp_code}')
                            else:
                                await ABH.send_message(wfffp, '❌ تعذر استخراج كود التأكيد أو إنشاء رمز 2FA يدوي.')

                        except Exception as manual_err:
                            await ABH.send_message(wfffp, f'❌ فشلت المحاولة اليدوية أيضاً: {manual_err}')
                            
                    break 

    except Exception as err:
        print(f"خطأ في فحص الرسائل: {err}")

print('الحماية شغالة')
