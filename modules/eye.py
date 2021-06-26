# by @dently

from .. import loader, utils
import requests
def register(cb):
	cb(CheckerTGMod())
class CheckerTGMod(loader.Module):
	"""Модуль ГлазБога - поиск слитой информации по номеру/айди"""
	strings = {
		'name': 'ГлазБога',
		'check': '<b>Делаем запрос к API...</b>',
		'version': '1.1'
   'vf': '1.1'
		}
	def __init__(self):
		self.name = self.strings['name']
		self._me = None
		self._ratelimit = []
	async def client_ready(self, client, db):
		self._db = db
		self._client = client
		self.me = await client.get_me()
	async def checkcmd(self, m):
		""".check <реплай/айди>
		"""
		await check(m, self.strings['check'], self.strings['version'])
	async def pcheckcmd(self, m):
		""" .pcheck <реплай/номер>
		"""
		await check(m, self.strings['check'], self.strings['version'], 'p')
	async def scheckcmd(self, m):
		""".scheck <реплай/айди>
		"""
		await check(m, self.strings['check'], self.strings['version'], save=True)
	async def spcheckcmd(self, m):
		""".spcheck <реплай/номер>
		"""
		await check(m, self.strings['check'], self.strings['version'], 'p', True)

async def check(m, string, version, arg='u', save=False):
	reply = await m.get_reply_message()
	if utils.get_args_raw(m):
		user = utils.get_args_raw(m)
	elif reply:
		try:
			if arg == 'u':
				user = str(reply.sender.id)
			elif arg == 'p':
				user = reply.contact.phone_number[1:]
		except Exception as e:
			await m.edit(f"<b>Ошибка:</b> {e}")
			return
	else:
		await m.edit("<b>А кого чекать?</b>")
		return
	await m.edit(string)
	url_arg = ("uid" if arg == 'u' else "phone")
	resp = requests.get('http://api.murix.ru/eye?v=' + vf + '&' + url_arg + '=' + user).json()['data']
	if save:
		await m.edit(f"<b>Ответ API:</b> <code>{resp}</code>")
	else:
		await m.edit(f"<b>Ответ API:</b> <code>{resp}</code>")
