# Panda Userbot <https://github.com/ilhammansiz/PandaX_Userbot>
# Recode by Ilham Mansiz
# ••••••••••••••••••••••√•••••••••••••√√√••••••••

import sys


from .._database._var import Var, Database
from ..versions import __version__
import os
from .classstring import *
from .._misc.client import ErUbotSession
from .._misc.botclient import ErUserbotToken
from .._database import pyDatabase
DB = pyDatabase()
from telethon import TelegramClient
import sys
import logging

BOT_TOKEN = DB.get_key("BOT_TOKEN") or os.environ.get("BOT_TOKEN", None)
CEKBOT = "5293882146:AAFQIjmaC9ObBu98PAvctLu0QxkckfOJrz4"

LOGS = logging.getLogger("ErUbot")
loop = None


BOT_MODE = DB.get_key("MODE_DUAL")
DUAL_MODE = DB.get_key("DUAL_MODE")

##•••••••••••••••Rwrite by Er Rickow••||||•••
## Mode Userbot

try:
    if Var.STRING_SESSION:
        ErBot = ErUserbotSession(
            ErSession(Var.STRING_SESSION, LOGS),
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
            app_version=__version__,
        )
    else:
        ErBot = None
except Exception as e:
    print(f"STRING_SESSION- {str(e)}")
    sys.exit()

try:
    if DB.get_key("SESSION2") or Var.STRING_SESSION2:
        ErBot2 = ErUserbotSession(
            ErSession(DB.get_key("SESSION2") or Var.STRING_SESSION2, LOGS),
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
            app_version=__version__,
        )
    else:
        ErBot2 = None
except Exception as e:
    print(f"STRING_SESSION2- {str(e)}")
    sys.exit()

try:
    if DB.get_key("SESSION3") or Var.STRING_SESSION3:
        ErBot3 = ErUserbotSession(
            ErSession(DB.get_key("SESSION3") or Var.STRING_SESSION3, LOGS),
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
            app_version=__version__,
        )
    else:
        ErBot3 = None
except Exception as e:
    print(f"STRING_SESSION3- {str(e)}")
    sys.exit()


try:
    if Var.STRING_SESSION and DB.get_key("BOT_TOKEN") or Database.BOT_TOKEN:
        tgbot = ErUserbotToken(
            "BOT_TOKEN",
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
            app_version=__version__,
        )

    else:
        tgbot = None
except Exception as e:
    print(f"BOT-TOKEN- {str(e)}")
    sys.exit()





## SESSION MUTLTI 50

try:
    if DB.get_key("SESSION4") or Var.STRING_SESSION4:
        ErBot4 = ErUserbotSession(
            ErSession(DB.get_key("SESSION4") or Var.STRING_SESSION4, LOGS),
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
            app_version=__version__,
        )
    else:
        ErBot4 = None
except Exception as e:
    print(f"STRING_SESSION4- {str(e)}")
    sys.exit()

try:
    if DB.get_key("SESSION5") or Var.STRING_SESSION5:
        ErBot5 = ErUserbotSession(
            ErSession(DB.get_key("SESSION5") or Var.STRING_SESSION5, LOGS),
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
            app_version=__version__,
        )
    else:
        ErBot5 = None
except Exception as e:
    print(f"STRING_SESSION5- {str(e)}")
    sys.exit()

try:
    if DB.get_key("SESSION6") or Var.STRING_SESSION6:
        ErBot6 = ErUserbotSession(
            ErSession(DB.get_key("SESSION6") or Var.STRING_SESSION6, LOGS),
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
            app_version=__version__,
        )
    else:
        ErBot6 = None
except Exception as e:
    print(f"STRING_SESSION6- {str(e)}")
    sys.exit()

try:
    if DB.get_key("SESSION7") or Var.STRING_SESSION7:
        ErBot7 = ErUserbotSession(
            ErSession(DB.get_key("SESSION7") or Var.STRING_SESSION7, LOGS),
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
            app_version=__version__,
        )
    else:
        ErBot7 = None
except Exception as e:
    print(f"STRING_SESSION7- {str(e)}")
    sys.exit()


try:
    if DB.get_key("SESSION8") or Var.STRING_SESSION8:
        ErBot8 = ErUserbotSession(
            ErSession(DB.get_key("SESSION8") or Var.STRING_SESSION8, LOGS),
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
            app_version=__version__,
        )
    else:
        ErBot8 = None
except Exception as e:
    print(f"STRING_SESSION8- {str(e)}")
    sys.exit()

try:
    if DB.get_key("SESSION9") or Var.STRING_SESSION9:
        ErBot9 = ErUserbotSession(
            ErSession(DB.get_key("SESSION9") or Var.STRING_SESSION9, LOGS),
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
            app_version=__version__,
        )
    else:
        ErBot9 = None
