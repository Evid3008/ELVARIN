import re
import os
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID", "27331305"))
API_HASH = getenv("API_HASH", "ed125c760d1c0362d263d8d86fc9cac7")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN", "7295133595:AAGIYk7ehk_Xr4eByiv07HhT7T-XDU")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb://localhost:27017/ElvarinXMusic")
MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME", "Elvarin X Music")
PRIVATE_BOT_MODE = getenv("PRIVATE_BOT_MODE", None)

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 900))

# Audio Quality Settings (Premium Quality for Telegram/Heroku)
AUDIO_QUALITY = getenv("AUDIO_QUALITY", "STUDIO")  # STUDIO quality for premium sound
AUDIO_BITRATE = getenv("AUDIO_BITRATE", "320k")  # High bitrate for premium quality
AUDIO_SAMPLE_RATE = getenv("AUDIO_SAMPLE_RATE", "48000")  # 48kHz for premium quality
AUDIO_CHANNELS = getenv("AUDIO_CHANNELS", "2")  # Stereo for premium sound
MAX_FILE_SIZE = getenv("MAX_FILE_SIZE", "50MB")
# Enhanced audio filters for premium sound quality
AUDIO_FILTERS = getenv("AUDIO_FILTERS", "bass=g=15:f=120,treble=g=8:f=12000,volume=1.3,highpass=f=20,lowpass=f=22000,compand=.3|.3:1|1:-90/-60|-60/-40|-40/-30|-20/-20:6:0:-90:0.2")

# Female Chatbot Assistant Settings
CHATBOT_ENABLED = bool(getenv("CHATBOT_ENABLED", "True"))  # Enable female chatbot
CHATBOT_NAME = getenv("CHATBOT_NAME", "Gudiya")  # Assistant name
CHATBOT_AGE = getenv("CHATBOT_AGE", "17")  # Assistant age (11th class)
CHATBOT_FATHER = getenv("CHATBOT_FATHER", "Papa")  # Father's name
CHATBOT_MOTHER = getenv("CHATBOT_MOTHER", "Mummy")  # Mother's name
CHATBOT_STATE = getenv("CHATBOT_STATE", "Madhya Pradesh")  # State
CHATBOT_CITY = getenv("CHATBOT_CITY", "Bhopal")  # City
CHATBOT_COUNTRY = getenv("CHATBOT_COUNTRY", "India")  # Country
CHATBOT_PROFESSION = getenv("CHATBOT_PROFESSION", "Student (11th Class)")  # Profession
CHATBOT_INSPIRATION = getenv("CHATBOT_INSPIRATION", "Shivali")  # Inspiration

# Gemini AI Settings
GEMINI_API_KEY = getenv("GEMINI_API_KEY", "AIzaSyA6kIR_P6IvrbQwADvsWo77vifSPQLCx5M")  # Gemini API key
GEMINI_MODEL = getenv("GEMINI_MODEL", "gemini-pro")  # Gemini model
CHATBOT_PERSONALITY = getenv("CHATBOT_PERSONALITY", "cute, playful, and sassy Indian girl from Bhopal")  # Personality

# Chatbot Performance Settings
CHATBOT_RATE_LIMIT = int(getenv("CHATBOT_RATE_LIMIT", "5"))  # Max responses per minute per user
CHATBOT_COOLDOWN = int(getenv("CHATBOT_COOLDOWN", "10"))  # Cooldown between responses
CHATBOT_MAX_TOKENS = int(getenv("CHATBOT_MAX_TOKENS", "150"))  # Max response length
CHATBOT_TIMEOUT = int(getenv("CHATBOT_TIMEOUT", "10"))  # AI response timeout in seconds

# Flood Protection Settings (Critical for Bot Stability)
FLOOD_LIMIT = int(getenv("FLOOD_LIMIT", "10"))  # Max commands per minute per user
FLOOD_WINDOW = int(getenv("FLOOD_WINDOW", "60"))  # Time window in seconds
FLOOD_COOLDOWN = int(getenv("FLOOD_COOLDOWN", "30"))  # Cooldown period in seconds
FLOOD_AUTO_BAN = bool(getenv("FLOOD_AUTO_BAN", "True"))  # Auto-ban flooders
FLOOD_BAN_DURATION = int(getenv("FLOOD_BAN_DURATION", "3600"))  # Ban duration in seconds (1 hour)

