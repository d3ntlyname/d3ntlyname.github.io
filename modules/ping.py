# выебистый пингер бу твоя мать (@dently)

from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.types import MessageEntityMention as mem
from .. import loader, utils
from datetime import datetime
from statistics import mean, median, stdev

def register(cb):
	cb(PingMod())


class PingMod(loader.Module):
	"""Более точный пинг с небольшой аналитикой"""

	strings = {
		'name': 'Ping',
		'samples': 5,
		'timeout': 1
	}

	def __init__(self):
		self.name = self.strings['name']
		self._me = None
		self._ratelimit = []

	async def client_ready(self, client, db):
		self.db = db
		self._client = client
		self.me = await client.get_me()
		if not self.db.get(self.strings["name"], 'samples'):
			self.db.set(self.strings['name'], 'samples', self.strings['samples'])
		if not self.db.get(self.strings['name'], 'timeout'):
			self.db.set(self.strings['name'], 'timeout', self.strings['timeout'])

	async def pingcmd(self, message):
		"""Пингует себя или бота, если указать его юзернейм аргументом"""
		a = self.db.get(self.strings["name"], "samples")
		if not isinstance(a, int):
			a = self.strings['samples']
		t = self.db.get(self.strings['name'], 'timeout')
		if not isinstance(t, int):
			t = self.strings['timeout']
		r = utils.get_args(message)
		entity = "me"
		if r and (message.entities and isinstance(message.entities[0], mem)):
			try:
				if (await message.client.get_entity(r[0][1:])).bot:
					entity = r[0]
				else:
					await message.edit(f'<b>{r[0][1:]}</b> не является ботом')
					return
			except:
				await message.edit(f'<b>{r[0][1:]}</b> не является ботом либо не существует')
				return
		ping_msg, ping_data, ping_ans = await pping(message, entity, a, t)
		ping = f"""<code>Телеги:</code> {str(median(ping_data))[0:5]}
<code>В среднем:</code> {str(mean(ping_data))[0:5]}
<code>Максимум:</code> {str(max(ping_data))[0:5]}
<code>Минимум:</code> {str(min(ping_data))[0:5]}
<code>Юзербота:</code> {str(stdev(ping_data))[0:5]}"""
		results = 0
		for x in ping_data:
			results += (0 if x >= t*1000 else 1)
		ok = ("DeNTLy" if results == len(ping_data) else f"{results}/{len(ping_data)}")
		entity = ('' if entity == 'me' else f' <b>{entity[1:]}</b>')
		await message.edit(f"{ok} >{entity}\n{ping}")
		for i in ping_msg:
			await i.delete()
		for i in ping_ans:
			await i.delete()
			
	async def pingsetcmd(self, message):
		""".samples <число>: кол-во попыток пинга
		.timeout <число>: время ожидания ответа в секундах
		Установка параметров для пинга"""
		r = utils.get_args(message)
		if not r or len(r) == 1 or len(r) > 2 or r[0] not in [".samples", ".timeout"]:
			await message.edit(f'Читай <code>.help {self.strings["name"]}</code>')
			return
		if r[0] in [".samples", ".timeout"]:
			if r[1].isnumeric():
				if r[0] == ".samples":
					s = (25 if int(r[1]) > 25 else (int(r[1]) if int(r[1]) > 3 else 3))
				else:
					s = (60 if int(r[1]) > 60 else (int(r[1]) if int(r[1]) > 1 else 1))
				self.db.set(self.strings['name'], r[0][1:], s)
				await message.edit(f"Параметр <b>{r[0]}</b> установлен на <i>{s}</i>")
			else:
				await message.edit(f'Параметр <code>{r[0]}</code> должен быть целым числом')
			
async def pping(message, entity, samples, timeout):
	await message.edit("<i>🥵</i>")
	ping_msg = []
	ping_data = []
	ping_ans = []
	if entity != 'me':
		async with message.client.conversation(entity) as conv:
			for _ in range(samples):
				resp = conv.wait_event(events.NewMessage(incoming=True, from_users=entity), timeout=timeout)
				msg = await message.client.send_message(entity, "/start")
				try:
					start = datetime.now()
					resp = await resp
					end = datetime.now()
					duration = (end - start).microseconds / 1000
					ping_ans.append(resp)
				except:
					duration = timeout*1000
				ping_data.append(duration)
				ping_msg.append(msg)
	else:
		for _ in range(samples):
			start = datetime.now()
			msg = await message.client.send_message(entity, "ping")
			end = datetime.now()
			duration = (end - start).microseconds / 1000
			ping_data.append(duration)
			ping_msg.append(msg)
	return (ping_msg, ping_data, ping_ans)