except Exception as e:
    print(f"STRING_SESSION9- {str(e)}")
    sys.exit()


try:
    if DB.get_key("SESSION10") or Var.STRING_SESSION10:
        ErBot10 = ErUserbotSession(
            ErSession(DB.get_key("SESSION10") or Var.STRING_SESSION10, LOGS),
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
            app_version=__version__,
        )
    else:
        ErBot10 = None
except Exception as e:
    print(f"STRING_SESSION10- {str(e)}")
    sys.exit()

try:
    if DB.get_key("SESSION11") or Var.STRING_SESSION11:
        ErBot11 = ErUserbotSession(
            ErSession(DB.get_key("SESSION11") or Var.STRING_SESSION11, LOGS),
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
            app_version=__version__,
        )
    else:
        ErBot11 = None
except Exception as e:
    print(f"STRING_SESSION11- {str(e)}")
    sys.exit()


try:
    if DB.get_key("SESSION12") or Var.STRING_SESSION12:
        ErBot12 = ErUserbotSession(
            ErSession(DB.get_key("SESSION12") or Var.STRING_SESSION12, LOGS),
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
            app_version=__version__,
        )
    else:
        ErBot12 = None
except Exception as e:
    print(f"STRING_SESSION12- {str(e)}")
    sys.exit()

try:
    if DB.get_key("SESSION13") or Var.STRING_SESSION13:
        ErBot13 = ErUserbotSession(
            ErSession(DB.get_key("SESSION13") or Var.STRING_SESSION13, LOGS),
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
            app_version=__version__,
        )
    else:
        ErBot13 = None
except Exception as e:
    print(f"STRING_SESSION13- {str(e)}")
    sys.exit()

try:
    if DB.get_key("SESSION14") or Var.STRING_SESSION14:
        ErBot14 = ErUserbotSession(
            ErSession(DB.get_key("SESSION14") or Var.STRING_SESSION14, LOGS),
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
            app_version=__version__,
        )
    else:
        ErBot14 = None
except Exception as e:
    print(f"STRING_SESSION14- {str(e)}")
    sys.exit()

try:
    if DB.get_key("SESSION15") or Var.STRING_SESSION15:
        ErBot15 = ErUserbotSession(
            ErSession(DB.get_key("SESSION15") or Var.STRING_SESSION15, LOGS),
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
            app_version=__version__,
        )
    else:
        ErBot15 = None
except Exception as e:
    print(f"STRING_SESSION15- {str(e)}")
    sys.exit()


try:
    if DB.get_key("SESSION16") or Var.STRING_SESSION16:
        ErBot16 = ErUserbotSession(
            ErSession(DB.get_key("SESSION16") or Var.STRING_SESSION16, LOGS),
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
            app_version=__version__,
        )
    else:
        ErBot16 = None
except Exception as e:
    print(f"STRING_SESSION16- {str(e)}")
    sys.exit()

try:
    if DB.get_key("SESSION17") or Var.STRING_SESSION17:
        ErBot17 = ErUserbotSession(
            ErSession(DB.get_key("SESSION17") or Var.STRING_SESSION17, LOGS),
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
            app_version=__version__,
        )
    else:
        ErBot17 = None
except Exception as e:
    print(f"STRING_SESSION3- {str(e)}")
    sys.exit()


try:
    if DB.get_key("SESSION18") or Var.STRING_SESSION18:
        ErBot18 = ErUserbotSession(
            ErSession(DB.get_key("SESSION18") or Var.STRING_SESSION18, LOGS),
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
            app_version=__version__,
        )
    else:
        ErBot18 = None
except Exception as e:
    print(f"STRING_SESSION18- {str(e)}")
    sys.exit()

try:
    if DB.get_key("SESSION19") or Var.STRING_SESSION19:
        ErBot19 = ErUserbotSession(
            ErSession(DB.get_key("SESSION19") or Var.STRING_SESSION19, LOGS),
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
            app_version=__version__,
        )
    else:
        ErBot19 = None
except Exception as e:
    print(f"STRING_SESSION19- {str(e)}")
    sys.exit()

try:
    if DB.get_key("SESSION20") or Var.STRING_SESSION20:
        ErBot20 = ErUserbotSession(
            ErSession(DB.get_key("SESSION20") or Var.STRING_SESSION20, LOGS),
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
            app_version=__version__,
        )
    else:
        ErBot20 = None
except Exception as e:
    print(f"STRING_SESSION20- {str(e)}")
    sys.exit()

try:
    if DB.get_key("SESSION21") or Var.STRING_SESSION21:
        ErBot21 = ErUserbotSession(
            ErSession(DB.get_key("SESSION21") or Var.STRING_SESSION21, LOGS),
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
            app_version=__version__,
        )
    else:
        ErBot21 = None
