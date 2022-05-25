import os
from os import getenv
from dotenv import load_dotenv

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "AQAtV73gHRoq1x1JLl4PfK6RKmLR_Iei2-YsFB1FzF2kfV4T2c5Y8ks8dsC6BR250i_I4B2swVWEhW5c4SlUxCg0y2jq8-cPXbzmDoiaRPYR9PbE2FxvhYgRc9ykuBs_2WaNSu4xHaPEfLfBF3ee7SIH_s8khvw7jPrztWzKR6lFDYs9L1vKRhcmzeuHB8eWGQ_4cwpsFiibaKcRN1s8ehcim-6xJvB3h-DoA9YMMP9StTI08E9A77xTQAv-9BeEqZsOOpGKxxKbqrv_IXdBgaLyXHLuHojllsO7flPVxjbB-GbIejqOQYUJh9XGDkcazh22-lVkZPd8lM00q0DMQd26AAAAATjT6qIA")
BOT_TOKEN = getenv("BOT_TOKEN", "5332462277:AAFfa-Dx5NAEba4IOy6AOFz_9lO0OgmZvds")
BOT_NAME = getenv("BOT_NAME", "LuksMusicbot")
API_ID = int(getenv("API_ID", 10918415))
API_HASH = getenv("API_HASH", "182a25b7f4ce2c1dc17fc5563d762b0a")
MONGODB_URL = getenv("MONGODB_URL", "mongodb+srv://nusrte:Nusret.2006@cluster0.r8ckx.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
OWNER_NAME = getenv("OWNER_NAME", "imperatorbey")
ALIVE_NAME = getenv("ALIVE_NAME", "LuksMusicbot")
BOT_USERNAME = getenv("BOT_USERNAME", "LuksMusicbot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "LuksMusicAsisstant")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "NeonSUP")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "LuksBots")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5371871534").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/e184200a18fd3fcd015a2.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "100"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/XTQ05/muudvideo")
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/e184200a18fd3fcd015a2.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/e184200a18fd3fcd015a2.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/e184200a18fd3fcd015a2.jpg")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/e184200a18fd3fcd015a2.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/e184200a18fd3fcd015a2.jpg")
