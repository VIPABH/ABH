from telethon.tl.types import (
    InputMessagesFilterDocument,
    InputMessagesFilterUrl
)
from JoKeRUB import l313l

plugin_category = "extra"

# قائمة المعرفات التي سيتم استثناؤها
excluded_user_ids = [793977288, 1421907917, 7308514832, 6387632922]

@l313l.ar_cmd(
    pattern="امسح(\s*| \d+)$",  # يسمح بإضافة عدد التكرار في الأمر إن رغبت
    command=("امسح", plugin_category),
    info={
        "header": "لحذف الرسائل من نوع معين.",
        "description": "يحذف الرسائل مثل الصور، الفيديوهات، الروابط، وغيرها بناءً على الفلاتر المحددة.",
        "usage": ["{tr}امسح"],
        "examples": "{tr}امسح",
    },
)
async def delete_filtered_messages(event):
    await event.delete()

    try:
        filters = [
            InputMessagesFilterDocument,  
            InputMessagesFilterUrl
        ]
        
        total_deleted = 0

        for msg_filter in filters:
            async for message in event.client.iter_messages(event.chat_id, filter=msg_filter):
                if message.sender_id in excluded_user_ids:
                    continue 
                if message:
                    await message.delete()  # حذف الرسالة
                    total_deleted += 1  # زيادة عدد الرسائل المحذوفة

        if total_deleted > 0:
            await event.reply(f"تم حذف {total_deleted} رسالة تحتوي على روابط أو مستندات!")
        
        else:
            await event.reply("لا توجد رسائل تطابق الفلاتر المحددة!")

    except Exception as e:
        await event.reply(f"حدث خطأ أثناء الحذف: {str(e)}")
