from telethon.tl.types import (
    InputMessagesFilterRoundVideo,
    InputMessagesFilterDocument,
    InputMessagesFilterPhotos,
    InputMessagesFilterSticker,
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
            InputMessagesFilterRoundVideo,  # فيديوهات دائرية
            InputMessagesFilterDocument,    # مستندات
            InputMessagesFilterSticker,     # ملصقات
            InputMessagesFilterPhotos,      # صور
            InputMessagesFilterVideo,       # فيديوهات عادية
            InputMessagesFilterGif,         # صور متحركة (GIFs)
            InputMessagesFilterUrl          # رسائل تحتوي على روابط
        ]
        
        # عدد الرسائل المحذوفة
        total_deleted = 0
        limit = 1000  # تحديد حد أقصى لعدد الرسائل المحذوفة في كل مرة

        # تطبيق الفلاتر وحذف الرسائل
        for msg_filter in filters:
            async for message in event.client.iter_messages(event.chat_id, filter=msg_filter, limit=limit):
                try:
                    await message.delete()  # حذف الرسالة
                    total_deleted += 1  # زيادة عدد الرسائل المحذوفة
                except Exception as e:
                    print(f"حدث خطأ أثناء حذف الرسالة: {str(e)}")  # يمكننا تسجيل الأخطاء هنا

        # إرسال رسالة تأكيد بعد الانتهاء من الحذف
        if total_deleted > 0:
            await event.reply(f"تم حذف {total_deleted} رسالة تحتوي على روابط، صور، فيديوهات، ملصقات أو مستندات!")
        else:
            await event.reply("لا توجد رسائل تطابق الفلاتر المحددة!")

    except Exception as e:
        # في حالة حدوث خطأ أثناء الحذف
        error_message = f"حدث خطأ أثناء الحذف: {str(e)}"
        # تسجيل الخطأ (اختياري) في وحدة التحكم أو سجلات البوت
        print(f"Error occurred: {error_message}")
        # إرسال رسالة للمستخدم
        await event.reply(error_message)
