import asyncio 
import logging 
from telethon.tl.types import DocumentAttributeFilename 
from .. import loader, utils 
 
logger = logging.getLogger(__name__) 
 
 
@loader.tds 
class ToGifMod(loader.Module): 
 """Конвертирует видео в гифку""" 
 strings = {"name": "ToGif", 
      "wf": "<b>А где реплай?</b>", 
      "wn": "<b>Ашибка(</b>", 
      "tnf":"<b>Это не видеофайл!</b>"} 
 
  
 @loader.unrestricted 
 async def togifcmd(self, message): 
  """.togif <реплай на видео>""" 
  reply = await message.get_reply_message() 
  if not reply or not reply.file: 
   await message.edit(self.strings["wf"]) 
   return 
  name = 'gif.gif'
  if not name: 
   await message.edit(self.strings["wn"]) 
   return 
  fn = reply.file.name 
  if not fn: 
   fn = "" 
  fs = reply.file.size 
   
  [await message.edit(f"<b>Установка: {fn}</b>") if fs > 500000 else ...] 
  file = await reply.download_media(bytes) 
  [await message.edit(f"<b>Отправляем...</b>") if fs > 500000 else ...] 
  await message.client.send_file(message.to_id, file, force_document=False, reply_to=reply, attributes=[DocumentAttributeFilename(file_name=name)]) 
  await message.delete()
