# by @dently

from .. import loader, utils 
from telethon import functions 
from telethon.tl.functions.contacts import BlockRequest 
from telethon.tl.functions.messages import ReportSpamRequest 
 

@loader.tds 
class UnBlockNaxyiMod(loader.Module): 
    """Помощь для AutoBlackList""" 
    strings={"name": "UnBlock"} 
 
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
            await message.client(functions.contacts.DeleteContactRequest(id=user.id))
            await message.edit(f"<b><a href='tg://user?id={user.id}'>{user.first_name}</a> добавлен в список AutoBlackList</b>") 
        except: return await message.edit("<b>Даун, что-то пошло по пизде</b>")
