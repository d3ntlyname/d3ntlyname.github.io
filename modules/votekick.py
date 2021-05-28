from .. import loader, utils 
import io 
from telethon import functions, types 
from asyncio import sleep 
from telethon.errors import ChatAdminRequiredError 
from telethon.tl.functions.channels import EditBannedRequest 
from telethon.tl.types import ChatBannedRights 
@loader.tds 
class VoteKickMod(loader.Module): 
 """Vote for Kick or Ban""" 
 strings = {'name': 'VoteKick'} 
 async def votekickcmd(self, message): 
  if  message.is_private: 
   return message.edit('Это не чат') 
  await message.edit('Подготовка...') 
  reply = await message.get_reply_message() 
  if not reply: 
   return await message.edit("Кого кикать?(Ответь командой на сообщение)") 
  user=await reply.get_sender() 
  await message.edit("⌛ | Голосование закончится через 2 минуты") 
  a=await message.client.send_file(message.to_id, types.InputMediaPoll( 
   poll=types.Poll( 
   id=1488228, 
   question=f'📢 | Голосование за кик {user.first_name}', 
   answers=[ 
    types.PollAnswer('Выкинуть', b'1'), 
    types.PollAnswer('Оставить', b'2') 
   ], 
   quiz=False 
   ) 
  )) 
  await sleep(60) 
  await a.reply("⌛ | Осталось 60 секунд") 
  await sleep(60) 
  msgs=[_ async for _ in message.client.iter_messages(message.to_id,ids=a.id)] 
  await a.delete() 
  if msgs[0].media.results.total_voters==0: 
   return await message.reply("😁 | Пользователь остался в чате") 
  if msgs[0].media.results.results[0].voters>msgs[0].media.results.results[1].voters: 
   try: 
    await message.client.kick_participant(message.chat_id, user.id) 
   except: 
    return await message.reply("😐 | Эй уебок, у тебя нету прав администратора") 
   return await message.reply("🚫 | Пользователя выкинули из чата") 
  else: 
   return await message.reply("😁 | Пользователь остался в чате") 
   
 async def votebancmd(self, message): 
  if  message.is_private: 
   return message.edit('😐 | Эй уебок, это не чат') 
  await message.edit('Подготовка...') 
  reply = await message.get_reply_message() 
  if not reply: 
   return await message.edit("Кого кикать?(Ответь командой на сообщение)") 
  user=await reply.get_sender() 
  await message.edit("🔚 | Голосование закончится через 2 минуты") 
  a=await message.client.send_file(message.to_id, types.InputMediaPoll( 
   poll=types.Poll( 
   id=1488228, 
   question=f'📢 | Голосование за кик {user.first_name}', 
   answers=[ 
    types.PollAnswer('Выкинуть', b'1'), 
    types.PollAnswer('Оставить', b'2') 
   ], 
   quiz=False 
   ) 
  )) 
  await sleep(60) 
  await a.reply("⌛ | Осталось 60 секунд") 
  await sleep(60) 
  msgs=[_ async for _ in message.client.iter_messages(message.to_id,ids=a.id)] 
  await a.delete() 
  if msgs[0].media.results.total_voters==0: 
   return await message.reply("😁 | Пользователь остался в чате") 
  if msgs[0].media.results.results[0].voters>msgs[0].media.results.results[1].voters: 
   try: 
    await message.client(EditBannedRequest(message.chat_id, user.id, ChatBannedRights(until_date=None, view_messages=True))) 
   except: 
    return await message.reply("😐 | Эй уебок, у тебя нету прав администратора") 
   return await message.reply("🚫 | Пользователь забанен в чате") 
  else: 
   return await message.reply("😁 | Пользователь остался в чате")
