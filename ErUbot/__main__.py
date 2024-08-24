# Copyright (C) 2021 PandaUserbot <https://github.com/ilhammansiz/PandaX_Userbot>
# Import Panda Userbot
# Recode by Ilham Mansiz
# t.me/PandaUserbot
# ••••••••••••••••••••••√•••••••••••••√√√••••••••

import sys
import ErUbot
from ErUbot import LOGS, Database, Config
import contextlib
from session.multisession_ import *

cmdhr = Config.COMMAND_HAND_LER



from . import resources


"""
async def memulai():
    await resources.buka(f"telethon")
    await resources.bukabot(f"assistant")
"""

def start():
    userbot.LOOP.run_until_complete(resources.ClientMultiTelethon())
    userbot.LOOP.run_until_complete(resources.memulai())
    #userbot.LOOP.run_until_complete(resources.cloneplugins())
    #userbot.LOOP.run_until_complete(resources.clonevc())
    userbot.LOOP.run_until_complete(resources.join())
    LOGS.info(f"꧁༺ Panda Userbot ༻꧂\n⚙️ Version:{userbot.__version__} [TELAH DIAKTIFKAN]")
    if ErBot:
        ErBot.send_message(PRIVATE, THON_ON.format(ErBot.me.username, userbot.__version__, cmdhr, total))
    if ErBot2:
        ErBot2.send_message(PRIVATE, THON_ON.format(ErBot2.me.username, userbot.__version__, cmdhr, total))
    if ErBot3:
        ErBot3.send_message(PRIVATE, THON_ON.format(ErBot3.me.username, userbot.__version__, cmdhr, total))
             


if __name__ == "__main__":
    if pdB.get_key("SESSION") or Database.SESSION:
        usersss = Telethon()
        total = 50 - usersss
        start()
        LOGS.info(f"Total Clients = {total} Users")
    if pdB.get_key("PyroSESSION") or Database.PyroSESSION:
        Pyrogram()
        
    
if ErBot:
    try:
        if len(sys.argv) in {1, 3, 4}:
            with contextlib.suppress(ConnectionError):
                ErBot.run_until_disconnected()
        else:
            ErBot.disconnect()    
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)

if ErBot2:
    try:
        if len(sys.argv) in {1, 3, 4}:
            with contextlib.suppress(ConnectionError):
                ErBot2.run_until_disconnected()
        else:
            ErBot2.disconnect()    
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)

if ErBot3:
    try:
        if len(sys.argv) in {1, 3, 4}:
            with contextlib.suppress(ConnectionError):
                ErBot3.run_until_disconnected()
        else:
            ErBot3.disconnect()    
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)
if ErBot4:
    try:
        if len(sys.argv) in {1, 3, 4}:
            with contextlib.suppress(ConnectionError):
                ErBot4.run_until_disconnected()
        else:
            ErBot4.disconnect()    
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)
if ErBot5:
    try:
        if len(sys.argv) in {1, 3, 4}:
            with contextlib.suppress(ConnectionError):
                ErBot5.run_until_disconnected()
        else:
            ErBot5.disconnect()    
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)
if ErBot6:
    try:
        if len(sys.argv) in {1, 3, 4}:
            with contextlib.suppress(ConnectionError):
                ErBot6.run_until_disconnected()
        else:
            ErBot6.disconnect()    
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)



if ErBot7:
    try:
        if len(sys.argv) in {1, 3, 4}:
            with contextlib.suppress(ConnectionError):
                ErBot7.run_until_disconnected()
        else:
            ErBot7.disconnect()    
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)



if ErBot8:
    try:
        if len(sys.argv) in {1, 3, 4}:
            with contextlib.suppress(ConnectionError):
                ErBot8.run_until_disconnected()
        else:
            ErBot8.disconnect()    
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)

if ErBot9:
    try:
        if len(sys.argv) in {1, 3, 4}:
            with contextlib.suppress(ConnectionError):
                ErBot9.run_until_disconnected()
        else:
            ErBot9.disconnect()    
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)

if ErBot10:
    try:
        if len(sys.argv) in {1, 3, 4}:
            with contextlib.suppress(ConnectionError):
                ErBot10.run_until_disconnected()
        else:
            ErBot10.disconnect()    
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)

