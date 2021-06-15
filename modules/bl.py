# by @dently

from .. import loader, utils 
from telethon.tl.functions.contacts import BlockRequest 
from telethon.tl.functions.messages import ReportSpamRequest 
from .. import loader, utils 
from telethon import functions 
 
 
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
            return await message.edit("<b>[AutoBlackList] Активирован!</b>") 
     
        if autobl == False: 
            self.db.set("AutoBlackList", "status", True) 
            self.db.set("AutoBlackList", "message", "") 
            return await message.edit("<b>[AutoBlackList] Активирован!</b>") 
        self.db.set("AutoBlackList", "status", False) 
        return await message.edit("<b>[AutoBlackList] Деактивирован!</b>") 
 
 
    async def autoblstatuscmd(self, message): 
        """Проверить статус AutoBlackList""" 
        await message.edit(f"<b>[AutoBlackList - Status]</b>\n\n" 
                           f"<b>Кидать в ЧС</b> - {self.db.get('AutoBlackList', 'status')}\n" 
                           f"<b>Удалять чаты</b> - {self.db.get('AutoBlackList', 'delchat')}") 
 
 
    async def autodelchatcmd(self, message): 
        """Автоматически удаляет диалог после того, как кинет в ЧС""" 
        autodel = self.db.get("AutoBlackList", "delchat", False) 
        if autodel == False: 
            self.db.set("AutoBlackList", "delchat", True) 
            return await message.edit("<b>[AutoBlackList • DelChat] Активирован!</b>") 
        self.db.set("AutoBlackList", "delchat", False) 
        return await message.edit("<b>[AutoBlackList • DelChat] Деактивирован!</b>") 
 
    async def unblockcmd(self, message): 
  """Удалить юзера с списка"""
        args = utils.get_args_raw(message) 
        reply = await message.get_reply_message() 
        if not reply: 
            return await message.edit("<b>Даун, а где реплай?</b>") 
        else: 
            user = await message.client.get_entity(reply.sender_id) 
        try: 
            await message.client(functions.contacts.AddContactRequest(id=user.id,  
                                                                      first_name=user.first_name, 
                                                                      last_name=' ', 
                                                                      phone='мобила', 
                                                                      add_phone_privacy_exception=False)) 
            await message.edit(f"<b><a href='tg://user?id={user.id}'>{user.first_name}</a> удален из списка AutoBlackList</b>") 
        except: return await message.edit("<b>Даун, что-то пошло по пизде</b>")

    async def blockcmd(self, message): 
  """Добавить юзера в список"""
        args = utils.get_args_raw(message) 
        reply = await message.get_reply_message() 
        if not reply: 
            return await message.edit("<b>Даун, а где реплай?</b>") 
        else: 
            user = await message.client.get_entity(reply.sender_id) 
        try: 
            await message.client(BlockRequest(user.id)) 
            await message.client(ReportSpamRequest(user.id)) 
            await message.edit(f"<b><a href='tg://user?id={user.id}'>{user.first_name}</a> добавлен в список AutoBlackList</b>") 
        except: return await message.edit("<b>Даун, что-то пошло по пизде</b>")

    async def watcher(self, message): 
        """Вау, это watcher, я что-то смог из него сделать. Поздравьте меня)""" 
        try: 
            if message.sender_id == (await message.client.get_me()).id: return 
            if self.db.get("AutoBlackList", "status", True): 
                if message.is_private and message.sender_id != 777000: 
                    user = await message.client.get_entity(message.chat_id) 
                    if user.contact == False and user.bot == False: 
                        await message.client(BlockRequest(message.chat_id)) 
                        await message.client(ReportSpamRequest(message.chat_id)) 
                        if self.db.get("AutoBlackList", "delchat") == True: 
                            await message.client.delete_dialog(message.chat_id) 
        except (AttributeError, TypeError): pass
