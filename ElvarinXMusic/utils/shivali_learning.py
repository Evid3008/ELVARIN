"""
Shivali Learning System
Observes and learns from Shivali's chat patterns to mimic her responses
"""

import json
import os
import time
import re
from typing import Dict, List, Optional, Tuple
from datetime import datetime
from collections import defaultdict, deque
import difflib

import config
from ElvarinXMusic import LOGGER


class ShivaliLearningSystem:
    """Learning system to observe and mimic Shivali's chat patterns"""
    
    def __init__(self):
        self.target_username = config.SHIVALI_USERNAME
        self.chat_file = config.SHIVALI_CHAT_FILE
        self.learning_enabled = config.SHIVALI_LEARNING_ENABLED
        self.min_chats_to_learn = config.SHIVALI_LEARNING_RATE
        self.similarity_threshold = config.SHIVALI_RESPONSE_SIMILARITY
        
        # Chat storage
        self.shivali_chats: List[Dict] = []
        self.response_patterns: Dict[str, List[str]] = defaultdict(list)
        self.chat_contexts: Dict[str, List[str]] = defaultdict(list)
        
        # Load existing data
        self.load_chat_data()
        
        # Statistics
        self.total_chats_observed = 0
        self.total_responses_learned = 0
        self.last_learning_time = 0
    
    def load_chat_data(self):
        """Load existing chat data from file"""
        try:
            if os.path.exists(self.chat_file):
                with open(self.chat_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    self.shivali_chats = data.get('chats', [])
                    self.response_patterns = data.get('patterns', {})
                    self.chat_contexts = data.get('contexts', {})
                    self.total_chats_observed = data.get('total_chats', 0)
                    self.total_responses_learned = data.get('total_responses', 0)
                    LOGGER.info(f"Loaded {len(self.shivali_chats)} Shivali chats from file")
        except Exception as e:
            LOGGER.error(f"Error loading chat data: {e}")
            self.shivali_chats = []
            self.response_patterns = {}
            self.chat_contexts = {}
    
    def save_chat_data(self):
        """Save chat data to file"""
        try:
            data = {
                'chats': self.shivali_chats[-1000:],  # Keep last 1000 chats
                'patterns': dict(self.response_patterns),
                'contexts': dict(self.chat_contexts),
                'total_chats': self.total_chats_observed,
                'total_responses': self.total_responses_learned,
                'last_updated': datetime.now().isoformat()
            }
            
            with open(self.chat_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
                
            LOGGER.info(f"Saved {len(self.shivali_chats)} Shivali chats to file")
        except Exception as e:
            LOGGER.error(f"Error saving chat data: {e}")
    
    def is_shivali_message(self, message_text: str, username: str) -> bool:
        """Check if message is from Shivali"""
        if not username or not message_text:
            return False
        
        # Check username match
        username_match = (
            username.lower() == self.target_username.lower() or
            f"@{self.target_username}" in username.lower() or
            self.target_username.lower() in username.lower()
        )
        
        return username_match and len(message_text.strip()) > 0
    
    def record_shivali_chat(self, message_text: str, chat_id: int, message_id: int, timestamp: float):
        """Record Shivali's chat for learning"""
        if not self.learning_enabled:
            return
        
        try:
            chat_data = {
                'text': message_text,
                'chat_id': chat_id,
                'message_id': message_id,
                'timestamp': timestamp,
                'date': datetime.fromtimestamp(timestamp).isoformat()
            }
            
            self.shivali_chats.append(chat_data)
            self.total_chats_observed += 1
            
            # Learn from the message
            self.learn_from_message(message_text)
            
            # Save periodically
            if len(self.shivali_chats) % 10 == 0:
                self.save_chat_data()
                
        except Exception as e:
            LOGGER.error(f"Error recording Shivali chat: {e}")
    
    def learn_from_message(self, message_text: str):
        """Learn patterns from Shivali's message"""
        try:
            # Extract patterns
            words = message_text.lower().split()
            
            # Learn response patterns
            for i, word in enumerate(words):
                if i < len(words) - 1:
                    next_word = words[i + 1]
                    self.response_patterns[word].append(next_word)
            
            # Learn context patterns
            if len(words) >= 2:
                context = ' '.join(words[:2])
                self.chat_contexts[context].append(message_text)
            
            self.total_responses_learned += 1
            
        except Exception as e:
            LOGGER.error(f"Error learning from message: {e}")
    
    def find_similar_context(self, user_message: str) -> Optional[str]:
        """Find similar context from Shivali's chats"""
        try:
            user_words = user_message.lower().split()
            best_match = None
            best_similarity = 0
            
            for context, responses in self.chat_contexts.items():
                context_words = context.split()
                
                # Calculate similarity
                similarity = difflib.SequenceMatcher(
                    None, 
                    ' '.join(user_words[:2]), 
                    context
                ).ratio()
                
                if similarity > best_similarity and similarity >= self.similarity_threshold:
                    best_similarity = similarity
                    best_match = context
            
            return best_match
            
        except Exception as e:
            LOGGER.error(f"Error finding similar context: {e}")
            return None
    
    def generate_shivali_response(self, user_message: str) -> Optional[str]:
        """Generate response mimicking Shivali's style"""
        if not self.learning_enabled or len(self.shivali_chats) < self.min_chats_to_learn:
            return None
        
        try:
            # Find similar context
            similar_context = self.find_similar_context(user_message)
            
            if similar_context and similar_context in self.chat_contexts:
                # Get responses for similar context
                responses = self.chat_contexts[similar_context]
                
                if responses:
                    # Return a random response from similar context
                    import random
                    return random.choice(responses)
            
            # Fallback: find similar words and generate response
            user_words = user_message.lower().split()
            response_words = []
            
            for word in user_words:
                if word in self.response_patterns:
                    # Get next word pattern
                    next_words = self.response_patterns[word]
                    if next_words:
                        import random
                        response_words.append(random.choice(next_words))
            
            if response_words:
                return ' '.join(response_words)
            
            return None
            
        except Exception as e:
            LOGGER.error(f"Error generating Shivali response: {e}")
            return None
    
    def get_learning_stats(self) -> Dict:
        """Get learning system statistics"""
        return {
            'learning_enabled': self.learning_enabled,
            'target_username': self.target_username,
            'total_chats_observed': self.total_chats_observed,
            'total_responses_learned': self.total_responses_learned,
            'patterns_learned': len(self.response_patterns),
            'contexts_learned': len(self.chat_contexts),
            'min_chats_required': self.min_chats_to_learn,
            'can_generate_responses': len(self.shivali_chats) >= self.min_chats_to_learn,
            'last_chat_count': len(self.shivali_chats)
        }
    
    def is_ready_to_learn(self) -> bool:
        """Check if system has enough data to learn"""
        return len(self.shivali_chats) >= self.min_chats_to_learn
    
    def get_recent_chats(self, count: int = 5) -> List[Dict]:
        """Get recent chats from Shivali"""
        return self.shivali_chats[-count:] if self.shivali_chats else []


# Global learning system instance
shivali_learning = ShivaliLearningSystem()


def record_shivali_message(message_text: str, username: str, chat_id: int, message_id: int):
    """Record message if it's from Shivali"""
    if shivali_learning.is_shivali_message(message_text, username):
        shivali_learning.record_shivali_chat(message_text, chat_id, message_id, time.time())


def get_shivali_response(user_message: str) -> Optional[str]:
    """Get Shivali-style response"""
    return shivali_learning.generate_shivali_response(user_message)


def get_learning_stats() -> Dict:
    """Get learning system statistics"""
    return shivali_learning.get_learning_stats()


def is_learning_ready() -> bool:
    """Check if learning system is ready"""
    return shivali_learning.is_ready_to_learn()
