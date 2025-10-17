from ElvarinXMusic.core.bot import Hotty
from ElvarinXMusic.core.dir import dirr
from ElvarinXMusic.core.git import git
from ElvarinXMusic.core.userbot import Userbot
from ElvarinXMusic.misc import dbb, heroku

from SafoneAPI import SafoneAPI
from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Hotty()
userbot = Userbot()
api = SafoneAPI()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()

APP = "ELVARIN_KUDI_BOT"  # connect music api key "Dont change it"
