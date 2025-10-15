import asyncio

from ElvarinXMusic import app
from pyrogram import filters
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from config import MUSIC_BOT_NAME

@app.on_message(filters.command(["alive"]))
async def start(client: Client, message: Message):
    await message.reply_video(
        video=f"https://graph.org/file/e999c40cb700e7c684b75.mp4",
        caption=f"❤️ ʜᴇʏ {message.from_user.mention}\n\n🔮 ɪ ᴀᴍ {MUSIC_BOT_NAME}\n\n✨ ɪ ᴀᴍ ғᴀsᴛ ᴀɴᴅ ᴩᴏᴡᴇʀғᴜʟ ᴍᴜsɪᴄ ᴩʟᴀʏᴇʀ ʙᴏᴛ ᴡɪᴛʜ sᴏᴍᴇ ᴀᴡᴇsᴏᴍᴇ ғᴇᴀᴛᴜʀᴇs.\n\n💫 ɪғ ʏᴏᴜ ʜᴀᴠᴇ ᴀɴʏ ǫᴜᴇsᴛɪᴏɴs ᴛʜᴇɴ ᴊᴏɪɴ ᴏᴜʀ sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ🤍...\n\n━━━━━━━━━━━━━━━━━━❄",
        reply_markup=InlineKeyboardMarkup(
            [
               [
            InlineKeyboardButton(
                text="—͟͟͞͞E 𝐕 𝐈 𝐃™ 🥀", url="https://t.me/iq4u8"
            ),
            InlineKeyboardButton(
                text="⇌", callback_data="autoplay_mode"
            ),
            InlineKeyboardButton(
                text="˹𝐁ᴇᴀᴛꭙ 𝐅ʟᴏᴡ™ ˼ | Support", url="https://t.me/iq4us"
            ),
        ],
                [
            InlineKeyboardButton(
                text="˹𝐁ᴇᴀᴛꭙ 𝐅ʟᴏᴡ™ ˼ | 𝐔𝐩𝐝𝐚𝐭𝐞𝐬", url="https://t.me/evidzone"
            ),
                ],
                [
                    InlineKeyboardButton(
                        "✯ ᴄʟᴏsᴇ ✯", callback_data="close"
                    )
                ],
            ]
        )
    )
