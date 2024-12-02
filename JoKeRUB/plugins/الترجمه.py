from asyncio import sleep
import requests
import json
from JoKeRUB.helpers.functions.functions import translate
from JoKeRUB import l313l
from telethon import events, types
from ..sql_helper.globals import addgvar, delgvar, gvarstatus
from ..core.managers import edit_delete, edit_or_reply
from ..helpers.functions import soft_deEmojify

trans = {
    'af': 'afrikaans',
    'sq': 'albanian',
    'am': 'amharic',
    'ar': 'arabic',
    'hy': 'armenian',
    'az': 'azerbaijani',
    'eu': 'basque',
    'be': 'belarusian',
    'bn': 'bengali',
    'bs': 'bosnian',
    'bg': 'bulgarian',
    'ca': 'catalan',
    'ceb': 'cebuano',
    'ny': 'chichewa',
    'zh-cn': 'chinese (simplified)',
    'zh-tw': 'chinese (traditional)',
    'co': 'corsican',
    'hr': 'croatian',
    'cs': 'czech',
    'da': 'danish',
    'nl': 'dutch',
    'en': 'english',
    'eo': 'esperanto',
    'et': 'estonian',
    'tl': 'filipino',
    'fi': 'finnish',
    'fr': 'french',
    'fy': 'frisian',
    'gl': 'galician',
    'ka': 'georgian',
    'de': 'german',
    'el': 'greek',
    'gu': 'gujarati',
    'ht': 'haitian creole',
    'ha': 'hausa',
    'haw': 'hawaiian',
    'iw': 'hebrew',
    'he': 'hebrew',
    'hi': 'hindi',
    'hmn': 'hmong',
    'hu': 'hungarian',
    'is': 'icelandic',
    'ig': 'igbo',
    'id': 'indonesian',
    'ga': 'irish',
    'it': 'italian',
    'ja': 'japanese',
    'jw': 'javanese',
    'kn': 'kannada',
    'kk': 'kazakh',
    'km': 'khmer',
    'ko': 'korean',
    'ku': 'kurdish (kurmanji)',
    'ky': 'kyrgyz',
    'lo': 'lao',
    'la': 'latin',
    'lv': 'latvian',
    'lt': 'lithuanian',
    'lb': 'luxembourgish',
    'mk': 'macedonian',
    'mg': 'malagasy',
    'ms': 'malay',
    'ml': 'malayalam',
    'mt': 'maltese',
    'mi': 'maori',
    'mr': 'marathi',
    'mn': 'mongolian',
    'my': 'myanmar (burmese)',
    'ne': 'nepali',
    'no': 'norwegian',
    'or': 'odia',
    'ps': 'pashto',
    'fa': 'persian',
    'pl': 'polish',
    'pt': 'portuguese',
    'pa': 'punjabi',
    'ro': 'romanian',
    'ru': 'russian',
    'sm': 'samoan',
    'gd': 'scots gaelic',
    'sr': 'serbian',
    'st': 'sesotho',
    'sn': 'shona',
    'sd': 'sindhi',
    'si': 'sinhala',
    'sk': 'slovak',
    'sl': 'slovenian',
    'so': 'somali',
    'es': 'spanish',
    'su': 'sundanese',
    'sw': 'swahili',
    'sv': 'swedish',
    'tg': 'tajik',
    'ta': 'tamil',
    'te': 'telugu',
    'th': 'thai',
    'tr': 'turkish',
    'uk': 'ukrainian',
    'ur': 'urdu',
    'ug': 'uyghur',
    'uz': 'uzbek',
    'vi': 'vietnamese',
    'cy': 'welsh',
    'xh': 'xhosa',
    'yi': 'yiddish',
    'yo': 'yoruba',
    'zu': 'zulu',
}

async def gtrans(text, lan):
    try:
        response = translate(text, lang_tgt=lan)
        if response == 400:
            return Flase
    except Exception as er:
        return f"حدث خطأ \n{er}"
    return response

@l313l.ar_cmd(
    pattern="ترجمة ([\s\S]*)",
    command=("ترجمة", "tools"),
    info={
        "header": "To translate the text to required language.",
        "note": "For langugage codes check [this link](https://bit.ly/2SRQ6WU)",
        "usage": [
            "{tr}tl <language code> ; <text>",
            "{tr}tl <language codes>",
        ],
        "examples": "{tr}tl te ; Catuserbot is one of the popular bot",
    },
)
async def _(event):
    "To translate the text."
    input_str = event.pattern_match.group(1)
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        text = previous_message.message
        lan = input_str or "en"
    elif ";" in input_str:
        lan, text = input_str.split(";")
    else:
        return await edit_delete(
            event, "** قم بالرد على الرسالة للترجمة **", time=5
        )
    text = soft_deEmojify(text.strip())
    lan = lan.strip()
    if len(text) < 2:
        return await edit_delete(event, "قم بكتابة ما تريد ترجمته!")
    try:
      
        output_str = f"**تمت الترجمة من ar الى {lan}**\
                \n`{trans}`"
        await edit_or_reply(event, output_str)
    except Exception as exc:
        await edit_delete(event, f"**خطا:**\n`{exc}`", time=5)


@l313l.ar_cmd(pattern="(الترجمة الفورية|الترجمه الفوريه|ايقاف الترجمة|ايقاف الترجمه)")
async def reda(event):
    if gvarstatus("transnow"):
        delgvar("transnow")
        await edit_delete(event, "**᯽︙ تم تعطيل الترجمه الفورية **")
    else:
        addgvar("transnow", "Reda") 
        await edit_delete(event, "**᯽︙ تم تفعيل الترجمه الفورية**")

@l313l.ar_cmd(pattern="لغة الترجمة")
async def Reda_is_Here(event):
    t = event.text.replace(".لغة الترجمة", "")
    t = t.replace(" ", "")
    try:  
        lang = langs[t]
    except BaseException as er:
        return await edit_delete(event, "**᯽︙ !تأكد من قائمة اللغات. لا يوجد هكذا لغة**")
    addgvar("translang", lang)
    await edit_delete(event, f"**᯽︙ تم تغير لغة الترجمة الى {lang} بنجاح ✓ **")

# Reda
@l313l.on(events.NewMessage(outgoing=True))
async def reda(event):
    if gvarstatus("transnow"):
        if event.media or isinstance(event.media, types.MessageMediaDocument) or isinstance(event.media, types.MessageMediaInvoice):
            print ("JoKeRUB")
        else:
            original_message = event.message.message
            translated_message = await gtrans(soft_deEmojify(original_message.strip()), gvarstatus("translang") or "en")
            await event.message.edit(translated_message)
