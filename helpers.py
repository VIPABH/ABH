from telethon.tl.functions.channels import GetParticipantRequest
from telethon import TelegramClient, events, connection, Button
from telethon.errors import UserNotParticipantError
from client import *
import asyncio
ABH = 1910015590
def send(message, **kwargs):
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
    if r.get(f"{key}:{uid}"):return
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
        r.set(f"{key}:{uid}", 1, ex=120)
