from helpers import *
from .ABHS import *
import asyncio, re
data = create('data.json')
@REACTBOT.on(events.NewMessage)
async def is_user_check(e):
    user = await is_user(e, REACTBOT)
    if not user:
        raise events.StopPropagation
b = [
    [Button.inline('اضف قناة', data='add_chat', style='success', icon=336920350212227131),
    Button.inline('القنوات', data='chats', style=blue, icon=336920350212227131),],
    [Button.inline('طريقة الاستخدام', data='use', style=blue, icon=1269403972611866648),
    Button.inline('معلومات اخرى', data='info', style=green, icon=5397916757333654639),]]
@REACTBOT.on(events.NewMessage(pattern=r'^/start'))
async def start(e):
    await e.reply(f'اهلا عزيزي ( {await ment(e)} ) اني بوت رياكشن \n وظيفتي اسوي تفاعلات على المسجات ب قناتك , شنو تحب تسوي؟', buttons=b)
session = {}
user_chats = {} 
back = [Button.inline('الرجوع', data='back')]
years, months, days = get_years_months_days('2026-08-14')
@REACTBOT.on(events.CallbackQuery(data=re.compile(r'^(add_chat|chats|use|info|back)$')))
async def react_callback(e):
    await e.answer()
    data = e.data.decode('utf-8')
    sender_id = e.sender_id
    if data == 'back':
        return await e.edit('شنو تحب تسوي؟', buttons=b)
    elif data == 'add_chat':
        session[sender_id] = data
        return await e.reply('ارسل الان يوزر او ايدي او رابط القناة')
    elif data == 'chats':
        if sender_id not in user_chats or not user_chats[sender_id]:
            return await e.edit('عذراً بس ما عندك قنوات مضافة', buttons=back)            
        text = 'القنوات المضافة👇🏾:\n'
        chat_ids = list(user_chats[sender_id].keys())
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
