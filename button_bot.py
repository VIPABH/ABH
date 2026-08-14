from helpers import *
from client import *
@BUTTON_BOT.on(events.NewMessage(pattern=r'^/start$'))
async def start(e):
    if not e.is_private:return
    user = await is_user(e)
    if not is_user:return
    photo = await get_profile_photo(e)
    if photo:
        await BUTTON_BOT.send_file(e.chat_id, file=photo, caption=f'اهلا عزيزي ( {await ment(e)} ) اني بوت مال ازرار استخدامي سهل و بسيط ارسل `الاوامر`', reply_to=e.id)
    else:
        await BUTTON_BOT.send_message(e.chat_id, message=f'اهلا عزيزي ( {await ment(e)} ) اني بوت مال ازرار استخدامي سهل و بسيط ارسل `الاوامر`', reply_to=e.id)
@BUTTON_BOT.on(events.NewMessage(pattern=r'^الاوامر$'))
async def command(e):
    if not e.is_private:return
    await e.reply(
    f"""
<b>طريقة استخدام الأمر:</b>

<code>زر + لون الزر</code> أو بدون لون ليكون افتراضيًا.

بعدها:
<code>اسم الزر + الرابط + الإيموجي المميز</code>

<b>مثال:</b>
<code>زراخضر المبرمج https://t.me/K_4x1</code> {custom_emoji(5465374681915727405)}
""",
    parse_mode="html"
)
