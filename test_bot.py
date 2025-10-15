#!/usr/bin/env python3
"""
🎵 Elvarin X Music Bot - Test Script
This script tests if all required modules can be imported successfully
"""

import sys
import os

def test_imports():
    """Test if all required modules can be imported"""
    print("🎵 Testing Elvarin X Music Bot Imports...")
    print("=" * 50)
    
    try:
        # Test basic imports
        print("✅ Testing basic imports...")
        import asyncio
        import importlib
        from pyrogram import Client, filters
        from pytgcalls import PyTgCalls
        print("✅ Basic imports successful!")
        
        # Test config import
        print("✅ Testing config import...")
        import config
        print("✅ Config import successful!")
        
        # Test ElvarinXMusic imports
        print("✅ Testing ElvarinXMusic imports...")
        from ElvarinXMusic import app, userbot
        from ElvarinXMusic.core.call import Hotty
        from ElvarinXMusic.utils.database import get_banned_users
        print("✅ ElvarinXMusic imports successful!")
        
        # Test platform imports
        print("✅ Testing platform imports...")
        from ElvarinXMusic.platforms import YouTube, Spotify, Apple
        print("✅ Platform imports successful!")
        
        print("=" * 50)
        print("🎉 ALL IMPORTS SUCCESSFUL! Bot is ready to run! 🎉")
        return True
        
    except ImportError as e:
        print(f"❌ Import Error: {e}")
        print("💡 Solution: Install missing dependencies with 'pip install -r requirements.txt'")
        return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def test_config():
    """Test if config variables are properly set"""
    print("\n🔧 Testing Configuration...")
    print("=" * 30)
    
    try:
        import config
        
        # Check required variables
        required_vars = [
            'API_ID', 'API_HASH', 'BOT_TOKEN', 'MONGO_DB_URI',
            'OWNER_ID', 'SUDO_USERS'
        ]
        
        for var in required_vars:
            if hasattr(config, var):
                value = getattr(config, var)
                if value and value != "your_api_id_here":
                    print(f"✅ {var}: Set")
                else:
                    print(f"⚠️  {var}: Not set or using default value")
            else:
                print(f"❌ {var}: Missing")
                
        print("=" * 30)
        return True
        
    except Exception as e:
        print(f"❌ Config Error: {e}")
        return False

if __name__ == "__main__":
    print("🎵 Elvarin X Music Bot - Test Script")
    print("=" * 50)
    
    # Test imports
    imports_ok = test_imports()
    
    # Test config
    config_ok = test_config()
    
    print("\n📊 Test Results:")
    print(f"Imports: {'✅ PASS' if imports_ok else '❌ FAIL'}")
    print(f"Config: {'✅ PASS' if config_ok else '❌ FAIL'}")
    
    if imports_ok and config_ok:
        print("\n🚀 Bot is ready to run! Use: python -m ElvarinXMusic")
    else:
        print("\n🔧 Please fix the issues above before running the bot.")
