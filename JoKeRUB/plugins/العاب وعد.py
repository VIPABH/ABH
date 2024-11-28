import re
from telethon import events
from JoKeRUB import l313l
import asyncio
import re
from telethon import events

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
@l313l.on(events.NewMessage(pattern=r"^\.العب(?: (\d+))?$"))
async def play_command(event):
    # الحصول على الرقم المدخل بعد الأمر .العب أو ضبط القيمة الافتراضية على 1
    number = int(event.pattern_match.group(1)) if event.pattern_match.group(1) else 1

    # أرسل الكلمة "كلمات" كإشارة للبداية
    await event.respond("كلمات")

    # عداد لاستقبال الرسائل
    counter = 0

    # بدء مراقبة الرسائل داخل حلقة
    async for new_event in l313l.iter_messages(event.chat_id, from_user=1421907917):
        if counter >= number:
            break  # التوقف عند استكمال العدد المطلوب من الرسائل

        # محاولة استخراج الكلمة بين الأقواس بعد ↢
        try:
            word_match = re.search(r"↢ \((.*?)\)", new_event.text)
            if word_match:
                word = word_match.group(1)
                await event.respond(f"الكلمة ↢ « {word} »")
            else:
                await event.respond("⌔∮ لم أتمكن من استخراج الكلمة بين الأقواس ⚠️")
        except Exception as e:
            await event.respond(f"⌔∮ حدث خطأ أثناء معالجة الرسالة: {str(e)} ⚠️")

        # زيادة العداد
        counter += 1
