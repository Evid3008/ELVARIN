import asyncio
import importlib
from sys import argv
from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from ElvarinXMusic import LOGGER, app, userbot
from ElvarinXMusic.core.call import Hotty
from ElvarinXMusic.misc import sudo
from ElvarinXMusic.plugins import ALL_MODULES
from ElvarinXMusic.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS
from ElvarinXMusic.utils.song_stability import stability_monitor, background_cleanup


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
        importlib.import_module("ElvarinXMusic.plugins" + all_module)
    LOGGER("ElvarinXMusic.plugins").info("Successfully Imported Modules...")
    await userbot.start()
    await Hotty.start()
    try:
        await Hotty.stream_call("https://graph.org/file/e999c40cb700e7c684b75.mp4")
    except NoActiveGroupCall:
        LOGGER("ElvarinXMusic").error(
            "Please turn on the videochat of your log group\channel.\n\nStopping Bot..."
        )
        exit()
    except:
        pass
    await Hotty.decorators()
    
        # Start background cleanup tasks
        asyncio.create_task(stability_monitor())
        asyncio.create_task(background_cleanup())
        LOGGER("ElvarinXMusic").info("Background cleanup tasks started")
    
    LOGGER("ElvarinXMusic").info(
        "ᴅʀᴏᴘ ʏᴏᴜʀ ɢɪʀʟꜰʀɪᴇɴᴅ'ꜱ ɴᴜᴍʙᴇʀ ᴀᴛ @evidclue ᴊᴏɪɴ @TEAM_FERA , @evidzone ꜰᴏʀ ᴀɴʏ ɪꜱꜱᴜᴇꜱ"
    )
    await idle()
    await app.stop()
    await userbot.stop()
    LOGGER("ElvarinXMusic").info("Stopping Elvarin Music Bot...")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
