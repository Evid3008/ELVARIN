from pyrogram import filters
from pyrogram.types import Message

from ElvarinXMusic import app
from ElvarinXMusic.core.call import Hotty
from ElvarinXMusic.utils.database import set_loop
from ElvarinXMusic.utils.decorators import AdminRightsCheck
from ElvarinXMusic.utils.inline import close_markup
from config import BANNED_USERS
import config


@app.on_message(
    filters.command(["end", "stop", "cend", "cstop"]) & filters.group & ~BANNED_USERS
)
@AdminRightsCheck
async def stop_music(cli, message: Message, _, chat_id):
    if not len(message.command) == 1:
        return
    
    # Stop vvplay retries if active
    if config.vvplay_retry_active and config.vvplay_retry_chat == chat_id:
        config.vvplay_retry_active = False
        config.vvplay_retry_chat = None
        await message.reply_text("🛑 VVPlay retries stopped!")
        return
    
    await Hotty.stop_stream(chat_id)
    await set_loop(chat_id, 0)
    await message.reply_text(
        _["admin_5"].format(message.from_user.mention), reply_markup=close_markup(_)
    )
