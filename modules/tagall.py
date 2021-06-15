# боже,_я_eбал_этот_мир_в_рот... :/ by @d3ntly
import logging
import requests
from .. import loader, utils

logger = logging.getLogger(__name__)

def register(cb):
    cb(TagAllMod())

def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

class TagAllMod(loader.Module):

    strings = {"name":"ТегАлл"}

    def init(self):
        self.config = loader.ModuleConfig("DEFAULT_MENTION_MESSAGE", "Привет, давай общаться!🥺❤️\n                👉🏻👈🏻", "Default message of mentions")
        self.name = self.strings["name"]

    async def client_ready(self, client, db):
        self.client = client

    async def tagallcmd(self, message):
        arg = utils.get_args_raw(message)

        logger.error(message)
        notifies = []
        async for user in self.client.iter_participants(message.to_id):
            notifies.append("<a href=\"tg://user?id="+ str(user.id) +"\">\u206c\u206f</a>")
        chunkss = list(chunks(notifies, 5))
        logger.error(chunkss)
        await message.delete()
        for chunk in chunkss:
            await self.client.send_message(message.to_id, (self.config["DEFAULT_MENTION_MESSAGE"] if not arg else arg) + '\u206c\u206f'.join(chunk))
