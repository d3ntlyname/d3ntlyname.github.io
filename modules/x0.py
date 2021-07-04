# by @dentlyftg

from .. import loader, utils  # pylint: disable=relative-beyond-top-level 
import logging 
from requests import post 
import io 
 
logger = logging.getLogger(__name__) 
 
@loader.tds 
class X0atMod(loader.Module): 
 """Загрузчик ваших файлов на бесплатный хостинг x0.at""" 
 strings = {"name": "X0at"} 
 
 async def client_ready(self, client, db): 
  self.client = client 
  
  
 @loader.sudo 
 async def x0cmd(self, message): 
  """.x0 <реплай на файл>"""
  await message.edit("<b>Загрузка...</b>") 
  reply = await message.get_reply_message() 
  if not reply: 
   await message.edit("<b>Ответь на файл!</b>") 
   return 
  media = reply.media 
  if not media: 
   file = io.BytesIO(bytes(reply.raw_text, "utf-8")) 
   file.name = "module.py" 
  else: 
   file = io.BytesIO(await self.client.download_file(media)) 
   file.name = reply.file.name if reply.file.name else  reply.file.id+reply.file.ext 
  try: 
   x0at = post('https://x0.at', files={'file': file}) 
  except ConnectionError as e: 
   await message.edit("<b>Ошибка соединения :(</b>") 
   return 
  url = x0at.text 
  xz = f"<a href="{url}">URL:</a> <code>{url}</code>"
  await message.edit(xz)
