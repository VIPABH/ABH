from telethon.tl.types import (
    InputMessagesFilterRoundVideo,
    InputMessagesFilterSticker,
    InputMessagesFilterDocument,
    InputMessagesFilterPhotos,
    InputMessagesFilterVideo,
    InputMessagesFilterGif,
    InputMessagesFilterUrl
)
from JoKeRUB import l313l

plugin_category = "extra"

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
    try:
        # أنواع الفلاتر التي سيتم تطبيقها
        filters = [
            InputMessagesFilterRoundVideo,
            InputMessagesFilterSticker,
            InputMessagesFilterDocument,  
            InputMessagesFilterPhotos, 
            InputMessagesFilterVideo,  
            InputMessagesFilterGif,     
            InputMessagesFilterUrl      
        ]
        
        # عدد الرسائل المحذوفة
        total_deleted = 0

        # تطبيق الفلاتر وحذف الرسائل
        for msg_filter in filters:
            async for message in event.client.iter_messages(event.chat_id, filter=msg_filter):
                if msg_filter == InputMessagesFilterSticker:
                    if message.sticker:  # التحقق من وجود ملصق في الرسالة
                        await message.delete()  # حذف الرسالة
                        total_deleted += 1  # زيادة عدد الرسائل المحذوفة
                else:
                    await message.delete()  # حذف الرسالة
                    total_deleted += 1  # زيادة عدد الرسائل المحذوفة

        # إرسال رسالة تأكيد بعد الانتهاء من الحذف
        if total_deleted > 0:
            await event.reply(f"تم حذف {total_deleted} رسالة تحتوي على روابط، صور، فيديوهات أو مستندات!")
        else:
            await event.reply("لا توجد رسائل تطابق الفلاتر المحددة!")

    except Exception as e:
        await event.reply(f"حدث خطأ أثناء الحذف: {str(e)}")