if ErBot11:
    try:
        if len(sys.argv) in {1, 3, 4}:
            with contextlib.suppress(ConnectionError):
                ErBot11.run_until_disconnected()
        else:
            ErBot11.disconnect()    
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)
if ErBot12:
    try:
        if len(sys.argv) in {1, 3, 4}:
            with contextlib.suppress(ConnectionError):
                ErBot12.run_until_disconnected()
        else:
            ErBot12.disconnect()    
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)
if ErBot13:
    try:
        if len(sys.argv) in {1, 3, 4}:
            with contextlib.suppress(ConnectionError):
                ErBot13.run_until_disconnected()
        else:
            ErBot13.disconnect()    
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)

if ErBot14:
    try:
        if len(sys.argv) in {1, 3, 4}:
            with contextlib.suppress(ConnectionError):
                ErBot14.run_until_disconnected()
        else:
            ErBot14.disconnect()    
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)

if ErBot15:
    try:
        if len(sys.argv) in {1, 3, 4}:
            with contextlib.suppress(ConnectionError):
                ErBot15.run_until_disconnected()
        else:
            ErBot15.disconnect()    
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)

if ErBot16:
    try:
        if len(sys.argv) in {1, 3, 4}:
            with contextlib.suppress(ConnectionError):
                ErBot16.run_until_disconnected()
        else:
            ErBot16.disconnect()    
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)
if ErBot17:
    try:
        if len(sys.argv) in {1, 3, 4}:
            with contextlib.suppress(ConnectionError):
                ErBot17.run_until_disconnected()
        else:
            ErBot17.disconnect()    
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)
if ErBot18:
    try:
        if len(sys.argv) in {1, 3, 4}:
            with contextlib.suppress(ConnectionError):
                ErBot18.run_until_disconnected()
        else:
            ErBot18disconnect()    
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)

if ErBot19:
    try:
        if len(sys.argv) in {1, 3, 4}:
            with contextlib.suppress(ConnectionError):
                ErBot19.run_until_disconnected()
        else:
            ErBot19.disconnect()    
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)

if ErBot20:
    try:
        if len(sys.argv) in {1, 3, 4}:
            with contextlib.suppress(ConnectionError):
                ErBot21.run_until_disconnected()
        else:
            ErBot21.disconnect()    
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)

if ErBot21:
    try:
        if len(sys.argv) in {1, 3, 4}:
            with contextlib.suppress(ConnectionError):
                ErBot21.run_until_disconnected()
        else:
            ErBot21.disconnect()    
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)
if ErBot22:
    try:
        if len(sys.argv) in {1, 3, 4}:
            with contextlib.suppress(ConnectionError):
                ErBot22.run_until_disconnected()
        else:
            ErBot22.disconnect()    
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)
if ErBot23:
    try:
        if len(sys.argv) in {1, 3, 4}:
            with contextlib.suppress(ConnectionError):
                ErBot23.run_until_disconnected()
        else:
            ErBot23.disconnect()    
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)

if ErBot24:
    try:
        if len(sys.argv) in {1, 3, 4}:
            with contextlib.suppress(ConnectionError):
                ErBot24.run_until_disconnected()
        else:
            ErBot24.disconnect()    
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)

if ErBot25:
    try:
        if len(sys.argv) in {1, 3, 4}:
            with contextlib.suppress(ConnectionError):
                ErBot25.run_until_disconnected()
        else:
            ErBot25.disconnect()    
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)

if ErBot26:
    try:
        if len(sys.argv) in {1, 3, 4}:
            with contextlib.suppress(ConnectionError):
                ErBot26.run_until_disconnected()
        else:
            ErBot26.disconnect()    
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)
if ErBot27:
    try:
        if len(sys.argv) in {1, 3, 4}:
            with contextlib.suppress(ConnectionError):
                ErBot27.run_until_disconnected()
        else:
            ErBot27.disconnect()    
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)
if ErBot28:
    try:
        if len(sys.argv) in {1, 3, 4}:
            with contextlib.suppress(ConnectionError):
                ErBot28.run_until_disconnected()
        else:
            ErBot28.disconnect()    
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)

if ErBot29:
    try:
        if len(sys.argv) in {1, 3, 4}:
            with contextlib.suppress(ConnectionError):
                ErBot29.run_until_disconnected()
        else:
            ErBot29.disconnect()    
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)

if ErBot30:
    try:
        if len(sys.argv) in {1, 3, 4}:
            with contextlib.suppress(ConnectionError):
                ErBot30.run_until_disconnected()
        else:
            ErBot30.disconnect()    
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)

