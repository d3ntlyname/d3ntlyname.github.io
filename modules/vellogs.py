# иди нахуй дура

from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from .. import loader, utils
from datetime import datetime


def register(cb):
 cb(PingerMod())


class PingerMod(loader.Module):
 """Точный пинг, дентли топ все другие лохи"""

 strings = {'name': 'Ping'}

 def init(self):
  self.name = self.strings['name']
  self._me = None
  self._ratelimit = []

 async def client_ready(self, client, db):
  self._db = db
  self._client = client
  self.me = await client.get_me()

 async def pingcmd(self, message):
  """пингует"""
  a = 5
  r = utils.get_args(message)
  if r and r[0].isdigit():
   a = int(r[0])
  ping_msg = []
  ping_data = []
  for _ in range(a):
   start = datetime.now()
   msg = await message.client.send_message("me", "🤩")
   end = datetime.now()
   duration = (end - start).microseconds / 1000
   ping_data.append(duration)
   ping_msg.append(msg)
  ping = sum(ping_data) / len(ping_data)
  await message.edit(f"<b>VeLLogs > </b><b>{str(ping)[0:5]} мс</b>")
  for i in ping_msg:
   await i.delete()
