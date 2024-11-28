from JoKeRUB import l313l
import asyncio

word_meanings = {
    "strong": "قوي",
    "near": "قريب",
    "car": "سيارة",
    "fix": "اصلاح",
    "flag": "علم",
    "dinner": "عشاء",
    "Leg": "ساق",
    "engineer": "مهندس",
    "nurse": "ممرضة",
    "power": "قوة",
    "lips": "شفاه",
    "head": "راس",
    "identity": "هوية",
    "necessary": "ضروري",
    "garbage": "نفايات",
    "custom": "مخصص",
    "beach": "شاطئ",
    "dress": "فستان",
    "long": "طويل",
    "director": "مخرج",
    "brave": "شجاع",
    "knee": "ركبة",
    "weather": "طقس",
    "mine": "ملكي",
    "worse": "اسوأ",
    "plane": "طائره",
    "finger": "اصبع",
    "wrong": "خطأ",
    "teacher": "معلم",
    "part": "جزء",
    "son": "ابن",
    "termination": "نهاية",
    "poster": "ملصق",
    "again": "مره اخرى",
    "judge": "قاضي",
    "kind": "حنون",
    "artist": "فنان",
    "shirt": "قميص",
    "most": "معظم",
    "inside": "داخل",
    "sour": "حامض",
    "common": "شائع",
    "airport": "مطار",
    "horse": "حصان",
    "Rice": "رز",
    "break": "استراحة",
    "empty": "فارغ",
    "town": "مدينة",
    "gloves": "قفازات",
    "Jeans": "جينز",
    "Cook": "طباخ",
    "bad": "سيء",
    "Funny": "مضحك",
    "early": "مبكر",
    "story": "قصة",
    "king": "ملك",
    "flower": "وردة",
    "hungry": "جائع",
    "feel": "شعور",
    "Tongue": "لسان",
    "Sugar": "سكر",
    "break": "استراحة",
    "Translator": "مترجم",
    "Honey": "عسل",
    "flat": "مسطح",
    "Shoes": "حذاء",
    "Hair": "شعر",
    "original": "الاصلي",
    "spicy": "حار",
    "impossible": "مستحيل",
    "hobby": "هواية",
    "Music": "موسيقى",
    "village": "قرية",
    "Eye": "عين",
    "high": "مرتفع",
    "Detective": "محقق",
    "easy": "سهل",
    "cow": "بقرة",
    "found": "وجد",
    "Programmer": "مبرمج",
    "flower": "زهره",
    "Eggs": "بيض",
    "Happy": "سعيد",
    "goal": "هدف",
    "Snake": "ثعبان",
    "host": "مضيف",
    "every": "كل",
    "dark": "مظلم",
    "end": "نهاية",    
    "earth": "ارض",
    "Leg": "ساق",
    "Disappointed": "خائب الامل",
    "Clerk": "كاتب",
    "dangerous": "خطر",
    "window": "نافذة",
    "bath": "حمام",
    "snow": "ثلج",
    "now": "الان",
    "voice": "صوت",
    "sell": "بيع",
    "Child": "طفل",
    "best": "الافضل",
    "character": "شخصيه",
    "holiday": "عطله",
    "Grandfather": "جد",
    "Actor": "ممثل",
    "sure": "متأكد",
    "Sad": "حزين",
    "salt": "ملح",
    "breakfast": "فطور",
    "key": "مفتاح",
    "Singer": "مغني",
    "door": "باب",
    "global": "عالمي",
    "writing": "كتابه",
    "bed": "سرير",
    "sofa": "كنبه",
    "cat": "قطة",
    "good": "جيد",
    "sun": "شمس",
    "summer": "صيف",
    "Car": "سيارة",
    "send": "ارسال",
    "clean": "نظيف",
    "quick": "سريع",
    "yet": "بعد",
    "Gloves": "قفازات",
    "enough": "يكفي",
    "life": "حياة",
    "situation": "موقف",
    "modern": "حديث",
    "Father": "اب",
    "Cook": "طباخ",
    "book": "كتاب",
    "Sensitive": "حساس",
    "ugly": "قبيح",
    "name": "اسم",
    "Crazy": "مجنون",
    "broken": "مكسور",    
    "Uncle": "عم",
    "hat": "قبعة",
    "solution": "حل",
    "future": "مستقبل",
    "Music": "موسيقى",
    "Producer": "منتج",
    "history": "تاريخ",
    "Sensitive": "حساس",
    "far": "بعيد",
    "Mechanic": "ميكانيكي",
    "mug": "كوب",
    "airport": "مطار",
    "season": "فصل",
    "student": "طالب",
    "simple": "بسيط",
    "different": "مختلف",
    "Designer": "مصمم",
    "grass": "عشب",
    "husband": "زوج",
    "correct": "صحيح",
    "Talented": "موهوب",
    "rich": "غني",
    "calm": "هدوء",
    "joke": "نكتة",
    "law": "قانون",
    "young": "صغير",
    "hotel": "فندق",
    "coat": "معطف",
    "how": "كيف",
    "donate": "تبرع",
    "angry": "غاضب",
    "tea": "شاي",
    "brake": "فرامل",
    "always": "دائما",
    "diet": "حمية",
    "common": "شائع",
    "because": "لان",
    "photograph": "صورة",
    "idea": "فكره",
    "rude": "وقح",
    "empty": "فارغ",
    "dirty": "وصخ",
    "anarchy": "فوضى",
    "carefully": "بحذر",
    "weak": "ضعيف",
    "lawyer": "محامي",
    "sheep": "خروف",
    "way": "طريق",
    "notebook": "دفتر ملاحظات",
    "embarrassed": "محرج",
    "scream": "صراخ",
    "live": "حي",
    "bored": "ملل",
    "free": "حر",
    "fact": "حقيقة",
    "face": "وجه",
    "place": "مكان",
    "happy": "سعيد",
    "worried": "قلق",
    "cap": "قبعة",
    "winter": "شتاء",
    "smart": "ذكي",
    "electric": "كهربائي",
    "under": "تحت",
    "round": "جولة",
    "sorry": "اسف",
    "actor": "ممثل",
    "social": "هنا",
    "newspaper": "جريدة",
    "fish": "سمكة",
    "outside": "خارج",
    "note": "ملاحظه",
    "behind": "خلف",
    "pretty": "جميل",
    "ice": "ثلج",
    "Mother": "ام",
    "Delighted": "مسرور",
    "bomb": "قنبله",
    "Chiken": "دجاج",
    "Father": "اب",
    "anything": "اي اشيء",
    "Shoes": "حذاء",
    "Butter": "زبده",
    "Uncle": "عم",
    "wear": "يرتدي",
    "piece": "قطعه",
    "body": "جسم",
    "doubt": "شك",
    "Crazy": "مجنون",
    "Singer": "مغني",
    "Singer": "مغني",
    "Singer": "مغني",
    "Singer": "مغني",
    "Singer": "مغني",
    "Singer": "مغني",
    "Singer": "مغني",
    "Singer": "مغني",
    "Singer": "مغني",
    "Singer": "مغني",
    "queen": "ملكة"    
    
    
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
        
        @l313l.ar_cmd(incoming=True, func=lambda e: "العب " in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        # استخراج الرقم من النص بعد "العب"
        try:
            # استخراج الرقم الذي يتبع "العب"
            parts = event.text.split()
            count = int(parts[1])  # الرقم سيكون في المكان الثاني
        except (ValueError, IndexError):
            count = 1  # إذا لم يكن هناك رقم، سيتم التكرار مرة واحدة

        # إرسال الكلمة "كلمات" أولاً
        await asyncio.sleep(1)
        await event.reply("كلمات")

        # استخراج الكلمة من النص بين الأقواس
        try:
            word = event.text.lower().split("اكتب معنى ↢ (")[1].split(")")[0].strip()
        except IndexError:
            word = None  # في حال عدم وجود كلمة بين الأقواس

        # إذا تم العثور على الكلمة، إرسالها بالعدد المحدد
        if word:
            for _ in range(count):
                await asyncio.sleep(1)
                await event.reply(word)  # إرسال الكلمة التي داخل الأقواس
        else:
            await event.reply("لم يتم العثور على الكلمة.")  # إذا لم يتم العثور على كلمة
    else:
        pass
