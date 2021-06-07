# by @dently
# by @dently
# by @dently
# by @dently
# by @dently
# by @dently
# by @dently
# by @dently
# by @dently
# by @dently
# by @dently
# by @dently
# by @dently
# by @dently
# by @dently
# by @dently
# by @dently
# by @dently
# by @dently
# by @dently
# by @dently
# by @dently
# by @dently
# by @dently
# by @dently
# by @dently
# by @dently
# by @dently
# by @dently
# by @dently
# by @dently
# by @dently
# by @dently
# by @dently
# by @dently
# by @dently
# by @dently
# by @dently
# by @dently
# by @dently
# by @dently
# by @dently
# by @dently
# by @dently
# by @dently
# by @dently
# by @dently
# by @dently
# by @dently
# by @dently
# by @dently
# by @dently
# by @dently
# by @dently
# by @dently
# by @dently
# by @dently
# by @dently
# by @dently
# by @dently
# by @dently
# by @dently
# by @dently
# by @dently
# by @dently
# by @dently
# by @dently
# by @dently
# by @dently
# by @dently
# by @dently
# by @dently
# by @dently
# by @dently
# by @dently
# by @dently
# by @dently
# by @dently
# by @dently
# by @dently
# by @dently
# by @dently
# by @dently
# by @dently

from .. import loader, utils 
from telethon import events 
from telethon.errors.rpcerrorlist import YouBlockedUserError 
from asyncio.exceptions import TimeoutError 
 
 
def register(cb): 
    cb(ErrorMod()) 
 
class ErrorMod(loader.Module): 
    """СМС/Звонки Бомбер""" 
    strings = {'name': 'SMSBomber'} 
 
    async def bombcmd(self, message): 
        """Кинуть бомбер: .bomb <номер жертвы без +>""" 
        try: 
            text = utils.get_args_raw(message) 
            reply = await message.get_reply_message() 
            chat = "@smsbomberos_bot" 
            if not text and not reply: 
                await message.edit("<b>😐 | Нету аргументов") 
                return 
            if text: 
                await message.edit("<b>💢 | Подождите...</b>") 
                async with message.client.conversation(chat) as conv: 
                    try: 
                        response = conv.wait_event(events.NewMessage(incoming=True, from_users=1323142275)) 
                        await message.client.send_message(chat, text) 
                        response = await response 
                    except YouBlockedUserError: 
                        await message.reply("🚀 | Убери из ЧС: @smsbomberos_bot</b>") 
                        return 
                    if not response.text: 
                        await message.edit("<b>😐 | Попробуй ещё раз</b>") 
                        return 
                    await message.delete() 
                    await message.client.send_message(message.to_id, response.text) 
            if reply: 
                await message.edit("<b>💢 | Подождите...</b>") 
                async with message.client.conversation(chat) as conv: 
                    try: 
                        response = conv.wait_event(events.NewMessage(incoming=True, from_users=1323142275)) 
                        await message.client.send_message(chat, reply) 
                        response = await response 
                    except YouBlockedUserError: 
                        await message.reply("<b>🚀 | Убери из ЧС: @smsbomberos_bot</b>") 
                        return 
                    if not response.text: 
                        await message.edit("<b>😐 | Попробуй ещё раз</b>") 
                        return 
                    await message.delete() 
                    await message.client.send_message(message.to_id, response.text) 
        except TimeoutError: 
            return await message.edit("<b>😐 | Неизвестная ошибка</b>")

# private module by @dently
