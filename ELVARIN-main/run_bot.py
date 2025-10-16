#!/usr/bin/env python3
"""
🎵 Elvarin X Music Bot - Run Script
This script runs the bot with proper error handling
"""

import sys
import os
import asyncio
from pathlib import Path

def check_requirements():
    """Check if all requirements are met"""
    print("🔍 Checking requirements...")
    
    # Check if .env file exists
    if not os.path.exists('.env'):
        print("❌ .env file not found!")
        print("💡 Please create .env file with your configuration")
        return False
    
    # Check if ElvarinXMusic directory exists
    if not os.path.exists('ElvarinXMusic'):
        print("❌ ElvarinXMusic directory not found!")
        print("💡 Please make sure you're in the correct directory")
        return False
    
    print("✅ Requirements check passed!")
    return True

def run_bot():
    """Run the bot"""
    try:
        print("🎵 Starting Elvarin X Music Bot...")
        print("=" * 50)
        
        # Import and run the bot
        from ElvarinXMusic import __main__
        
        # Run the bot
        asyncio.run(__main__.init())
        
    except KeyboardInterrupt:
        print("\n🛑 Bot stopped by user")
    except Exception as e:
        print(f"❌ Error starting bot: {e}")
        print("💡 Check your configuration and try again")

if __name__ == "__main__":
    print("🎵 Elvarin X Music Bot - Run Script")
    print("=" * 50)
    
    # Check requirements
    if not check_requirements():
        sys.exit(1)
    
    # Run the bot
    run_bot()
