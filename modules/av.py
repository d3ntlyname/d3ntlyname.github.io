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
  text = text[:4096]
  chat = "@MicroAV_bot"
  async with message.client.conversation(chat) as conv: 
   res = conv.wait_event(events.NewMessage(incoming=True, from_users=1898472077))
   await message.edit("🧬 <b>Анализирую...</b>")
   await message.client.send_message(chat, text)
   res = await res
   usme = reply.file.name
   name = usme.split('.')[0] 
   form = usme.split('.')[1] 
   siz = int(reply.file.size / 1000)
   await message.edit(res.text+f"\n\n🔖 Название файла: <i>{name}</i>\n🔐 Формат файла: <i>{form}</i>\n📁 Размер файла: <i>{siz} MB</i>\n\n<b><a href='https://d3ntly.ml/modules/av.py'>⚜️ Ссылка на MicroAV</a></b>")
   await message.client.delete_dialog(chat)
