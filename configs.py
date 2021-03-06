# (c) @Aks_support01_bot

import os


class Config(object):
    API_ID = int(os.environ.get("API_ID", 12345))
    API_HASH = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    BOT_SESSION_NAME = os.environ.get("BOT_SESSION_NAME", "MdiskSearchBot")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", "")
    CHANNEL_ID = int(os.environ.get("CHANNEL_ID", -100))
    BOT_USERNAME = os.environ.get("BOT_USERNAME")
    BOT_OWNER = int(os.environ.get("BOT_OWNER"))
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", None)
    ABOUT_BOT_TEXT = """<b>This is Search Bot.

π€ πΌπ π½π°πΌπ΄: <a href='https://t.me/Movies_searching_req_bot'>MoviesSearchingBot</a>

π π»π°π½πΆππ°πΆπ΄ : <a href='https://www.python.org'> Python V3</a>

π π»πΈπ±ππ°ππ: <a href='https://docs.pyrogram.org'> Pyrogram</a>

π‘ ππ΄πππ΄π: <a href='https://heroku.com'>Heroku</a>

π¨βπ» π²ππ΄π°ππ΄π³ π±π: <a href='https://t.me/Movies_searching_req_bot'>MoviesSearchingBot</a></b>
"""

    ABOUT_HELP_TEXT = """<b>π¨βπ» π³π΄ππ΄π»πΎπΏπ΄π : <a href='https://t.me/HBMoviesGod'>@HBMoviesGod</a>

πΈπ πππ ππππ ππππ πΎπ π π±ππ π»πππ ππππ ππππ πππ π²ππ π²ππππππ πΎππ π³ππππππππ.</b>
"""

    HOME_TEXT = """
<b>π·ππ’ π±ππ! {}π€,

πΈ'π Private filter ππππππ π±ππ.π€</a>

πΈ π²ππ ππππππ π ππππ πππ ππππβ

<a>πΌπππ ππππ β€ By @Movies_searching_req_bot</a></b>
"""


    START_MSG = """
<b>π·ππ’ π±ππ! {}π€,

πΈ'π Private Filter ππππππ π±ππ.π€</a>

πΈ π²ππ ππππππ π ππππ πππ ππππβ

<a>Made With β€ By @Movies_searching_req_bot</a></b>
"""