except Exception as e:
    print(f"STRING_SESSION21- {str(e)}")
    sys.exit()


try:
    if DB.get_key("SESSION22") or Var.STRING_SESSION22:
        ErBot22 = ErUserbotSession(
            ErSession(DB.get_key("SESSION22") or Var.STRING_SESSION22, LOGS),
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
            app_version=__version__,
        )
    else:
        ErBot22 = None
except Exception as e:
    print(f"STRING_SESSION22- {str(e)}")
    sys.exit()

try:
    if DB.get_key("SESSION23") or Var.STRING_SESSION23:
        ErBot23 = ErUserbotSession(
            ErSession(DB.get_key("SESSION23") or Var.STRING_SESSION23, LOGS),
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
            app_version=__version__,
        )
    else:
        ErBot23 = None
except Exception as e:
    print(f"STRING_SESSION23- {str(e)}")
    sys.exit()

try:
    if DB.get_key("SESSION24") or Var.STRING_SESSION24:
        ErBot24 = ErUserbotSession(
            ErSession(DB.get_key("SESSION24") or Var.STRING_SESSION24, LOGS),
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
            app_version=__version__,
        )
    else:
        ErBot24 = None
except Exception as e:
    print(f"STRING_SESSION42- {str(e)}")
    sys.exit()

try:
    if DB.get_key("SESSION25") or Var.STRING_SESSION25:
        ErBot25 = ErUserbotSession(
            ErSession(DB.get_key("SESSION25") or Var.STRING_SESSION25, LOGS),
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
            app_version=__version__,
        )
    else:
        ErBot25 = None
except Exception as e:
    print(f"STRING_SESSION25- {str(e)}")
    sys.exit()

try:
    if DB.get_key("SESSION26") or Var.STRING_SESSION26:
        ErBot26 = ErUserbotSession(
            ErSession(DB.get_key("SESSION26") or Var.STRING_SESSION26, LOGS),
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
            app_version=__version__,
        )
    else:
        ErBot26 = None
except Exception as e:
    print(f"STRING_SESSION26- {str(e)}")
    sys.exit()

try:
    if DB.get_key("SESSION27") or Var.STRING_SESSION27:
        ErBot27 = ErUserbotSession(
            ErSession(DB.get_key("SESSION27") or Var.STRING_SESSION27, LOGS),
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
            app_version=__version__,
        )
    else:
        ErBot27 = None
except Exception as e:
    print(f"STRING_SESSION27- {str(e)}")
    sys.exit()

try:
    if DB.get_key("SESSION28") or Var.STRING_SESSION28:
        ErBot28 = ErUserbotSession(
            ErSession(DB.get_key("SESSION28") or Var.STRING_SESSION28, LOGS),
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
            app_version=__version__,
        )
    else:
        ErBot28 = None
except Exception as e:
    print(f"STRING_SESSION28- {str(e)}")
    sys.exit()

try:
    if DB.get_key("SESSION29") or Var.STRING_SESSION29:
        ErBot29 = ErUserbotSession(
            ErSession(DB.get_key("SESSION29") or Var.STRING_SESSION29, LOGS),
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
            app_version=__version__,
        )
    else:
        ErBot29 = None
except Exception as e:
    print(f"STRING_SESSION29- {str(e)}")
    sys.exit()


try:
    if DB.get_key("SESSION30") or Var.STRING_SESSION30:
        ErBot30 = ErUserbotSession(
            ErSession(DB.get_key("SESSION30") or Var.STRING_SESSION30, LOGS),
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
            app_version=__version__,
        )
    else:
        ErBot30 = None
except Exception as e:
    print(f"STRING_SESSION30- {str(e)}")
    sys.exit()

try:
    if DB.get_key("SESSION31") or Var.STRING_SESSION31:
        ErBot31 = ErUserbotSession(
            ErSession(DB.get_key("SESSION31") or Var.STRING_SESSION31, LOGS),
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
            app_version=__version__,
        )
    else:
        ErBot31 = None
except Exception as e:
    print(f"STRING_SESSION31- {str(e)}")
    sys.exit()

try:
    if DB.get_key("SESSION32") or Var.STRING_SESSION32:
        ErBot32 = ErUserbotSession(
            ErSession(DB.get_key("SESSION32") or Var.STRING_SESSION32, LOGS),
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
            app_version=__version__,
        )
    else:
        ErBot32 = None
except Exception as e:
    print(f"STRING_SESSION32- {str(e)}")
    sys.exit()

try:
    if DB.get_key("SESSION33") or Var.STRING_SESSION33:
        ErBot33 = ErUserbotSession(
            ErSession(DB.get_key("SESSION33") or Var.STRING_SESSION33, LOGS),
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
            app_version=__version__,
        )
    else:
        ErBot33 = None
except Exception as e:
    print(f"STRING_SESSION33- {str(e)}")
    sys.exit()


