from JoKeRUB import l313l
import asyncio

# دالة الرد على أمر "العب"
@l313l.ar_cmd(pattern="العب")
async def start_game(event):
    # الرد بكلمة "انقليزي" عندما يكتب المستخدم "العب"
    await event.reply("انقليزي")
    await asyncio.sleep(1)  # تأخير بسيط لكي يتمكن المستخدم من كتابة الكلمة

# دالة الرد على أمر "معنى ↢ (الكلمة)"
@l313l.ar_cmd(pattern=r"معنى ↢ \((.*)\)")  # استخدام تعبير منتظم لالتقاط الكلمة بشكل صحيح
async def handle_meaning(event):
    # الحصول على الكلمة المدخلة بعد "معنى ↢ (الكلمة)"
    word = event.pattern_match.group(1).strip().lower()

    # تحديد الرد بناءً على الكلمة المدخلة
    if word == "identity":
        await event.reply("هوية")
    elif word == "necessary":
        await event.reply("ضروري")
    elif word == "garbage":
        await event.reply("نفايات")
    elif word == "custom":
        await event.reply("مخصص")
    elif word == "beach":
        await event.reply("شاطئ")
    elif word == "dress":
        await event.reply("فستان")
    elif word == "long":
        await event.reply("طويل")
    elif word == "director":
        await event.reply("مخرج")
    elif word == "brave":
        await event.reply("شجاع")
    elif word == "knee":
        await event.reply("ركبة")
    elif word == "weather":
        await event.reply("طقس")
    elif word == "mine":
        await event.reply("ملكي")
    elif word == "worse":
        await event.reply("اسوأ")
    elif word == "plane":
        await event.reply("طائره")
    elif word == "finger":
        await event.reply("اصبع")
    elif word == "wrong":
        await event.reply("خطأ")
    elif word == "teacher":
        await event.reply("معلم")
    elif word == "part":
        await event.reply("جزء")
    elif word == "son":
        await event.reply("ابن")
    elif word == "termination":
        await event.reply("نهاية")
    elif word == "poster":
        await event.reply("ملصق")
    elif word == "again":
        await event.reply("مره اخرى")
    elif word == "judge":
        await event.reply("قاضي")
    elif word == "kind":
        await event.reply("حنون")
    elif word == "artist":
        await event.reply("فنان")
    elif word == "shirt":
        await event.reply("قميص")
    elif word == "most":
        await event.reply("معظم")
    elif word == "inside":
        await event.reply("داخل")
    elif word == "sour":
        await event.reply("حامض")
    elif word == "strong":
        await event.reply("قوي")
    elif word == "near":
        await event.reply("قريب")
    elif word == "car":
        await event.reply("سيارة")
    elif word == "fix":
        await event.reply("اصلاح")
    elif word == "flag":
        await event.reply("علم")
    elif word == "dinner":
        await event.reply("عشاء")
    elif word == "town":
        await event.reply("مدينة")
    elif word == "gloves":
        await event.reply("قفازات")
    elif word == "original":
        await event.reply("الاصلي")
    else:
        await event.reply("لا يوجد معنى لهذه الكلمة.")  # إذا كانت الكلمة غير موجودة
