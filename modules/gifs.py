# by @dently

import random
from .. import loader, utils 
 
@loader.tds 
class GifssMod(loader.Module): 
    """ 
Модуль Gifs — поиск гифок
    """ 
    strings = {"name": "Gifs"} 
 
    async def gifcmd(self, message): 
        """.gif <название>, чтобы найти гифку по названию""" 
        args = utils.get_args_raw(message) 
        k = random.randint(0, 6)
        reply = await message.get_reply_message() 
        if not args: 
            return await message.edit("<b>[Gifs] Нету аргументов</b>")  
        try: 
            music = await message.client.inline_query('gif', args) 
            await message.delete() 
            await message.client.send_file(message.to_id, music[k].result.media, reply_to=reply.id if reply else None) 
        except: return await message.client.send_message(message.chat_id, f"<b>[Gifs] Гифка с названием <code>{args}</code> не найдена</b>")