try:
    if DB.get_key("SESSION34") or Var.STRING_SESSION34:
        ErBot34 = ErUserbotSession(
            ErSession(DB.get_key("SESSION34") or Var.STRING_SESSION34, LOGS),
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
            app_version=__version__,
        )
    else:
        ErBot34 = None
except Exception as e:
    print(f"STRING_SESSION34- {str(e)}")
    sys.exit()

try:
    if DB.get_key("SESSION35") or Var.STRING_SESSION35:
        ErBot35 = ErUserbotSession(
            ErSession(DB.get_key("SESSION35") or Var.STRING_SESSION35, LOGS),
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
            app_version=__version__,
        )
    else:
        ErBot35 = None
except Exception as e:
    print(f"STRING_SESSION35- {str(e)}")
    sys.exit()


try:
    if DB.get_key("SESSION36") or Var.STRING_SESSION36:
        ErBot36 = ErUserbotSession(
            ErSession(DB.get_key("SESSION36") or Var.STRING_SESSION36, LOGS),
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
            app_version=__version__,
        )
    else:
        ErBot36 = None
except Exception as e:
    print(f"STRING_SESSION2- {str(e)}")
    sys.exit()

try:
    if DB.get_key("SESSION37") or Var.STRING_SESSION37:
        ErBot37 = ErUserbotSession(
            ErSession(DB.get_key("SESSION37") or Var.STRING_SESSION37, LOGS),
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
            app_version=__version__,
        )
    else:
        ErBot37 = None
except Exception as e:
    print(f"STRING_SESSION37- {str(e)}")
    sys.exit()

try:
    if DB.get_key("SESSION38") or Var.STRING_SESSION38:
        ErBot38 = ErUserbotSession(
            ErSession(DB.get_key("SESSION38") or Var.STRING_SESSION38, LOGS),
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
            app_version=__version__,
        )
    else:
        ErBot38 = None
except Exception as e:
    print(f"STRING_SESSION38- {str(e)}")
    sys.exit()

try:
    if DB.get_key("SESSION39") or Var.STRING_SESSION39:
        ErBot39 = ErUserbotSession(
            ErSession(DB.get_key("SESSION3") or Var.STRING_SESSION39, LOGS),
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
            app_version=__version__,
        )
    else:
        ErBot39 = None
except Exception as e:
    print(f"STRING_SESSION39- {str(e)}")
    sys.exit()


try:
    if DB.get_key("SESSION40") or Var.STRING_SESSION40:
        ErBot40 = ErUserbotSession(
            ErSession(DB.get_key("SESSION40") or Var.STRING_SESSION40, LOGS),
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
            app_version=__version__,
        )
    else:
        ErBot40 = None
except Exception as e:
    print(f"STRING_SESSION40- {str(e)}")
    sys.exit()

try:
    if DB.get_key("SESSION41") or Var.STRING_SESSION41:
        ErBot41 = ErUserbotSession(
            ErSession(DB.get_key("SESSION41") or Var.STRING_SESSION41, LOGS),
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
            app_version=__version__,
        )
    else:
        ErBot41 = None
except Exception as e:
    print(f"STRING_SESSION41- {str(e)}")
    sys.exit()


try:
    if DB.get_key("SESSION42") or Var.STRING_SESSION42:
        ErBot42 = ErUserbotSession(
            ErSession(DB.get_key("SESSION42") or Var.STRING_SESSION42, LOGS),
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
            app_version=__version__,
        )
    else:
        ErBot42 = None
except Exception as e:
    print(f"STRING_SESSION42- {str(e)}")
    sys.exit()

try:
    if DB.get_key("SESSION43") or Var.STRING_SESSION43:
        ErBot43 = ErUserbotSession(
            ErSession(DB.get_key("SESSION43") or Var.STRING_SESSION43, LOGS),
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
            app_version=__version__,
        )
    else:
        ErBot43 = None
except Exception as e:
    print(f"STRING_SESSION43- {str(e)}")
    sys.exit()



try:
    if DB.get_key("SESSION44") or Var.STRING_SESSION44:
        ErBot44 = ErUserbotSession(
            ErSession(DB.get_key("SESSION44") or Var.STRING_SESSION44, LOGS),
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
            app_version=__version__,
        )
    else:
        ErBot44 = None
except Exception as e:
    print(f"STRING_SESSION44- {str(e)}")
    sys.exit()

try:
    if DB.get_key("SESSION45") or Var.STRING_SESSION45:
        ErBot45 = ErUserbotSession(
            ErSession(DB.get_key("SESSION45") or Var.STRING_SESSION45, LOGS),
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
            app_version=__version__,
        )
    else:
        ErBot45 = None
except Exception as e:
    print(f"STRING_SESSION45- {str(e)}")
    sys.exit()



