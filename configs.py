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

🤖 𝙼𝚈 𝙽𝙰𝙼𝙴: <a href='https://t.me/Movies_searching_req_bot'>MoviesSearchingBot</a>

📝 𝙻𝙰𝙽𝙶𝚄𝙰𝙶𝙴 : <a href='https://www.python.org'> Python V3</a>

📚 𝙻𝙸𝙱𝚁𝙰𝚁𝚈: <a href='https://docs.pyrogram.org'> Pyrogram</a>

📡 𝚂𝙴𝚁𝚅𝙴𝚁: <a href='https://heroku.com'>Heroku</a>

👨‍💻 𝙲𝚁𝙴𝙰𝚃𝙴𝙳 𝙱𝚈: <a href='https://t.me/Movies_searching_req_bot'>MoviesSearchingBot</a></b>
"""

    ABOUT_HELP_TEXT = """<b>👨‍💻 𝙳𝙴𝚅𝙴𝙻𝙾𝙿𝙴𝚁 : <a href='https://t.me/HBMoviesGod'>@HBMoviesGod</a>

𝙸𝚏 𝚈𝚘𝚞 𝚆𝚊𝚗𝚝 𝚈𝚘𝚞𝚛 𝙾𝚠𝚗 𝙱𝚘𝚝 𝙻𝚒𝚔𝚎 𝚃𝚑𝚒𝚜 𝚃𝚑𝚎𝚗 𝚈𝚘𝚞 𝙲𝚊𝚗 𝙲𝚘𝚗𝚝𝚊𝚌𝚝 𝙾𝚞𝚛 𝙳𝚎𝚟𝚎𝚕𝚘𝚙𝚎𝚛.</b>
"""

    HOME_TEXT = """
<b>𝙷𝚎𝚢 𝙱𝚛𝚘! {}🤗,

𝙸'𝚖 Private filter 𝚂𝚎𝚊𝚛𝚌𝚑 𝙱𝚘𝚝.🤖</a>

𝙸 𝙲𝚊𝚗 𝚂𝚎𝚊𝚛𝚌𝚑 🔍 𝚆𝚑𝚊𝚝 𝚈𝚘𝚞 𝚆𝚊𝚗𝚝❗

<a>𝙼𝚊𝚍𝚎 𝚆𝚒𝚝𝚑 ❤ By @Movies_searching_req_bot</a></b>
"""


    START_MSG = """
<b>𝙷𝚎𝚢 𝙱𝚛𝚘! {}🤗,

𝙸'𝚖 Private Filter 𝚂𝚎𝚊𝚛𝚌𝚑 𝙱𝚘𝚝.🤖</a>

𝙸 𝙲𝚊𝚗 𝚂𝚎𝚊𝚛𝚌𝚑 🔍 𝚆𝚑𝚊𝚝 𝚈𝚘𝚞 𝚆𝚊𝚗𝚝❗

<a>Made With ❤ By @Movies_searching_req_bot</a></b>
"""


