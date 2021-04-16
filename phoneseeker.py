#CLOWN DESIGN HAHA
from .. import loader, utils
import telethon
import logging
logger = logging.getLogger(__name__)
def register(cb):
    cb(PhoneSeakMod())
@loader.tds
class PhoneSeakMod(loader.Module):
    """а)"""
    strings = {"name": "PhoneSeeker"}
    async def seekcmd(self, message):
        await message.edit("<b>Ищем.</b>")
        users = await message.client.get_participants(message.to_id)
        await message.client.send_message("me", "--------------------")
        for user in users:
            if not user.bot:
                if str(user.phone) != 'None':
                    await message.client.send_message("me", f"@{user.username} - +{user.phone}")
        await message.client.send_message("me", "--------------------")


