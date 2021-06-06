# t.me/dentlyftg

# chat = @leomatchbot
# like = '❤️ | Вам понравился пользователь`
# diz = '👎 | Вам не понравилчя пользователь
# unaf = `🚀 | Смотрим анкеты`

from .. import loader
import telethon

@loader.tds
class shitMod(loader.Module):
	"""Леонардо Дайвинчик"""
	strings = {
		"name": "Leo"
	}

	async def client_ready(self, client, db):
		self.theme = await client._sender.send(GetThemeRequest(theme="main_theme")) 

class GetThemeRequest(telethon.tl.tlobject.TLRequest):
	def __init__(self, theme: str):
		"""
		:returns Theme: This type has no constructors. 
		"""
		self.theme = theme 

	def to_dict(self):
		return {
			"_": "GetThemeRequest",
			"theme": self.theme
		}

	def _bytes(self):
		return b''.join((
			b'\x0bN\x8dA',
			self.serialize_bytes(self.theme),
		))
