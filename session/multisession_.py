# Copyright (C) 2021 PandaUserbot <https://github.com/ilhammansiz/PandaX_Userbot>
# maintaince 2023 pyrogram & telethon
# jangan di hapus ga semuanya dihapus lu paham 😏
# Pembaruan 2023 skala besar dengan menggabungkan 2 basis telethon and pyrogram.
# Dibuat dari berbagai userbot yang pernah ada.
# t.me/pandac0de t.me/pandauserbot

from telethon import functions, utils
from pyrogram import idle
from .._database._var import Var, Database
from logging import getLogger
from .._database import pdB
from .client import *

from .pyroclient import *
import sys
LOGS = getLogger(__name__)
import os

from pyrogram import __version__ as pyrover
PRIVATE = int(os.environ.get("PRIVATE_GROUP_BOT_API_ID"))


cmdhr = os.environ.get("COMMAND_HAND_LER") or "."

MSG_ON = """
꧁༺ Er Userbot\n\n
User - @{} 
Pyrogram Version - `{}' `[HAVE ENABLED]` 
Type `{}alive` to Check Bot 
Total Clients - {}
"""


THON_ON = """
꧁༺ Er Userbot ༻꧂\n\n
User - @{} 
Version - `{}' `[HAVE ENABLED]` 
Type `{}alive` to Check Bot 
Total Clients - {}
"""


