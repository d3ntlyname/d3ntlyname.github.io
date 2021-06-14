from .. import loader, utils
from telethon import TelegramClient
from telethon.tl.patched import Message
from telethon.tl.types import ChatBannedRights
from telethon.tl.functions.channels import EditBannedRequest


@loader.tds
class AutoBanMod(loader.Module):
    """АвтоБан"""
    strings = {'name': 'AutoBan'}

    async def client_ready(self, client: TelegramClient, db):
        self.client = client
        self.db = db

    async def abancmd(self, message: Message):
        """.aban <@ или реплай> или <list>"""
        users = self.db.get("AutoBan", "users", [])
        args = utils.get_args_raw(message)
        reply = await message.get_reply_message()

        if not (args or reply):
            return await message.edit("<b>[AutoBan] Нет аргументов или реплая</b>")

        if args == "list":
            if not users:
                return await message.edit("<b>Список юзеров для автобана пуст</b>")

            msg = ""
            for _ in users:
                try:
                    user = await self.client.get_entity(_)
                    msg += f"• <a href=\"tg://user?id={user.id}\">{user.first_name}</a>\n"
                except:
                    users.remove(_)
                    self.db.set("AutoBan", "users", users)
                    return await message.edit("<b>[AutoBan] Произошла ошибка, повтори команду</b>")

            return await message.edit(f"<b>Список пользователей в автобане:<b>\n\n{msg}")

        try:
            user = await self.client.get_entity(reply.sender_id if reply else args if not args.isnumeric() else int(args))
        except ValueError:
            return await message.edit("<b>[AutoBan] Не удалось найти пользователя</b>")

        if user.id not in users:
            users.append(user.id)
            text = "добавлен в список автобана"
        else:
            users.remove(user.id)
            text = "удален из списка автобана"

        self.db.set("AutoBan", "users", users)
        await message.edit(f"<b>[AutoBan] {user.first_name} был {text}</b>")


    async def achatcmd(self, message: Message):
        """.achat <list;ничего> добавить чат в список автобана"""
        chats = self.db.get("AutoBan", "chats", [])
        args = utils.get_args_raw(message)
        chat_id = message.chat_id

        if args == "list":
            if not chats:
                return await message.edit("<b>Список чатов для автобана пуст</b>")

            msg = ""
            for _ in chats:
                try:
                    chat = await self.client.get_entity(_)
                    msg += f"• {chat.title} | {chat.id}\n"
                except:
                    chats.remove(_)
                    self.db.set("AutoBan", "users", chats)
                    return await message.edit("<b>[AutoBan] Произошла ошибка, повтори команду</b>")

            return await message.edit(f"<b>Список чатов для автобана:</b>\n\n{msg}")

        if message.is_private:
            return await message.edit("<b>[AutoBan] Это не чат</b>")

        if chat_id not in chats:
            chats.append(chat_id)
            text = "добавлен в список чатов"
        else:
            chats.remove(chat_id)
            text = "удален из списка чатов"

        self.db.set("AutoBan", "chats", chats)
        return await message.edit(f"<b>[AutoBan] {text}</b>")


    async def watcher(self, message: Message):
        try:
            users = self.db.get("AutoBan", "users", [])
            chats = self.db.get("AutoBan", "chats", [])
            user = message.sender
            chat_id = message.chat_id

            if chat_id not in chats:
                return

            if user.id in users:
                for _ in chats:
                    try:
                        await self.client(
                            EditBannedRequest(
                                _, user.id, ChatBannedRights(
                                    until_date=None, view_messages=True
                                )
                            )
                        )
                    except: pass
                return await message.respond(f"<b>[AutoBan] {user.first_name} забанен</b>")
        except:
            pass
