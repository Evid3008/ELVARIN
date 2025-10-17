import asyncio
import time
import psutil
import gc
from typing import Dict, Optional
import config

class SongPlayStability:
    def __init__(self):
        self.active_streams = {}
        self.stream_retries = {}
        self.last_cleanup = time.time()
        self.memory_warnings = 0
        
    async def check_memory_usage(self) -> bool:
        """Check if memory usage is within limits with proactive cleanup"""
        try:
            process = psutil.Process()
            memory_mb = process.memory_info().rss / 1024 / 1024
            
            # Proactive cleanup at 70% of limit
            cleanup_threshold = config.MEMORY_LIMIT_MB * 0.7
            
            if memory_mb > cleanup_threshold:
                await self.proactive_cleanup()
                # Check again after cleanup
                memory_mb = process.memory_info().rss / 1024 / 1024
            
            # Warning only at 90% of limit
            warning_threshold = config.MEMORY_LIMIT_MB * 0.9
            
            if memory_mb > warning_threshold:
                self.memory_warnings += 1
                if self.memory_warnings >= 2:  # Reduced from 3 to 2
                    await self.emergency_cleanup()
                    return False
            else:
                self.memory_warnings = 0
                
            return True
        except:
            return True
    
    async def proactive_cleanup(self):
        """Proactive memory cleanup before warnings"""
        try:
            # Clean up old stream tracking
            await self.cleanup_old_streams()
            
            # Force garbage collection
            gc.collect()
            
            # Clear any cached data
            if hasattr(self, 'cached_data'):
                self.cached_data.clear()
                
        except:
            pass
    
    async def emergency_cleanup(self):
        """Emergency memory cleanup"""
        try:
            gc.collect()
            self.memory_warnings = 0
        except:
            pass
    
    async def track_stream(self, chat_id: int, stream_id: str):
        """Track active stream"""
        self.active_streams[chat_id] = {
            'stream_id': stream_id,
            'start_time': time.time(),
            'retries': 0
        }
    
    async def untrack_stream(self, chat_id: int):
        """Remove stream tracking"""
        if chat_id in self.active_streams:
            del self.active_streams[chat_id]
    
    async def get_stream_retry_count(self, chat_id: int) -> int:
        """Get retry count for stream"""
        if chat_id in self.active_streams:
            return self.active_streams[chat_id]['retries']
        return 0
    
    async def increment_stream_retry(self, chat_id: int):
        """Increment retry count"""
        if chat_id in self.active_streams:
            self.active_streams[chat_id]['retries'] += 1
    
    async def can_retry_stream(self, chat_id: int) -> bool:
        """Check if stream can be retried"""
        retry_count = await self.get_stream_retry_count(chat_id)
        return retry_count < config.STREAM_RETRY_LIMIT
    
    async def cleanup_old_streams(self):
        """Clean up old stream tracking"""
        current_time = time.time()
        if current_time - self.last_cleanup > 300:  # 5 minutes
            old_streams = []
            for chat_id, data in self.active_streams.items():
                if current_time - data['start_time'] > 1800:  # 30 minutes
                    old_streams.append(chat_id)
            
            for chat_id in old_streams:
                del self.active_streams[chat_id]
            
            self.last_cleanup = current_time
    
    async def get_stability_stats(self) -> Dict:
        """Get stability statistics"""
        await self.cleanup_old_streams()
        return {
            'active_streams': len(self.active_streams),
            'memory_warnings': self.memory_warnings,
            'total_retries': sum(data['retries'] for data in self.active_streams.values())
        }

# Global instance
song_stability = SongPlayStability()

# Auto cleanup task
async def stability_monitor():
    while True:
        try:
            # Continuous monitoring every 30 seconds
            await song_stability.cleanup_old_streams()
            await song_stability.check_memory_usage()
            
            # Proactive cleanup every 2 minutes
            await asyncio.sleep(30)
            
        except:
            await asyncio.sleep(30)

# Background cleanup task
async def background_cleanup():
    while True:
        try:
            # Force cleanup every 5 minutes
            await song_stability.proactive_cleanup()
            await asyncio.sleep(300)  # 5 minutes
        except:
            await asyncio.sleep(300)
