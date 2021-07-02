# by @dently
from asyncio import sleep
from .. import loader, utils 
from telethon.tl.functions.contacts import BlockRequest, UnblockRequest
from telethon.tl.functions.messages import ReportSpamRequest 
 
 
def register(cb): 
    cb(AutoBlackListMod()) 
 
class AutoBlackListMod(loader.Module): 
    """Кидает всех неконтактов в чёрный список""" 
    strings = {'name': 'AutoBlackList'} 
 
    async def client_ready(self, client, db): 
        self.db = db 
     
    async def autoblcmd(self, message): 
        """Включить/выключить режим""" 
        args = utils.get_args_raw(message) 
        autobl = self.db.get("AutoBlackList", "status", False) 
        if args: 
            self.db.set("AutoBlackList", "status", True) 
            self.db.set("AutoBlackList", "message", str(args)) 
            return await message.edit("<b>[AutoBlackList]</b> Активирован!") 
     
        if autobl == False: 
            self.db.set("AutoBlackList", "status", True) 
            self.db.set("AutoBlackList", "message", "") 
            return await message.edit("<b>[PM=BL] > Активирован!</b>") 
        self.db.set("AutoBlackList", "status", False) 
        return await message.edit("<b>[PM=BL] > Деактивирован!</b>") 
 
 
    async def autoblstatuscmd(self, message): 
        """Проверить статус AutoBlackList""" 
        await message.edit(f"<b>[PM=BL]</b>\n\n" 
                           f"<b>Кидать в BL</b> - {self.db.get('AutoBlackList', 'status')}\n" 
                           f"<b>Удалять чаты</b> - {self.db.get('AutoBlackList', 'delchat')}") 
 
 
    async def autodelchatcmd(self, message): 
        """Автоматически удаляет диалог после того, как кинет в чёрный список""" 
        autodel = self.db.get("AutoBlackList", "delchat", False) 
        if autodel == False: 
            self.db.set("AutoBlackList", "delchat", True) 
            return await message.edit("<b>[AutoBlackList Mode - DelChat]</b> Активирован!") 
        self.db.set("AutoBlackList", "delchat", False) 
        return await message.edit("<b>[AutoBlackList Mode - DelChat]</b> Деактивирован!") 
 
 
    async def watcher(self, message): 
        """Вау, это watcher, я что-то смог из него сделать. Поздравьте меня)""" 
        try: 
            if message.sender_id == (await message.client.get_me()).id: return 
            if self.db.get("AutoBlackList", "status", True): 
                if message.is_private and message.sender_id != 777000: 
                    user = await message.client.get_entity(message.chat_id) 
                    if user.contact == False and user.bot == False: 
                        await message.client(BlockRequest(message.chat_id)) 
                        sleep(1)
                        await message.client(UnblockRequest(message.chat_id))
                        if self.db.get("AutoBlackList", "delchat") == True: 
                            await message.client.delete_dialog(message.chat_id) 
        except (AttributeError, TypeError): pass