def Telethon():
    failed = 0
    if pdB.get_key("SESSION") or Var.STRING_SESSION and Database.BOT_TOKEN:
        try:
            ErBot.connect()
            tgbot.start(bot_token=Database.BOT_TOKEN)
            config = ErBot(functions.help.GetConfigRequest())
            for option in config.dc_options:
                if option.ip_address == ErBot.session.server_address:
                    if ErBot.session.dc_id != option.id:
                        LOGS.warning(
                            f"Fixed DC ID in session from {ErBot.session.dc_id}"
                            f" to {option.id}"
                    )
                    ErBot.session.set_dc(option.id, option.ip_address, option.port)
                    ErBot.session.save()
                    break
            tgbot.me = tgbot.get_me()
            ErBot.me = ErBot.get_me()
            ErBot.uid = tgbot.uid = utils.get_peer_id(ErBot.me)      
            if pdB.get_key("BOT_USERNAME"):
                pdB.set_key("BOT_USERNAME", tgbot.me.username)
            if pdB.get_key("OWNER_ID") or [] or Var.OWNER_ID == 0:
                Var.OWNER_ID = utils.get_peer_id(ErBot.me)
                pdB.set_key("OWNER_ID", Var.OWNER_ID)
            else:
                pdB.set_key("OWNER_ID", ErBot.uid)
           
        except Exception as e:
            LOGS.error(f"STRING_SESSION1 - {e}")
            sys.exit()
            
    if pdB.get_key("SESSION2") or Var.STRING_SESSION2 and Database.BOT_TOKEN:
        try:
            ErBot2.connect()
            config = ErBot2(functions.help.GetConfigRequest())
            for option in config.dc_options:
                if option.ip_address == ErBot2.session.server_address:
                    if ErBot2.session.dc_id != option.id:
                        LOGS.warning(
                            f"Fixed DC ID in session from {ErBot2.session.dc_id}"
                            f" to {option.id}"
                    )
                    ErBot2.session.set_dc(option.id, option.ip_address, option.port)
                    ErBot2.session.save()
                    break
            tgbot.get_me()
            ErBot2.me = ErBot2.get_me()
            ErBot2.uid = tgbot.uid = utils.get_peer_id(ErBot2.me)
            if pdB.get_key("OWNER_ID") or Var.OWNER_ID == 0:
                Var.OWNER_ID = utils.get_peer_id(ErBot2.me)
                pdB.set_key("OWNER_ID", Var.OWNER_ID)
            else:
                pdB.set_key("OWNER_ID", ErBot2.uid)
        except Exception as e:
            LOGS.error(f"STRING_SESSION2 - {e}")
            sys.exit()

    if pdB.get_key("SESSION3") or Var.STRING_SESSION3 and Database.BOT_TOKEN:
        try:
            ErBot3.connect()
            config = ErBot3(functions.help.GetConfigRequest())
            for option in config.dc_options:
                if option.ip_address == ErBot3.session.server_address:
                    if ErBot3.session.dc_id != option.id:
                        LOGS.warning(
                            f"Fixed DC ID in session from {ErBot3.session.dc_id}"
                            f" to {option.id}"
                    )
                    ErBot3.session.set_dc(option.id, option.ip_address, option.port)
                    ErBot3.session.save()
                    break
            tgbot.get_me()
            ErBot3.me = ErBot3.get_me()
            ErBot3.uid = tgbot.uid = utils.get_peer_id(ErBot3.me)
            if pdB.get_key("OWNER_ID") or Var.OWNER_ID == 0:
                Var.OWNER_ID = utils.get_peer_id(ErBot3.me)
                pdB.set_key("OWNER_ID", Var.OWNER_ID)
            else:
                pdB.set_key("OWNER_ID", ErBot3.uid)
        except Exception as e:
            LOGS.error(f"STRING_SESSION3 - {e}")
            sys.exit()

    if pdB.get_key("SESSION4") or Var.STRING_SESSION4 and Database.BOT_TOKEN:
        try:
            ErBot4.connect()
            config = ErBot4(functions.help.GetConfigRequest())
            for option in config.dc_options:
                if option.ip_address == ErBot4.session.server_address:
                    if ErBot4.session.dc_id != option.id:
                        LOGS.warning(
                            f"Fixed DC ID in session from {ErBot4.session.dc_id}"
                            f" to {option.id}"
                    )
                    ErBot4.session.set_dc(option.id, option.ip_address, option.port)
                    ErBot4.session.save()
                    break
            tgbot.get_me()
            ErBot4.me = ErBot4.get_me()
            ErBot4.uid = tgbot.uid = utils.get_peer_id(ErBot4.me)
            if pdB.get_key("OWNER_ID") or Var.OWNER_ID == 0:
                Var.OWNER_ID = utils.get_peer_id(ErBot4.me)
                pdB.set_key("OWNER_ID", Var.OWNER_ID)
            else:
                pdB.set_key("OWNER_ID", ErBot4.uid)
        except Exception as e:
            LOGS.error(f"STRING_SESSION4 - {e}")
            sys.exit()

    if pdB.get_key("SESSION5") or Var.STRING_SESSION5 and Database.BOT_TOKEN:
        try:
            ErBot5.connect()
            config = ErBot5(functions.help.GetConfigRequest())
            for option in config.dc_options:
                if option.ip_address == ErBot5.session.server_address:
                    if ErBot5.session.dc_id != option.id:
                        LOGS.warning(
                            f"Fixed DC ID in session from {ErBot5.session.dc_id}"
                            f" to {option.id}"
                    )
                    ErBot5.session.set_dc(option.id, option.ip_address, option.port)
                    ErBot5.session.save()
                    break
            tgbot.get_me()
            ErBot5.me = ErBot5.get_me()
            ErBot5.uid = tgbot.uid = utils.get_peer_id(ErBot5.me)
            if pdB.get_key("OWNER_ID") or Var.OWNER_ID == 0:
                Var.OWNER_ID = utils.get_peer_id(ErBot5.me)
                pdB.set_key("OWNER_ID", Var.OWNER_ID)
            else:
                pdB.set_key("OWNER_ID", ErBot5.uid)
        except Exception as e:
            LOGS.error(f"STRING_SESSION5 - {e}")
            sys.exit()

    if pdB.get_key("SESSION6") or Var.STRING_SESSION6 and Database.BOT_TOKEN:
        try:
            ErBot6.connect()
            config = ErBot6(functions.help.GetConfigRequest())
            for option in config.dc_options:
                if option.ip_address == ErBot6.session.server_address:
                    if ErBot6.session.dc_id != option.id:
                        LOGS.warning(
                            f"Fixed DC ID in session from {ErBot6.session.dc_id}"
                            f" to {option.id}"
                    )
                    ErBot6.session.set_dc(option.id, option.ip_address, option.port)
                    ErBot6.session.save()
                    break
            tgbot.get_me()
            ErBot6.me = ErBot6.get_me()
            ErBot6.uid = tgbot.uid = utils.get_peer_id(ErBot6.me)
            if pdB.get_key("OWNER_ID") or Var.OWNER_ID == 0:
                Var.OWNER_ID = utils.get_peer_id(ErBot6.me)
                pdB.set_key("OWNER_ID", Var.OWNER_ID)
            else:
                pdB.set_key("OWNER_ID", ErBot6.uid)
        except Exception as e:
            LOGS.error(f"STRING_SESSION6 - {e}")
            sys.exit()

    if pdB.get_key("SESSION7") or Var.STRING_SESSION7 and Database.BOT_TOKEN:
        try:
            ErBot7.connect()
            config = ErBot7(functions.help.GetConfigRequest())
            for option in config.dc_options:
                if option.ip_address == ErBot7.session.server_address:
                    if ErBot7.session.dc_id != option.id:
                        LOGS.warning(
                            f"Fixed DC ID in session from {ErBot7.session.dc_id}"
                            f" to {option.id}"
                    )
                    ErBot7.session.set_dc(option.id, option.ip_address, option.port)
                    ErBot7.session.save()
                    break
            tgbot.get_me()
            ErBot7.me = ErBot7.get_me()
            ErBot7.uid = tgbot.uid = utils.get_peer_id(ErBot7.me)
            if pdB.get_key("OWNER_ID") or Var.OWNER_ID == 0:
                Var.OWNER_ID = utils.get_peer_id(ErBot7.me)
                pdB.set_key("OWNER_ID", Var.OWNER_ID)
            else:
                pdB.set_key("OWNER_ID", ErBot7.uid)
        except Exception as e:
            LOGS.error(f"STRING_SESSION7 - {e}")
            sys.exit()

    if pdB.get_key("SESSION8") or Var.STRING_SESSION8 and Database.BOT_TOKEN:
        try:
            ErBot8.connect()
            config = ErBot8(functions.help.GetConfigRequest())
            for option in config.dc_options:
                if option.ip_address == ErBot8.session.server_address:
                    if ErBot8.session.dc_id != option.id:
                        LOGS.warning(
                            f"Fixed DC ID in session from {ErBot8.session.dc_id}"
                            f" to {option.id}"
                    )
                    ErBot8.session.set_dc(option.id, option.ip_address, option.port)
                    ErBot8.session.save()
                    break
            tgbot.get_me()
            ErBot8.me = ErBot8.get_me()
            ErBot8.uid = tgbot.uid = utils.get_peer_id(ErBot8.me)
            if pdB.get_key("OWNER_ID") or Var.OWNER_ID == 0:
                Var.OWNER_ID = utils.get_peer_id(ErBot8.me)
                pdB.set_key("OWNER_ID", Var.OWNER_ID)
            else:
                pdB.set_key("OWNER_ID", ErBot8.uid)
        except Exception as e:
            LOGS.error(f"STRING_SESSION8 - {e}")
            sys.exit()

    if pdB.get_key("SESSION9") or Var.STRING_SESSION9 and Database.BOT_TOKEN:
        try:
            ErBot9.connect()
            config = ErBot9(functions.help.GetConfigRequest())
            for option in config.dc_options:
                if option.ip_address == ErBot9.session.server_address:
                    if ErBot9.session.dc_id != option.id:
                        LOGS.warning(
                            f"Fixed DC ID in session from {ErBot9.session.dc_id}"
                            f" to {option.id}"
                    )
                    ErBot9.session.set_dc(option.id, option.ip_address, option.port)
                    ErBot9.session.save()
                    break
            tgbot.get_me()
            ErBot9.me = ErBot9.get_me()
            ErBot9.uid = tgbot.uid = utils.get_peer_id(ErBot9.me)
            if pdB.get_key("OWNER_ID") or Var.OWNER_ID == 0:
                Var.OWNER_ID = utils.get_peer_id(ErBot9.me)
                pdB.set_key("OWNER_ID", Var.OWNER_ID)
            else:
                pdB.set_key("OWNER_ID", ErBot9.uid)
        except Exception as e:
            LOGS.error(f"STRING_SESSION9 - {e}")
            sys.exit()

    if pdB.get_key("SESSION10") or Var.STRING_SESSION10 and Database.BOT_TOKEN:
        try:
            ErBot10.connect()
            config = ErBot10(functions.help.GetConfigRequest())
            for option in config.dc_options:
                if option.ip_address == ErBot10.session.server_address:
                    if ErBot10.session.dc_id != option.id:
                        LOGS.warning(
                            f"Fixed DC ID in session from {ErBot10.session.dc_id}"
                            f" to {option.id}"
                    )
                    ErBot10.session.set_dc(option.id, option.ip_address, option.port)
                    ErBot10.session.save()
                    break
            tgbot.get_me()
            ErBot10.me = ErBot10.get_me()
            ErBot10.uid = tgbot.uid = utils.get_peer_id(ErBot10.me)
            if pdB.get_key("OWNER_ID") or Var.OWNER_ID == 0:
                Var.OWNER_ID = utils.get_peer_id(ErBot10.me)
                pdB.set_key("OWNER_ID", Var.OWNER_ID)
            else:
                pdB.set_key("OWNER_ID", ErBot10.uid)
        except Exception as e:
            LOGS.error(f"STRING_SESSION10 - {e}")
            sys.exit()

    if pdB.get_key("SESSION11") or Var.STRING_SESSION11 and Database.BOT_TOKEN:
        try:
            ErBot11.connect()
            config = ErBot11(functions.help.GetConfigRequest())
            for option in config.dc_options:
                if option.ip_address == ErBot11.session.server_address:
                    if ErBot11.session.dc_id != option.id:
                        LOGS.warning(
                            f"Fixed DC ID in session from {ErBot11.session.dc_id}"
                            f" to {option.id}"
                    )
                    ErBot11.session.set_dc(option.id, option.ip_address, option.port)
                    ErBot11.session.save()
                    break
            tgbot.get_me()
            ErBot11.me = ErBot11.get_me()
            ErBot11.uid = tgbot.uid = utils.get_peer_id(ErBot11.me)
            if pdB.get_key("OWNER_ID") or Var.OWNER_ID == 0:
                Var.OWNER_ID = utils.get_peer_id(ErBot11.me)
                pdB.set_key("OWNER_ID", Var.OWNER_ID)
            else:
                pdB.set_key("OWNER_ID", ErBot11.uid)
        except Exception as e:
            LOGS.error(f"STRING_SESSION11 - {e}")
            sys.exit()

    if pdB.get_key("SESSION12") or Var.STRING_SESSION12 and Database.BOT_TOKEN:
        try:
            ErBot12.connect()
            config = ErBot12(functions.help.GetConfigRequest())
            for option in config.dc_options:
                if option.ip_address == ErBot12.session.server_address:
                    if ErBot12.session.dc_id != option.id:
                        LOGS.warning(
                            f"Fixed DC ID in session from {ErBot12.session.dc_id}"
                            f" to {option.id}"
                    )
                    ErBot12.session.set_dc(option.id, option.ip_address, option.port)
                    ErBot12.session.save()
                    break
            tgbot.get_me()
            ErBot12.me = ErBot12.get_me()
            ErBot12.uid = tgbot.uid = utils.get_peer_id(ErBot12.me)
            if pdB.get_key("OWNER_ID") or Var.OWNER_ID == 0:
                Var.OWNER_ID = utils.get_peer_id(ErBot12.me)
                pdB.set_key("OWNER_ID", Var.OWNER_ID)
            else:
                pdB.set_key("OWNER_ID", ErBot12.uid)
        except Exception as e:
            LOGS.error(f"STRING_SESSION12 - {e}")
            sys.exit()

    if pdB.get_key("SESSION13") or Var.STRING_SESSION13 and Database.BOT_TOKEN:
        try:
            ErBot13.connect()
            config = ErBot13(functions.help.GetConfigRequest())
            for option in config.dc_options:
                if option.ip_address == ErBot13.session.server_address:
                    if ErBot13.session.dc_id != option.id:
                        LOGS.warning(
                            f"Fixed DC ID in session from {ErBot13.session.dc_id}"
                            f" to {option.id}"
                    )
                    ErBot13.session.set_dc(option.id, option.ip_address, option.port)
                    ErBot13.session.save()
                    break
            tgbot.get_me()
            ErBot13.me = ErBot13.get_me()
            ErBot13.uid = tgbot.uid = utils.get_peer_id(ErBot13.me)
            if pdB.get_key("OWNER_ID") or Var.OWNER_ID == 0:
                Var.OWNER_ID = utils.get_peer_id(ErBot13.me)
                pdB.set_key("OWNER_ID", Var.OWNER_ID)
            else:
                pdB.set_key("OWNER_ID", ErBot13.uid)
        except Exception as e:
            LOGS.error(f"STRING_SESSION13 - {e}")
            sys.exit()

    if pdB.get_key("SESSION14") or Var.STRING_SESSION14 and Database.BOT_TOKEN:
        try:
            ErBot14.connect()
            config = ErBot14(functions.help.GetConfigRequest())
            for option in config.dc_options:
                if option.ip_address == ErBot14.session.server_address:
                    if ErBot14.session.dc_id != option.id:
                        LOGS.warning(
                            f"Fixed DC ID in session from {ErBot14.session.dc_id}"
                            f" to {option.id}"
                    )
                    ErBot14.session.set_dc(option.id, option.ip_address, option.port)
                    ErBot14.session.save()
                    break
            tgbot.get_me()
            ErBot14.me = ErBot14.get_me()
            ErBot14.uid = tgbot.uid = utils.get_peer_id(ErBot14.me)
            if pdB.get_key("OWNER_ID") or Var.OWNER_ID == 0:
                Var.OWNER_ID = utils.get_peer_id(ErBot14.me)
                pdB.set_key("OWNER_ID", Var.OWNER_ID)
            else:
                pdB.set_key("OWNER_ID", ErBot14.uid)
        except Exception as e:
            LOGS.error(f"STRING_SESSION14 - {e}")
            sys.exit()

    if pdB.get_key("SESSION15") or Var.STRING_SESSION15 and Database.BOT_TOKEN:
        try:
            ErBot15.connect()
            config = ErBot15(functions.help.GetConfigRequest())
            for option in config.dc_options:
                if option.ip_address == ErBot15.session.server_address:
                    if ErBot15.session.dc_id != option.id:
                        LOGS.warning(
                            f"Fixed DC ID in session from {ErBot15.session.dc_id}"
                            f" to {option.id}"
                    )
                    ErBot15.session.set_dc(option.id, option.ip_address, option.port)
                    ErBot15.session.save()
                    break
            tgbot.get_me()
            ErBot15.me = ErBot15.get_me()
            ErBot15.uid = tgbot.uid = utils.get_peer_id(ErBot15.me)
            if pdB.get_key("OWNER_ID") or Var.OWNER_ID == 0:
                Var.OWNER_ID = utils.get_peer_id(ErBot15.me)
                pdB.set_key("OWNER_ID", Var.OWNER_ID)
            else:
                pdB.set_key("OWNER_ID", ErBot15.uid)
        except Exception as e:
            LOGS.error(f"STRING_SESSION15 - {e}")
            sys.exit()

    if pdB.get_key("SESSION16") or Var.STRING_SESSION16 and Database.BOT_TOKEN:
        try:
            ErBot16.connect()
            config = ErBot16(functions.help.GetConfigRequest())
            for option in config.dc_options:
                if option.ip_address == ErBot16.session.server_address:
                    if ErBot16.session.dc_id != option.id:
                        LOGS.warning(
                            f"Fixed DC ID in session from {ErBot16.session.dc_id}"
                            f" to {option.id}"
                    )
                    ErBot16.session.set_dc(option.id, option.ip_address, option.port)
                    ErBot16.session.save()
                    break
            tgbot.get_me()
            ErBot16.me = ErBot16.get_me()
            ErBot16.uid = tgbot.uid = utils.get_peer_id(ErBot16.me)
            if pdB.get_key("OWNER_ID") or Var.OWNER_ID == 0:
                Var.OWNER_ID = utils.get_peer_id(ErBot16.me)
                pdB.set_key("OWNER_ID", Var.OWNER_ID)
            else:
                pdB.set_key("OWNER_ID", ErBot16.uid)
        except Exception as e:
            LOGS.error(f"STRING_SESSION16 - {e}")
            sys.exit()

    if pdB.get_key("SESSION17") or Var.STRING_SESSION17 and Database.BOT_TOKEN:
        try:
            ErBot17.connect()
            config = ErBot17(functions.help.GetConfigRequest())
            for option in config.dc_options:
                if option.ip_address == ErBot17.session.server_address:
                    if ErBot17.session.dc_id != option.id:
                        LOGS.warning(
                            f"Fixed DC ID in session from {ErBot17.session.dc_id}"
                            f" to {option.id}"
                    )
                    ErBot17.session.set_dc(option.id, option.ip_address, option.port)
                    ErBot17.session.save()
                    break
            tgbot.get_me()
            ErBot17.me = ErBot17.get_me()
            ErBot17.uid = tgbot.uid = utils.get_peer_id(ErBot17.me)
            if pdB.get_key("OWNER_ID") or Var.OWNER_ID == 0:
                Var.OWNER_ID = utils.get_peer_id(ErBot17.me)
                pdB.set_key("OWNER_ID", Var.OWNER_ID)
            else:
                pdB.set_key("OWNER_ID", ErBot17.uid)
        except Exception as e:
            LOGS.error(f"STRING_SESSION17 - {e}")
            sys.exit()

    if pdB.get_key("SESSION18") or Var.STRING_SESSION18 and Database.BOT_TOKEN:
        try:
            ErBot18.connect()
            config = ErBot18(functions.help.GetConfigRequest())
            for option in config.dc_options:
                if option.ip_address == ErBot18.session.server_address:
                    if ErBot18.session.dc_id != option.id:
                        LOGS.warning(
                            f"Fixed DC ID in session from {ErBot18.session.dc_id}"
                            f" to {option.id}"
                    )
                    ErBot18.session.set_dc(option.id, option.ip_address, option.port)
                    ErBot18.session.save()
                    break
            tgbot.get_me()
            ErBot18.me = ErBot18.get_me()
            ErBot18.uid = tgbot.uid = utils.get_peer_id(ErBot18.me)
            if pdB.get_key("OWNER_ID") or Var.OWNER_ID == 0:
                Var.OWNER_ID = utils.get_peer_id(ErBot18.me)
                pdB.set_key("OWNER_ID", Var.OWNER_ID)
            else:
                pdB.set_key("OWNER_ID", ErBot18.uid)
        except Exception as e:
            LOGS.error(f"STRING_SESSION18 - {e}")
            sys.exit()

    if pdB.get_key("SESSION19") or Var.STRING_SESSION19 and Database.BOT_TOKEN:
        try:
            ErBot19.connect()
            config = ErBot19(functions.help.GetConfigRequest())
            for option in config.dc_options:
                if option.ip_address == ErBot19.session.server_address:
                    if ErBot19.session.dc_id != option.id:
                        LOGS.warning(
                            f"Fixed DC ID in session from {ErBot19.session.dc_id}"
                            f" to {option.id}"
                    )
                    ErBot19.session.set_dc(option.id, option.ip_address, option.port)
                    ErBot19.session.save()
                    break
            tgbot.get_me()
            ErBot19.me = ErBot19.get_me()
            ErBot19.uid = tgbot.uid = utils.get_peer_id(ErBot19.me)
            if pdB.get_key("OWNER_ID") or Var.OWNER_ID == 0:
                Var.OWNER_ID = utils.get_peer_id(ErBot19.me)
                pdB.set_key("OWNER_ID", Var.OWNER_ID)
            else:
                pdB.set_key("OWNER_ID", ErBot19.uid)
        except Exception as e:
            LOGS.error(f"STRING_SESSION2 - {e}")
            sys.exit()

    if pdB.get_key("SESSION20") or Var.STRING_SESSION20 and Database.BOT_TOKEN:
        try:
            ErBot20.connect()
            config = ErBot20(functions.help.GetConfigRequest())
            for option in config.dc_options:
                if option.ip_address == ErBot20.session.server_address:
                    if ErBot20.session.dc_id != option.id:
                        LOGS.warning(
                            f"Fixed DC ID in session from {ErBot20.session.dc_id}"
                            f" to {option.id}"
                    )
                    ErBot20.session.set_dc(option.id, option.ip_address, option.port)
                    ErBot20.session.save()
                    break
            tgbot.get_me()
            ErBot20.me = ErBot20.get_me()
            ErBot20.uid = tgbot.uid = utils.get_peer_id(ErBot20.me)
            if pdB.get_key("OWNER_ID") or Var.OWNER_ID == 0:
                Var.OWNER_ID = utils.get_peer_id(ErBot20.me)
                pdB.set_key("OWNER_ID", Var.OWNER_ID)
            else:
                pdB.set_key("OWNER_ID", ErBot20.uid)
        except Exception as e:
            LOGS.error(f"STRING_SESSION20 - {e}")
            sys.exit()

    if pdB.get_key("SESSION21") or Var.STRING_SESSION21 and Database.BOT_TOKEN:
        try:
            ErBot21.connect()
            config = ErBot21(functions.help.GetConfigRequest())
            for option in config.dc_options:
                if option.ip_address == ErBot21.session.server_address:
                    if ErBot21.session.dc_id != option.id:
                        LOGS.warning(
                            f"Fixed DC ID in session from {ErBot21.session.dc_id}"
                            f" to {option.id}"
                    )
                    ErBot21.session.set_dc(option.id, option.ip_address, option.port)
                    ErBot21.session.save()
                    break
            tgbot.get_me()
            ErBot21.me = ErBot21.get_me()
            ErBot21.uid = tgbot.uid = utils.get_peer_id(ErBot21.me)
            if pdB.get_key("OWNER_ID") or Var.OWNER_ID == 0:
                Var.OWNER_ID = utils.get_peer_id(ErBot21.me)
                pdB.set_key("OWNER_ID", Var.OWNER_ID)
            else:
                pdB.set_key("OWNER_ID", ErBot21.uid)
        except Exception as e:
            LOGS.error(f"STRING_SESSION21 - {e}")
            sys.exit()

    if pdB.get_key("SESSION22") or Var.STRING_SESSION22 and Database.BOT_TOKEN:
        try:
            ErBot22.connect()
            config = ErBot22(functions.help.GetConfigRequest())
            for option in config.dc_options:
                if option.ip_address == ErBot22.session.server_address:
                    if ErBot22.session.dc_id != option.id:
                        LOGS.warning(
                            f"Fixed DC ID in session from {ErBot22.session.dc_id}"
                            f" to {option.id}"
                    )
                    ErBot22.session.set_dc(option.id, option.ip_address, option.port)
                    ErBot22.session.save()
                    break
            tgbot.get_me()
            ErBot22.me = ErBot22.get_me()
            ErBot22.uid = tgbot.uid = utils.get_peer_id(ErBot22.me)
            if pdB.get_key("OWNER_ID") or Var.OWNER_ID == 0:
                Var.OWNER_ID = utils.get_peer_id(ErBot22.me)
                pdB.set_key("OWNER_ID", Var.OWNER_ID)
            else:
                pdB.set_key("OWNER_ID", ErBot22.uid)
        except Exception as e:
            LOGS.error(f"STRING_SESSION22 - {e}")
            sys.exit()

    if pdB.get_key("SESSION23") or Var.STRING_SESSION23 and Database.BOT_TOKEN:
        try:
            ErBot23.connect()
            config = ErBot23(functions.help.GetConfigRequest())
            for option in config.dc_options:
                if option.ip_address == ErBot23.session.server_address:
                    if ErBot23.session.dc_id != option.id:
                        LOGS.warning(
                            f"Fixed DC ID in session from {ErBot23.session.dc_id}"
                            f" to {option.id}"
                    )
                    ErBot23.session.set_dc(option.id, option.ip_address, option.port)
                    ErBot23.session.save()
                    break
            tgbot.get_me()
            ErBot23.me = ErBot23.get_me()
            ErBot23.uid = tgbot.uid = utils.get_peer_id(ErBot23.me)
            if pdB.get_key("OWNER_ID") or Var.OWNER_ID == 0:
                Var.OWNER_ID = utils.get_peer_id(ErBot23.me)
                pdB.set_key("OWNER_ID", Var.OWNER_ID)
            else:
                pdB.set_key("OWNER_ID", ErBot23.uid)
        except Exception as e:
            LOGS.error(f"STRING_SESSION23 - {e}")
            sys.exit()

    if pdB.get_key("SESSION24") or Var.STRING_SESSION24 and Database.BOT_TOKEN:
        try:
            ErBot24.connect()
            config = ErBot24(functions.help.GetConfigRequest())
            for option in config.dc_options:
                if option.ip_address == ErBot24.session.server_address:
                    if ErBot24.session.dc_id != option.id:
                        LOGS.warning(
                            f"Fixed DC ID in session from {ErBot24.session.dc_id}"
                            f" to {option.id}"
                    )
                    ErBot24.session.set_dc(option.id, option.ip_address, option.port)
                    ErBot24.session.save()
                    break
            tgbot.get_me()
            ErBot24.me = ErBot24.get_me()
            ErBot24.uid = tgbot.uid = utils.get_peer_id(ErBot24.me)
            if pdB.get_key("OWNER_ID") or Var.OWNER_ID == 0:
                Var.OWNER_ID = utils.get_peer_id(ErBot24.me)
                pdB.set_key("OWNER_ID", Var.OWNER_ID)
            else:
                pdB.set_key("OWNER_ID", ErBot24.uid)
        except Exception as e:
            LOGS.error(f"STRING_SESSION24 - {e}")
            sys.exit()

    if pdB.get_key("SESSION25") or Var.STRING_SESSION25 and Database.BOT_TOKEN:
        try:
            ErBot25.connect()
            config = ErBot25(functions.help.GetConfigRequest())
            for option in config.dc_options:
                if option.ip_address == ErBot25.session.server_address:
                    if ErBot25.session.dc_id != option.id:
                        LOGS.warning(
                            f"Fixed DC ID in session from {ErBot25.session.dc_id}"
                            f" to {option.id}"
                    )
                    ErBot25.session.set_dc(option.id, option.ip_address, option.port)
                    ErBot25.session.save()
                    break
            tgbot.get_me()
            ErBot25.me = ErBot25.get_me()
            ErBot25.uid = tgbot.uid = utils.get_peer_id(ErBot25.me)
            if pdB.get_key("OWNER_ID") or Var.OWNER_ID == 0:
                Var.OWNER_ID = utils.get_peer_id(ErBot25.me)
                pdB.set_key("OWNER_ID", Var.OWNER_ID)
            else:
                pdB.set_key("OWNER_ID", ErBot25.uid)
        except Exception as e:
            LOGS.error(f"STRING_SESSION25 - {e}")
            sys.exit()

    if pdB.get_key("SESSION26") or Var.STRING_SESSION26 and Database.BOT_TOKEN:
        try:
            ErBot26.connect()
            config = ErBot26(functions.help.GetConfigRequest())
            for option in config.dc_options:
                if option.ip_address == ErBot26.session.server_address:
                    if ErBot26.session.dc_id != option.id:
                        LOGS.warning(
                            f"Fixed DC ID in session from {ErBot26.session.dc_id}"
                            f" to {option.id}"
                    )
                    ErBot26.session.set_dc(option.id, option.ip_address, option.port)
                    ErBot26.session.save()
                    break
            tgbot.get_me()
            ErBot26.me = ErBot26.get_me()
            ErBot26.uid = tgbot.uid = utils.get_peer_id(ErBot26.me)
            if pdB.get_key("OWNER_ID") or Var.OWNER_ID == 0:
                Var.OWNER_ID = utils.get_peer_id(ErBot26.me)
                pdB.set_key("OWNER_ID", Var.OWNER_ID)
            else:
                pdB.set_key("OWNER_ID", ErBot26.uid)
        except Exception as e:
            LOGS.error(f"STRING_SESSION26 - {e}")
            sys.exit()

    if pdB.get_key("SESSION27") or Var.STRING_SESSION27 and Database.BOT_TOKEN:
        try:
            ErBot27.connect()
            config = ErBot27(functions.help.GetConfigRequest())
            for option in config.dc_options:
                if option.ip_address == ErBot27.session.server_address:
                    if ErBot27.session.dc_id != option.id:
                        LOGS.warning(
                            f"Fixed DC ID in session from {ErBot27.session.dc_id}"
                            f" to {option.id}"
                    )
                    ErBot27.session.set_dc(option.id, option.ip_address, option.port)
                    ErBot27.session.save()
                    break
            tgbot.get_me()
            ErBot27.me = ErBot27.get_me()
            ErBot27.uid = tgbot.uid = utils.get_peer_id(ErBot27.me)
            if pdB.get_key("OWNER_ID") or Var.OWNER_ID == 0:
                Var.OWNER_ID = utils.get_peer_id(ErBot27.me)
                pdB.set_key("OWNER_ID", Var.OWNER_ID)
            else:
                pdB.set_key("OWNER_ID", ErBot27.uid)
        except Exception as e:
            LOGS.error(f"STRING_SESSION27 - {e}")
            sys.exit()

    if pdB.get_key("SESSION28") or Var.STRING_SESSION28 and Database.BOT_TOKEN:
        try:
            ErBot28.connect()
            config = ErBot28(functions.help.GetConfigRequest())
            for option in config.dc_options:
                if option.ip_address == ErBot28.session.server_address:
                    if ErBot28.session.dc_id != option.id:
                        LOGS.warning(
                            f"Fixed DC ID in session from {ErBot28.session.dc_id}"
                            f" to {option.id}"
                    )
                    ErBot28.session.set_dc(option.id, option.ip_address, option.port)
                    ErBot28.session.save()
                    break
            tgbot.get_me()
            ErBot28.me = ErBot28.get_me()
            ErBot28.uid = tgbot.uid = utils.get_peer_id(ErBot28.me)
            if pdB.get_key("OWNER_ID") or Var.OWNER_ID == 0:
                Var.OWNER_ID = utils.get_peer_id(ErBot28.me)
                pdB.set_key("OWNER_ID", Var.OWNER_ID)
            else:
                pdB.set_key("OWNER_ID", ErBot28.uid)
        except Exception as e:
            LOGS.error(f"STRING_SESSION28 - {e}")
            sys.exit()

    if pdB.get_key("SESSION29") or Var.STRING_SESSION29 and Database.BOT_TOKEN:
        try:
            ErBot29.connect()
            config = ErBot29(functions.help.GetConfigRequest())
            for option in config.dc_options:
                if option.ip_address == ErBot29.session.server_address:
                    if ErBot29.session.dc_id != option.id:
                        LOGS.warning(
                            f"Fixed DC ID in session from {ErBot29.session.dc_id}"
                            f" to {option.id}"
                    )
                    ErBot29.session.set_dc(option.id, option.ip_address, option.port)
                    ErBot29.session.save()
                    break
            tgbot.get_me()
            ErBot29.me = ErBot29.get_me()
            ErBot29.uid = tgbot.uid = utils.get_peer_id(ErBot29.me)
            if pdB.get_key("OWNER_ID") or Var.OWNER_ID == 0:
                Var.OWNER_ID = utils.get_peer_id(ErBot29.me)
                pdB.set_key("OWNER_ID", Var.OWNER_ID)
            else:
                pdB.set_key("OWNER_ID", ErBot29.uid)
        except Exception as e:
            LOGS.error(f"STRING_SESSION29 - {e}")
            sys.exit()

    if pdB.get_key("SESSION30") or Var.STRING_SESSION30 and Database.BOT_TOKEN:
        try:
            ErBot30.connect()
            config = ErBot30(functions.help.GetConfigRequest())
            for option in config.dc_options:
                if option.ip_address == ErBot2.session.server_address:
                    if ErBot30.session.dc_id != option.id:
                        LOGS.warning(
                            f"Fixed DC ID in session from {ErBot30.session.dc_id}"
                            f" to {option.id}"
                    )
                    ErBot30.session.set_dc(option.id, option.ip_address, option.port)
                    ErBot30.session.save()
                    break
            tgbot.get_me()
            ErBot30.me = ErBot30.get_me()
            ErBot30.uid = tgbot.uid = utils.get_peer_id(ErBot30.me)
            if pdB.get_key("OWNER_ID") or Var.OWNER_ID == 0:
                Var.OWNER_ID = utils.get_peer_id(ErBot30.me)
                pdB.set_key("OWNER_ID", Var.OWNER_ID)
            else:
                pdB.set_key("OWNER_ID", ErBot30.uid)
        except Exception as e:
            LOGS.error(f"STRING_SESSION30 - {e}")
            sys.exit()

    if pdB.get_key("SESSION31") or Var.STRING_SESSION31 and Database.BOT_TOKEN:
        try:
            ErBot31.connect()
            config = ErBot31(functions.help.GetConfigRequest())
            for option in config.dc_options:
                if option.ip_address == ErBot31.session.server_address:
                    if ErBot31.session.dc_id != option.id:
                        LOGS.warning(
                            f"Fixed DC ID in session from {ErBot31.session.dc_id}"
                            f" to {option.id}"
                    )
                    ErBot31.session.set_dc(option.id, option.ip_address, option.port)
                    ErBot31.session.save()
                    break
            tgbot.get_me()
            ErBot31.me = ErBot31.get_me()
            ErBot31.uid = tgbot.uid = utils.get_peer_id(ErBot31.me)
            if pdB.get_key("OWNER_ID") or Var.OWNER_ID == 0:
                Var.OWNER_ID = utils.get_peer_id(ErBot31.me)
                pdB.set_key("OWNER_ID", Var.OWNER_ID)
            else:
                pdB.set_key("OWNER_ID", ErBot31.uid)
        except Exception as e:
            LOGS.error(f"STRING_SESSION31 - {e}")
            sys.exit()

    if pdB.get_key("SESSION32") or Var.STRING_SESSION32 and Database.BOT_TOKEN:
        try:
            ErBot32.connect()
            config = ErBot32(functions.help.GetConfigRequest())
            for option in config.dc_options:
                if option.ip_address == ErBot32.session.server_address:
                    if ErBot32.session.dc_id != option.id:
                        LOGS.warning(
                            f"Fixed DC ID in session from {ErBot32.session.dc_id}"
                            f" to {option.id}"
                    )
                    ErBot32.session.set_dc(option.id, option.ip_address, option.port)
                    ErBot32.session.save()
                    break
            tgbot.get_me()
            ErBot32.me = ErBot32.get_me()
            ErBot32.uid = tgbot.uid = utils.get_peer_id(ErBot32.me)
            if pdB.get_key("OWNER_ID") or Var.OWNER_ID == 0:
                Var.OWNER_ID = utils.get_peer_id(ErBot32.me)
                pdB.set_key("OWNER_ID", Var.OWNER_ID)
            else:
                pdB.set_key("OWNER_ID", ErBot32.uid)
        except Exception as e:
            LOGS.error(f"STRING_SESSION32 - {e}")
            sys.exit()

    if pdB.get_key("SESSION33") or Var.STRING_SESSION33 and Database.BOT_TOKEN:
        try:
            ErBot33.connect()
            config = ErBot33(functions.help.GetConfigRequest())
            for option in config.dc_options:
                if option.ip_address == ErBot33.session.server_address:
                    if ErBot33.session.dc_id != option.id:
                        LOGS.warning(
                            f"Fixed DC ID in session from {ErBot33.session.dc_id}"
                            f" to {option.id}"
                    )
                    ErBot33.session.set_dc(option.id, option.ip_address, option.port)
                    ErBot33.session.save()
                    break
            tgbot.get_me()
            ErBot33.me = ErBot33.get_me()
            PandaBo33.uid = tgbot.uid = utils.get_peer_id(ErBot33.me)
            if pdB.get_key("OWNER_ID") or Var.OWNER_ID == 0:
                Var.OWNER_ID = utils.get_peer_id(ErBot33.me)
                pdB.set_key("OWNER_ID", Var.OWNER_ID)
            else:
                pdB.set_key("OWNER_ID", ErBot33.uid)
        except Exception as e:
            LOGS.error(f"STRING_SESSION33 - {e}")
            sys.exit()

    if pdB.get_key("SESSION34") or Var.STRING_SESSION34 and Database.BOT_TOKEN:
        try:
            ErBot34.connect()
            config = ErBot34(functions.help.GetConfigRequest())
            for option in config.dc_options:
                if option.ip_address == ErBot34.session.server_address:
                    if ErBot34.session.dc_id != option.id:
                        LOGS.warning(
                            f"Fixed DC ID in session from {ErBot34.session.dc_id}"
                            f" to {option.id}"
                    )
                    ErBot34.session.set_dc(option.id, option.ip_address, option.port)
                    ErBot34.session.save()
                    break
            tgbot.get_me()
            ErBot34.me = ErBot34.get_me()
            ErBot34.uid = tgbot.uid = utils.get_peer_id(ErBot34.me)
            if pdB.get_key("OWNER_ID") or Var.OWNER_ID == 0:
                Var.OWNER_ID = utils.get_peer_id(ErBot34.me)
                pdB.set_key("OWNER_ID", Var.OWNER_ID)
            else:
                pdB.set_key("OWNER_ID", ErBot34.uid)
        except Exception as e:
            LOGS.error(f"STRING_SESSION34 - {e}")
            sys.exit()

    if pdB.get_key("SESSION35") or Var.STRING_SESSION35 and Database.BOT_TOKEN:
        try:
            ErBot35.connect()
            config = ErBot35(functions.help.GetConfigRequest())
            for option in config.dc_options:
                if option.ip_address == ErBot35.session.server_address:
                    if ErBot35.session.dc_id != option.id:
                        LOGS.warning(
                            f"Fixed DC ID in session from {ErBot35.session.dc_id}"
                            f" to {option.id}"
                    )
                    ErBot35.session.set_dc(option.id, option.ip_address, option.port)
                    ErBot35.session.save()
                    break
            tgbot.get_me()
            ErBot35.me = ErBot35.get_me()
            ErBot35.uid = tgbot.uid = utils.get_peer_id(ErBot35.me)
            if pdB.get_key("OWNER_ID") or Var.OWNER_ID == 0:
                Var.OWNER_ID = utils.get_peer_id(ErBot35.me)
                pdB.set_key("OWNER_ID", Var.OWNER_ID)
            else:
                pdB.set_key("OWNER_ID", ErBot35.uid)
        except Exception as e:
            LOGS.error(f"STRING_SESSION35 - {e}")
            sys.exit()

    if pdB.get_key("SESSION36") or Var.STRING_SESSION36 and Database.BOT_TOKEN:
        try:
            ErBot36.connect()
            config = ErBot36(functions.help.GetConfigRequest())
            for option in config.dc_options:
                if option.ip_address == ErBot36.session.server_address:
                    if ErBot36.session.dc_id != option.id:
                        LOGS.warning(
                            f"Fixed DC ID in session from {ErBot36.session.dc_id}"
                            f" to {option.id}"
                    )
                    ErBot36.session.set_dc(option.id, option.ip_address, option.port)
                    ErBot36.session.save()
                    break
            tgbot.get_me()
            ErBot36.me = ErBot36.get_me()
            PandaBo36.uid = tgbot.uid = utils.get_peer_id(ErBot36.me)
            if pdB.get_key("OWNER_ID") or Var.OWNER_ID == 0:
                Var.OWNER_ID = utils.get_peer_id(ErBot36.me)
                pdB.set_key("OWNER_ID", Var.OWNER_ID)
            else:
                pdB.set_key("OWNER_ID", ErBot36.uid)
        except Exception as e:
            LOGS.error(f"STRING_SESSION36 - {e}")
            sys.exit()
     
    if pdB.get_key("SESSION37") or Var.STRING_SESSION37 and Database.BOT_TOKEN:
        try:
            ErBot37.connect()
            config = ErBot37(functions.help.GetConfigRequest())
            for option in config.dc_options:
                if option.ip_address == ErBot37.session.server_address:
                    if ErBot37.session.dc_id != option.id:
                        LOGS.warning(
                            f"Fixed DC ID in session from {ErBot37.session.dc_id}"
                            f" to {option.id}"
                    )
                    ErBot37.session.set_dc(option.id, option.ip_address, option.port)
                    ErBot37.session.save()
                    break
            tgbot.get_me()
            ErBot37.me = ErBot37.get_me()
            ErBot37.uid = tgbot.uid = utils.get_peer_id(ErBot37.me)
            if pdB.get_key("OWNER_ID") or Var.OWNER_ID == 0:
                Var.OWNER_ID = utils.get_peer_id(ErBot37.me)
                pdB.set_key("OWNER_ID", Var.OWNER_ID)
            else:
                pdB.set_key("OWNER_ID", ErBot37.uid)
        except Exception as e:
            LOGS.error(f"STRING_SESSION37 - {e}")
            sys.exit()

    if pdB.get_key("SESSION38") or Var.STRING_SESSION38 and Database.BOT_TOKEN:
        try:
            ErBot38.connect()
            config = ErBot38(functions.help.GetConfigRequest())
            for option in config.dc_options:
                if option.ip_address == ErBot38.session.server_address:
                    if ErBot38.session.dc_id != option.id:
                        LOGS.warning(
                            f"Fixed DC ID in session from {ErBot38.session.dc_id}"
                            f" to {option.id}"
                    )
                    ErBot38.session.set_dc(option.id, option.ip_address, option.port)
                    ErBot38.session.save()
                    break
            tgbot.get_me()
            ErBot38.me = ErBot38.get_me()
            ErBot38.uid = tgbot.uid = utils.get_peer_id(ErBot38.me)
            if pdB.get_key("OWNER_ID") or Var.OWNER_ID == 0:
                Var.OWNER_ID = utils.get_peer_id(ErBot38.me)
                pdB.set_key("OWNER_ID", Var.OWNER_ID)
            else:
                pdB.set_key("OWNER_ID", ErBot38.uid)
        except Exception as e:
            LOGS.error(f"STRING_SESSION38 - {e}")
            sys.exit()

    if pdB.get_key("SESSION39") or Var.STRING_SESSION39 and Database.BOT_TOKEN:
        try:
            ErBot39.connect()
            config = ErBot39(functions.help.GetConfigRequest())
            for option in config.dc_options:
                if option.ip_address == ErBot39.session.server_address:
                    if ErBot39.session.dc_id != option.id:
                        LOGS.warning(
                            f"Fixed DC ID in session from {ErBot39.session.dc_id}"
                            f" to {option.id}"
                    )
                    ErBot39.session.set_dc(option.id, option.ip_address, option.port)
                    ErBot39.session.save()
                    break
            tgbot.get_me()
            ErBot39.me = ErBot39.get_me()
            ErBot39.uid = tgbot.uid = utils.get_peer_id(ErBot39.me)
            if pdB.get_key("OWNER_ID") or Var.OWNER_ID == 0:
                Var.OWNER_ID = utils.get_peer_id(ErBot39.me)
                pdB.set_key("OWNER_ID", Var.OWNER_ID)
            else:
                pdB.set_key("OWNER_ID", ErBot39.uid)
        except Exception as e:
            LOGS.error(f"STRING_SESSION39 - {e}")
            sys.exit()

    if pdB.get_key("SESSION40") or Var.STRING_SESSION40 and Database.BOT_TOKEN:
        try:
            ErBot40.connect()
            config = ErBot40(functions.help.GetConfigRequest())
            for option in config.dc_options:
                if option.ip_address == ErBot40.session.server_address:
                    if ErBot40.session.dc_id != option.id:
                        LOGS.warning(
                            f"Fixed DC ID in session from {ErBot40.session.dc_id}"
                            f" to {option.id}"
                    )
                    ErBot40.session.set_dc(option.id, option.ip_address, option.port)
                    ErBot40.session.save()
                    break
            tgbot.get_me()
            ErBot40.me = ErBot40.get_me()
            PandaBo40.uid = tgbot.uid = utils.get_peer_id(ErBot40.me)
            if pdB.get_key("OWNER_ID") or Var.OWNER_ID == 0:
                Var.OWNER_ID = utils.get_peer_id(ErBot40.me)
                pdB.set_key("OWNER_ID", Var.OWNER_ID)
            else:
                pdB.set_key("OWNER_ID", ErBot40.uid)
        except Exception as e:
            LOGS.error(f"STRING_SESSION40 - {e}")
            sys.exit()
     
    if pdB.get_key("SESSION41") or Var.STRING_SESSION41 and Database.BOT_TOKEN:
        try:
            ErBot41.connect()
            config = ErBot41(functions.help.GetConfigRequest())
            for option in config.dc_options:
                if option.ip_address == ErBot41.session.server_address:
                    if ErBot41.session.dc_id != option.id:
                        LOGS.warning(
                            f"Fixed DC ID in session from {ErBot41.session.dc_id}"
                            f" to {option.id}"
                    )
                    ErBot41.session.set_dc(option.id, option.ip_address, option.port)
                    ErBot41.session.save()
                    break
            tgbot.get_me()
            ErBot41.me = ErBot41.get_me()
            ErBot41.uid = tgbot.uid = utils.get_peer_id(ErBot41.me)
            if pdB.get_key("OWNER_ID") or Var.OWNER_ID == 0:
                Var.OWNER_ID = utils.get_peer_id(ErBot41.me)
                pdB.set_key("OWNER_ID", Var.OWNER_ID)
            else:
                pdB.set_key("OWNER_ID", ErBot41.uid)
        except Exception as e:
            LOGS.error(f"STRING_SESSION41 - {e}")
            sys.exit()

    if pdB.get_key("SESSION42") or Var.STRING_SESSION42 and Database.BOT_TOKEN:
        try:
            ErBot42.connect()
            config = ErBot42(functions.help.GetConfigRequest())
            for option in config.dc_options:
                if option.ip_address == ErBot42.session.server_address:
                    if ErBot42.session.dc_id != option.id:
                        LOGS.warning(
                            f"Fixed DC ID in session from {ErBot42.session.dc_id}"
                            f" to {option.id}"
                    )
                    ErBot42.session.set_dc(option.id, option.ip_address, option.port)
                    ErBot42.session.save()
                    break
            tgbot.get_me()
            ErBot42.me = ErBot42.get_me()
            ErBot42.uid = tgbot.uid = utils.get_peer_id(ErBot42.me)
            if pdB.get_key("OWNER_ID") or Var.OWNER_ID == 0:
                Var.OWNER_ID = utils.get_peer_id(ErBot42.me)
                pdB.set_key("OWNER_ID", Var.OWNER_ID)
            else:
                pdB.set_key("OWNER_ID", ErBot42.uid)
        except Exception as e:
            LOGS.error(f"STRING_SESSION42 - {e}")
            sys.exit()

    if pdB.get_key("SESSION43") or Var.STRING_SESSION43 and Database.BOT_TOKEN:
        try:
            ErBot43.connect()
            config = ErBot43(functions.help.GetConfigRequest())
            for option in config.dc_options:
                if option.ip_address == ErBot43.session.server_address:
                    if ErBot43.session.dc_id != option.id:
                        LOGS.warning(
                            f"Fixed DC ID in session from {ErBot43.session.dc_id}"
                            f" to {option.id}"
                    )
                    ErBot43.session.set_dc(option.id, option.ip_address, option.port)
                    ErBot43.session.save()
                    break
            tgbot.get_me()
            ErBot43.me = ErBot43.get_me()
            ErBot43.uid = tgbot.uid = utils.get_peer_id(ErBot43.me)
            if pdB.get_key("OWNER_ID") or Var.OWNER_ID == 0:
                Var.OWNER_ID = utils.get_peer_id(ErBot43.me)
                pdB.set_key("OWNER_ID", Var.OWNER_ID)
            else:
                pdB.set_key("OWNER_ID", ErBot43.uid)
        except Exception as e:
            LOGS.error(f"STRING_SESSION43 - {e}")
            sys.exit()

    if pdB.get_key("SESSION44") or Var.STRING_SESSION44 and Database.BOT_TOKEN:
        try:
            ErBot44.connect()
            config = ErBot44(functions.help.GetConfigRequest())
            for option in config.dc_options:
                if option.ip_address == ErBot44.session.server_address:
                    if ErBot44.session.dc_id != option.id:
                        LOGS.warning(
                            f"Fixed DC ID in session from {ErBot44.session.dc_id}"
                            f" to {option.id}"
                    )
                    ErBot44.session.set_dc(option.id, option.ip_address, option.port)
                    ErBot44.session.save()
                    break
            tgbot.get_me()
            ErBot44.me = ErBot44.get_me()
            ErBot44.uid = tgbot.uid = utils.get_peer_id(ErBot44.me)
            if pdB.get_key("OWNER_ID") or Var.OWNER_ID == 0:
                Var.OWNER_ID = utils.get_peer_id(ErBot44.me)
                pdB.set_key("OWNER_ID", Var.OWNER_ID)
            else:
                pdB.set_key("OWNER_ID", ErBot44.uid)
        except Exception as e:
            LOGS.error(f"STRING_SESSION44 - {e}")
            sys.exit()
     
    if pdB.get_key("SESSION45") or Var.STRING_SESSION45 and Database.BOT_TOKEN:
        try:
            ErBot45.connect()
            config = ErBot45(functions.help.GetConfigRequest())
            for option in config.dc_options:
                if option.ip_address == ErBot45.session.server_address:
                    if ErBot45.session.dc_id != option.id:
                        LOGS.warning(
                            f"Fixed DC ID in session from {ErBot45.session.dc_id}"
                            f" to {option.id}"
                    )
                    ErBot45.session.set_dc(option.id, option.ip_address, option.port)
                    ErBot45.session.save()
                    break
            tgbot.get_me()
            ErBot45.me = ErBot45.get_me()
            ErBot45.uid = tgbot.uid = utils.get_peer_id(ErBot45.me)
            if pdB.get_key("OWNER_ID") or Var.OWNER_ID == 0:
                Var.OWNER_ID = utils.get_peer_id(ErBot45.me)
                pdB.set_key("OWNER_ID", Var.OWNER_ID)
            else:
                pdB.set_key("OWNER_ID", ErBot45.uid)
        except Exception as e:
            LOGS.error(f"STRING_SESSION45 - {e}")
            sys.exit()

    if pdB.get_key("SESSION46") or Var.STRING_SESSION46 and Database.BOT_TOKEN:
        try:
            ErBot46.connect()
            config = ErBot46(functions.help.GetConfigRequest())
            for option in config.dc_options:
                if option.ip_address == ErBot46.session.server_address:
                    if ErBot46.session.dc_id != option.id:
                        LOGS.warning(
                            f"Fixed DC ID in session from {ErBot46.session.dc_id}"
                            f" to {option.id}"
                    )
                    ErBot46.session.set_dc(option.id, option.ip_address, option.port)
                    ErBot46.session.save()
                    break
            tgbot.get_me()
            ErBot46.me = ErBot46.get_me()
            ErBot46.uid = tgbot.uid = utils.get_peer_id(ErBot46.me)
            if pdB.get_key("OWNER_ID") or Var.OWNER_ID == 0:
                Var.OWNER_ID = utils.get_peer_id(ErBot46.me)
                pdB.set_key("OWNER_ID", Var.OWNER_ID)
            else:
                pdB.set_key("OWNER_ID", ErBot46.uid)
        except Exception as e:
            LOGS.error(f"STRING_SESSION46 - {e}")
            sys.exit()

    if pdB.get_key("SESSION47") or Var.STRING_SESSION47 and Database.BOT_TOKEN:
        try:
            ErBot47.connect()
            config = ErBot47(functions.help.GetConfigRequest())
            for option in config.dc_options:
                if option.ip_address == ErBot47.session.server_address:
                    if ErBot47.session.dc_id != option.id:
                        LOGS.warning(
                            f"Fixed DC ID in session from {ErBot47.session.dc_id}"
                            f" to {option.id}"
                    )
                    ErBot47.session.set_dc(option.id, option.ip_address, option.port)
                    ErBot47.session.save()
                    break
            tgbot.get_me()
            ErBot47.me = ErBot47.get_me()
            ErBot47.uid = tgbot.uid = utils.get_peer_id(ErBot47.me)
            if pdB.get_key("OWNER_ID") or Var.OWNER_ID == 0:
                Var.OWNER_ID = utils.get_peer_id(ErBot47.me)
                pdB.set_key("OWNER_ID", Var.OWNER_ID)
            else:
                pdB.set_key("OWNER_ID", ErBot47.uid)
        except Exception as e:
            LOGS.error(f"STRING_SESSION47 - {e}")
            sys.exit()

    if pdB.get_key("SESSION33") or Var.STRING_SESSION33 and Database.BOT_TOKEN:
        try:
            ErBot48.connect()
            config = ErBot48(functions.help.GetConfigRequest())
            for option in config.dc_options:
                if option.ip_address == ErBot48.session.server_address:
                    if ErBot48.session.dc_id != option.id:
                        LOGS.warning(
                            f"Fixed DC ID in session from {ErBot48.session.dc_id}"
                            f" to {option.id}"
                    )
                    ErBot48.session.set_dc(option.id, option.ip_address, option.port)
                    ErBot48.session.save()
                    break
            tgbot.get_me()
            ErBot48.me = ErBot48.get_me()
            ErBot48.uid = tgbot.uid = utils.get_peer_id(ErBot48.me)
            if pdB.get_key("OWNER_ID") or Var.OWNER_ID == 0:
                Var.OWNER_ID = utils.get_peer_id(ErBot48.me)
                pdB.set_key("OWNER_ID", Var.OWNER_ID)
            else:
                pdB.set_key("OWNER_ID", ErBot48.uid)
        except Exception as e:
            LOGS.error(f"STRING_SESSION48 - {e}")
            sys.exit()
     
    if pdB.get_key("SESSION49") or Var.STRING_SESSION49 and Database.BOT_TOKEN:
        try:
            ErBot49.connect()
            config = ErBot49(functions.help.GetConfigRequest())
            for option in config.dc_options:
                if option.ip_address == ErBot49.session.server_address:
                    if ErBot49.session.dc_id != option.id:
                        LOGS.warning(
                            f"Fixed DC ID in session from {ErBot49.session.dc_id}"
                            f" to {option.id}"
                    )
                    ErBot49.session.set_dc(option.id, option.ip_address, option.port)
                    ErBot49.session.save()
                    break
            tgbot.get_me()
            ErBot49.me = ErBot49.get_me()
            ErBot49.uid = tgbot.uid = utils.get_peer_id(ErBot49.me)
            if pdB.get_key("OWNER_ID") or Var.OWNER_ID == 0:
                Var.OWNER_ID = utils.get_peer_id(ErBot49.me)
                pdB.set_key("OWNER_ID", Var.OWNER_ID)
            else:
                pdB.set_key("OWNER_ID", ErBot49.uid)
        except Exception as e:
            LOGS.error(f"STRING_SESSION49 - {e}")
            sys.exit()

    if pdB.get_key("SESSION50") or Var.STRING_SESSION50 and Database.BOT_TOKEN:
        try:
            ErBot50.connect()
            config = ErBot50(functions.help.GetConfigRequest())
            for option in config.dc_options:
                if option.ip_address == ErBot50.session.server_address:
                    if ErBot50.session.dc_id != option.id:
                        LOGS.warning(
                            f"Fixed DC ID in session from {ErBot50.session.dc_id}"
                            f" to {option.id}"
                    )
                    ErBot50.session.set_dc(option.id, option.ip_address, option.port)
                    ErBot50.session.save()
                    break
            tgbot.get_me()
            ErBot50.me = ErBot50.get_me()
            ErBot50.uid = tgbot.uid = utils.get_peer_id(ErBot50.me)
            if pdB.get_key("OWNER_ID") or Var.OWNER_ID == 0:
                Var.OWNER_ID = utils.get_peer_id(ErBot50.me)
                pdB.set_key("OWNER_ID", Var.OWNER_ID)
            else:
                pdB.set_key("OWNER_ID", ErBot50.uid)
        except Exception as e:
            LOGS.error(f"STRING_SESSION50 - {e}")
            sys.exit()

    if not pdB.get_key("SESSION") or Var.STRING_SESSION and Database.BOT_TOKEN:
        failed += 1
    if not pdB.get_key("SESSION2") or Var.STRING_SESSION2 and Database.BOT_TOKEN:
        failed += 1
    if not pdB.get_key("SESSION3") or Var.STRING_SESSION3 and Database.BOT_TOKEN:
        failed += 1
    if not pdB.get_key("SESSION4") or Var.STRING_SESSION4 and Database.BOT_TOKEN:
        failed += 1
    if not pdB.get_key("SESSION5") or Var.STRING_SESSION5 and Database.BOT_TOKEN:
        failed += 1
    if not pdB.get_key("SESSION6") or Var.STRING_SESSION6 and Database.BOT_TOKEN:
        failed += 1
    if not pdB.get_key("SESSION7") or Var.STRING_SESSION7 and Database.BOT_TOKEN:
        failed += 1
    if not pdB.get_key("SESSION8") or Var.STRING_SESSION8 and Database.BOT_TOKEN:
        failed += 1
    if not pdB.get_key("SESSION9") or Var.STRING_SESSION9 and Database.BOT_TOKEN:
        failed += 1
    if not pdB.get_key("SESSION10") or Var.STRING_SESSION10 and Database.BOT_TOKEN:
        failed += 1
    if not pdB.get_key("SESSION11") or Var.STRING_SESSION11 and Database.BOT_TOKEN:
        failed += 1
    if not pdB.get_key("SESSION12") or Var.STRING_SESSION12 and Database.BOT_TOKEN:
        failed += 1
    if not pdB.get_key("SESSION13") or Var.STRING_SESSION13 and Database.BOT_TOKEN:
        failed += 1
    if not pdB.get_key("SESSION14") or Var.STRING_SESSION14 and Database.BOT_TOKEN:
        failed += 1
    if not pdB.get_key("SESSION15") or Var.STRING_SESSION15 and Database.BOT_TOKEN:
        failed += 1
    if not pdB.get_key("SESSION16") or Var.STRING_SESSION16 and Database.BOT_TOKEN:
        failed += 1
    if not pdB.get_key("SESSION17") or Var.STRING_SESSION17 and Database.BOT_TOKEN:
        failed += 1
    if not pdB.get_key("SESSION18") or Var.STRING_SESSION18 and Database.BOT_TOKEN:
        failed += 1
    if not pdB.get_key("SESSION19") or Var.STRING_SESSION19 and Database.BOT_TOKEN:
        failed += 1
    if not pdB.get_key("SESSION20") or Var.STRING_SESSION20 and Database.BOT_TOKEN:
        failed += 1
    if not pdB.get_key("SESSION21") or Var.STRING_SESSION21 and Database.BOT_TOKEN:
        failed += 1
    if not pdB.get_key("SESSION22") or Var.STRING_SESSION22 and Database.BOT_TOKEN:
        failed += 1
    if not pdB.get_key("SESSION23") or Var.STRING_SESSION23 and Database.BOT_TOKEN:
        failed += 1
    if not pdB.get_key("SESSION24") or Var.STRING_SESSION24 and Database.BOT_TOKEN:
        failed += 1
    if not pdB.get_key("SESSION25") or Var.STRING_SESSION25 and Database.BOT_TOKEN:
        failed += 1
    if not pdB.get_key("SESSION26") or Var.STRING_SESSION26 and Database.BOT_TOKEN:
        failed += 1
    if not pdB.get_key("SESSION27") or Var.STRING_SESSION27 and Database.BOT_TOKEN:
        failed += 1
    if not pdB.get_key("SESSION28") or Var.STRING_SESSION28 and Database.BOT_TOKEN:
        failed += 1
    if not pdB.get_key("SESSION29") or Var.STRING_SESSION29 and Database.BOT_TOKEN:
        failed += 1
    if not pdB.get_key("SESSION30") or Var.STRING_SESSION30 and Database.BOT_TOKEN:
        failed += 1
    if not pdB.get_key("SESSION31") or Var.STRING_SESSION31 and Database.BOT_TOKEN:
        failed += 1
    if not pdB.get_key("SESSION32") or Var.STRING_SESSION32 and Database.BOT_TOKEN:
        failed += 1
    if not pdB.get_key("SESSION33") or Var.STRING_SESSION33 and Database.BOT_TOKEN:
        failed += 1
    if not pdB.get_key("SESSION34") or Var.STRING_SESSION34 and Database.BOT_TOKEN:
        failed += 1
    if not pdB.get_key("SESSION35") or Var.STRING_SESSION35 and Database.BOT_TOKEN:
        failed += 1
    if not pdB.get_key("SESSION36") or Var.STRING_SESSION36 and Database.BOT_TOKEN:
        failed += 1
    if not pdB.get_key("SESSION37") or Var.STRING_SESSION37 and Database.BOT_TOKEN:
        failed += 1
    if not pdB.get_key("SESSION38") or Var.STRING_SESSION38 and Database.BOT_TOKEN:
        failed += 1
    if not pdB.get_key("SESSION39") or Var.STRING_SESSION39 and Database.BOT_TOKEN:
        failed += 1
    if not pdB.get_key("SESSION40") or Var.STRING_SESSION41 and Database.BOT_TOKEN:
        failed += 1
    if not pdB.get_key("SESSION42") or Var.STRING_SESSION42 and Database.BOT_TOKEN:
        failed += 1
    if not pdB.get_key("SESSION43") or Var.STRING_SESSION43 and Database.BOT_TOKEN:
        failed += 1
    if not pdB.get_key("SESSION44") or Var.STRING_SESSION44 and Database.BOT_TOKEN:
        failed += 1
    if not pdB.get_key("SESSION45") or Var.STRING_SESSION45 and Database.BOT_TOKEN:
        failed += 1
    if not pdB.get_key("SESSION46") or Var.STRING_SESSION46 and Database.BOT_TOKEN:
        failed += 1
    if not pdB.get_key("SESSION47") or Var.STRING_SESSION47 and Database.BOT_TOKEN:
        failed += 1
    if not pdB.get_key("SESSION48") or Var.STRING_SESSION48 and Database.BOT_TOKEN:
        failed += 1
    if not pdB.get_key("SESSION49") or Var.STRING_SESSION49 and Database.BOT_TOKEN:
        failed += 1
    if not pdB.get_key("SESSION50") or Var.STRING_SESSION50 and Database.BOT_TOKEN:
        failed += 1
    return failed

def Pyrogram():
    if pdB.get_key("PyroSESSION") or Database.PyroSESSION and Database.BOT_TOKEN:
        if app.bot:
            print("Activating assistant.\n")
            app.bot.start()
            print("Assistant activated.\n")
            asistant = app.import_module("ErUbot/modules/pyrogram/asistant/", exclude=app.NoLoad())
            print(f"\n\n{asistant} modules Loaded Sucesfull\n\n")
        else:
            print("Assistant start unsuccessful, please check that you have given the bot token.\n")
            print("skipping assistant start !")
        
    if app:
        print("Activating assistant.\n")
        app.start()
        print("Assistant activated.\n")
    else:
        print("Assistant start unsuccessful, please check that you have given the bot token.\n")
        print("skipping assistant start !")
    print("Modules: Installing.\n\n")
    modules = app.import_module("ErUbot/modules/pyrogram/", exclude=app.NoLoad())
    print(f"\n\n{modules} modules Loaded Sucesfull\n\n")
    print(f"⚙️ Er Userbot {pyrover} Telah Aktif")
    idle()
    
