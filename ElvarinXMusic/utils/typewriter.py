import asyncio
from pyrogram.types import Message


async def typewriter_effect(message: Message, text: str, delay: float = 0.1):
    """
    Create a typewriter effect for text with animated dots
    """
    # Split the text into main text and dots part
    if "..." in text:
        main_text, dots_part = text.split("...", 1)
        dots_part = "..." + dots_part
    else:
        main_text = text
        dots_part = ""
    
    # Type the main text character by character
    current_text = ""
    for char in main_text:
        current_text += char
        try:
            await message.edit_text(current_text + dots_part)
            await asyncio.sleep(delay)
        except:
            pass
    
    # If there are dots, animate them
    if dots_part.startswith("..."):
        dot_variations = [".", "..", "...", "....", "...", "..", "."]
        for _ in range(3):  # Repeat the animation 3 times
            for dots in dot_variations:
                try:
                    await message.edit_text(main_text + dots)
                    await asyncio.sleep(0.3)
                except:
                    pass
    
    return message


async def processing_with_typewriter(message: Message, base_text: str = "✨ 𝑷𝒓𝒐𝒄𝒆𝒔𝒔𝒊𝒏𝒈", delay: float = 0.1):
    """
    Show processing message with typewriter effect and animated dots
    """
    # First show the base text
    try:
        await message.edit_text(base_text)
        await asyncio.sleep(0.5)
    except:
        pass
    
    # Then add dots with animation
    dot_variations = [".", "..", "...", "....", "...", "..", "."]
    for _ in range(5):  # Repeat the animation 5 times
        for dots in dot_variations:
            try:
                await message.edit_text(base_text + dots)
                await asyncio.sleep(0.4)
            except:
                pass
    
    return message
