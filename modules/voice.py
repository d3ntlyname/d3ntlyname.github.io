# by @dently

from .. import loader, utils 
from telethon import events 
from telethon.errors.rpcerrorlist import YouBlockedUserError 
from asyncio.exceptions import TimeoutError 
 
 
def register(cb): 
    cb(VoiceEMod()) 
 
class VoiceEMod(loader.Module): 
    """Распознаёт текст с голосового сообщения""" 
    strings = {'name': 'Voice'} 
 
    async def voicecmd(self, message): 
        """.voice <реплай на войс>""" 
        try: 
            text = ""
            reply = await message.get_reply_message() 
            chat = "@voicybot" 
            if not reply: 
                await message.edit("<b>Ответь на войс!</b>") 
                return 
            if text: 
                async with message.client.conversation(chat) as conv: 
                    try: 
                        response = conv.wait_event(events.NewMessage(incoming=True, from_users=259276793)) 
                        await message.client.send_message(chat, reply) 
                        response = await response 
                        r = "<code>" + response.text + "</code>"
                        r = r.replace("При поддержке Бородач Клуба", "")
                    except YouBlockedUserError: 
                        await message.reply("<b>Сними <a href='tg://user?id=259276793'>Voicy</a> с ЧС</b>") 
                        return 
                    if not response.text: 
                        await message.edit("<b>Ошибка API :(</b>") 
                        return
                    await message.edit(r) 
            if reply: 
                async with message.client.conversation(chat) as conv: 
                    try: 
                        response = conv.wait_event(events.NewMessage(incoming=True, from_users=259276793)) 
                        await message.client.send_message(chat, reply) 
                        response = await response 
                        r = "<code>" + response.text + "</code>"
                        r = r.replace("При поддержке Бородач Клуба", "")
                    except YouBlockedUserError: 
                        await message.reply("<b>Сними <a href='tg://user?id=259276793'>Voicy</a> с ЧС</b>") 
                        return 
                    if not response.text: 
                        await message.edit("<b>Ошибка API :(</b>") 
                        return 
                    await message.edit(r) 
        except TimeoutError: 
            return await message.edit("<b>Ошибка API :(</b>")
