from telethon.tl.functions.channels import GetParticipantRequest
from telethon import TelegramClient, events, connection, Button
from telethon.errors import UserNotParticipantError
from client import *
import asyncio
ABH = 1910015590
def send(client, message, **kwargs):
    task = asyncio.create_task(
        BUTTON_BOT.send_message(ABH, message, **kwargs)
    )
    task.add_done_callback(_log_task_result)
    return task
def _log_task_result(task):
    try:
        task.result()
    except Exception as e:
        print(f"fire_send_message failed: {e}")
class Me:
    async def init(self, ABH):
        self.me = await ABH.get_me()
        self.id = self.me.id
        self.name = self.me.first_name
channels = [
    'ANYMOUSupdate', 
    'x04ou'
]
async def is_in_channel(user_id, channel_username):
    try:
        await ABH(GetParticipantRequest(channel_username, user_id))
        return True
    except UserNotParticipantError:
        return False
    except Exception as e:
        hint(f"Error checking {channel_username} for {user_id}: {e}")
        return False
async def is_user(e):
    if not e.is_private:
        raise events.StopPropagation
    uid = e.sender_id
    if r.get(f"{ME.id}:{uid}"):return
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
        r.set(f"{ME.id}:{uid}", 1, ex=120)
async def get_profile_photo(id, user=None):
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
        if not hasattr(entity, 'first_name') or (hasattr(entity, 'id') and entity.id != user_id):
            entity = await ABH.get_entity(user_id)
            name = getattr(entity, 'first_name', 'مستخدم') or 'مستخدم'
        if user_id not in mentions_dict:
            mentions_dict[user_id] = f"[{name}](tg://user?id={user_id})"
        return f"[{name}](tg://user?id={user_id})"
    except Exception as e:
        return "غير معروف"
def custom_emoji(emoji):
    selected = random.choice(emoji) if isinstance(emoji, (list, tuple)) else emoji
    return f'<tg-emoji emoji-id={selected}>⬆️</tg-emoji>'
