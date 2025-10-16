"""
Female Chatbot Message Handler
Handles incoming messages and responds as female assistant
"""

import asyncio
from pyrogram import filters, Client
from pyrogram.types import Message

import config
from ElvarinXMusic import app, LOGGER
from ElvarinXMusic.utils.female_chatbot import process_chatbot_message
from ElvarinXMusic.utils.chat_learning import (
    record_target_message, 
    get_target_response, 
    get_learning_stats,
    is_learning_ready
)


@app.on_message(filters.text & filters.group & ~filters.bot & ~filters.me)
async def handle_chatbot_message(client: Client, message: Message):
    """Handle messages for female chatbot"""
    
    # Record target user's messages for learning
    username = message.from_user.username or ""
    record_target_message(
        message.text, 
        username, 
        message.chat.id, 
        message.id
    )
    
    # Check if chatbot is enabled
    if not config.CHATBOT_ENABLED:
        return
    
    # Skip if message is too short or contains commands
    if len(message.text) < 3 or message.text.startswith('/'):
        return
    
    # Skip if message mentions bot but is not a personal question
    if '@' in message.text and config.MUSIC_BOT_NAME.lower() not in message.text.lower():
        return
    
    try:
        user_id = message.from_user.id
        user_name = message.from_user.first_name or "User"
        
        # Try to get target user-style response first
        target_response = get_target_response(message.text)
        
        if target_response and is_learning_ready():
            # Use target user's style response
            await message.reply_text(
                f"@{message.from_user.username} {target_response}" if message.from_user.username 
                else f"{user_name} {target_response}",
                reply_to_message_id=message.id
            )
            return
        
        # Fallback to normal chatbot response
        response, should_tag = await process_chatbot_message(
            message.text, 
            user_id, 
            user_name
        )
        
        if should_tag:
            # Tag user and send response
            await message.reply_text(
                f"@{message.from_user.username} {response}" if message.from_user.username 
                else f"{user_name} {response}",
                reply_to_message_id=message.id
            )
        else:
            # Send response without tagging (for rate limit messages)
            await message.reply_text(response)
            
    except Exception as e:
        LOGGER.error(f"Chatbot message handler error: {e}")


@app.on_message(filters.command(["chatbot"]) & filters.group)
async def chatbot_info_command(client: Client, message: Message):
    """Show chatbot information"""
    
    if not config.CHATBOT_ENABLED:
        return await message.reply_text("❌ Chatbot is currently disabled.")
    
    stats = get_chatbot_stats()
    
    info_text = f"""
🤖 **Female Chatbot Assistant - Gudiya**

👤 **Name:** {stats['personal_data']['name']}
🎂 **Age:** {stats['personal_data']['age']} years (11th Class)
👨‍👩‍👧‍👦 **Family:** Special responses for family questions 😊
🏠 **Location:** {stats['personal_data']['city']}, {stats['personal_data']['state']}, {stats['personal_data']['country']}
💼 **Profession:** {stats['personal_data']['profession']}
✨ **Inspiration:** {stats['personal_data']['inspiration']}

📊 **Stats:**
• Active Users: {stats['active_users']}
• Gemini AI: {'✅ Available' if stats['gemini_available'] else '❌ Not Available'}

💬 **How to use:**
• Just mention me or ask personal questions
• I'll respond as a cute Bhopal girl
• Rate limit: {config.CHATBOT_RATE_LIMIT} messages per minute
• Special responses for family questions! 😉
    """
    
    await message.reply_text(info_text)


@app.on_message(filters.command(["chatbot_stats"]) & filters.group)
async def chatbot_stats_command(client: Client, message: Message):
    """Show detailed chatbot statistics"""
    
    if not config.CHATBOT_ENABLED:
        return await message.reply_text("❌ Chatbot is currently disabled.")
    
    stats = get_chatbot_stats()
    
    stats_text = f"""
📊 **Chatbot Statistics**

👥 **Users:**
• Active Users: {stats['active_users']}
• Cooldown Users: {stats['cooldown_users']}

🤖 **AI Status:**
• Gemini AI: {'✅ Connected' if stats['gemini_available'] else '❌ Disconnected'}
• Model: {config.GEMINI_MODEL}

⚙️ **Settings:**
• Rate Limit: {config.CHATBOT_RATE_LIMIT} msg/min
• Cooldown: {config.CHATBOT_COOLDOWN}s
• Max Tokens: {config.CHATBOT_MAX_TOKENS}
• Timeout: {config.CHATBOT_TIMEOUT}s
    """
    
    await message.reply_text(stats_text)


@app.on_message(filters.command(["learning_stats"]) & filters.group)
async def learning_stats_command(client: Client, message: Message):
    """Show learning system statistics"""
    
    if not config.LEARNING_ENABLED:
        return await message.reply_text("❌ Learning system is disabled.")
    
    stats = get_learning_stats()
    
    stats_text = f"""
📊 **Chat Learning System Stats**

👤 **Target User:** @{stats['target_username']}
📚 **Learning Status:** {'✅ Ready' if stats['can_generate_responses'] else '⏳ Learning...'}

📈 **Statistics:**
• Chats Observed: {stats['total_chats_observed']}
• Responses Learned: {stats['total_responses_learned']}
• Patterns Learned: {stats['patterns_learned']}
• Contexts Learned: {stats['contexts_learned']}

⚙️ **Settings:**
• Min Chats Required: {stats['min_chats_required']}
• Learning Enabled: {'✅ Yes' if stats['learning_enabled'] else '❌ No'}
• Can Generate Responses: {'✅ Yes' if stats['can_generate_responses'] else '❌ No'}

💡 **How it works:**
• Observes @{stats['target_username']} messages
• Learns response patterns and style
• Mimics responses when similar questions asked
• Requires {stats['min_chats_required']} chats to start learning
    """
    
    await message.reply_text(stats_text)


def get_chatbot_stats():
    """Get chatbot statistics"""
    from ElvarinXMusic.utils.female_chatbot import get_chatbot_stats as _get_stats
    return _get_stats()
