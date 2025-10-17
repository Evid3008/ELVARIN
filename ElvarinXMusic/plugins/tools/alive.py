import asyncio
import random
import datetime
from typing import List, Dict
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from ElvarinXMusic import app
from config import MUSIC_BOT_NAME, SUDO_USERS, LOGGER_ID
import config
from ElvarinXMusic.logging import LOGGER
from ElvarinXMusic.utils.admin_check import admin_check

# Secret Wish System
class SecretWishSystem:
    def __init__(self):
        self.target_group_id = -1002119794892  # Your group ID
        self.target_user_id = 7620347246  # Target user ID
        
        # Wish messages in different styles
        self.morning_messages = [
            "Good morning sunshine! ☀️ Hope you have an amazing day ahead! 💕",
            "Rise and shine beautiful! 🌅 Sending you lots of love and positive vibes! ✨",
            "Morning gorgeous! 🌸 May your day be filled with happiness and success! 💖",
            "सुप्रभात प्यारे! ☀️ आज का दिन आपके लिए बहुत खुशियां लेकर आए! 💕",
            "सुबह की शुभकामनाएं! 🌅 आपका दिन मंगलमय हो! ✨"
        ]
        
        self.afternoon_messages = [
            "Good afternoon sweetheart! 🌞 Hope your day is going amazing! 💕",
            "Afternoon vibes! ☀️ Sending you warm hugs and love! 🤗",
            "शुभ दोपहर प्यारे! 🌞 आपका दिन कैसा चल रहा है? 💕",
            "दोपहर की शुभकामनाएं! ☀️ आपको गर्मजोशी से बधाई! 🤗"
        ]
        
        self.evening_messages = [
            "Good evening my dear! 🌆 Hope you had a wonderful day! 💕",
            "Evening greetings! 🌅 Wishing you a peaceful evening! ✨",
            "शुभ संध्या प्यारे! 🌆 आपका दिन कैसा रहा? 💕",
            "शाम की शुभकामनाएं! 🌅 आपकी शाम शांतिपूर्ण हो! ✨"
        ]
        
        self.night_messages = [
            "Good night sweet dreams! 🌙 Sleep tight and wake up refreshed! 💕",
            "Night night beautiful! 🌟 Wishing you peaceful sleep! ✨",
            "शुभ रात्रि मीठे सपने! 🌙 आराम से सोएं! 💕",
            "रात की शुभकामनाएं! 🌟 आपकी नींद शांतिपूर्ण हो! ✨"
        ]

    def get_current_greeting_type(self) -> str:
        """Get current greeting type based on time"""
        current_hour = datetime.datetime.now().hour
        
        if 5 <= current_hour < 12:
            return "morning"
        elif 12 <= current_hour < 17:
            return "afternoon"
        elif 17 <= current_hour < 23:
            return "evening"
        else:
            return "night"

    def get_random_message(self, greeting_type: str) -> str:
        """Get random message for greeting type"""
        if greeting_type == "morning":
            return random.choice(self.morning_messages)
        elif greeting_type == "afternoon":
            return random.choice(self.afternoon_messages)
        elif greeting_type == "evening":
            return random.choice(self.evening_messages)
        else:  # night
            return random.choice(self.night_messages)

    async def send_wish(self, greeting_type: str = None):
        """Send wish message to target user"""
        try:
            if greeting_type is None:
                greeting_type = self.get_current_greeting_type()
            
            message = self.get_random_message(greeting_type)
            
            # Send simple wish message (no reply, no tag)
            await app.send_message(
                chat_id=self.target_group_id,
                text=message,
                disable_notification=False
            )
            
            LOGGER(__name__).info(f"Secret wish sent: {greeting_type} - {message[:50]}...")
            
        except Exception as e:
            LOGGER(__name__).error(f"Error sending secret wish: {e}")

# Global instance
secret_wish_system = SecretWishSystem()

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

@app.on_message(filters.command("wish") & filters.user(SUDO_USERS))
async def wish_command(client, message: Message):
    """
    Manual wish command for sudo users (only works in logger group)
    """
    try:
        # Check if it's the logger group
        if message.chat.id != config.LOGGER_ID:
            await message.reply_text("❌ **This command only works in logger group!**")
            return
        
        # Get current greeting type
        greeting_type = secret_wish_system.get_current_greeting_type()
        
        # Send wish
        await secret_wish_system.send_wish(greeting_type)
        
        # Confirm to user
        await message.reply_text(
            f"✅ **Wish sent!**\n"
            f"**Type:** {greeting_type.title()}\n"
            f"**Target:** User ID {secret_wish_system.target_user_id}\n"
            f"**Group:** {secret_wish_system.target_group_id}"
        )
        
        LOGGER(__name__).info(f"Manual wish sent by {message.from_user.id}")
        
    except Exception as e:
        await message.reply_text(f"❌ **Error sending wish:** {e}")
        LOGGER(__name__).error(f"Error in wish command: {e}")

@app.on_message(filters.command("wish") & filters.group)
async def wish_command_group(client, message: Message):
    """
    Wish command disabled for group users
    """
    await message.reply_text("❌ **This command is disabled for group users!**")