if ErBot31:
    try:
        if len(sys.argv) in {1, 3, 4}:
            with contextlib.suppress(ConnectionError):
                ErBot31.run_until_disconnected()
        else:
            ErBot31.disconnect()    
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)
if ErBot32:
    try:
        if len(sys.argv) in {1, 3, 4}:
            with contextlib.suppress(ConnectionError):
                ErBot32.run_until_disconnected()
        else:
            ErBot32.disconnect()    
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)
if ErBot33:
    try:
        if len(sys.argv) in {1, 3, 4}:
            with contextlib.suppress(ConnectionError):
                ErBot33.run_until_disconnected()
        else:
            ErBot33.disconnect()    
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)

if ErBot34:
    try:
        if len(sys.argv) in {1, 3, 4}:
            with contextlib.suppress(ConnectionError):
                ErBot34.run_until_disconnected()
        else:
            ErBot34.disconnect()    
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)

if ErBot36:
    try:
        if len(sys.argv) in {1, 3, 4}:
            with contextlib.suppress(ConnectionError):
                ErBot36.run_until_disconnected()
        else:
            ErBot36.disconnect()    
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)

if ErBot37:
    try:
        if len(sys.argv) in {1, 3, 4}:
            with contextlib.suppress(ConnectionError):
                ErBot37.run_until_disconnected()
        else:
            ErBot37.disconnect()    
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)
if ErBot38:
    try:
        if len(sys.argv) in {1, 3, 4}:
            with contextlib.suppress(ConnectionError):
                ErBot38.run_until_disconnected()
        else:
            ErBot38.disconnect()    
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)
if ErBot39:
    try:
        if len(sys.argv) in {1, 3, 4}:
            with contextlib.suppress(ConnectionError):
                ErBot39.run_until_disconnected()
        else:
            ErBot39.disconnect()    
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)

if ErBot40:
    try:
        if len(sys.argv) in {1, 3, 4}:
            with contextlib.suppress(ConnectionError):
                ErBot40.run_until_disconnected()
        else:
            ErBot40.disconnect()    
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)

if ErBot41:
    try:
        if len(sys.argv) in {1, 3, 4}:
            with contextlib.suppress(ConnectionError):
                ErBot41.run_until_disconnected()
        else:
            ErBot41.disconnect()    
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)
if ErBot42:
    try:
        if len(sys.argv) in {1, 3, 4}:
            with contextlib.suppress(ConnectionError):
                ErBot42.run_until_disconnected()
        else:
            ErBot42.disconnect()    
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)
if ErBot43:
    try:
        if len(sys.argv) in {1, 3, 4}:
            with contextlib.suppress(ConnectionError):
                ErBot43.run_until_disconnected()
        else:
            ErBot43.disconnect()    
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)
if ErBot44:
    try:
        if len(sys.argv) in {1, 3, 4}:
            with contextlib.suppress(ConnectionError):
                ErBot44.run_until_disconnected()
        else:
            ErBot44.disconnect()    
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)

if ErBot45:
    try:
        if len(sys.argv) in {1, 3, 4}:
            with contextlib.suppress(ConnectionError):
                ErBot45.run_until_disconnected()
        else:
            ErBot45.disconnect()    
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)

if ErBot46:
    try:
        if len(sys.argv) in {1, 3, 4}:
            with contextlib.suppress(ConnectionError):
                ErBot46.run_until_disconnected()
        else:
            ErBot46.disconnect()    
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)

if ErBot47:
    try:
        if len(sys.argv) in {1, 3, 4}:
            with contextlib.suppress(ConnectionError):
                ErBot47.run_until_disconnected()
        else:
            ErBot47.disconnect()    
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)

if ErBot48:
    try:
        if len(sys.argv) in {1, 3, 4}:
            with contextlib.suppress(ConnectionError):
                ErBot48.run_until_disconnected()
        else:
            ErBot48.disconnect()    
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)

if ErBot49:
    try:
        if len(sys.argv) in {1, 3, 4}:
            with contextlib.suppress(ConnectionError):
                ErBot49.run_until_disconnected()
        else:
            ErBot49.disconnect()    
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)
if ErBot35:
    try:
        if len(sys.argv) in {1, 3, 4}:
            with contextlib.suppress(ConnectionError):
                ErBot35.run_until_disconnected()
        else:
            ErBot35.disconnect()    
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)
        
if ErBot50:
    try:
        if len(sys.argv) in {1, 3, 4}:
            with contextlib.suppress(ConnectionError):
                ErBot50.run_until_disconnected()
        else:
            ErBot50.disconnect()    
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)
