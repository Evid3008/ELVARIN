@app.on_message(
    filters.command(["vvplay"]) & filters.group & ~BANNED_USERS
)
@vvplay_flood_protect()
@stable_play
@quality_preserved
async def vvplay_command(client, message: Message):
    """Simple and reliable video play command"""
    language = await get_lang(message.chat.id)
    _ = get_string(language)
    
    if not message.reply_to_message:
        return await message.reply_text("❌ Please reply to a video file")
    
    if not message.reply_to_message.video:
        return await message.reply_text("❌ Please reply to a video file")
    
    mystic = await message.reply_text("🎬 Processing movie...")
    
    try:
        # Simple download
        await mystic.edit_text("📥 Downloading...")
        file_path = await Telegram.get_filepath(video=message.reply_to_message.video)
        
        await app.download_media(
            message.reply_to_message,
            file_name=file_path
        )
        
        if not os.path.exists(file_path):
            return await mystic.edit_text("❌ Download failed")
        
        await mystic.edit_text("✅ Downloaded!")
        
        # Simple conversion
        await mystic.edit_text("⚡ Converting...")
        output_path = file_path.replace(".mp4", "_vc.mp4")
        
        cmd = [
            "ffmpeg", "-i", file_path,
            "-c:v", "libx264", "-preset", "fast",
            "-c:a", "aac", "-b:a", "128k",
            "-y", output_path
        ]
        
        process = await asyncio.create_subprocess_exec(*cmd)
        await process.wait()
        
        if not os.path.exists(output_path):
            return await mystic.edit_text("❌ Conversion failed")
        
        await mystic.edit_text("✅ Converting complete!")
        
        # Simple streaming
        details = {
            "title": "Movie",
            "link": await Telegram.get_link(message),
            "path": output_path,
            "dur": 0,
        }
        
        await mystic.edit_text("🎬 Starting...")
        
        await stream(
            _,
            mystic,
            message.from_user.id,
            details,
            message.chat.id,
            message.from_user.first_name,
            message.chat.id,
            video=True,
            streamtype="telegram",
            forceplay=True,
        )
        
        await mystic.edit_text("✅ Movie started!")
        
        # Clean up
        try:
            os.remove(file_path)
            os.remove(output_path)
        except:
            pass
            
    except Exception as e:
        LOGGER(__name__).error(f"VVPlay error: {e}")
        await mystic.edit_text(f"❌ Error: {str(e)[:100]}...")
