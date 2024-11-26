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
        await event.reply("غني")
    else:
        pass
@l313l.ar_cmd(incoming=True, func=lambda e: "calm" in e.text.lower(), edited=False)
async def reply_salam(event):

    if event.sender_id == 1421907917:
        await event.reply("هدوء")
    else:
        pass
@l313l.ar_cmd(incoming=True, func=lambda e: "joke" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await event.reply("نكتة")
    else:
        pass
@l313l.ar_cmd(incoming=True, func=lambda e: "law" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await event.reply("قانون")
    else:
        pass
@l313l.ar_cmd(incoming=True, func=lambda e: "young" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await event.reply("صغير")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "hotel" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await event.reply("فندق")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "coat" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await event.reply("معطف")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "how" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await event.reply("كيف")
    else:
        pass
@l313l.ar_cmd(incoming=True, func=lambda e: "donate" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await event.reply("تبرع")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "angry" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await event.reply("غاضب")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "tea" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await event.reply("شاي")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "brake" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await event.reply("فرامل")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "always" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await event.reply("دائما")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "diet" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await event.reply("حمية")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "common" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await event.reply("شائع")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "because" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await event.reply("لان")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "photograph" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await event.reply("صورة")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "idea" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await event.reply("فكره")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "Rude" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await event.reply("وقح")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "empty" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await event.reply("فارغ")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "dirty" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await event.reply("وصخ")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "anarchy" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await event.reply("فوضى")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "carefully" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await event.reply("بحذر")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "weak" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await event.reply("ضعيف")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "Lawyer" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await event.reply("محامي")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "sheep" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await event.reply("خروف")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "way" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await event.reply("طريق")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "notebook" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await event.reply("دفتر ملاحظات")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "embarrassed" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await event.reply("محرج")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "scream" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await event.reply("صراخ")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "live" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await event.reply("حي")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "Bored" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await event.reply("ملل")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "free" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await event.reply("حر")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "fact" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await event.reply("حقيقة")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "Face" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await event.reply("وجه")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "place" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await event.reply("مكان")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "Happy" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await event.reply("سعيد")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "Worried" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await event.reply("قلق")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "Cap" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await event.reply("قبعة")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "winter" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await event.reply("شتاء")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "smart" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await event.reply("ذكي")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "electric" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await event.reply("كهربائي")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "under" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await event.reply("تحت")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "round" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await event.reply("جولة")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "sorry" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await event.reply("اسف")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "Actor" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await event.reply("ممثل")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "social" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await event.reply("هنا")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "newspaper" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await event.reply("جريدة")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "fish" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await event.reply("سمكة")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "outside" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await event.reply("خارج")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "note" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await event.reply("ملاحظه")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "behind" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await event.reply("خلف")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "pretty" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await event.reply("جميل")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "difficult" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await event.reply("صعب")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "queen" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await event.reply("ملكة")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "Uncle" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await event.reply("عم")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "hat" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await event.reply("قبعة")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "Director" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await event.reply("مخرج")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "solution" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await event.reply("حل")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "future" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await event.reply("مستقبل")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "Music" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await event.reply("موسيقى")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "Producer" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await event.reply("منتج")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "history" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await event.reply("تاريخ")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "Sensitive" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await event.reply("حساس")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "Mechanic" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await event.reply("ميكانيكي")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "far" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await event.reply("بعيد")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "mug" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await event.reply("كوب")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "airport" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await event.reply("مطار")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "season" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await event.reply("فصل")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "student" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await event.reply("طالب")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "simple" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await event.reply("طالب")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "different" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await event.reply("مختلف")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "Partner" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await event.reply("شريك")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "Funny" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await event.reply("مضحك")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "Designer" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await event.reply("مصمم")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "grass" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await event.reply("عشب")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "husband" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await event.reply("زوج")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "correct" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await event.reply("صحيح")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "clean" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await event.reply("نظيف")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "quick" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await event.reply("سريع")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "yet" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await event.reply("بعد")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "Gloves" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await event.reply("قفازات")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "enough" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await event.reply("يكفي")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "Head" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await event.reply("راس")
    else:
        pass
