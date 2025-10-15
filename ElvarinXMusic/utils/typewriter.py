import asyncio
from pyrogram.types import Message


async def typewriter_effect(message: Message, text: str, delay: float = 0.2):
    """
    Create a typewriter effect for text with animated dots
    Flood protection included to prevent Telegram API limits
    """
    # Split the text into main text and dots part
    if "..." in text:
        main_text, dots_part = text.split("...", 1)
        dots_part = "..." + dots_part
    else:
        main_text = text
        dots_part = ""
    
    # Type the main text character by character with flood protection
    current_text = ""
    for char in main_text:
        current_text += char
        try:
            await message.edit_text(current_text + dots_part)
            await asyncio.sleep(delay * 2)  # Slower to prevent flood
        except:
            pass
    
    # If there are dots, animate them with limited cycles
    if dots_part.startswith("..."):
        dot_variations = [".", "..", "...", "....", "...", "..", "."]
        max_cycles = 2  # Reduced cycles to prevent flood
        
        for cycle in range(max_cycles):
            for dots in dot_variations:
                try:
                    await message.edit_text(main_text + dots)
                    await asyncio.sleep(0.8)  # Much slower to prevent flood
                except:
                    pass
            
            # Additional delay between cycles
            if cycle < max_cycles - 1:
                await asyncio.sleep(1.5)
    
    return message


async def processing_with_typewriter(message: Message, base_text: str = "✨ 𝑷𝒓𝒐𝒄𝒆𝒔𝒔𝒊𝒏𝒈", delay: float = 0.1):
    """
    Show processing message with typewriter effect and animated dots
    Flood protection included to prevent Telegram API limits
    """
    # First show the base text
    try:
        await message.edit_text(base_text)
        await asyncio.sleep(1.0)  # Longer delay to prevent flood
    except:
        pass
    
    # Then add dots with animation - limited cycles to prevent flood
    dot_variations = [".", "..", "...", "....", "...", "..", "."]
    max_cycles = 3  # Reduced cycles to prevent flood
    
    for cycle in range(max_cycles):
        for dots in dot_variations:
            try:
                await message.edit_text(base_text + dots)
                await asyncio.sleep(1.2)  # Much slower to prevent flood
            except:
                pass
        
        # Additional delay between cycles
        if cycle < max_cycles - 1:
            await asyncio.sleep(2.0)
    
    return message
