## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "AgC5D2MB3u9U0zqKdlZsxpq0gi1hpgCaHhW224oOhP6nYbrE7MbTpbfF92qJX7lAW_prur_HWLXCDsiQLkfHhbbCBsZZo1T70Rty-XwT5a-YtgxHO8GaXTu-ZY5Q9wQUpUCbJDvovMXXBuCs-irslFAa-CRqZTV9h9lwg7ltmA18f8PHG3egNMrdMWqtfxG1eX52hAiyq2HxW8ZTgXOSC6Tj2DEUyny3f2uZRIIzn_naHUV_1fV2solK1lJwII_0D2euz5Iz8_TTKXKOJfRNMzkBQWbMGQ9ko1nAZutvcSZzogZJepZXq2Els6sVe3JhnOJTe36D2Z0cRfxyM0LB_k7zMzMTnQA")
BOT_TOKEN = getenv("BOT_TOKEN", "5510473712:AAEnR5uojX2JTjx-ig_8UjN8PFMpZDWKNSE")
BOT_NAME = getenv("BOT_NAME", "- Music Khaled .")
API_ID = int(getenv("API_ID", "13142929"))
API_HASH = getenv("API_HASH", "422dcbcc81972039a6c24969b116e1e9")
OWNER_NAME = getenv("OWNER_NAME", "Khalid")
OWNER_USERNAME = getenv("OWNER_USERNAME", "E_M_K")
ALIVE_NAME = getenv("ALIVE_NAME", "Khalid")
BOT_USERNAME = getenv("BOT_USERNAME", "MSCVIPBOT")
OWNER_ID = getenv("OWNER_ID", "1951693700")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "Music Khaled")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "M_D_I")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "M_D_I")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1951693700").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/407ce4c57a645c11f65c0.jpg")
START_PIC = getenv("START_PIC", "https://te.legra.ph/file/e22e5d1f0ccd57fa5f677.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "10"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/khaled1q/xyz")
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/402c519808f75bd9b1803.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/c74686f70a1b918060b8e.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.jpg")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/478f9fa85efb2740f2544.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.jpg")
IMG_6 = getenv("IMG_6", "https://te.legra.ph/file/430dcf25456f2bb38109f.jpg")
