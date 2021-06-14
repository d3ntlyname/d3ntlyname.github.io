# by @dently

from .. import loader, utils 
 
@loader.tds 
class SearchMusicMod(loader.Module): 
    """
Модуль FindMusic - поиск музыки
Работает через бота @lybot, @vkm_bot и @muzyka_tiktok_bot 
    """ 
    strings = {"name": "FindMusic"} 
 
    async def ysmcmd(self, message): 
        """Используй: .ytm <название>, чтобы найти музыку по названию""" 
        args = utils.get_args_raw(message) 
        reply = await message.get_reply_message() 
        if not args: 
            return await message.edit("<b>[FindMusic] Нету аргументов...</b>")  
        try: 
            await message.edit("<b>[FindMusic] Загрузка...</b>") 
            music = await message.client.inline_query('lybot', args) 
            await message.delete() 
            await message.client.send_file(message.to_id, music[0].result.document, reply_to=reply.id if reply else None) 
        except: return await message.client.send_message(message.chat_id, f"<b>[FindMusic] Музыка с названием <code>{args}</code> не найдена...</b>")

    async def vkmcmd(self, message): 
        """Используй: .vkm <название>, чтобы найти музыку по названию""" 
        args = utils.get_args_raw(message) 
        reply = await message.get_reply_message() 
        if not args: 
            return await message.edit("<b>[FindMusic] Нету аргументов...</b>")  
        try: 
            await message.edit("<b>[FindMusic] Загрузка...</b>") 
            music = await message.client.inline_query('vkm_bot', args) 
            await message.delete() 
            await message.client.send_file(message.to_id, music[0].result.document, reply_to=reply.id if reply else None) 
        except: return await message.client.send_message(message.chat_id, f"<b>[FindMusic] Музыка с названием <code>{args}</code> не найдена...</b>")

    async def jrmcmd(self, message): 
        """Используй: .ttm <название>, чтобы найти музыку по названию""" 
        args = utils.get_args_raw(message) 
        reply = await message.get_reply_message() 
        if not args: 
            return await message.edit("<b>[FindMusic] Нету аргументов...</b>")  
        try: 
            await message.edit("<b>[FindMusic] Загрузка...</b>") 
            music = await message.client.inline_query('muzyka_tiktok_bot', args) 
            await message.delete() 
            await message.client.send_file(message.to_id, music[0].result.document, reply_to=reply.id if reply else None) 
        except: return await message.client.send_message(message.chat_id, f"<b>[FindMusic] Музыка с названием <code>{args}</code> не найдена...</b>")
