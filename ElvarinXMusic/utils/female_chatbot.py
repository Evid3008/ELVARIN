"""
Female Chatbot Assistant System
Intelligent AI-powered assistant with personal data and controlled responses
"""

import asyncio
import time
import re
from typing import Dict, List, Optional, Tuple
from datetime import datetime, timedelta
from collections import defaultdict, deque

import config
from ElvarinXMusic import LOGGER

try:
    import google.generativeai as genai
    GEMINI_AVAILABLE = True
except ImportError:
    GEMINI_AVAILABLE = False
    LOGGER.warning("Google Generative AI not available. Install with: pip install google-generativeai")


class FemaleChatbot:
    """Intelligent female chatbot assistant with personal data"""
    
    def __init__(self):
        self.personal_data = {
            "name": config.CHATBOT_NAME,
            "age": config.CHATBOT_AGE,
            "father": config.CHATBOT_FATHER,
            "mother": config.CHATBOT_MOTHER,
            "state": config.CHATBOT_STATE,
            "city": config.CHATBOT_CITY,
            "country": config.CHATBOT_COUNTRY,
            "profession": config.CHATBOT_PROFESSION,
            "personality": config.CHATBOT_PERSONALITY
        }
        
        # Rate limiting
        self.user_responses: Dict[int, deque] = defaultdict(lambda: deque())
        self.user_cooldowns: Dict[int, float] = {}
        
        # Initialize Gemini AI
        self.gemini_model = None
        if GEMINI_AVAILABLE and config.GEMINI_API_KEY:
            try:
                genai.configure(api_key=config.GEMINI_API_KEY)
                self.gemini_model = genai.GenerativeModel(config.GEMINI_MODEL)
                LOGGER.info("Gemini AI initialized successfully")
            except Exception as e:
                LOGGER.error(f"Failed to initialize Gemini AI: {e}")
        
        # Personal data keywords for detection
        self.personal_keywords = {
            "name": ["name", "naam", "what's your name", "tumhara naam", "apka naam"],
            "age": ["age", "umar", "how old", "kitne saal", "age kya hai"],
            "father": ["father", "papa", "dad", "baap", "father's name"],
            "mother": ["mother", "mummy", "mom", "maa", "mother's name"],
            "state": ["state", "rajya", "which state", "konsa state"],
            "city": ["city", "sheher", "which city", "konsa city", "kahan rehti ho"],
            "country": ["country", "desh", "which country", "konsa country"],
            "profession": ["profession", "job", "work", "kaam", "what do you do"]
        }
        
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
                LOGGER.error(f"Chatbot cleanup error: {e}")
    
    async def _cleanup_old_data(self):
        """Clean up old response history"""
        current_time = time.time()
        
        for user_id in list(self.user_responses.keys()):
            responses = self.user_responses[user_id]
            while responses and responses[0] < current_time - 60:  # Keep last minute
                responses.popleft()
            
            if not responses:
                del self.user_responses[user_id]
        
        # Clean up expired cooldowns
        for user_id in list(self.user_cooldowns.keys()):
            if self.user_cooldowns.get(user_id, 0) < current_time:
                self.user_cooldowns.pop(user_id, None)
    
    def is_on_cooldown(self, user_id: int) -> bool:
        """Check if user is on cooldown"""
        cooldown_end = self.user_cooldowns.get(user_id, 0)
        return cooldown_end > time.time()
    
    def get_cooldown_remaining(self, user_id: int) -> int:
        """Get remaining cooldown time in seconds"""
        cooldown_end = self.user_cooldowns.get(user_id, 0)
        remaining = int(cooldown_end - time.time())
        return max(0, remaining)
    
    def check_rate_limit(self, user_id: int) -> Tuple[bool, str]:
        """Check if user has exceeded rate limit"""
        current_time = time.time()
        
        # Check cooldown
        if self.is_on_cooldown(user_id):
            remaining = self.get_cooldown_remaining(user_id)
            return True, f"⏳ Please wait {remaining} seconds before asking again."
        
        # Add current response
        self.user_responses[user_id].append(current_time)
        
        # Check rate limit
        recent_responses = [resp for resp in self.user_responses[user_id] 
                           if resp > current_time - 60]  # Last minute
        
        if len(recent_responses) > config.CHATBOT_RATE_LIMIT:
            self.user_cooldowns[user_id] = time.time() + config.CHATBOT_COOLDOWN
            return True, f"🚫 Too many messages! Max {config.CHATBOT_RATE_LIMIT} per minute."
        
        return False, ""
    
    def detect_personal_question(self, message: str) -> Optional[str]:
        """Detect if message is asking about personal data"""
        message_lower = message.lower()
        
        for data_type, keywords in self.personal_keywords.items():
            for keyword in keywords:
                if keyword in message_lower:
                    return data_type
        
        return None
    
    def get_personal_response(self, data_type: str, user_name: str) -> str:
        """Get response for personal data questions"""
        responses = {
            "name": f"Hi {user_name}! My name is {self.personal_data['name']} 😊",
            "age": f"I'm {self.personal_data['age']} years old! Still young and energetic 💫",
            "father": f"My father's name is {self.personal_data['father']} 🥰",
            "mother": f"My mother's name is {self.personal_data['mother']} ❤️",
            "state": f"I'm from {self.personal_data['state']}! Beautiful state 🌟",
            "city": f"I live in {self.personal_data['city']}! Love this city 🏙️",
            "country": f"I'm from {self.personal_data['country']}! Proud to be Indian 🇮🇳",
            "profession": f"I work as a {self.personal_data['profession']}! Love helping with music 🎵"
        }
        
        return responses.get(data_type, f"I'm {self.personal_data['name']}, nice to meet you! 😊")
    
    async def get_ai_response(self, message: str, user_name: str) -> str:
        """Get AI response using Gemini"""
        if not self.gemini_model:
            return f"Hi {user_name}! I'm {self.personal_data['name']}, your music assistant! How can I help you today? 🎵"
        
        try:
            # Create personality prompt
            personality_prompt = f"""
            You are {self.personal_data['name']}, a {self.personal_data['personality']} from {self.personal_data['city']}, {self.personal_data['state']}, {self.personal_data['country']}.
            
            Rules:
            1. Always respond as a friendly Indian girl
            2. Keep responses under {config.CHATBOT_MAX_TOKENS} characters
            3. Use emojis and be cheerful
            4. Don't reveal you're an AI
            5. Be helpful and supportive
            6. Use Hindi/English mix naturally
            
            User message: {message}
            User name: {user_name}
            
            Respond as {self.personal_data['name']}:
            """
            
            # Get AI response with timeout
            response = await asyncio.wait_for(
                self._get_gemini_response(personality_prompt),
                timeout=config.CHATBOT_TIMEOUT
            )
            
            # Clean and limit response
            response = self._clean_response(response)
            return response[:config.CHATBOT_MAX_TOKENS]
            
        except asyncio.TimeoutError:
            return f"Sorry {user_name}, I'm a bit busy right now! Try again in a moment 😅"
        except Exception as e:
            LOGGER.error(f"AI response error: {e}")
            return f"Hi {user_name}! I'm {self.personal_data['name']}! How can I help you? 🎵"
    
    async def _get_gemini_response(self, prompt: str) -> str:
        """Get response from Gemini AI"""
        try:
            response = self.gemini_model.generate_content(prompt)
            return response.text
        except Exception as e:
            LOGGER.error(f"Gemini API error: {e}")
            raise e
    
    def _clean_response(self, response: str) -> str:
        """Clean AI response"""
        # Remove any AI-related mentions
        response = re.sub(r'\b(ai|artificial intelligence|bot|assistant)\b', 'I', response, flags=re.IGNORECASE)
        
        # Ensure it starts with a greeting or response
        if not response.strip():
            return "Hi! How can I help you? 😊"
        
        return response.strip()
    
    async def process_message(self, message: str, user_id: int, user_name: str) -> Tuple[str, bool]:
        """
        Process user message and return response
        Returns: (response, should_tag_user)
        """
        # Check rate limit
        is_limited, limit_message = self.check_rate_limit(user_id)
        if is_limited:
            return limit_message, False
        
        # Detect personal questions
        personal_type = self.detect_personal_question(message)
        if personal_type:
            response = self.get_personal_response(personal_type, user_name)
            return response, True
        
        # Get AI response for general questions
        response = await self.get_ai_response(message, user_name)
        return response, True
    
    def get_stats(self) -> Dict:
        """Get chatbot statistics"""
        return {
            "active_users": len(self.user_responses),
            "cooldown_users": len(self.user_cooldowns),
            "gemini_available": self.gemini_model is not None,
            "personal_data": self.personal_data
        }


# Global chatbot instance
female_chatbot = FemaleChatbot()


async def process_chatbot_message(message: str, user_id: int, user_name: str) -> Tuple[str, bool]:
    """Process message through female chatbot"""
    return await female_chatbot.process_message(message, user_id, user_name)


def get_chatbot_stats() -> Dict:
    """Get chatbot statistics"""
    return female_chatbot.get_stats()
