# by @dently

from .. import loader, utils 
from telethon import events 
from telethon.errors.rpcerrorlist import YouBlockedUserError 
from asyncio.exceptions import TimeoutError 
 
 
def register(cb): 
    cb(TextagramMod()) 
 
class TextagramMod(loader.Module): 
    """Изменяет шрифт текста""" 
    strings = {'name': 'Textagram'} 
 
    async def textcmd(self, message): 
        """Изменяет шрифт текста .text <текст>""" 
        try: 
            text = utils.get_args_raw(message) 
            reply = await message.get_reply_message() 
            chat = "@textagrambot" 
            if not text and not reply: 
                await message.edit("<b>Пожалуйста, пришлите текст для обработки</b>") 
                return 
            if text: 
                async with message.client.conversation(chat) as conv: 
                    try: 
                        response = conv.wait_event(events.NewMessage(incoming=True, from_users=767253642)) 
                        await message.client.send_message(chat, text) 
                        await message.client.delete_dialog(767253642)
                        response = await response 
                    except YouBlockedUserError: 
                        await message.reply("<b>Сними <a href='tg://user?id=767253642'>Textagram</a> с чс</b>") 
                        return 
                    if not response.text: 
                        await message.edit("<b>Попробуй ещё раз</b>") 
                        return 
                    await message.delete() 
                    await message.client.send_message(message.to_id, response.text) 
            if reply: 
                async with message.client.conversation(chat) as conv: 
                    try: 
                        response = conv.wait_event(events.NewMessage(incoming=True, from_users=767253642)) 
                        await message.client.send_message(chat, reply) 
                        await message.client.delete_dialog(767253642)
                        response = await response 
                    except YouBlockedUserError: 
                        await message.reply("<b>Сними <a href='tg://user?id=767253642'>Textagram</a> с чс</b>") 
                        return 
                    if not response.text: 
                        await message.edit("<b>Попробуй ещё раз</b>") 
                        return 
                    await message.delete() 
                    await message.client.send_message(message.to_id, response.text) 
        except TimeoutError: 
            return await message.edit("<b>Неизвестная ошибка</b>")
