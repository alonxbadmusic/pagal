import asyncio
import importlib

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from Spy import LOGGER, app, userbot
from Spy.core.call import Sagar
from Spy.misc import sudo
from Spy.plugins import ALL_MODULES
from Spy.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error("Assistant client variables not defined, exiting...")
        exit()
    await sudo()
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("Spy.plugins" + all_module)
    LOGGER("Spy.plugins").info("sᴜᴄᴄᴇssғᴜʟʟʏ ɪᴍᴘᴏʀᴛᴇᴅ ᴀʟʟ ᴍᴏᴅᴜʟᴇs...")
    await userbot.start()
    await Sagar.start()
    try:
        await Sagar.stream_call("https://envs.sh/9tj.mp4")
    except NoActiveGroupCall:
        LOGGER("Spy").error(
            "ʙsᴅᴋ ᴠᴄ ᴛᴏ ᴏɴ ᴋᴀʀʟᴇ  ʟᴏɢ ɢʀᴏᴜᴘ\ᴄʜᴀɴɴᴇʟ ᴋɪ.\n\n ᴏɴ ᴋᴀʀᴋᴇ ᴀᴀ ᴛᴀʙ ᴛᴀᴋ ʙᴏᴛ ʙᴀɴᴅ ᴋᴀʀ ʀʜᴀ ʜᴏᴏɴ..."
        )
        exit()
    except:
        pass
    await Sagar.decorators()
    LOGGER("Spy").info(
        "ᴍᴜsɪᴄ ʙᴏᴛ sᴛᴀʀᴛᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ, ɴᴏᴡ ɢɪʙ ʏᴏᴜʀ ɢɪʀʟғʀɪᴇɴᴅ ᴄʜᴜᴛ ɪɴ @tmm_support_chat"
    )
    await idle()
    await app.stop()
    await userbot.stop()
    LOGGER("Spy").info("ᴍᴀᴀ ᴄʜᴜᴅᴀ ᴍᴀɪɴ ʙᴏᴛ ʙᴀɴᴅ ᴋᴀʀ ʀʜᴀ sʏsᴛᴇᴍ Mᴜsɪᴄ Bᴏᴛ...")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
