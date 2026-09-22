from telethon.tl.functions.channels import GetParticipantRequest
from telethon.tl.types import ChannelParticipantAdmin
from telethon.errors import UserNotParticipantError
from telethon.tl.types import Channel
from datetime import datetime
from io import BytesIO
from helpers import *
from .ABHS import *
import asyncio, re
data = create('data.json')
session = {}
@REACTBOT.on(events.NewMessage)
async def is_user_check(e):
    user = await is_user(e, REACTBOT)
    if not user:
        raise events.StopPropagation
    if not (e.sender_id in session):return
    target = None
    if e.text.startswith('@') or e.text.isdigit() or e.text.startswith('https://'):
        target = e.text
    else:
        return await e.reply('عذرا الايدي او اليوزر غير صحيح', buttons=back)
    try:
        chat = await REACTBOT.get_entity(target)
    except:return await e.edit('عذرا بس ماكدرت اوفر معلومات القناة هاي', buttons=back)
    if not chat:return await e.reply('عذرا بس ماكو هيج قناة')
    if not isinstance(chat, Channel) or not chat.broadcast:
        return await e.reply('صديقي اتفقنه تضيف قناة مو شيء اخر!', buttons=back)
    try:
        bot_user = await REACTBOT.get_me()
        participant = await REACTBOT(GetParticipantRequest(
            channel=chat,
            participant=bot_user.id
        ))    
        is_admin = isinstance(participant.participant, (ChannelParticipantAdmin))
        if not is_admin:
            return await e.reply("البوت مو مشرف! ارفعه مشرف بالاول وعيد المحاولة", buttons=back)
    except UserNotParticipantError:
        return await e.reply("❌ البوت غير موجود في القناة! يرجى إضافته ورفعه مشرفاً أولاً.", buttons=back)
    owner = await get_channel_owner(chat)
    photo_file = None
    if chat.photo:
        photo_bytes = await REACTBOT.download_profile_photo(chat, file=bytes)
        if photo_bytes:
            photo_file = BytesIO(photo_bytes)
            photo_file.name = "photo.jpg"
    session[e.sender_id] = {
        'channel_name': chat.title,
        'channel_id': chat.id,
        'owner': owner.id,
        'added_by': e.sender_id,
        'row_text': e.text,
        }
    buttons = [
        Button.inline('نعم', data=f'yes', style=green),
        Button.inline('لا', data=f'no', style=red),
    ]
    if photo_file:
        return await e.reply("⚙️ **هل تريد حفظ القناة؟:**", file=photo_file, buttons=buttons)
    return await e.reply("⚙️ **هل تريد حفظ القناة؟:**", buttons=buttons)
b = [
    [Button.inline('اضف قناة', data='add_chat', style='success', icon=336920350212227131),
    Button.inline('القنوات', data='chats', style=blue, icon=336920350212227131),],
    [Button.inline('طريقة الاستخدام', data='use', style=blue, icon=1269403972611866648),
    Button.inline('معلومات اخرى', data='info', style=green, icon=5397916757333654639),]]
@REACTBOT.on(events.NewMessage(pattern=r'^/start'))
async def start(e):
    p = profile(e.sender_id)
    input_media = await get_input_media(p.get('media', None))
    text = f'اهلا عزيزي ( {await ment(e)} ) اني بوت رياكشن \n وظيفتي اسوي تفاعلات على المسجات ب قناتك , شنو تحب تسوي؟'
    await PROFILE_SEND(REACTBOT, e, text, buttons=b)
back = [Button.inline('الرجوع', data='back', style=red, icon=5352759161945867747)]
years, months, days = get_years_months_days('2026-08-14')
@REACTBOT.on(events.CallbackQuery(data=re.compile(r'^(add_chat|chats|use|info|back|yes|no)')))
async def react_callback(e):
    await e.answer()
    data = e.data.decode('utf-8')
    sender_id = e.sender_id
    if data == 'back':
        if sender_id in session:del session[sender_id]
        return await e.edit('شنو تحب تسوي؟', buttons=b)
    elif data == 'add_chat':
        session[sender_id] = data
        return await e.edit('ارسل الان يوزر او ايدي او رابط القناة')
    elif data == 'chats':
        if not str(sender_id) in data or not data[sender_id]:
            return await e.edit('عذراً بس ما عندك قنوات مضافة', buttons=back)
        text = 'القنوات المضافة👇🏾:\n'
        chat_ids = list(data[sender_id].keys())
        chats_info = await REACTBOT.get_entity([int(c_id) for c_id in chat_ids])
        if not isinstance(chats_info, list):
            chats_info = [chats_info]
        for i, channel in enumerate(chats_info, start=1):
            text += f'\n{i}- {channel.title} ( `{channel.id}` )'
        return await e.edit(text, buttons=back)
    elif data == 'use':
        text = '''
اهلا عزيزي حياك الله 
الاستخدام سهل و بسيط كل ما عليك هو تطبيق الشروط الاتية
1- ارفع البوت مشرف بالقناة لا يهم الصلاحيات
2- اربط البوت من زر ( **اضف قناة** )
3- ممنوع طرد البوت من القناة او تنزيله من الاشراف
4- احذف البوت عبر الازرار من قسم القنوات
5- ممنوع تخريب اي شيء يخص البوت

البوت مجهز كليا وكل الثغرات تم تجهيز لها الحماية المناسبة
في حال تمت مخالفة القوانين سيتم حظرك من البوت رسميا ابلاغ المطور ب مخالفتك
        '''
        return await e.edit(text, buttons=back)
    elif data == 'info':
        text = f'''
اهلا عزيزي ( {await ment(e)} )
اني بوت رياكشن عمري ( {months} أشهر ) و ( {days} يوم )
مبرمجي هو ابن هاشم , ( @wfffp - @k_4x1 )
اني متاح للاستخدام المجاني والمقابل فقط هو الاستفادة❤
تكدر تخصص كل قناة عبر الضغط على اسمها في قسم القنوات
لرؤية باقي البوتات ( @ABHBOTS )
        '''
        return await e.edit(text, buttons=back)
    elif data == 'no':return await e.edit('تم تجاهل الحفظ👍🏾', buttons=back)
    elif data == 'yes':
        db = session.get(e.sender_id, None)
        if not db:return await e.edit('اكو نقص بالمعلومات , عيد المحاولة', buttons=back)
        await e.answer("يجري الحفظ")
        owner = db.get('owner')
        chat = db.get('channel_id')
        data[chat] = {
            'owner': owner,
            'added_by': db.get('added_by'),
            'row_text': db.get('row_text'),
            'react': 5,
            'views': 5,
            'at_time': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        with open('info.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        return await e.edit(
            f"✅ **تمت إضافة القناة بنجاح!**\n\n"
            f"🆔 القناة: ( `{chat}` )\n"
            f"👑 أيدي المالك: ( `{owner or 'غير معروف'}` )\n"
            f'✉ النص المرفق ( {db.get('row_text')} )\n'
            f"⏰ وقت الحفظ: ( `{data[str(chat)]['at_time']}` )",
            buttons=back
        )
