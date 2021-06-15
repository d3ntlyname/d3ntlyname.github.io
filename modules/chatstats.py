# by @dentlyftg

from .. import loader 
from telethon.tl.types import * 
@loader.tds 
class ChatstatsMod(loader.Module): 
  "Статистика чата" 
  strings = {"name": "Chatstats"} 
  @loader.owner 
  async def statscmd(self, m): 
   await m.edit("<b>Подсчитываем...</b>") 
   all = str((await m.client.get_messages(m.to_id, limit=0)).total) 
   phote = str((await m.client.get_messages(m.to_id, limit=0, filter=InputMessagesFilterPhotos())).total) 
   video = str((await m.client.get_messages(m.to_id, limit=0, filter=InputMessagesFilterVideo())).total) 
   music = str((await m.client.get_messages(m.to_id, limit=0, filter=InputMessagesFilterMusic())).total) 
   voice = str((await m.client.get_messages(m.to_id, limit=0, filter=InputMessagesFilterVideo())).total) 
   vidv = str((await m.client.get_messages(m.to_id, limit=0, filter=InputMessagesFilterRoundVideo())).total) 
   file = str((await m.client.get_messages(m.to_id, limit=0, filter=InputMessagesFilterDocument())).total) 
   urls = str((await m.client.get_messages(m.to_id, limit=0, filter=InputMessagesFilterUrl())).total) 
   gifs = str((await m.client.get_messages(m.to_id, limit=0, filter=InputMessagesFilterGif())).total) 
   ip = str((await m.client.get_messages(m.to_id, limit=0, filter=InputMessagesFilterGeo())).total) 
   cont = str((await m.client.get_messages(m.to_id, limit=0, filter=InputMessagesFilterContacts())).total) 
   await m.edit( 
     ("<b>Всего сообщений:</b> {}\n"+ 
     "<b>Всего фотографий:</b> {}\n"+ 
     "<b>Всего видео:</b> {}\n"+ 
     "<b>Всего аудио: :</b> {}\n"+ 
     "<b>Всего войсов:</b> {}\n"+ 
     "<b>Всего видеовойсов:</b> {}\n"+ 
     "<b>Всего файлов:</b> {}\n"+ 
     "<b>Всего ссылок:</b> {}\n"+ 
     "<b>Всего GIF:</b> {}\n"+ 
     "<b>Всего IP:</b> {}\n"+ 
     "<b>Контаков:</b> {}").format(all, photo, video, musik, voice, vidv, file, urls, gifs, ip, cont))
