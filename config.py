## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "BABsiTDXWSL9meZbm-dluqkUrXWb5xvUCwJ4XkHJ1_kKDC7Z1gvgZ_p2KGMo90oPK92V6s2SYDkKRRclz-nXKvX2JdnL-_FWjtxJbnjURThIPfeUo2VMHAjb4KrBAVAgtLrKsp7aFFIfIB8KAk45z-zcDhrficZyFsIbu81mPyh4HSO2m-qVofgTUL3GpTzQqlWROFlSwLkX7YS-j7ApCtyhG3M8gvq4K3cJs_fpivgyE2Naj-vJruZeS1F3pH_hXIZrGgLYvraZOUnIROZt8XytuCJnd1OuHpiT32YBevUEkqQwToVvYusOql7MqZtGhybV6W2spbha5eS6jYFg9-gjAAAAATNWuRMA")
BOT_TOKEN = getenv("BOT_TOKEN", "5549348756:AAEEMqYUfEZ_lOtGed9Xhw5NOE1y093mig8")
BOT_NAME = getenv("BOT_NAME", "music")
API_ID = int(getenv("API_ID", "17851488"))
API_HASH = getenv("API_HASH", "61fafaeb70ad022ce6ca0879d7fc4c25")
OWNER_NAME = getenv("OWNER_NAME", "EL LOL")
OWNER_USERNAME = getenv("OWNER_USERNAME", "A_h_m_e_dE")
ALIVE_NAME = getenv("ALIVE_NAME", "EL LOL")
BOT_USERNAME = getenv("BOT_USERNAME", "ii_m_k_o_bot")
OWNER_ID = getenv("OWNER_ID", "5300856245")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "Ahmednnt")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "G6_9R")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "G6_9R")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1854384004").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/407ce4c57a645c11f65c0.jpg")
START_PIC = getenv("START_PIC", "https://te.legra.ph/file/7713b9828bced85d9b46e.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "10"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/muntazer995/ing")
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/402c519808f75bd9b1803.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/c74686f70a1b918060b8e.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.jpg")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/478f9fa85efb2740f2544.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.jpg")
IMG_6 = getenv("IMG_6", "https://te.legra.ph/file/430dcf25456f2bb38109f.jpg")
