from telethon.tl.types import (
    InputMessagesFilterRoundVideo,
    InputMessagesFilterDocument,
    InputMessagesFilterPhotos,
    InputMessagesFilterVideo,
    InputMessagesFilterGif,
    InputMessagesFilterUrl,
    InputMessagesFilterSticker  # إضافة فلتر الملصقات
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
            InputMessagesFilterRoundVideo,  # فيديوهات دائرية
            InputMessagesFilterDocument,   # مستندات
            InputMessagesFilterSticker,    # ملصقات
            InputMessagesFilterPhotos,     # صور
            InputMessagesFilterVideo,      # فيديوهات عادية
            InputMessagesFilterGif,        # صور متحركة (GIFs)
            InputMessagesFilterUrl         # رسائل تحتوي على روابط
        ]
        
        # عدد الرسائل المحذوفة
        total_deleted = 0

        # تطبيق الفلاتر وحذف الرسائل
        for msg_filter in filters:
            async for message in event.client.iter_messages(event.chat_id, filter=msg_filter):
                await message.delete()  # حذف الرسالة
                total_deleted += 1  # زيادة عدد الرسائل المحذوفة

        # إرسال رسالة تأكيد بعد الانتهاء من الحذف
        if total_deleted > 0:
            await event.reply(f"تم حذف {total_deleted} رسالة تحتوي على روابط، صور، فيديوهات، ملصقات أو مستندات!")
        else:
            await event.reply("لا توجد رسائل تطابق الفلاتر المحددة!")

    except Exception as e:
        await event.reply(f"حدث خطأ أثناء الحذف: {str(e)}")
