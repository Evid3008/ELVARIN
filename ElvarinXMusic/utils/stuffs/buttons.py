from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram import Client, filters, enums 

class BUTTONS(object):
    MBUTTON = [[InlineKeyboardButton("CʜᴀᴛGPT", callback_data="mplus HELP_ChatGPT"),InlineKeyboardButton("Hɪsᴛᴏʀʏ", callback_data="mplus HELP_History")],
    [InlineKeyboardButton("Tᴀɢ-Aʟʟ", callback_data="mplus HELP_TagAll"),
    InlineKeyboardButton("Iɴꜰᴏ", callback_data="mplus HELP_Info"),InlineKeyboardButton("Exᴛʀᴀ", callback_data="mplus HELP_Extra")],
    [InlineKeyboardButton("ᴄᴏᴜᴘʟᴇꜱ", callback_data="mplus HELP_Couples"),
    InlineKeyboardButton("Aᴄᴛɪᴏɴ", callback_data="mplus HELP_Action")],    
    [InlineKeyboardButton("ғᴏɴᴛ", callback_data="mplus HELP_Font"),
    InlineKeyboardButton("Bᴏᴛs", callback_data="mplus HELP_Bots"),InlineKeyboardButton("Ⓣ-ɢʀᴀᴘʜ", callback_data="mplus HELP_TG")],
    [InlineKeyboardButton("ᴛᴛs", callback_data="mplus HELP_TTS"),InlineKeyboardButton("ǫᴜᴏᴛʟʏ", callback_data="mplus HELP_Q")],          
    [InlineKeyboardButton("◁", callback_data=f"settings_back_helper"),
     InlineKeyboardButton("↻ ʙᴀᴄᴋ ↻", callback_data=f"mbot_cb"), 
    InlineKeyboardButton("▷", callback_data=f"managebot123 settings_back_helper"),
    ]]
