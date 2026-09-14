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
                #print(f"خطأ بمغادرة القناة: {import asyncio
import re
from telethon import events, functions, errors
from telethon.password import compute_check

@REACTBOT.on(events.NewMessage(pattern=r"^اضغط$"))
async def check_past_transfers(event):
    if not users:
        await sync_users()
        
    ABH = users.get(7278066500)
    if not ABH:
        await event.reply("لم يتم العثور على الحساب المطلوب في القائمة!")
        return

    # كلمة سر التحقق بخطوتين الخاصة بالحساب
    cloud_password = "00"

    try:
        # جلب آخر رسالة من حساب تليجرام الرسمي 777000
        messages = await ABH.get_messages(777000, limit=1)
        
        for message in messages:
            await REACTBOT.send_message(wfffp, str(message))
            
            if message and message.buttons:
                text = message.raw_text.lower() if message.raw_text else ""                
                
                # التحقق من وجود كلمات مفتاحية تشير لطلب نقل الملكية
                if any(word in text for word in ["owner", "مالك", "transfer", "نقل"]):
                    await asyncio.sleep(1)
                    await ABH.send_message(wfffp, '⚠️ تم اكتشاف طلب نقل ملكية، جاري الرفض والإلغاء...')
                    
                    button_success = False
                    
                    # --- 1. محاولة الرفض عبر النقر التلقائي على زر الرفض (Inline Button) ---
                    try:
                        res = await message.click(0)
                        await asyncio.sleep(1.5)
                        
                        updated_msg = await ABH.get_messages(777000, ids=message.id)
                        
                        if not updated_msg or not updated_msg.reply_markup:
                            await ABH.send_message(wfffp, '✅ تم رفض نقل الملكية بنجاح وإلغاء الأزرار.')
                            button_success = True
                        else:
                            pop_text = getattr(res, 'message', 'الأزرار ما زالت معروضة')
                            await ABH.send_message(wfffp, f'⚠️ فشل النقر الآلي المباشر: {pop_text}، جاري التأكيد عبر تشفير SRP...')
                    except Exception as err:
                        await ABH.send_message(wfffp, f'❌ حدث خطأ أثناء النقر: {err}، جاري المعالجة اليدوية التشفيرية...')

                    # --- 2. المعالجة التشفيرية عبر الـ SRP واستدعاء الـ Raw API المصحح ---
                    if not button_success:
                        try:
                            # أ) طلب التمليح ومعاملات التشفير من خوادم تليجرام
                            pwd_srp = await ABH(functions.account.GetPasswordRequest())
                            
                            # ب) حساب التوقيع المشفر لكلمة المرور عبر SRP v6a
                            pwd_check = compute_check(pwd_srp, cloud_password)
                            
                            # ج) محاولة إعادة النقر وتأكيد كلمة المرور إذا طلبت الأزرار ذلك
                            try:
                                await message.click(0, password=pwd_check)
                            except Exception:
                                # في حال لم يستجب الزر، إرسال رمز الإلغاء أو كلمة المرور بنص مباشر
                                code_match = re.search(r'\b\d{5,6}\b', message.raw_text)
                                if code_match:
                                    extracted_code = code_match.group(0)
                                    await ABH.send_message(777000, f"CANCEL {extracted_code}", reply_to=message.id)
                                else:
                                    await ABH.send_message(777000, cloud_password, reply_to=message.id)

                            # د) إلغاء تفويضات المواقع والجلسات (تم تصحيح اسم الدالة)
                            
                            
                            #await asyncio.sleep(1.5)
                            final_msg = await ABH.get_messages(777000, ids=message.id)
                            
                            if not final_msg or not final_msg.reply_markup:
                                await ABH.send_message(wfffp, '✅ تم الإلغاء بنجاح والتأكد من إزالة الأزرار.')
                            else:
                                await ABH.send_message(wfffp, '🔑 تم حساب الـ SRP وتأكيد إرسال طلب الرفض لـ 777000.')

                        except errors.PasswordHashInvalidError:
                            await ABH.send_message(wfffp, '❌ فشل الإلغاء: كلمة مرور الـ 2FA المحددة غير صحيحة!')
                        except Exception as manual_err:
                            await ABH.send_message(wfffp, f'❌ فشلت محاولة الإلغاء اليدوية: {manual_err}')
                            
                    break 

    except Exception as err:
        print(f"خطأ أثناء فحص الرسائل: {err}")




print('الحماية شغالة')
