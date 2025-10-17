import asyncio
import random
from pyrogram.types import Message


def get_random_emoji():
    """
    Get a random animated emoji from the list
    """
    emojis = [
        "👀", "🦋", "🐰", "🐟", "🌸", "🎬", "🎲", "🪄", "🐱", "🔍",
        "👁", "🎃", "🎄", "🎆", "🎇", "✨", "🎉", "🎊", "🎈", "🍭",
        "🐈", "🐇", "🐁", "🐖", "🎲"
    ]
    return random.choice(emojis)


async def random_emoji_animation(message: Message):
    """
    Show random animated emoji instead of typewriter effect
    Creates a simple emoji drop animation
    """
    # List of random emojis for animation - only large animated ones in Telegram
    emojis = [
        "👀", "🦋", "🐰", "🐟", "🌸", "🎬", "🎲", "🪄", "🐱", "🔍",
        "👁", "🎃", "🎄", "🎆", "🎇", "✨", "🎉", "🎊", "🎈", "🍭",
        "🐈", "🐇", "🐁", "🐖", "🎲"
    ]
    
    # Select a random emoji
    selected_emoji = random.choice(emojis)
    
    # Simple animation - emoji appears and stays
    try:
        await message.edit_text(f"{selected_emoji}")
        await asyncio.sleep(0.5)  # Short delay
    except:
        pass
    
    return message


async def processing_with_typewriter(message: Message, base_text: str = "✨ 𝑷𝒓𝒐𝒄𝒆𝒔𝒔𝒊𝒏𝒈", delay: float = 0.1):
    """
    Show random emoji animation instead of typewriter effect
    """
    # List of random emojis for animation - only large animated ones in Telegram
    emojis = [
        "👀", "🦋", "🐰", "🐟", "🌸", "🎬", "🎲", "🪄", "🐱", "🔍",
        "👁", "🎃", "🎄", "🎆", "🎇", "✨", "🎉", "🎊", "🎈", "🍭",
        "🐈", "🐇", "🐁", "🐖", "🎲"
    ]
    
    # Select a random emoji
    selected_emoji = random.choice(emojis)
    
    # Replace the message with just the emoji
    try:
        await message.edit_text(f"{selected_emoji}")
        await asyncio.sleep(0.5)  # Short delay
    except:
        pass
    
    return message
