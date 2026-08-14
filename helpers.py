from telethon.tl.functions.channels import GetParticipantRequest
from telethon import TelegramClient, events, connection, Button
from telethon.errors import UserNotParticipantError
from client import *
import asyncio
wfffp = 1910015590
def hint(message, **kwargs):
    task = asyncio.create_task(
        BUTTON_BOT.send_message(message, **kwargs)
    )
    task.add_done_callback(_log_task_result)
    return task
def _log_task_result(task):
    try:
        task.result()
    except Exception as e:
        print(f"fire_send_message failed: {e}")
channels = [
    'ANYMOUSupdate', 
    'x04ou']
async def is_in_channel(user_id, channel_username):
    try:
        return await BUTTON_BOT(GetParticipantRequest(channel=channel_username, participant=user_id))
    except UserNotParticipantError:
        return False
    except:
        return False
async def is_user(e):
    if not e.is_private:
        raise events.StopPropagation
    uid = e.sender_id
    me = await BUTTON_BOT.get_me()
    if r.get(f"{me.id}:{uid}"):return
    results = await asyncio.gather(
        *(is_in_channel(uid, ch) for ch in channels))
    buttons = [
        [Button.url(f"اشترك في {ch}", url=f"https://t.me/{ch}")]
        for ch, joined in zip(channels, results)
        if not joined]
    if buttons:
        await e.reply(
            "🔐 للوصول إلى خدمات البوت يجب الاشتراك في القنوات التالية:",
            buttons=buttons,
        )
        raise events.StopPropagation
    else:
        r.set(f"{me.id}:{uid}", 1, ex=120)
async def get_profile_photo(id, user=None):
    photos = []
    try:
        user = user if user else await BUTTON_BOT.get_entity(id)
        photos = await BUTTON_BOT.get_profile_photos(user, limit=1)
        if photos:
            return photos[0]
        else:
            return None
    except:
            return None
async def ment(entity):
    try:
        user_id = None
        name = None
        if isinstance(entity, int):
            user_id = entity
        elif isinstance(entity, str) and entity.isdigit():
            user_id = int(entity)
        elif hasattr(entity, 'sender_id'): 
            user_id = entity.sender_id
        elif hasattr(entity, 'id'): 
            user_id = entity.id
        if not user_id:
            return "غير معروف"
        if user_id in mentions_dict:
            return mentions_dict[user_id]
        user_data = profile(user_id)
        if user_data:
            name = user_data.get('name') if isinstance(user_data, dict) else getattr(user_data, 'name', None)
        if not name:
            if not hasattr(entity, 'first_name') or (hasattr(entity, 'id') and entity.id != user_id):
                entity = await BUTTON_BOT.get_entity(user_id)
            name = getattr(entity, 'first_name', 'مستخدم') or 'مستخدم'
        if user_id not in mentions_dict:
            mentions_dict[user_id] = f"[{name}](tg://user?id={user_id})"
        return f"[{name}](tg://user?id={user_id})"
    except Exception as e:
        return "غير معروف"
def custom_emoji(emoji):
    selected = random.choice(emoji) if isinstance(emoji, (list, tuple)) else emoji
    return f'<tg-emoji emoji-id={selected}>⬆️</tg-emoji>'
