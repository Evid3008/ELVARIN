import time
import asyncio
from collections import defaultdict, deque
from typing import Dict, Set, Optional
import config

class FloodProtection:
    def __init__(self):
        self.user_commands = defaultdict(lambda: deque())
        self.user_violations = defaultdict(int)
        self.banned_users = set()
        self.cooldowns = defaultdict(float)
        
    def flood_check(self, user_id: int, command: str) -> tuple[bool, str]:
        """Check if user is flooding commands"""
        current_time = time.time()
        
        # Check if user is banned
        if user_id in self.banned_users:
            return False, "🚫 You are temporarily banned for flooding. Try again later."
        
        # Check cooldown
        cooldown_key = f"{user_id}_{command}"
        if current_time < self.cooldowns.get(cooldown_key, 0):
            remaining = int(self.cooldowns[cooldown_key] - current_time)
            return False, f"⏳ Please wait {remaining} seconds before using {command} again."
        
        # Get command limits
        limits = {
            "play": config.RATE_LIMIT_PLAY,
            "search": config.RATE_LIMIT_SEARCH,
            "download": config.RATE_LIMIT_DOWNLOAD,
            "vvplay": config.RATE_LIMIT_DOWNLOAD,
            "admin": config.RATE_LIMIT_ADMIN
        }
        
        cooldowns = {
            "play": config.COOLDOWN_PLAY,
            "search": config.COOLDOWN_SEARCH,
            "download": config.COOLDOWN_DOWNLOAD,
            "vvplay": config.COOLDOWN_VVPLAY,
            "admin": 1
        }
        
        limit = limits.get(command, 3)
        cooldown = cooldowns.get(command, 5)
        
        # Clean old commands
        user_commands = self.user_commands[user_id]
        while user_commands and current_time - user_commands[0] > config.FLOOD_WINDOW:
            user_commands.popleft()
        
        # Check if limit exceeded
        if len(user_commands) >= limit:
            self.user_violations[user_id] += 1
            
            # Auto-ban if too many violations
            if config.FLOOD_AUTO_BAN and self.user_violations[user_id] >= 3:
                self.banned_users.add(user_id)
                return False, f"🚫 Banned for {config.FLOOD_BAN_DURATION//60} minutes due to repeated flooding."
            
            return False, f"⚠️ Too many {command} commands. Wait {config.FLOOD_COOLDOWN} seconds."
        
        # Add command and set cooldown
        user_commands.append(current_time)
        self.cooldowns[cooldown_key] = current_time + cooldown
        
        return True, ""
    
    def set_command_cooldown(self, user_id: int, command: str, duration: int):
        """Set manual cooldown for user"""
        cooldown_key = f"{user_id}_{command}"
        self.cooldowns[cooldown_key] = time.time() + duration
    
    def is_user_banned(self, user_id: int) -> bool:
        """Check if user is banned"""
        return user_id in self.banned_users
    
    def cleanup_old_data(self):
        """Clean up old data to prevent memory leaks"""
        current_time = time.time()
        
        # Clean old commands
        for user_id in list(self.user_commands.keys()):
            user_commands = self.user_commands[user_id]
            while user_commands and current_time - user_commands[0] > config.FLOOD_WINDOW * 2:
                user_commands.popleft()
            
            if not user_commands:
                del self.user_commands[user_id]
        
        # Clean old cooldowns
        for key in list(self.cooldowns.keys()):
            if current_time > self.cooldowns[key]:
                del self.cooldowns[key]
        
        # Clean old violations
        for user_id in list(self.user_violations.keys()):
            if user_id not in self.user_commands:
                del self.user_violations[user_id]
    
    def get_flood_stats(self) -> Dict:
        """Get flood protection statistics"""
        return {
            "active_users": len(self.user_commands),
            "banned_users": len(self.banned_users),
            "total_violations": sum(self.user_violations.values()),
            "active_cooldowns": len(self.cooldowns)
        }

# Global instance
flood_protection = FloodProtection()

# Auto cleanup task
async def auto_cleanup():
    while True:
        await asyncio.sleep(config.MEMORY_CLEANUP_INTERVAL)
        flood_protection.cleanup_old_data()
