import os
from os import getenv
from dotenv import load_dotenv

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "AQAwA7v77X3sRIXn_wXnmU2ek2Z2vvsyf0PhQJbJC-idAepFGUqWsdAx5msFbOcPqzq4Pnj-_AJoX6IyfZ9XSLdPuDQ5xnVnrrkuFYuQBPCqUh0qgyWagSmXAAZ2-fLywEHrD__JzrfqGUTmyEF1hE-FoR2fJkJ_FQLIu8DqB7A-y7O9IU8cNeUZwhvtCyoIGkjciLzFK4V7sXgLZNka0LOc9fNj3BlNvA8vWVEGzrHu0aUjQfOqIhJ1SeFAbhqSpEaY639Mp6_nYnJqwOAS65zglJSjmXvZmERAIKC8Jq0msIrS_Fgjr-JkO4nlDOgmjWA8sBS5O7W7Yk9vuc1IuWaOAAAAATR7T2EA")
BOT_TOKEN = getenv("BOT_TOKEN", "5332462277:AAFfa-Dx5NAEba4IOy6AOFz_9lO0OgmZvds")
BOT_NAME = getenv("BOT_NAME", "LuksMusicbot")
API_ID = int(getenv("API_ID", 11661168))
API_HASH = getenv("API_HASH", "30cc640b6977480660e650f71d52d1ae")
MONGODB_URL = getenv("MONGODB_URL", "mongodb+srv://nusrte:Nusret.2006@cluster0.r8ckx.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
OWNER_NAME = getenv("OWNER_NAME", "imperatorbey")
ALIVE_NAME = getenv("ALIVE_NAME", "LuksMusicbot")
BOT_USERNAME = getenv("BOT_USERNAME", "LuksMusicbot)
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