try:
    if DB.get_key("SESSION46") or Var.STRING_SESSION46:
        ErBot46 = ErUserbotSession(
            ErSession(DB.get_key("SESSION40") or Var.STRING_SESSION46, LOGS),
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
            app_version=__version__,
        )
    else:
        ErBot46 = None
except Exception as e:
    print(f"STRING_SESSION46- {str(e)}")
    sys.exit()

try:
    if DB.get_key("SESSION47") or Var.STRING_SESSION47:
        ErBot47 = ErUserbotSession(
            ErSession(DB.get_key("SESSION47") or Var.STRING_SESSION47, LOGS),
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
            app_version=__version__,
        )
    else:
        ErBot47 = None
except Exception as e:
    print(f"STRING_SESSION47- {str(e)}")
    sys.exit()



try:
    if DB.get_key("SESSION48") or Var.STRING_SESSION48:
        ErBot48 = ErUserbotSession(
            ErSession(DB.get_key("SESSION48") or Var.STRING_SESSION48, LOGS),
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
            app_version=__version__,
        )
    else:
        ErBot48 = None
except Exception as e:
    print(f"STRING_SESSION48- {str(e)}")
    sys.exit()

try:
    if DB.get_key("SESSION49") or Var.STRING_SESSION49:
        ErBot49 = ErUserbotSession(
            ErSession(DB.get_key("SESSION49") or Var.STRING_SESSION49, LOGS),
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
            app_version=__version__,
        )
    else:
        ErBot49 = None
except Exception as e:
    print(f"STRING_SESSION49- {str(e)}")
    sys.exit()



try:
    if DB.get_key("SESSION50") or Var.STRING_SESSION50:
        ErBot50 = ErUserbotSession(
            ErSession(DB.get_key("SESSION50") or Var.STRING_SESSION50, LOGS),
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
            app_version=__version__,
        )
    else:
        ErBot50 = None
except Exception as e:
    print(f"STRING_SESSION50- {str(e)}")
    sys.exit()

    
 ## VC SESSION
vclient = ErBot
"""
try:
    if Var.VC_STRING_SESSION:
        vclient = TelegramClient(
            ErSession(Var.VC_STRING_SESSION, LOGS),
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH,
        )
    else:
        vclient = None
except Exception as e:
    print(f"VC_STRING_SESSION- {str(e)}")
    sys.exit()
"""    
try:
    if Var.VC_STRING_SESSION2:
        vclient2 = TelegramClient(
            ErSession(Var.VC_STRING_SESSION2, LOGS),
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
            app_version=__version__,
        )
    else:
        vclient2 = None
except Exception as e:
    print(f"VC_STRING_SESSION2- {str(e)}")
    sys.exit()


try:
    if Var.VC_STRING_SESSION3:
        vclient3 = TelegramClient(
            ErSession(Var.VC_STRING_SESSION3, LOGS),
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
            app_version=__version__,
        )
    else:
        vclient3 = None
except Exception as e:
    print(f"VC_STRING_SESSION3- {str(e)}")
    sys.exit()
try:
    if Var.VC_STRING_SESSION4:
        vclient4 = TelegramClient(
            ErSession(Var.VC_STRING_SESSION4, LOGS),
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
            app_version=__version__,
        )
    else:
        vclient4 = None
except Exception as e:
    print(f"VC_STRING_SESSION4- {str(e)}")
    sys.exit()
try:
    if Var.VC_STRING_SESSION5:
        vclient5 = TelegramClient(
            ErSession(Var.VC_STRING_SESSION5, LOGS),
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
            app_version=__version__,
        )
    else:
        vclient5 = None
except Exception as e:
    print(f"VC_STRING_SESSION5- {str(e)}")
    sys.exit()
    
try:
    if Var.VC_STRING_SESSION6:
        vclient6 = TelegramClient(
            ErSession(Var.VC_STRING_SESSION6, LOGS),
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
            app_version=__version__,
        )
    else:
        vclient6 = None
except Exception as e:
    print(f"VC_STRING_SESSION6- {str(e)}")
    sys.exit()
 
try:
    if Var.VC_STRING_SESSION7:
        vclient7 = TelegramClient(
            ErSession(Var.VC_STRING_SESSION7, LOGS),
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
            app_version=__version__,
        )
    else:
        vclient7 = None
except Exception as e:
    print(f"VC_STRING_SESSION7- {str(e)}")
    sys.exit()
try:
    if Var.VC_STRING_SESSION8:
        vclient8 = TelegramClient(
            ErSession(Var.VC_STRING_SESSION8, LOGS),
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
            app_version=__version__,
        )
    else:
        vclient8 = None
except Exception as e:
    print(f"VC_STRING_SESSION8- {str(e)}")
    sys.exit()
