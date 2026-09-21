from helpers import *
from .ABHS import *
import asyncio
@REACTBOT.on(events.NewMessage)
async def is_user_check(e):
    user = await is_user(e, REACTBOT)
    if not user:
        raise events.StopPropagation
@REACTBOT.on(events.NewMessage(pattern=r'^/start'))
async def start(e):
    if not e.is_private:return
    id = e.sender_id
    if id in session:return
    b = [
        [Button.inline('اضف قناة', data='add_chat', style='success', icon=336920350212227131),
        Button.inline('القنوات', data='chats', style=blue, icon=336920350212227131),],
        [Button.inline('طريقة الاستخدام', data='chats', style=blue, icon=1269403972611866648),
        Button.inline('معلومات اخرى', data='chats', style=green, icon=5397916757333654639),]]
    await e.reply(f'اهلا عزيزي ( {await ment(e)} ) اني بوت رياكشن \n وظيفتي اسوي تفاعلات على المسجات ب قناتك , شنو تحب تسوي؟', buttons=b)
