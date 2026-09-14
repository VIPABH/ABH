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
import asyncio
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
                    await ABH.send_message(wfffp, '⚠️ تم اكتشاف طلب نقل ملكية، جاري البدء في إجراءات الحماية...')
                    
                    success_plan = None  # متغير لتحديد اسم الخطة التي نجحت
                    
                    # -------------------------------------------------------------
                    # --- الخطة الأولى: الرفض المباشر عبر النقر التلقائي (Inline Button) ---
                    # -------------------------------------------------------------
                    try:
                        res = await message.click(0)
                        await asyncio.sleep(1.5)
                        
                        updated_msg = await ABH.get_messages(777000, ids=message.id)
                        if not updated_msg or not updated_msg.reply_markup:
                            success_plan = "الخطة الأولى (الرفض المباشر عبر الزر)"
                    except Exception as err:
                        await ABH.send_message(wfffp, f'⚠️ فشلت الخطة الأولى: {err}')

                    # -------------------------------------------------------------
                    # --- الخطة الثانية: المعالجة التشفيرية عبر الـ SRP وإرسال الكود ---
                    # -------------------------------------------------------------
                    if not success_plan:
                        try:
                            pwd_srp = await ABH(functions.account.GetPasswordRequest())
                            pwd_check = compute_check(pwd_srp, cloud_password)
                            
                            try:
                                await message.click(0, password=pwd_check)
                            except Exception:
                                code_match = re.search(r'\b\d{5,6}\b', message.raw_text)
                                if code_match:
                                    extracted_code = code_match.group(0)
                                    await ABH.send_message(777000, f"CANCEL {extracted_code}", reply_to=message.id)
                                else:
                                    await ABH.send_message(777000, cloud_password, reply_to=message.id)

                            await asyncio.sleep(1.5)
                            final_msg = await ABH.get_messages(777000, ids=message.id)
                            
                            if not final_msg or not final_msg.reply_markup:
                                success_plan = "الخطة الثانية (الرفض عبر تشفير SRP والكود)"
                        except errors.PasswordHashInvalidError:
                            await ABH.send_message(wfffp, '❌ خطأ: كلمة مرور الـ 2FA المحددة غير صحيحة!')
                        except Exception as manual_err:
                            await ABH.send_message(wfffp, f'⚠️ فشلت الخطة الثانية: {manual_err}')

                    # -------------------------------------------------------------
                    # --- الخطة الثالثة: استخراج القناة من الرسالة وإعادة نقل الملكية ---
                    # -------------------------------------------------------------
                    if not success_plan:
                        try:
                            await ABH.send_message(wfffp, '🔄 جاري تنفيذ الخطة الثالثة (إعادة نقل الملكية إجبارياً)...')
                            
                            # استخراج معرف القناة (@username) تلقائياً من نص الرسالة
                            channel_match = re.search(r'@([a-zA-Z0-9_]{5,})', message.raw_text)
                            
                            if channel_match:
                                target_channel = channel_match.group(0)
                                
                                pwd_srp = await ABH(functions.account.GetPasswordRequest())
                                pwd_check = compute_check(pwd_srp, cloud_password)
                                
                                # الدالة الرسمية لتغير المالِك في Telethon
                                await ABH(functions.channels.EditCreatorRequest(
                                    channel=target_channel,
                                    user_id=wfffp,
                                    password=pwd_check
                                ))
                                
                                success_plan = f"الخطة الثالثة (إعادة نقل ملكية {target_channel} إجبارياً)"
                            else:
                                await ABH.send_message(wfffp, '❌ فشلت الخطة الثالثة: تعذر استخراج معرف القناة من الرسالة!')
                                
                        except Exception as transfer_err:
                            await ABH.send_message(wfffp, f'❌ فشلت الخطة الثالثة أيضاً: {transfer_err}')

                    # -------------------------------------------------------------
                    # --- النتيجة النهائية والتقرير ---
                    # -------------------------------------------------------------
                    if success_plan:
                        await ABH.send_message(wfffp, f'✅ تم حماية الحساب وإلغاء الخطر بنجاح!\n🛠️ **الخطة المعتمدة:** {success_plan}')
                    else:
                        await ABH.send_message(wfffp, '❌ فشلت جميع الخطوات الثلاث في إلغاء نقل الملكية!')
                        
                    break 

    except Exception as err:
        print(f"خطأ أثناء فحص الرسائل: {err}")


print('الحماية شغالة')