try:
    if Var.VC_STRING_SESSION9:
        vclient9 = TelegramClient(
            ErSession(Var.VC_STRING_SESSION9, LOGS),
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
            app_version=__version__,
        )
    else:
        vclient9 = None
except Exception as e:
    print(f"VC_STRING_SESSION9- {str(e)}")
    sys.exit()
    
try:
    if Var.VC_STRING_SESSION10:
        vclient10 = TelegramClient(
            ErSession(Var.VC_STRING_SESSION10, LOGS),
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
            app_version=__version__,
        )
    else:
        vclient10 = None
except Exception as e:
    print(f"VC_STRING_SESSION10- {str(e)}")
    sys.exit()
    
try:
    if Var.VC_STRING_SESSION11:
        vclient11 = TelegramClient(
            ErSession(Var.VC_STRING_SESSION11, LOGS),
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
            app_version=__version__,
        )
    else:
        vclient11 = None
except Exception as e:
    print(f"VC_STRING_SESSION11- {str(e)}")
    sys.exit()
 
try:
    if Var.VC_STRING_SESSION12:
        vclient12 = TelegramClient(
            ErSession(Var.VC_STRING_SESSION12, LOGS),
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
            app_version=__version__,
        )
    else:
        vclient12 = None
except Exception as e:
    print(f"VC_STRING_SESSION12- {str(e)}")
    sys.exit()
try:
    if Var.VC_STRING_SESSION13:
        vclient13 = TelegramClient(
            ErSession(Var.VC_STRING_SESSION13, LOGS),
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
            app_version=__version__,
        )
    else:
        vclient13 = None
except Exception as e:
    print(f"VC_STRING_SESSION13- {str(e)}")
    sys.exit()
try:
    if Var.VC_STRING_SESSION:
        vclient14 = TelegramClient(
            ErSession(Var.VC_STRING_SESSION14, LOGS),
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
            app_version=__version__,
        )
    else:
        vclient14 = None
except Exception as e:
    print(f"VC_STRING_SESSION14- {str(e)}")
    sys.exit()
    
try:
    if Var.VC_STRING_SESSION15:
        vclient15 = TelegramClient(
            ErSession(Var.VC_STRING_SESSION15, LOGS),
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
            app_version=__version__,
        )
    else:
        vclient15 = None
except Exception as e:
    print(f"VC_STRING_SESSION15- {str(e)}")
    sys.exit()
    
try:
    if Var.VC_STRING_SESSION16:
        vclient16 = TelegramClient(
            ErSession(Var.VC_STRING_SESSION16, LOGS),
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
            app_version=__version__,
        )
    else:
        vclient16 = None
except Exception as e:
    print(f"VC_STRING_SESSION16- {str(e)}")
    sys.exit()
 
try:
    if Var.VC_STRING_SESSION17:
        vclient17 = TelegramClient(
            ErSession(Var.VC_STRING_SESSION17, LOGS),
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
            app_version=__version__,
        )
    else:
        vclient17 = None
except Exception as e:
    print(f"VC_STRING_SESSION17- {str(e)}")
    sys.exit()
try:
    if Var.VC_STRING_SESSION18:
        vclient18 = TelegramClient(
            ErSession(Var.VC_STRING_SESSION18, LOGS),
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
            app_version=__version__,
        )
    else:
        vclient18 = None
except Exception as e:
    print(f"VC_STRING_SESSION18- {str(e)}")
    sys.exit()
try:
    if Var.VC_STRING_SESSION19:
        vclient19 = TelegramClient(
            ErSession(Var.VC_STRING_SESSION19, LOGS),
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
            app_version=__version__,
        )
    else:
        vclient19 = None
except Exception as e:
    print(f"VC_STRING_SESSION19- {str(e)}")
    sys.exit()
    
try:
    if Var.VC_STRING_SESSION20:
        vclient20 = TelegramClient(
            ErSession(Var.VC_STRING_SESSION20, LOGS),
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
            app_version=__version__,
        )
    else:
        vclient20 = None
except Exception as e:
    print(f"VC_STRING_SESSION20- {str(e)}")
    sys.exit()
    
try:
    if Var.VC_STRING_SESSION21:
        vclient21 = TelegramClient(
            ErSession(Var.VC_STRING_SESSION21, LOGS),
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
            app_version=__version__,
        )
    else:
        vclient21 = None
except Exception as e:
    print(f"VC_STRING_SESSION21- {str(e)}")
    sys.exit()
 
try:
    if Var.VC_STRING_SESSION22:
        vclient22 = TelegramClient(
            ErSession(Var.VC_STRING_SESSION, LOGS),
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
            app_version=__version__,
        )
    else:
        vclient22 = None
except Exception as e:
    print(f"VC_STRING_SESSION22- {str(e)}")
    sys.exit()
