import asyncio
from pyrogram import filters
from pyrogram.types import Message
from ElvarinXMusic import app, LOGGER
from ElvarinXMusic.utils.decorators.admins import AdminActual
from ElvarinXMusic.utils.decorators.language import language
from ElvarinXMusic.utils.inline import close_markup
from config import OWNER_ID

@app.on_message(filters.command("addmember") & filters.user(OWNER_ID))
@language
async def add_member(client, message: Message, _):
    if len(message.command) < 3:
        await message.reply_text(
            "**Usage:** `/addmember <username> <group_id>`\n"
            "**Example:** `/addmember @username -1001234567890`\n"
            "**Note:** Only owner can use this command."
        )
        return

    username = message.command[1]
    group_id = message.command[2]
    
    # Remove @ if present
    if username.startswith('@'):
        username = username[1:]
    
    try:
        # Convert group_id to int if it's a string
        if isinstance(group_id, str):
            group_id = int(group_id)
        
        # Get user by username
        try:
            user = await app.get_users(username)
            user_id = user.id
            user_name = user.first_name
        except Exception as e:
            await message.reply_text(f"❌ **Error finding user:** {str(e)}")
            return
        
        # Add user to group
        try:
            await app.add_chat_members(group_id, user_id)
            await message.reply_text(
                f"✅ **Successfully added user!**\n"
                f"**User:** @{username} ({user_name})\n"
                f"**Group ID:** `{group_id}`\n"
                f"**User ID:** `{user_id}`",
                reply_markup=close_markup(_)
            )
            LOGGER(__name__).info(f"Owner {message.from_user.id} added user {user_id} (@{username}) to group {group_id}")
            
        except Exception as e:
            await message.reply_text(f"❌ **Error adding user to group:** {str(e)}")
            return
            
    except ValueError:
        await message.reply_text("❌ **Invalid group ID!** Please provide a valid group ID.")
        return
    except Exception as e:
        await message.reply_text(f"❌ **Unexpected error:** {str(e)}")
        return

@app.on_message(filters.command("addmemberlink") & filters.user(OWNER_ID))
@language
async def add_member_link(client, message: Message, _):
    if len(message.command) < 3:
        await message.reply_text(
            "**Usage:** `/addmemberlink <username> <group_link>`\n"
            "**Example:** `/addmemberlink @username https://t.me/groupname`\n"
            "**Note:** Only owner can use this command."
        )
        return

    username = message.command[1]
    group_link = message.command[2]
    
    # Remove @ if present
    if username.startswith('@'):
        username = username[1:]
    
    try:
        # Get user by username
        try:
            user = await app.get_users(username)
            user_id = user.id
            user_name = user.first_name
        except Exception as e:
            await message.reply_text(f"❌ **Error finding user:** {str(e)}")
            return
        
        # Extract group username from link
        if "t.me/" in group_link:
            group_username = group_link.split("t.me/")[-1]
            if group_username.startswith("+"):
                group_username = group_username[1:]
        else:
            await message.reply_text("❌ **Invalid group link!** Please provide a valid Telegram group link.")
            return
        
        # Get group by username
        try:
            group = await app.get_chat(group_username)
            group_id = group.id
        except Exception as e:
            await message.reply_text(f"❌ **Error finding group:** {str(e)}")
            return
        
        # Add user to group
        try:
            await app.add_chat_members(group_id, user_id)
            await message.reply_text(
                f"✅ **Successfully added user!**\n"
                f"**User:** @{username} ({user_name})\n"
                f"**Group:** @{group_username}\n"
                f"**Group ID:** `{group_id}`\n"
                f"**User ID:** `{user_id}`",
                reply_markup=close_markup(_)
            )
            LOGGER(__name__).info(f"Owner {message.from_user.id} added user {user_id} (@{username}) to group @{group_username}")
            
        except Exception as e:
            await message.reply_text(f"❌ **Error adding user to group:** {str(e)}")
            return
            
    except Exception as e:
        await message.reply_text(f"❌ **Unexpected error:** {str(e)}")
        return

@app.on_message(filters.command("addmemberhelp") & filters.user(OWNER_ID))
@language
async def add_member_help(client, message: Message, _):
    help_text = """
**🔧 Add Member Commands (Owner Only)**

**1. Add by Group ID:**
`/addmember <username> <group_id>`
**Example:** `/addmember @username -1001234567890`

**2. Add by Group Link:**
`/addmemberlink <username> <group_link>`
**Example:** `/addmemberlink @username https://t.me/groupname`

**3. Help:**
`/addmemberhelp` - Show this help

**📝 Notes:**
• Only owner can use these commands
• Username can be with or without @
• Group ID should be negative number (e.g., -1001234567890)
• Group link should be valid Telegram group link
• Bot must be admin in the target group

**⚠️ Requirements:**
• Bot must be admin in target group
• Bot must have "Add Members" permission
• Target group must allow adding members
"""
    await message.reply_text(help_text, reply_markup=close_markup(_))
