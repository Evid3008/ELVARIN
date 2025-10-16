"""
Flood Protection System for Elvarin X Music Bot
Comprehensive rate limiting and flood prevention
"""

import time
import asyncio
from typing import Dict, List, Optional
from datetime import datetime, timedelta
from collections import defaultdict, deque

import config
from ElvarinXMusic import LOGGER


class FloodProtection:
    """Advanced flood protection system"""
    
    def __init__(self):
        self.user_commands: Dict[int, deque] = defaultdict(lambda: deque())
        self.user_cooldowns: Dict[int, float] = {}
        self.flood_violations: Dict[int, int] = defaultdict(int)
        self.banned_users: Dict[int, float] = {}
        self.command_stats: Dict[str, Dict[int, deque]] = defaultdict(lambda: defaultdict(lambda: deque()))
        
        # Cleanup task
        self.cleanup_task = None
        self.start_cleanup()
    
    def start_cleanup(self):
        """Start periodic cleanup task"""
        if self.cleanup_task is None or self.cleanup_task.done():
            self.cleanup_task = asyncio.create_task(self._cleanup_loop())
    
    async def _cleanup_loop(self):
        """Periodic cleanup of old data"""
        while True:
            try:
                await asyncio.sleep(60)  # Cleanup every minute
                await self._cleanup_old_data()
            except Exception as e:
                LOGGER.error(f"Flood protection cleanup error: {e}")
    
    async def _cleanup_old_data(self):
        """Clean up old command history and expired bans"""
        current_time = time.time()
        
        # Clean up old commands
        for user_id in list(self.user_commands.keys()):
            commands = self.user_commands[user_id]
            while commands and commands[0] < current_time - config.FLOOD_WINDOW:
                commands.popleft()
            
            if not commands:
                del self.user_commands[user_id]
        
        # Clean up expired cooldowns
        for user_id in list(self.user_commands.keys()):
            if self.user_cooldowns.get(user_id, 0) < current_time:
                self.user_cooldowns.pop(user_id, None)
        
        # Clean up expired bans
        for user_id in list(self.banned_users.keys()):
            if self.banned_users[user_id] < current_time:
                del self.banned_users[user_id]
                LOGGER.info(f"Flood ban expired for user {user_id}")
        
        # Clean up command-specific stats
        for command in list(self.command_stats.keys()):
            for user_id in list(self.command_stats[command].keys()):
                commands = self.command_stats[command][user_id]
                while commands and commands[0] < current_time - config.FLOOD_WINDOW:
                    commands.popleft()
                
                if not commands:
                    del self.command_stats[command][user_id]
            
            if not self.command_stats[command]:
                del self.command_stats[command]
    
    def is_user_banned(self, user_id: int) -> bool:
        """Check if user is currently banned for flooding"""
        if user_id in self.banned_users:
            if self.banned_users[user_id] > time.time():
                return True
            else:
                del self.banned_users[user_id]
        return False
    
    def is_on_cooldown(self, user_id: int) -> bool:
        """Check if user is on cooldown"""
        cooldown_end = self.user_cooldowns.get(user_id, 0)
        return cooldown_end > time.time()
    
    def get_cooldown_remaining(self, user_id: int) -> int:
        """Get remaining cooldown time in seconds"""
        cooldown_end = self.user_cooldowns.get(user_id, 0)
        remaining = int(cooldown_end - time.time())
        return max(0, remaining)
    
    def check_flood(self, user_id: int, command: str = None) -> tuple[bool, str]:
        """
        Check if user is flooding
        Returns: (is_flooding, message)
        """
        current_time = time.time()
        
        # Check if user is banned
        if self.is_user_banned(user_id):
            return True, "🚫 You are temporarily banned for flooding. Please wait before using commands."
        
        # Check cooldown
        if self.is_on_cooldown(user_id):
            remaining = self.get_cooldown_remaining(user_id)
            return True, f"⏳ Please wait {remaining} seconds before using commands again."
        
        # Add current command
        self.user_commands[user_id].append(current_time)
        
        # Check general flood limit
        recent_commands = [cmd for cmd in self.user_commands[user_id] 
                          if cmd > current_time - config.FLOOD_WINDOW]
        
        if len(recent_commands) > config.FLOOD_LIMIT:
            self._handle_flood_violation(user_id)
            return True, f"🚫 Flood detected! You can only use {config.FLOOD_LIMIT} commands per minute."
        
        # Check command-specific rate limits
        if command:
            self.command_stats[command][user_id].append(current_time)
            recent_cmd_commands = [cmd for cmd in self.command_stats[command][user_id]
                                 if cmd > current_time - config.FLOOD_WINDOW]
            
            rate_limit = self._get_command_rate_limit(command)
            if len(recent_cmd_commands) > rate_limit:
                self._handle_flood_violation(user_id)
                return True, f"🚫 Too many {command} commands! Max {rate_limit} per minute."
        
        return False, ""
    
    def _get_command_rate_limit(self, command: str) -> int:
        """Get rate limit for specific command"""
        command_lower = command.lower()
        
        if any(cmd in command_lower for cmd in ['play', 'vplay', 'p']):
            return config.RATE_LIMIT_PLAY
        elif any(cmd in command_lower for cmd in ['search', 'find']):
            return config.RATE_LIMIT_SEARCH
        elif any(cmd in command_lower for cmd in ['download', 'song']):
            return config.RATE_LIMIT_DOWNLOAD
        elif any(cmd in command_lower for cmd in ['vvplay']):
            return 1  # Very restrictive for vvplay
        elif any(cmd in command_lower for cmd in ['skip', 'pause', 'resume', 'stop']):
            return config.RATE_LIMIT_ADMIN
        else:
            return config.FLOOD_LIMIT // 2  # Default to half of general limit
    
    def _handle_flood_violation(self, user_id: int):
        """Handle flood violation"""
        self.flood_violations[user_id] += 1
        
        # Set cooldown
        cooldown_duration = config.FLOOD_COOLDOWN * self.flood_violations[user_id]
        self.user_cooldowns[user_id] = time.time() + cooldown_duration
        
        LOGGER.warning(f"Flood violation #{self.flood_violations[user_id]} for user {user_id}")
        
        # Auto-ban if enabled and violations exceed threshold
        if (config.FLOOD_AUTO_BAN and 
            self.flood_violations[user_id] >= 3):
            
            ban_duration = config.FLOOD_BAN_DURATION * self.flood_violations[user_id]
            self.banned_users[user_id] = time.time() + ban_duration
            
            LOGGER.error(f"Auto-banned user {user_id} for {ban_duration} seconds due to flooding")
    
    def set_cooldown(self, user_id: int, duration: int):
        """Set cooldown for user"""
        self.user_cooldowns[user_id] = time.time() + duration
    
    def get_command_cooldown(self, command: str) -> int:
        """Get cooldown duration for specific command"""
        command_lower = command.lower()
        
        if any(cmd in command_lower for cmd in ['vvplay']):
            return config.COOLDOWN_VVPLAY
        elif any(cmd in command_lower for cmd in ['play', 'vplay', 'p']):
            return config.COOLDOWN_PLAY
        elif any(cmd in command_lower for cmd in ['search', 'find']):
            return config.COOLDOWN_SEARCH
        elif any(cmd in command_lower for cmd in ['download', 'song']):
            return config.COOLDOWN_DOWNLOAD
        else:
            return 2  # Default cooldown
    
    def get_stats(self) -> Dict:
        """Get flood protection statistics"""
        return {
            "active_users": len(self.user_commands),
            "banned_users": len(self.banned_users),
            "cooldown_users": len(self.user_cooldowns),
            "total_violations": sum(self.flood_violations.values()),
            "command_stats": {cmd: len(users) for cmd, users in self.command_stats.items()}
        }


# Global flood protection instance
flood_protection = FloodProtection()


def flood_check(user_id: int, command: str = None) -> tuple[bool, str]:
    """Check if user is flooding"""
    return flood_protection.check_flood(user_id, command)


def set_command_cooldown(user_id: int, command: str):
    """Set cooldown for specific command"""
    duration = flood_protection.get_command_cooldown(command)
    flood_protection.set_cooldown(user_id, duration)


def is_user_banned(user_id: int) -> bool:
    """Check if user is banned"""
    return flood_protection.is_user_banned(user_id)


def get_flood_stats() -> Dict:
    """Get flood protection statistics"""
    return flood_protection.get_stats()
