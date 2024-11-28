from JoKeRUB import l313l
import asyncio

# قاموس للكلمات ومعانيها
word_meanings = {
    "strong": "قوي",
    "near": "قريب",
    "car": "سيارة",
    "fix": "اصلاح",
    "flag": "علم",
    "dinner": "عشاء",
    "town": "مدينة",
    "gloves": "قفازات",
    "original": "الاصلي"
}

# دالة واحدة للإجابة على كل كلمة
@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ (" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        # استخراج الكلمة من النص
        word = event.text.lower().split("اكتب معنى ↢ (")[1].split(")")[0].strip()

        # البحث عن المعنى في القاموس
        meaning = word_meanings.get(word)

        # إذا كانت الكلمة موجودة في القاموس، الرد بالمعنى
        if meaning:
            await asyncio.sleep(1)
            await event.reply(meaning)
        else:
            await asyncio.sleep(1)
            await event.reply("لا يوجد معنى لهذه الكلمة.")
    else:
        pass