try:
    if Var.VC_STRING_SESSION23:
        vclient23 = TelegramClient(
            ErSession(Var.VC_STRING_SESSION23, LOGS),
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
            app_version=__version__,
        )
    else:
        vclient23 = None
except Exception as e:
    print(f"VC_STRING_SESSION23- {str(e)}")
    sys.exit()
try:
    if Var.VC_STRING_SESSION24:
        vclient24 = TelegramClient(
            ErSession(Var.VC_STRING_SESSION24, LOGS),
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
            app_version=__version__,
        )
    else:
        vclient24 = None
except Exception as e:
    print(f"VC_STRING_SESSION24- {str(e)}")
    sys.exit()
    
try:
    if Var.VC_STRING_SESSION25:
        vclient25 = TelegramClient(
            ErSession(Var.VC_STRING_SESSION25, LOGS),
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
            app_version=__version__,
        )
    else:
        vclient25 = None
except Exception as e:
    print(f"VC_STRING_SESSION25- {str(e)}")
    sys.exit()
    
try:
    if Var.VC_STRING_SESSION26:
        vclient26 = TelegramClient(
            ErSession(Var.VC_STRING_SESSION26, LOGS),
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
            app_version=__version__,
        )
    else:
        vclient26 = None
except Exception as e:
    print(f"VC_STRING_SESSION26- {str(e)}")
    sys.exit()
 
try:
    if Var.VC_STRING_SESSION27:
        vclient27 = TelegramClient(
            ErSession(Var.VC_STRING_SESSION27, LOGS),
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
            app_version=__version__,
        )
    else:
        vclient27 = None
except Exception as e:
    print(f"VC_STRING_SESSION27- {str(e)}")
    sys.exit()
try:
    if Var.VC_STRING_SESSION28:
        vclient = TelegramClient(
            ErSession(Var.VC_STRING_SESSION28, LOGS),
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
            app_version=__version__,
        )
    else:
        vclient28 = None
except Exception as e:
    print(f"VC_STRING_SESSION28- {str(e)}")
    sys.exit()
try:
    if Var.VC_STRING_SESSION29:
        vclient29 = TelegramClient(
            ErSession(Var.VC_STRING_SESSION29, LOGS),
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
            app_version=__version__,
        )
    else:
        vclient29 = None
except Exception as e:
    print(f"VC_STRING_SESSION29- {str(e)}")
    sys.exit()
    
try:
    if Var.VC_STRING_SESSION30:
        vclient30 = TelegramClient(
            ErSession(Var.VC_STRING_SESSION30, LOGS),
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
            app_version=__version__,
        )
    else:
        vclient30 = None
except Exception as e:
    print(f"VC_STRING_SESSION30- {str(e)}")
    sys.exit()
    
try:
    if Var.VC_STRING_SESSION31:
        vclient31 = TelegramClient(
            ErSession(Var.VC_STRING_SESSION31, LOGS),
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
            app_version=__version__,
        )
    else:
        vclient31 = None
except Exception as e:
    print(f"VC_STRING_SESSION31- {str(e)}")
    sys.exit()
 
try:
    if Var.VC_STRING_SESSION32:
        vclient32 = TelegramClient(
            ErSession(Var.VC_STRING_SESSION32, LOGS),
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
            app_version=__version__,
        )
    else:
        vclient32 = None
except Exception as e:
    print(f"VC_STRING_SESSION32- {str(e)}")
    sys.exit()
try:
    if Var.VC_STRING_SESSION33:
        vclient33 = TelegramClient(
            ErSession(Var.VC_STRING_SESSION33, LOGS),
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
            app_version=__version__,
        )
    else:
        vclient33 = None
except Exception as e:
    print(f"VC_STRING_SESSION33- {str(e)}")
    sys.exit()
try:
    if Var.VC_STRING_SESSION34:
        vclient34 = TelegramClient(
            ErSession(Var.VC_STRING_SESSION34, LOGS),
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
            app_version=__version__,
        )
    else:
        vclient34 = None
except Exception as e:
    print(f"VC_STRING_SESSION34- {str(e)}")
    sys.exit()
    
try:
    if Var.VC_STRING_SESSION35:
        vclient35 = TelegramClient(
            ErSession(Var.VC_STRING_SESSION35, LOGS),
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
            app_version=__version__,
        )
    else:
        vclient35 = None
except Exception as e:
    print(f"VC_STRING_SESSION35- {str(e)}")
    sys.exit()
    
try:
    if Var.VC_STRING_SESSION36:
        vclient36 = TelegramClient(
            ErSession(Var.VC_STRING_SESSION36, LOGS),
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
            app_version=__version__,
        )
    else:
        vclient36 = None
except Exception as e:
    print(f"VC_STRING_SESSION36- {str(e)}")
    sys.exit()
 