# Rate Limiting Settings
RATE_LIMIT_PLAY = int(getenv("RATE_LIMIT_PLAY", "3"))  # Max play commands per minute
RATE_LIMIT_SEARCH = int(getenv("RATE_LIMIT_SEARCH", "5"))  # Max search commands per minute
RATE_LIMIT_DOWNLOAD = int(getenv("RATE_LIMIT_DOWNLOAD", "2"))  # Max download commands per minute
RATE_LIMIT_ADMIN = int(getenv("RATE_LIMIT_ADMIN", "10"))  # Max admin commands per minute

# Command Cooldowns (in seconds)
COOLDOWN_PLAY = int(getenv("COOLDOWN_PLAY", "5"))  # Play command cooldown
COOLDOWN_SEARCH = int(getenv("COOLDOWN_SEARCH", "3"))  # Search command cooldown
COOLDOWN_DOWNLOAD = int(getenv("COOLDOWN_DOWNLOAD", "10"))  # Download command cooldown
COOLDOWN_VVPLAY = int(getenv("COOLDOWN_VVPLAY", "15"))  # VVPlay command cooldown (longer due to processing)

# Stability Settings
MAX_RETRIES = int(getenv("MAX_RETRIES", "3"))
RETRY_DELAY = int(getenv("RETRY_DELAY", "5"))
CACHE_DURATION = int(getenv("CACHE_DURATION", "100"))
OVERLOAD_QUIET_MODE = getenv("OVERLOAD_QUIET_MODE", "True")
HEALTH_CHECK_INTERVAL = int(getenv("HEALTH_CHECK_INTERVAL", "30"))
MEMORY_CLEANUP_INTERVAL = int(getenv("MEMORY_CLEANUP_INTERVAL", "300"))

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", "-1002004045879"))

# Get this value from @BRANDRD_ROBOT on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", "5467532693"))

# Sudo users list
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5467532693 7732630047").split()))

# String Sessions
STRING1 = getenv("STRING1", None)
STRING2 = getenv("STRING2", None)
STRING3 = getenv("STRING3", None)
STRING4 = getenv("STRING4", None)
STRING5 = getenv("STRING5", None)

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/Evid3008/ELVARIN",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/TheAda_Channel")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/iq4us")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))

# Auto Gcast/Broadcast Handler (True = broadcast on , False = broadcast off During Hosting, Dont Do anything here.)
AUTO_GCAST = os.getenv("AUTO_GCAST")

# Auto Broadcast Message That You Want Use In Auto Broadcast In All Groups.
AUTO_GCAST_MSG = getenv("AUTO_GCAST_MSG", "")

# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "bcfe26b0ebc3428882a0b5fb3e872473")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "907c6a054c214005aeae1fd752273cc4")


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "50"))
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "25"))

SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "180"))
SONG_DOWNLOAD_DURATION_LIMIT = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "2000"))

# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @ELVARINSTRINGSESSION_BOT on Telegram
STRING1 = getenv("STRING_SESSION",  None)
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://files.catbox.moe/amrrdr.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://files.catbox.moe/x7iaev.jpg"
)
PLAYLIST_IMG_URL = "https://files.catbox.moe/bp9fza.jpg"
STATS_IMG_URL = "https://files.catbox.moe/nu138k.jpg"
TELEGRAM_AUDIO_URL = "https://files.catbox.moe/1g8z92.jpg"
TELEGRAM_VIDEO_URL = "https://files.catbox.moe/wnuci8.jpg"
STREAM_IMG_URL = "https://graph.org/file/e3d83ef044282deb07c4d-84f7233dc4f7aba8d0.jpg"
SOUNCLOUD_IMG_URL = "https://graph.org/file/6735bb8fa411ac0f2077f-d144a1aaf93762ef04.jpg"
YOUTUBE_IMG_URL = "https://graph.org/file/3a1371f58388c955510c9-d7e12d85ca16b14e0a.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://graph.org/file/3fa4726ac7ed75c14458d-5ea4995d76db809584.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://graph.org/file/f7158ea1e22c33dacfbeb-7565f9a37a20210a18.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://graph.org/file/b6b9e9cbc969747840e58-b7c11d4ac68cce40bd.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
