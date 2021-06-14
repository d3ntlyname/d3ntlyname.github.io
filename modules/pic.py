# by @dently

import random
from .. import loader, utils 
 
@loader.tds 
class SearchMusicMod(loader.Module): 
    """ 
Модуль SearchPic — поиск фотографий 
    """ 
    strings = {"name": "SearchPic"} 
 
    async def piccmd(self, message): 
        """.pic <название>, чтобы найти фотографию по названию""" 
        args = utils.get_args_raw(message) 
        k = random.randint(1, 5)
        reply = await message.get_reply_message() 
        if not args: 
            return await message.edit("<b>[SearchPic] Нету аргументов</b>")  
        try: 
            await message.edit("<b>[SearchPic] Загрузка...</b>") 
            music = await message.client.inline_query('pic', args) 
            await message.delete() 
            await message.client.send_file(message.to_id, music[k].result.photo, reply_to=reply.id if reply else None) 
        except: return await message.client.send_message(message.chat_id, f"<b>[SearchPic] Фотография с названием <code>{args}</code> не найдена</b>")
