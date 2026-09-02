from helpers import *
from .ABHS import *
import asyncio
rules = [
    'ممنوع تنقل ملكية لأي حساب من حساباتي', 
    'ممنوع تضيف اي حساب مو مضاف مسبقا',
    'ممنوع تنزل اي حساب من الاشراف',
]
text = f'**قوانين البوت!**\n'
for num, rule in enumerate(rules, start=1):
    text += f'{num}- `{rule}`\n'
text += 'البوت ممجاني بالكامل كل ما عليك الالتزام بالقوانين وفقط\n واذا حبيت تحذف التفاعلات او تطرد حساب معين انتقل الى قسم الاعدادات وهناك خصص مجموعتك مثل ما تحب'
session = {}
@REACTBOT.on(events.NewMessage)
async def is_user_check(e):
    if not e.is_private:
        raise events.StopPropagation
    user = await is_user(e, BUTTON_BOT)
    if not user:
        raise events.StopPropagation
@REACTBOT.on(events.NewMessage(pattern=r'^/start'))
async def start(e):
    id = e.sender_id
    if id in session:return
    session[id] = 'rules'
    await e.reply(f'اهلا عزيزي ( {await ment(e)} ) اني بوت رياكشن \n وظيفتي اسوي تفاعلات على المسجات ب قناتك')
    await asyncio.sleep(3)
    await e.respond(f'استخدامي سلس و واضح و بسيط فقط كل ما عليك فقط الالتزام بالقوانين')
    await asyncio.sleep(2.2)
    await e.respond(text)
    await asyncio.sleep(7)
    await e.respond('التزم بالقوانين واستمتع ب استخدامك للبوت, صنع ب حب بواسطة المبدع @k_4x1 ❤')
    del session[id]
