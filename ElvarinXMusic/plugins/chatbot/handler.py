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


@app.on_message(filters.text & filters.group & ~filters.bot & ~filters.me)
async def handle_chatbot_message(client: Client, message: Message):
    """Handle messages for female chatbot"""
    
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
        
        # Process message through chatbot
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
🤖 **Female Chatbot Assistant**

👤 **Name:** {stats['personal_data']['name']}
🎂 **Age:** {stats['personal_data']['age']} years
👨‍👩‍👧‍👦 **Family:** {stats['personal_data']['father']} & {stats['personal_data']['mother']}
🏠 **Location:** {stats['personal_data']['city']}, {stats['personal_data']['state']}, {stats['personal_data']['country']}
💼 **Profession:** {stats['personal_data']['profession']}

📊 **Stats:**
• Active Users: {stats['active_users']}
• Gemini AI: {'✅ Available' if stats['gemini_available'] else '❌ Not Available'}

💬 **How to use:**
• Just mention me or ask personal questions
• I'll respond as a friendly Indian girl
• Rate limit: {config.CHATBOT_RATE_LIMIT} messages per minute
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


def get_chatbot_stats():
    """Get chatbot statistics"""
    from ElvarinXMusic.utils.female_chatbot import get_chatbot_stats as _get_stats
    return _get_stats()
