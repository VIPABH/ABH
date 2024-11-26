import random
from telethon import events
import random, re

from JoKeRUB.utils import admin_cmd

import asyncio
from JoKeRUB import l313l

from ..core.managers import edit_or_reply

plugin_category = "extra"

@l313l.ar_cmd(incoming=True, func=lambda e: "rich" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("غني")
    else:
        pass
    
@l313l.ar_cmd(incoming=True, func=lambda e: "calm" in e.text.lower(), edited=False)
async def reply_salam(event):

    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("هدوء")
    else:
        pass
@l313l.ar_cmd(incoming=True, func=lambda e: "joke" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("نكتة")
    else:
        pass
@l313l.ar_cmd(incoming=True, func=lambda e: "law" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("قانون")
    else:
        pass
@l313l.ar_cmd(incoming=True, func=lambda e: "young" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("صغير")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "hotel" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("فندق")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "coat" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("معطف")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "how" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("كيف")
    else:
        pass
@l313l.ar_cmd(incoming=True, func=lambda e: "donate" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("تبرع")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "angry" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("غاضب")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "tea" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("شاي")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "brake" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("فرامل")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "always" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("دائما")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "diet" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("حمية")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "common" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("شائع")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "because" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("لان")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "photograph" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("صورة")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "idea" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("فكره")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "Rude" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("وقح")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "empty" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("فارغ")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "dirty" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("وصخ")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "anarchy" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("فوضى")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "carefully" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("بحذر")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "weak" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("ضعيف")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "Lawyer" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("محامي")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "sheep" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("خروف")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "way" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("طريق")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "notebook" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("دفتر ملاحظات")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "embarrassed" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("محرج")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "scream" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("صراخ")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "live" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("حي")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "Bored" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("ملل")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "free" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("حر")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "fact" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("حقيقة")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "Face" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("وجه")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "place" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("مكان")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "Happy" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("سعيد")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "Worried" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("قلق")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "Cap" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("قبعة")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "winter" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("شتاء")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "smart" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("ذكي")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "electric" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("كهربائي")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "under" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("تحت")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "round" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("جولة")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "sorry" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("اسف")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "Actor" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("ممثل")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "social" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("هنا")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "newspaper" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("جريدة")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "fish" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("سمكة")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "outside" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("خارج")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "note" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("ملاحظه")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "behind" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("خلف")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "pretty" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("جميل")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "difficult" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("صعب")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "queen" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("ملكة")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "Uncle" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("عم")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "hat" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("قبعة")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "Director" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("مخرج")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "solution" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("حل")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "future" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("مستقبل")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "Music" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("موسيقى")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "Producer" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("منتج")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "history" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("تاريخ")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "Sensitive" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("حساس")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "Mechanic" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("ميكانيكي")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "far" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("بعيد")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "mug" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("كوب")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "airport" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("مطار")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "season" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("فصل")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "student" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("طالب")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "simple" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("بسيط")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "different" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("مختلف")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "Partner" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("شريك")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "Funny" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("مضحك")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "Designer" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("مصمم")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "grass" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("عشب")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "husband" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("زوج")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "correct" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("صحيح")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "clean" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("نظيف")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "quick" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("سريع")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "yet" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("بعد")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "Gloves" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("قفازات")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "enough" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("يكفي")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "life" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("حياة")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "situation" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("موقف")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "modern" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("حديث")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "Father" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("اب")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "Cook" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("طباخ")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "book" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("كتاب")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "Dress" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("فستان")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "Sensitive" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("حساس")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "ugly" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("قبيح")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "name" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("اسم")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "Crazy" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("مجنون")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "broken" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("مكسور")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "sure" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("متأكد")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "Sad" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("حزين")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "salt" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("ملح")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "breakfast" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("فطور")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "key" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("مفتاح")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "Singer" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("مغني")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "door" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("باب")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "global" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("عالمي")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "writing" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("كتابه")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "bed" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("سرير")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "sofa" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("كنبه")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "cat" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("قطة")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "good" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("جيد")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "sun" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("شمس")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "summer" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("صيف")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "Car" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("سيارة")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "send" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("ارسال")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "earth" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("ارض")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "Leg" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("ساق")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "Disappointed" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("خائب الامل")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "Clerk" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("كاتب")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "dangerous" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("خطر")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "window" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("نافذة")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "bath" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("حمام")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "snow" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("ثلج")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "voice" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("صوت")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "sell" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("بيع")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "Engineer" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("مهندس")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "Child" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("طفل")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "best" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("الافضل")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "character" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("شخصيه")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "holiday" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("عطله")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "Grandfather" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("جد")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "Translator" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("مترجم")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "Actor" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("ممثل")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "spicy" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("حار")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "impossible" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("مستحيل")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "Honey" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("عسل")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "hobby" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("هواية")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "Music" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("موسيقى")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "village" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("قرية")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "Dress" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("فستان")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "Eye" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("عين")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "Talented" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("موهوب")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "high" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("مرتفع")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "Shoes" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("حذاء")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "Detective" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("محقق")
    else:
        pass
