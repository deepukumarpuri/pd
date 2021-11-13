# (c) @AbirHasan2005

import os


class Config(object):
    API_ID = os.environ.get("API_ID")
    API_HASH = os.environ.get("API_HASH")
    BOT_TOKEN = os.environ.get("BOT_TOKEN")
    SESSION_NAME = os.environ.get("SESSION_NAME", "Video-Merge-Bot")
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL")
    LOG_CHANNEL = os.environ.get("LOG_CHANNEL")
    MOVIE = os.environ.get("MOVIE", "DK_BOTZ")
    MOVIE_CHL = os.environ.get("MOVIE_CHL", "PDISKHINDIMOVIVE")
    PDISK_DOMAIN = int(os.environ.get("PDISK_DOMAIN"))
    MAX_RESULTS = int(os.environ.get("MAX_RESULTS", "50"))
    PDISK_USERNAME = os.environ.get("PDISK_USERNAME")
    PDISK_PASSWORD = os.environ.get("PDISK_PASSWORD")
    MONGODB_URI = os.environ.get("MONGODB_URI")
    BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
    BOT_OWNER = int(os.environ.get("BOT_OWNER", 1445283714))

    START_TEXT = """
**Hello {}, I AM PDISK MOVIE SEARCH BOT USE ME TO SERACH ON PDISK !

FOR MORE HELP SEND /help

🍃 Bᴏᴛ Mᴀɪɴᴛᴀɪɴᴇᴅ Bʏ : [Anonymous](https://t.me/DKBOTZHELP)**
"""
    ABOUT_TEXT = """
**● Developed By : [Anonymous](https://t.me/DKBOTZHELP)
● Updates Channel : [DKBOTZ](https://t.me/DKBOTZ)
● Support Group : [DKBOTZ Support Group](https://t.me/DKBOTZ)
● Donate Channel : [DKBOTZ FUTURE](https://t.me/DKBOTZFUTURE)
● Language : [Python 3](https://www.python.org)
● Library : [Pyrogram](https://docs.pyrogram.org)
● Server : [Heroku](https://heroku.com)

©️ Made By @DKBOTZ ❤️**
"""

    HELP_TEXT = """**Hello {}, It's Too Easy To Use Me..**
 
SEND /request Movie Name To Search On Pdisk.

© By @DKBOTZ ❤️**
"""
    
