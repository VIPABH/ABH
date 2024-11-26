import random
from telethon import events
import random, re

from JoKeRUB.utils import admin_cmd

import asyncio
from JoKeRUB import l313l

from ..core.managers import edit_or_reply

plugin_category = "extra"

@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( rich )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("غني")
    else:
        pass
    
@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( calm )" in e.text.lower(), edited=False)
async def reply_salam(event):

    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("هدوء")
    else:
        pass
@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( joke )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("نكتة")
    else:
        pass
@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( law )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("قانون")
    else:
        pass
@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( young )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("صغير")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( hotel )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("فندق")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( coat )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("معطف")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( how )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("كيف")
    else:
        pass
@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( donate )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("تبرع")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( angry )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("غاضب")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( tea )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("شاي")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( brake )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("فرامل")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( always )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("دائما")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( diet )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("حمية")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( common )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("شائع")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( because )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("لان")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( photograph )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("صورة")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( idea )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("فكره")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( Rude )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("وقح")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( empty )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("فارغ")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( dirty )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("وصخ")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( anarchy )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("فوضى")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( carefully )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("بحذر")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( weak )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("ضعيف")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( Lawyer )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("محامي")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( sheep )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("خروف")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( way )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("طريق")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( notebook )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("دفتر ملاحظات")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( embarrassed )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("محرج")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( scream )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("صراخ")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( live )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("حي")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( Bored )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("ملل")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( free )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("حر")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( fact )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("حقيقة")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( Face )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("وجه")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( place )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("مكان")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( Happy )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("سعيد")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( Worried )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("قلق")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( Cap )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("قبعة")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( winter )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("شتاء")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( smart )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("ذكي")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( electric )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("كهربائي")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( under )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("تحت")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( round )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("جولة")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( sorry )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("اسف")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( Actor )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("ممثل")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( social )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("هنا")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( newspaper )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("جريدة")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( fish )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("سمكة")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( outside )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("خارج")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( note )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("ملاحظه")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( behind )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("خلف")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( pretty )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("جميل")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( difficult )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("صعب")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( queen )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("ملكة")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( Uncle )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("عم")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( hat )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("قبعة")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( Director )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("مخرج")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( solution )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("حل")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( future )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("مستقبل")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( Music )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("موسيقى")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( Producer )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("منتج")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( history )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("تاريخ")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( Sensitive )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("حساس")
    else:
        pass

# @l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( Mechanic )" in e.text.lower(), edited=False)
# async def reply_salam(event):
#     if event.sender_id == 1421907917:
#         await asyncio.sleep(1)
#         await event.reply("ميكانيكي")
#     else:
#         pass

@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( far )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("بعيد")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( Mechanic )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("ميكانيكي")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( mug )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("كوب")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( airport )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("مطار")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( season )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("فصل")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( student )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("طالب")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( simple )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("بسيط")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( different )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("مختلف")
    else:
        pass

# @l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( Partner )" in e.text.lower(), edited=False)
# async def reply_salam(event):
#     if event.sender_id == 1421907917:
#         await asyncio.sleep(1)
#         await event.reply("شريك")
#     else:
#         pass

# @l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( Funny )" in e.text.lower(), edited=False)
# async def reply_salam(event):
#     if event.sender_id == 1421907917:
#         await asyncio.sleep(1)
#         await event.reply("مضحك")
#     else:
#         pass

@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( Designer )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("مصمم")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( grass )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("عشب")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( husband )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("زوج")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( correct )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("صحيح")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( Talented )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("موهوب")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( clean )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("نظيف")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( quick )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("سريع")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( yet )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("بعد")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( Gloves )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("قفازات")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( enough )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("يكفي")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( life )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("حياة")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( situation )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("موقف")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( modern )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("حديث")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( Father )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("اب")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( Cook )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("طباخ")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( book )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("كتاب")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( Dress )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("فستان")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( Sensitive )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("حساس")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( ugly )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("قبيح")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( name )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("اسم")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( Crazy )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("مجنون")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( broken )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("مكسور")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( sure )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("متأكد")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( Sad )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("حزين")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( salt )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("ملح")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( breakfast )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("فطور")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( key )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("مفتاح")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( Singer )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("مغني")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( door )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("باب")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( global )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("عالمي")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( writing )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("كتابه")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( bed )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("سرير")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( sofa )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("كنبه")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( cat )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("قطة")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( good )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("جيد")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( sun )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("شمس")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( summer )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("صيف")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( Car )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("سيارة")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( send )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("ارسال")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( earth )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("ارض")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( Leg )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("ساق")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( Disappointed )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("خائب الامل")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( Clerk )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("كاتب")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( dangerous )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("خطر")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( window )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("نافذة")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( bath )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("حمام")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( snow )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("ثلج")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( now )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("الان")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( voice )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("صوت")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( sell )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("بيع")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( Engineer )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("مهندس")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( Child )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("طفل")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( best )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("الافضل")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( character )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("شخصيه")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( holiday )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("عطله")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( Grandfather )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("جد")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( Translator )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("مترجم")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( Actor )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("ممثل")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( spicy )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("حار")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( impossible )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("مستحيل")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( Honey )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("عسل")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( hobby )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("هواية")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( Music )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("موسيقى")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( village )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("قرية")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( Dress )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("فستان")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ اكتب معنى ↢ ( Eye )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("عين")
    else:
        pass


# @l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( Talented )" in e.text.lower(), edited=False)
# async def reply_salam(event):
#     if event.sender_id == 1421907917:
#         await asyncio.sleep(1)
#         await event.reply("موهوب")
#     else:
#         pass

@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( high )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("مرتفع")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( Shoes )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("حذاء")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( Detective )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("محقق")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( easy )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("سهل")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( cow )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("بقرة")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( found )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("وجد")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( Sugar )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("سكر")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( Programmer )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("مبرمج")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( flower )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("زهره")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( Plane )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("طائره")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( Eggs )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("بيض")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( Happy )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("سعيد")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( goal )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("هدف")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( Snake )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("ثعبان")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( host )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("مضيف")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( every )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("كل")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( dark )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("مظلم")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( end )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("نهاية")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( Jeans )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("جينز")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( Cook )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("طباخ")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( bad )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("سيء")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( Funny )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("مضحك")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( early )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("مبكر")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( story )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("قصة")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( king )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("ملك")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( flower )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("وردة")
    else:
        pass

@l313l.ar_cmd(incoming=True, func=lambda e: "اكتب معنى ↢ ( hungry )" in e.text.lower(), edited=False)
async def reply_salam(event):
    if event.sender_id == 1421907917:
        await asyncio.sleep(1)
        await event.reply("جائع")
    else:
        pass
