import functools
import asyncio
import time
from typing import Callable, Any
from ElvarinXMusic.utils.song_stability import song_stability
import config

def stable_play(func: Callable) -> Callable:
    """Decorator for stable song play with crash protection"""
    @functools.wraps(func)
    async def wrapper(*args, **kwargs):
        # Extract chat_id from message
        message = None
        for arg in args:
            if hasattr(arg, 'chat') and hasattr(arg.chat, 'id'):
                message = arg
                break
        
        chat_id = message.chat.id if message else None
        
        try:
            # Check memory usage before play
            if not await song_stability.check_memory_usage():
                if message:
                    await message.reply_text("⚠️ High memory usage detected. Please wait...")
                await asyncio.sleep(5)
            
            # Track stream
            if chat_id:
                await song_stability.track_stream(chat_id, f"play_{int(time.time())}")
            
            # Execute with timeout
            result = await asyncio.wait_for(
                func(*args, **kwargs), 
                timeout=config.PLAY_TIMEOUT
            )
            
            return result
            
        except asyncio.TimeoutError:
            if message:
                await message.reply_text("⏰ Play timeout. Retrying...")
            
            # Retry logic
            if chat_id and await song_stability.can_retry_stream(chat_id):
                await song_stability.increment_stream_retry(chat_id)
                await asyncio.sleep(config.STREAM_RETRY_DELAY)
                return await wrapper(*args, **kwargs)
            else:
                if message:
                    await message.reply_text("❌ Play failed after retries. Please try again.")
                return None
                
        except Exception as e:
            if config.CRASH_RECOVERY:
                if message:
                    await message.reply_text("🔄 Recovering from error...")
                await asyncio.sleep(2)
                
                # Retry once more
                if chat_id and await song_stability.can_retry_stream(chat_id):
                    await song_stability.increment_stream_retry(chat_id)
                    try:
                        return await func(*args, **kwargs)
                    except:
                        pass
            
            if message:
                await message.reply_text("❌ Play error occurred. Please try again.")
            return None
            
        finally:
            # Clean up tracking
            if chat_id:
                await song_stability.untrack_stream(chat_id)
    
    return wrapper

def quality_preserved(func: Callable) -> Callable:
    """Decorator to preserve audio quality"""
    @functools.wraps(func)
    async def wrapper(*args, **kwargs):
        try:
            return await func(*args, **kwargs)
        except Exception as e:
            # If quality preservation fails, don't compromise
            if config.PRESERVE_AUDIO_QUALITY:
                raise e
            else:
                # Fallback to lower quality only if explicitly allowed
                if config.QUALITY_FALLBACK:
                    return await func(*args, **kwargs)
                else:
                    raise e
    
    return wrapper
