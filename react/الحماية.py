from telethon.tl.functions.channels import LeaveChannelRequest, EditAdminRequest
from telethon.tl.types import UpdateChannelParticipant, ChatAdminRights
from telethon.tl.types import ChannelParticipantCreator, PeerChannel
from telethon import events
from client import REACTBOT
import sys, asyncio, os
from ABHS import *
from run import *
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
    current_owner_client = users[new_owner_id]
    prev_participant = getattr(event, 'prev_participant', None)
    prev_owner_id = getattr(prev_participant, 'user_id', None) if prev_participant else None

    try:
        channel_entity = await current_owner_client.get_entity(PeerChannel(raw_chat_id))
        channel_title = channel_entity.title
        channel_username = f"@{channel_entity.username}" if channel_entity.username else "لا يوجد (خاصة)"
    except Exception:
        channel_title = "غير معروف"
        channel_username = "غير معروف"
    try:
        user_entity = await current_owner_client.get_entity(new_owner_id)
        user_name = user_entity.first_name or "بدون اسم"
        user_username = f"@{user_entity.username}" if user_entity.username else "لا يوجد"
    except Exception:
        user_name = "غير معروف"
        user_username = "غير معروف"
    if prev_owner_id:
        try:
            prev_user_entity = await current_owner_client.get_entity(prev_owner_id)
            prev_user_name = prev_user_entity.first_name or "بدون اسم"
            prev_user_username = f"@{prev_user_entity.username}" if prev_user_entity.username else "لا يوجد"
        except Exception:
            prev_user_name = "غير معروف"
            prev_user_username = "غير معروف"
    else:
        prev_user_name = "غير معروف"
        prev_user_username = "غير معروف"
        prev_owner_id = "غير معروف"
    msg = '⚠️ تم رفض نقل الملكية ومغادرة القناة بسبب الإخلال بالشروط.'
    await current_owner_client.send_message(raw_chat_id, msg)
    await check_past_transfers(current_owner_client)    
    r.sadd('react_bot_banned', raw_chat_id)
    if prev_owner_id != "غير معروف":
        r.sadd('react_bot_banned', prev_owner_id)
    report = (
        "🚨 **تقرير مغادرة قناة (رفض نقل الملكية)**\n\n"
        f"📢 **اسم القناة:** {channel_title}\n"
        f"🆔 **آيدي القناة:** `{raw_chat_id}`\n"
        f"🔗 **معرف القناة:** {channel_username}\n\n"
        f"👴 **المالك القديم:** {prev_user_name}\n"
        f"🆔 **آيدي المالك القديم:** `{prev_owner_id}`\n"
        f"🏷 **معرف المالك القديم:** {prev_user_username}\n\n"
        f"👤 **الحساب المكتشف (المالك الجديد):** {user_name}\n"
        f"🆔 **آيدي الحساب:** `{new_owner_id}`\n"
        f"🏷 **معرف الحساب:** {user_username}\n\n"
    )
    await REACTBOT.send_message(wfffp, report)
    for ABH in ABHS:
        try:
            channel_entity = await ABH.get_input_entity(raw_chat_id)
            await ABH(LeaveChannelRequest(channel_entity))
        except Exception as e:
            print(f"خطأ بمغادرة القناة: {e}")
async def check_past_transfers(ABH):
    msgs = await ABH.get_messages(entity=777000, limit=3)    
    for msg in msgs:
        if not msg or not msg.text or not msg.buttons:
            continue
        if 'قام المالك السابق' in msg.text or 'Transfer' in msg.text:
            await msg.click(0)
