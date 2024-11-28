from JoKeRUB import l313l
import asyncio

plugin_category = "extra"

# قاموس يحتوي على الكلمات ومعانيها
word_meanings = {
    "teacher": "مدرس",
    "live": "حياة",
    "book": "كتاب",
    "school": "مدرسة",
    "car": "سيارة",
    "computer": "كمبيوتر",
    "love": "حب",
    "friend": "صديق",
    # يمكنك إضافة المزيد من الكلمات هنا...
}

# دالة الرد على أمر "العب"
@l313l.ar_cmd(pattern="العب")
async def start_game(event):
    # الرد بكلمة "انقليزي" عندما يكتب المستخدم "العب"
    await event.reply("انقليزي")

    # ضع علمًا (Flag) أو حالة لتحديد الانتظار للكلمة التالية
    await asyncio.sleep(1)  # تأخير بسيط لكي يتمكن المستخدم من كتابة الكلمة

# دالة الرد على أمر "معنى ↢ (الكلمة)"
@l313l.ar_cmd(pattern="معنى ↢ \((.*)\)")
async def handle_meaning(event):
    # الحصول على الكلمة المدخلة بعد "معنى ↢ (الكلمة)"
    word = event.pattern_match.group(1).strip().lower()

    # إذا كانت الكلمة موجودة في القاموس، الرد بالمعنى
    meaning = word_meanings.get(word)
    
    if meaning:
        await event.reply(meaning)  # الرد بالمعنى إذا كان موجود
    else:
        await event.reply("لا يوجد معنى لهذا الكلمة.")  # إذا كانت الكلمة غير موجودة في القاموس
