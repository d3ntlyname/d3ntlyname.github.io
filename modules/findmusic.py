# by @dently

from .. import loader, utils 
import random
 
@loader.tds 
class SearchMusicMod(loader.Module): 
    """
Модуль FindMusic — поиск музыки
    """ 
    strings = {"name": "FindMusic"} 
 
    async def ytmcmd(self, message): 
        """.ytm <название>, чтобы найти музыку по названию в YouTube""" 
        args = utils.get_args_raw(message) 
        reply = await message.get_reply_message() 
        if not args: 
            return await message.edit("<b>[FindMusic] Нету аргументов</b>")  
        try: 
            await message.edit("<b>[FindMusic] Загрузка...</b>") 
            music = await message.client.inline_query('lybot', args) 
            await message.delete() 
            await message.client.send_file(message.to_id, music[0].result.document, reply_to=reply.id if reply else None) 
        except: return await message.client.send_message(message.chat_id, f"<b>[FindMusic] Музыка с названием <code>{args}</code> не найдена</b>")

    async def vkmcmd(self, message): 
        """.vkm <название>, чтобы найти музыку по названию в ВКонтакте""" 
        args = utils.get_args_raw(message) 
        g = random.randint(1, 5)
        reply = await message.get_reply_message() 
        if not args: 
            return await message.edit("<b>[FindMusic] Нету аргументов</b>")  
        try: 
            await message.edit("<b>[FindMusic] Загрузка...</b>") 
            music = await message.client.inline_query('vkm_bot', args) 
            await message.delete() 
            await message.client.send_file(message.to_id, music[g].result.document, reply_to=reply.id if reply else None) 
        except: return await message.client.send_message(message.chat_id, f"<b>[FindMusic] Музыка с названием <code>{args}</code> не найдена</b>")

    async def ttmcmd(self, message): 
        """.ttm <название>, чтобы найти музыку по названию в TikTok""" 
        args = utils.get_args_raw(message) 
        reply = await message.get_reply_message() 
        if not args: 
            return await message.edit("<b>[FindMusic] Нету аргументов</b>")  
        try: 
            await message.edit("<b>[FindMusic] Загрузка...</b>") 
            music = await message.client.inline_query('muzyka_tiktok_bot', args) 
            await message.delete() 
            await message.client.send_file(message.to_id, music[0].result.document, reply_to=reply.id if reply else None) 
        except: return await message.client.send_message(message.chat_id, f"<b>[FindMusic] Музыка с названием <code>{args}</code> не найдена</b>")
