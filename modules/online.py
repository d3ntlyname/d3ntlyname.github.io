# by @dently

from .. import loader 
from asyncio import sleep 
 
@loader.tds 
class EternalOnlineMod(loader.Module): 
    """Вечный онлайн.""" 
    strings = {'name': 'Online'} 
 
    async def client_ready(self, client, db): 
        self.db = db 
 
    async def onlinecmd(self, message): 
        """Включить вечный онлайн""" 
        if not self.db.get("Eternal Online", "status"): 
            self.db.set("Eternal Online", "status", True) 
            await message.edit("Вечный онлайн включен") 
            while self.db.get("Eternal Online", "status"): 
                msg = await message.client.send_message("me", "Telegram best messenger! 🤩")
                await msg.delete()
                await sleep(70) 
 
        else: 
            self.db.set("Eternal Online", "status", False) 
            await message.edit("Вечный онлайн выключен")

    async def watcher(self, message): 
        """Вау, это watcher, я что-то смог из него сделать. Поздравьте меня)""" 
        await message.client.send_read_acknowledge(message.chat_id, clear_mentions=True)
