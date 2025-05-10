import os
import logging
from logging.handlers import RotatingFileHandler




BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
API_ID = int(os.environ.get("API_ID", "20445873"))
API_HASH = os.environ.get("API_HASH", "057fd0be9d7c38526b143c582bceb24b")


OWNER_ID = int(os.environ.get("OWNER_ID", "6975428639"))
DB_URL = os.environ.get("DB_URL", "mongodb+srv://renamebot:amrenamebot@cluster0.5ornz.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DB_NAME", "Cluster0")


CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002290453971"))     #STUFF TO FORWARD

FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1002416627674"))  #LUSTY LEAKS

REQUEST_CHANNEL_1 = int(os.environ.get("REQUEST_CHANNEL_1", "-1002376786303"))   #HENTAI CHANNEL


REQUEST_CHANNEL_2 = int(os.environ.get("REQUEST_CHANNEL_2", "-1002489586500"))   #BACKUP 1 CHANNEL



START_PIC = os.environ.get("START_PIC", "https://www.wallpaperflare.com/celine-farach-girls-model-hd-4k-5k-happiness-smiling-wallpaper-pidxz")
FORCE_PIC = os.environ.get("FORCE_PIC", "https://www.wallpaperflare.com/girl-joy-hair-hand-beautiful-celine-farach-wallpaper-upkvm")

FILE_AUTO_DELETE = int(os.getenv("FILE_AUTO_DELETE", "0")) # auto delete in seconds


PORT = os.environ.get("PORT", "8040")
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))



try:
    ADMINS=[6848088376]
    for x in (os.environ.get("ADMINS", "6848088376 6975428639 5543390445 7607741983 5164955785 6882412087 1294071342 7734708695 7102930070 855607227 7883822378 7461481799 1156527620 5363691943 6882412087 5747254761 971705061").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")



CUSTOM_CAPTION = os.environ.get("<blockquote>2nd Channel: @Adult_18_Contents</blockquote>" + "\n" + "<blockquote>BACKUP: https://t.me/+n8ulQN5up1Y2NDdl</blockquote>", None)

PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "True") == "True" else False

DISABLE_CHANNEL_BUTTON = True if os.environ.get('DISABLE_CHANNEL_BUTTON', None) == "True" else False

BOT_STATS_TEXT = "<b>BOT UPTIME :</b>\n{uptime}"







USER_REPLY_TEXT = "<blockquote>❌𝑴𝒆𝒔𝒔𝒂𝒈𝒆 𝒌𝒚𝒖 𝒌𝒂𝒓 𝒓𝒂𝒉𝒂 𝒉𝒂𝒊 𝒈𝒂𝒏𝒅𝒖!, 𝒂𝒃𝒃 𝒕𝒖𝒋𝒉𝒆 𝒍𝒆𝒂𝒌𝒔 𝒏𝒉𝒊 𝒅𝒖𝒏𝒈𝒂</blockquote>"

START_MSG = os.environ.get("START_MESSAGE", "𝐌𝐮𝐭𝐡𝐚𝐥 𝐚𝐚 𝐠𝐚𝐲𝐚 {mention}\n\n<blockquote><b>𝐌α𝗂 𝑳𝑬𝑨𝑲𝑺 ᑯ𝖾𐓣𝖾 ωαᥣα ᑲⱺ𝗍 ɦυ❟ <u>𝐄𝗏𝖾𝗋𝗒 𝗛𝗢𝗟𝗘 ɦα𝗌 𝗍ⱺ ᑲ𝖾 𝗒ⱺυ𝗋 𝗚𝗢𝗔𝗟.</u> <a href=https://t.me/Adult_18_Contents>𝐊𝐡𝐚𝐣𝐚𝐧𝐚 𝐡𝐚𝐢</a></b></blockquote>.")

FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hᴇʟʟᴏ {mention}\n\n<b>Yᴏᴜ Nᴇᴇᴅ Tᴏ Jᴏɪɴ Iɴ Mʏ Cʜᴀɴɴᴇʟs Tᴏ Gᴇᴛ Fɪʟᴇs\n\n𝗦𝗮𝗮𝗿𝗲 𝗖𝗵𝗮𝗻𝗻𝗲𝗹 𝗷𝗼𝗶𝗻 𝗸𝗮𝗿 𝗷𝗮𝗹𝗱𝗶\n\nIғ ʏᴏᴜ ᴅᴏɴ'ᴛ ᴋɴᴏᴡ ʜᴏᴡ ᴛᴏ ɢᴇᴛ ғɪʟᴇ ᴄʜᴇᴄᴋ <a href=https://t.me/Adult_18_Contents/26>Tᴜᴛᴏʀɪᴀʟ</a></b>")




ADMINS.append(OWNER_ID)
ADMINS.append(6299192020)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
   

class Txt(object):
    about = f"""<b>😈 My Name :</b> <a href='https://t.me/JUST_TESTING_REBOT'>JUST TESTING REBOT 😈 </a>
<b>📝 Language :</b> <a href='https://python.org'>Python 3</a>
<b>📚 Library :</b> <a href='https://pyrogram.org'>Pyrogram 2.0</a>
<b>🚀 Server :</b> <a href='https://heroku.com'>Heroku</a>
<b>📢 Channel :</b> <a href='https://t.me/Lusty_Leaks'>Lusty Leaks</a>

    
<b>😈 Bot Made By :</b> @Aaru_2074"""
