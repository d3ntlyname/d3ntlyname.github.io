# by @dently

from .. import loader, utils

@loader.tds
class MyRepMod(loader.Module):
    """Модуль с вашей репутацией"""
    strings={"name":"Репутация"}

    async def client_ready(self, message, db):
        self.db=db
        self.db.set("MyRep", "repstatus", True)

    async def repcmd(self, message):
        """Включить/выключить режим репутации"""
        repstatus = self.db.get("MyRep", "repstatus")
        if repstatus is not True:
            self.db.set("MyRep", "repstatus", True)
            await message.edit(f"<b>Режим репутации включен!</b>")
        else:
            self.db.set("MyRep", "repstatus", False)
            await message.edit(f"<b>Режим репутации выключен!</b>")

    async def myrepcmd(self, message):
        """Посмотреть свою репутацию. Используй: .myrep <clear/ничего>"""
        args = utils.get_args_raw(message)
        if args == "clear":
            self.db.set("MyRep", "my_repa", 0)
            return await message.edit("<b>Моя репутация успешно очищена</b>")
        myrep = self.db.get("MyRep", "my_repa")
        repstatus = self.db.get("MyRep", "repstatus")
        if repstatus is not False:
            msg_repstatus = "<i>Включен</i>"
        else:
            msg_repstatus = "<i>Выключен</i>"
        await message.edit(f"</b> \n<b>Статус режима: </b>{msg_repstatus}<b>\nКол-во: <i>{myrep}</i></b>")

    async def watcher(self, message):
        try:
            number = self.db.get("MyRep", "my_repa", 0)
            repstatus = self.db.get("MyRep", "repstatus")
            if message.mentioned:
                if repstatus is not False:
                    if message.text == "+":
                        number += 1
                        self.db.set("MyRep", "my_repa", number)
                        await message.reply(f"<b>Ты повысил мою репутацию :)\nНовое значение: {number}</b>")
                    if message.text == "+2":
                        number += 2
                        self.db.set("MyRep", "my_repa", number)
                        await message.reply(f"<b>Ты повысил мою репутацию :)\nНовое значение: {number}</b>")
                    elif message.text == "-":
                        total = int(number) - 1
                        self.db.set("MyRep", "my_repa", total)
                        await message.reply(f"<b>Ты понизил мою репутацию :(\nНовое значение: {total}</b>")
        except: pass
