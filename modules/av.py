from .. import loader, utils
from telethon import events
import io 

@loader.tds
class AVMod(loader.Module):
 """Максимально простой антивирус проверяющий модули на код, который может удалить аккаунт"""
 strings = {'name': 'MicroAC'}

 async def avcmd(self, message):
  """.av <реплай на файл>"""
  reply = await message.get_reply_message()
  if not reply or not reply.file:
   await message.edit("<b>Ответь на файл!</b>")
   return
  text = await reply.download_media(bytes)
  text = str(text, "utf8")
  chat = 1898472077
  async with message.client.conversation(chat) as conv: 
   res = conv.wait_event(events.NewMessage(incoming=True, from_users=1898472077))
   await message.client.send_message(chat, text)
   res = await res
   await message.edit(res.text)
