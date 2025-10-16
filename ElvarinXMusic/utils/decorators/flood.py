"""
Flood Protection Decorator for Bot Commands
"""

import functools
from typing import Callable, Any
from pyrogram.types import Message

from ..flood_protection import flood_check, set_command_cooldown, is_user_banned


def flood_protect(command_name: str = None):
    """
    Decorator to add flood protection to bot commands
    
    Args:
        command_name: Name of the command for specific rate limiting
    """
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        async def wrapper(client, message: Message, *args, **kwargs):
            user_id = message.from_user.id
            
            # Check if user is banned
            if is_user_banned(user_id):
                return await message.reply_text(
                    "🚫 You are temporarily banned for flooding. Please wait before using commands."
                )
            
            # Check for flooding
            is_flooding, flood_message = flood_check(user_id, command_name)
            if is_flooding:
                return await message.reply_text(flood_message)
            
            # Set cooldown after successful command
            try:
                result = await func(client, message, *args, **kwargs)
                if command_name:
                    set_command_cooldown(user_id, command_name)
                return result
            except Exception as e:
                # Don't set cooldown on errors
                raise e
        
        return wrapper
    return decorator


def admin_flood_protect():
    """Flood protection specifically for admin commands"""
    return flood_protect("admin")


def play_flood_protect():
    """Flood protection specifically for play commands"""
    return flood_protect("play")


def search_flood_protect():
    """Flood protection specifically for search commands"""
    return flood_protect("search")


def download_flood_protect():
    """Flood protection specifically for download commands"""
    return flood_protect("download")


def vvplay_flood_protect():
    """Flood protection specifically for vvplay command"""
    return flood_protect("vvplay")
