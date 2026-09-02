from telethon.tl.functions.channels import GetParticipantRequest
from telethon import TelegramClient, events, connection, Button
from telethon.errors import UserNotParticipantError
from client import *
import asyncio, json
wfffp = 1910015590
channels = [
    'ANYMOUSupdate', 
    'x04ou']
async def is_in_channel(user_id, channel_username, ABH):
    try:
        return await ABH(GetParticipantRequest(channel=channel_username, participant=user_id))
    except UserNotParticipantError:
        return False
    except:
        return False
async def is_user(e, ABH):
    if not e.is_private:
        raise events.StopPropagation
    uid = e.sender_id
    me = await ABH.get_me()
    key = f"users:{me.id}"
    if r.get(f"{me.id}:{uid}"):return True
    results = await asyncio.gather(
        *(is_in_channel(uid, ch, BUTTON_BOT) for ch in channels))
    buttons = [
        [Button.url(f"اشترك في {ch}", url=f"https://t.me/{ch}")]
        for ch, joined in zip(channels, results)
        if not joined]
    if buttons:
        await e.reply(
            "🔐 للوصول إلى خدمات البوت يجب الاشتراك في القنوات التالية:",
            buttons=buttons,)
        return False
    r.set(f"{me.id}:{uid}", 1, ex=120)
    if r.sismember(key, e.sender_id):return True
    r.sadd(key, e.sender_id)
    photo = await get_profile_photo(e.sender_id)
    caption = f'تم تسجيل مستخدم جديد \n اسمه ( {await ment(e)} )\n ايديه  ( `{e.sender_id}` )'
    if photo:
        await ABH.send_file(wfffp, file=photo, caption=caption, reply_to=e.id)
    else:
        await ABH.send_message(e.chat_id, message=caption, reply_to=e.id)
    return True
async def get_profile_photo(id, ABH, user=None):
    photos = []
    try:
        user = user if user else await ABH.get_entity(id)
        photos = await ABH.get_profile_photos(user, limit=1)
        if photos:
            return photos[0]
        else:
            return None
    except:
            return None
async def ment(entity):
  if hasattr(entity, "sender"):
    user = await entity.get_sender()
  else:
    user = entity
  user_id = getattr(user, "id", getattr(entity, "sender_id", None))
  p = profile(user_id) if user_id else None
  first_name = getattr(user, "first_name", "مستخدم") if user else "مستخدم"
  name = p.get("name") if p and p.get("name") else first_name
  return f"[{name}](tg://user?id={user_id})"
def custom_emoji(emoji):
    selected = random.choice(emoji) if isinstance(emoji, (list, tuple)) else emoji
    return f'<tg-emoji emoji-id={selected}>⬆️</tg-emoji>'
def profile(user_id):
    data = r.get(f"user:{user_id}")
    return json.loads(data) if data else None
