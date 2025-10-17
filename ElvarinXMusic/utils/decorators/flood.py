import functools
from typing import Callable, Any
from .flood_protection import flood_protection

def flood_protect(command_name: str = None):
    """Flood protection decorator"""
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        async def wrapper(*args, **kwargs):
            # Extract user_id from message
            message = None
            for arg in args:
                if hasattr(arg, 'from_user') and hasattr(arg.from_user, 'id'):
                    message = arg
                    break
            
            if not message:
                return await func(*args, **kwargs)
            
            user_id = message.from_user.id
            command = command_name or func.__name__
            
            # Check flood protection
            allowed, error_msg = flood_protection.flood_check(user_id, command)
            
            if not allowed:
                await message.reply_text(error_msg)
                return
            
            return await func(*args, **kwargs)
        
        return wrapper
    return decorator

def admin_flood_protect():
    """Admin flood protection decorator"""
    return flood_protect("admin")

def play_flood_protect():
    """Play command flood protection decorator"""
    return flood_protect("play")

def search_flood_protect():
    """Search command flood protection decorator"""
    return flood_protect("search")

def download_flood_protect():
    """Download command flood protection decorator"""
    return flood_protect("download")

def vvplay_flood_protect():
    """VVPlay command flood protection decorator"""
    return flood_protect("vvplay")
