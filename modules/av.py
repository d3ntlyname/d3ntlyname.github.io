from .. import loader, utils
from telethon import events
import io 

@loader.tds
class AVMod(loader.Module):
 """Антивирус, проверяющий модуль на код, который может удалить ваш аккаунт"""
 strings = {'name': 'MicroAV'}

 async def avcmd(self, message):
  """.av <реплай на файл>"""
  reply = await message.get_reply_message()
  if not reply or not reply.file:
   await message.edit("❗ <b>Ответь на файл!</b>")
   return
  text = await reply.download_media(bytes)
  text = str(text, "utf-8")
  chat = "@MicroAV_bot"
  async with message.client.conversation(chat) as conv: 
   res = conv.wait_event(events.NewMessage(incoming=True, from_users=1898472077))
   await message.edit("📝 <b>Анализирую...</b>")
   await message.client.send_message(chat, text)
   res = await res
   await message.edit(res.text)
   await message.client.delete_dialog(chat)