try:
    if Var.VC_STRING_SESSION37:
        vclient37 = TelegramClient(
            ErSession(Var.VC_STRING_SESSION37, LOGS),
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
            app_version=__version__,
        )
    else:
        vclient37 = None
except Exception as e:
    print(f"VC_STRING_SESSION37- {str(e)}")
    sys.exit()
try:
    if Var.VC_STRING_SESSION38:
        vclient38 = TelegramClient(
            ErSession(Var.VC_STRING_SESSION38, LOGS),
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
            app_version=__version__,
        )
    else:
        vclient38 = None
except Exception as e:
    print(f"VC_STRING_SESSION38- {str(e)}")
    sys.exit()
try:
    if Var.VC_STRING_SESSION39:
        vclient39 = TelegramClient(
            ErSession(Var.VC_STRING_SESSION39, LOGS),
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
            app_version=__version__,
        )
    else:
        vclient39 = None
except Exception as e:
    print(f"VC_STRING_SESSION39- {str(e)}")
    sys.exit()
    
try:
    if Var.VC_STRING_SESSION40:
        vclient40 = TelegramClient(
            ErSession(Var.VC_STRING_SESSION40, LOGS),
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
            app_version=__version__,
        )
    else:
        vclient40 = None
except Exception as e:
    print(f"VC_STRING_SESSION40- {str(e)}")
    sys.exit()
    
try:
    if Var.VC_STRING_SESSION41:
        vclient41 = TelegramClient(
            ErSession(Var.VC_STRING_SESSION41, LOGS),
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
            app_version=__version__,
        )
    else:
        vclient41 = None
except Exception as e:
    print(f"VC_STRING_SESSION41- {str(e)}")
    sys.exit()
 
try:
    if Var.VC_STRING_SESSION42:
        vclient42 = TelegramClient(
            ErSession(Var.VC_STRING_SESSION42, LOGS),
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
            app_version=__version__,
        )
    else:
        vclient42 = None
except Exception as e:
    print(f"VC_STRING_SESSION42- {str(e)}")
    sys.exit()
try:
    if Var.VC_STRING_SESSION43:
        vclient43 = TelegramClient(
            ErSession(Var.VC_STRING_SESSION43, LOGS),
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
            app_version=__version__,
        )
    else:
        vclient43 = None
except Exception as e:
    print(f"VC_STRING_SESSION43- {str(e)}")
    sys.exit()
try:
    if Var.VC_STRING_SESSION44:
        vclient44 = TelegramClient(
            ErSession(Var.VC_STRING_SESSION44, LOGS),
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
            app_version=__version__,
        )
    else:
        vclient44 = None
except Exception as e:
    print(f"VC_STRING_SESSION44- {str(e)}")
    sys.exit()
    
try:
    if Var.VC_STRING_SESSION45:
        vclient45 = TelegramClient(
            ErSession(Var.VC_STRING_SESSION45, LOGS),
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
            app_version=__version__,
        )
    else:
        vclient45 = None
except Exception as e:
    print(f"VC_STRING_SESSION45- {str(e)}")
    sys.exit()
    
try:
    if Var.VC_STRING_SESSION46:
        vclient46 = TelegramClient(
            ErSession(Var.VC_STRING_SESSION46, LOGS),
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
            app_version=__version__,
        )
    else:
        vclient46 = None
except Exception as e:
    print(f"VC_STRING_SESSION46- {str(e)}")
    sys.exit()
 
try:
    if Var.VC_STRING_SESSION47:
        vclient47 = TelegramClient(
            ErSession(Var.VC_STRING_SESSION47, LOGS),
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
            app_version=__version__,
        )
    else:
        vclient47 = None
except Exception as e:
    print(f"VC_STRING_SESSION47- {str(e)}")
    sys.exit()
try:
    if Var.VC_STRING_SESSION48:
        vclient48 = TelegramClient(
            ErSession(Var.VC_STRING_SESSION48, LOGS),
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
            app_version=__version__,
        )
    else:
        vclient48 = None
except Exception as e:
    print(f"VC_STRING_SESSION48- {str(e)}")
    sys.exit()
try:
    if Var.VC_STRING_SESSION49:
        vclient49 = TelegramClient(
            ErSession(Var.VC_STRING_SESSION49, LOGS),
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
            app_version=__version__,
        )
    else:
        vclient49 = None
except Exception as e:
    print(f"VC_STRING_SESSION49- {str(e)}")
    sys.exit()
    

try:
    if Var.VC_STRING_SESSION50:
        vclient50 = TelegramClient(
            ErSession(Var.VC_STRING_SESSION50, LOGS),
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH,
            connection=ConnectionTcpAbridged,
            auto_reconnect=True,
            connection_retries=None,
            app_version=__version__,
        )
    else:
        vclient50 = None
except Exception as e:
    print(f"VC_STRING_SESSION50- {str(e)}")
    sys.exit()
    
    

    
