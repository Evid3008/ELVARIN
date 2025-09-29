# 🎵 Elvarin X Music Bot - Setup Guide

## 📋 Prerequisites

1. **Python 3.8+** installed on your system
2. **Git** installed
3. **Telegram Account** for API credentials
4. **MongoDB Account** for database

## 🔧 Step-by-Step Setup

### 1. Clone the Repository
```bash
git clone https://github.com/Evid3008/ELVARIN.git
cd ELVARIN
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Get API Credentials

#### Telegram API (Required)
1. Go to https://my.telegram.org/apps
2. Create a new application
3. Get your `API_ID` and `API_HASH`

#### Bot Token (Required)
1. Message @BotFather on Telegram
2. Create a new bot with `/newbot`
3. Get your `BOT_TOKEN`

#### MongoDB Database (Required)
1. Go to https://cloud.mongodb.com
2. Create a free cluster
3. Get your `MONGO_DB_URI`

### 4. Configure Environment Variables

Edit the `.env` file with your actual values:

```env
# Required Variables
API_ID=your_actual_api_id
API_HASH=your_actual_api_hash
BOT_TOKEN=your_actual_bot_token
MONGO_DB_URI=your_actual_mongodb_uri
OWNER_ID=your_telegram_user_id
LOGGER_ID=your_log_group_id

# String Sessions (Optional - for multiple assistants)
STRING1=your_string_session_1
STRING2=your_string_session_2
STRING3=your_string_session_3
STRING4=your_string_session_4
STRING5=your_string_session_5
```

### 5. Get String Sessions (Optional)

For multiple assistants, get string sessions from @ELVARINSTRINGSESSION_BOT

### 6. Run the Bot

```bash
python -m ElvarinXMusic
```

## 🚀 Heroku Deployment

### 1. Create Heroku App
```bash
heroku create your-app-name
```

### 2. Set Environment Variables
```bash
heroku config:set API_ID=your_api_id
heroku config:set API_HASH=your_api_hash
heroku config:set BOT_TOKEN=your_bot_token
heroku config:set MONGO_DB_URI=your_mongodb_uri
heroku config:set OWNER_ID=your_owner_id
heroku config:set SUDO_USERS=your_sudo_users
```

### 3. Deploy
```bash
git push heroku main
```

## 📱 Bot Commands

- `/start` - Start the bot
- `/help` - Get help
- `/play` - Play music
- `/pause` - Pause music
- `/resume` - Resume music
- `/skip` - Skip current song
- `/stop` - Stop music
- `/queue` - Show queue
- `/playlist` - Show playlist

## 🔧 Troubleshooting

### Common Issues:

1. **ModuleNotFoundError**: Install dependencies with `pip install -r requirements.txt`
2. **ImportError**: Check if all environment variables are set correctly
3. **MongoDB Connection Error**: Verify your MONGO_DB_URI
4. **Telegram API Error**: Check your API_ID and API_HASH

### Getting Help:

- Check logs for detailed error messages
- Ensure all required environment variables are set
- Verify your bot has proper permissions in groups

## 📞 Support

- GitHub: https://github.com/Evid3008/ELVARIN
- Telegram: @your_support_username

---

**Made with ❤️ by Elvarin Team**
