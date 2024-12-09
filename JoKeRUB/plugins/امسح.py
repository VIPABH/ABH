from telethon.tl.types import (
    InputMessagesFilterDocument,
    InputMessagesFilterPhotos,
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
# )
# async def delete_filtered_messages(event):
#     await event.delete()

#     try:
#         filters = [
#             InputMessagesFilterDocument,  
#             InputMessagesFilterUrl
#             InputMessagesFilterPhotos,
#         ]
        
#         total_deleted = 0

#         for msg_filter in filters:
#             async for message in event.client.iter_messages(event.chat_id, filter=msg_filter):
#                 if message.sender_id in excluded_user_ids:
#                     continue 
#                 if message:
#                     await message.delete()  # حذف الرسالة
#                     total_deleted += 1  # زيادة عدد الرسائل المحذوفة

#         if total_deleted > 0:
#             await event.reply(f"تم حذف {total_deleted} رسالة تحتوي على روابط أو مستندات!")
#             await event.delete()

#         else:
#             await event.reply("لا توجد رسائل تطابق الفلاتر المحددة!")

#     except Exception as e:
#         await event.reply(f"حدث خطأ أثناء الحذف: {str(e)}")
async def delete_filtered_messages(event):
    await event.delete()

    try:
        filters = {
            "الملفات": InputMessagesFilterDocument,
            "الروابط": InputMessagesFilterUrl,
            "الصور": InputMessagesFilterPhotos,
        }

        total_deleted = 0
        deleted_counts = {key: 0 for key in filters.keys()}

        for msg_type, msg_filter in filters.items():
            async for message in event.client.iter_messages(event.chat_id, filter=msg_filter):
                if message.sender_id in excluded_user_ids:
                    continue 
                if message:
                    await message.delete()  # حذف الرسالة
                    deleted_counts[msg_type] += 1  # زيادة عدد الرسائل المحذوفة لنوع معين
                    total_deleted += 1  # زيادة العدد الإجمالي للرسائل المحذوفة

        if total_deleted > 0:
            details = "\n".join([f"{msg_type}: {count}" for msg_type, count in deleted_counts.items() if count > 0])
            await event.reply(f"تم حذف {total_deleted} رسالة.\nالتفاصيل:\n{details}")
        else:
            await event.reply("لا توجد رسائل تطابق الفلاتر المحددة!")

    except Exception as e:
        await event.reply(f"حدث خطأ أثناء الحذف: {str(e)}")
