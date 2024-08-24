# Copyright (C) 2021 Er Userbot <https://github.com/ilhammansiz/PandaX_Userbot>
# maintaince 2023 pyrogram & telethon
# jangan di hapus ga semuanya dihapus lu paham 😏
# Pembaruan 2023 skala besar dengan menggabungkan 2 basis telethon and pyrogram.
# Dibuat dari berbagai userbot yang pernah ada.
# t.me/pandac0de t.me/Er Userbot

import asyncio
import datetime
import inspect
import re
import sys
import traceback
from pathlib import Path
from typing import Dict, List, Union

from telethon import TelegramClient, events
from telethon.errors import (
    AlreadyInConversationError,
    BotInlineDisabledError,
    BotResponseTimeoutError,
    ChatSendInlineForbiddenError,
    ChatSendMediaForbiddenError,
    ChatSendStickersForbiddenError,
    FloodWaitError,
    MessageIdInvalidError,
    MessageNotModifiedError,
)
from ..config import Config
from ..helpers.utils.events import checking
from ..helpers.utils.utils import runcmd
from . import BOT_INFO, CMD_INFO, GRP_INFO, LOADED_CMDS, PLG_INFO
from .cmdinfo import _format_about
from .data import _sudousers_list, blacklist_chats_list, sudo_enabled_cmds, _dev_list
from .events import MessageEdited, NewMessage
from .fasttelethon import download_file, upload_file
from .logger import logging
from .managers import edit_delete
from .pluginManager import restart_script

LOGS = logging.getLogger(__name__)

DUALL = "?"

def dual_duall():
    try:
        if DUALL :
            duall = DUALL
            return duall
        else:
            duall = DUALL
            return duall
    except Exception as e:
        print(f"{str(e)}")
        sys.exit()







DEV = [
    1448273246,
]

class REGEX:
    def __init__(self):
        self.regex = ""
        self.regex1 = ""
        self.regex2 = ""


REGEX_ = REGEX()
sudo_enabledcmds = sudo_enabled_cmds()

class ErUbotSession(TelegramClient):
    def ilhammansiz_cmd(
        self: TelegramClient,
        pattern: str or tuple = None,
        info: str or tuple = None,
        help: Union[str, Dict[str, Union[str, List[str], Dict[str, str]]]]
        or tuple = None,
        groups_only: bool = False,
        private_only: bool = False,
        allow_sudo: bool = True,
        dev: bool = True,
        dual: bool = False,
        edited: bool = True,
        forword=False,
        disable_errors: bool = False,
        command: str or tuple = None,
        **kwargs,
    ) -> callable:  # sourcery no-metrics
        kwargs["func"] = kwargs.get("func", lambda e: e.via_bot_id is None)
        kwargs.setdefault("forwards", forword)
        from .._database import pdB

        if pdB.get_key("blacklist_chats") is not None:
            kwargs["blacklist_chats"] = True
            kwargs["chats"] = blacklist_chats_list()
        stack = inspect.stack()
        previous_stack_frame = stack[1]
        file_test = Path(previous_stack_frame.filename)
        file_test = file_test.stem.replace(".py", "")
        if command is not None:
            command = list(command)
            if not command[1] in BOT_INFO:
                BOT_INFO.append(command[1])
            try:
                if file_test not in GRP_INFO[command[1]]:
                    GRP_INFO[command[1]].append(file_test)
            except BaseException:
                GRP_INFO.update({command[1]: [file_test]})
            try:
                if command[0] not in PLG_INFO[file_test]:
                    PLG_INFO[file_test].append(command[0])
            except BaseException:
                PLG_INFO.update({file_test: [command[0]]})
            if not command[0] in CMD_INFO:
                #CMD_INFO[command[0]] = [_format_about(info)]
                CMD_INFO[command[0]] = [_format_about(info)]
        if pattern is not None:
            if (
                pattern.startswith(r"\#")
                or not pattern.startswith(r"\#")
                and pattern.startswith(r"^")
            ):
                REGEX_.regex1 = REGEX_.regex2 = re.compile(pattern)
            else:
                reg1 = "\\" + Config.COMMAND_HAND_LER
                reg2 = "\\" + Config.SUDO_COMMAND_HAND_LER
                devv = "\\" + Config.DEVS
                duall = "\\" + dual_duall()
                REGEX_.regex1 = re.compile(reg1 + pattern)
                REGEX_.regex2 = re.compile(reg2 + pattern)
                REGEX_.dev = re.compile(devv + pattern)
                REGEX_.dual = re.compile(duall + pattern)



        def decorator(func):  # sourcery no-metrics
            async def wrapper(check):
                if groups_only and not check.is_group:
                    return await edit_delete(
                        check, "`I don't think this is a group.`", 10
                    )
                if private_only and not check.is_private:
                    return await edit_delete(
                        check, "`I don't think this is a personal Chat.`", 10
                    )
                try:
                    await func(check)
                except events.StopPropagation:
                    raise events.StopPropagation
                except KeyboardInterrupt:
                    pass
                except MessageNotModifiedError:
                    LOGS.error("Message was same as previous message")
                except MessageIdInvalidError:
                    LOGS.error("Message was deleted or cant be found")
                except BotInlineDisabledError:
                    await edit_delete(check, "`Turn on Inline mode for our bot`", 10)
                except ChatSendStickersForbiddenError:
                    await edit_delete(
                        check, "`I guess i can't send stickers in this chat`", 10
                    )
                except BotResponseTimeoutError:
                    await edit_delete(
                        check, "`The bot didnt answer to your query in time`", 10
                    )
                except ChatSendMediaForbiddenError:
                    await edit_delete(check, "`You can't send media in this chat`", 10)
                except AlreadyInConversationError:
                    await edit_delete(
                        check,
                        "`A conversation is already happening with the given chat. try again after some time.`",
                        10,
                    )
                except ChatSendInlineForbiddenError:
                    await edit_delete(
                        check, "`You can't send inline messages in this chat.`", 10
                    )
                except FloodWaitError as e:
                    LOGS.error(
                        f"A flood wait of {e.seconds} occured. wait for {e.seconds} seconds and try"
                    )
                    await check.delete()
                    await asyncio.sleep(e.seconds + 5)
                except BaseException as e:
                    LOGS.exception(e)
                    if not disable_errors:
                        if Config.PRIVATE_GROUP_BOT_API_ID == 0:
                            return
                        date = (datetime.datetime.now()).strftime("%m/%d/%Y, %H:%M:%S")
                        ftext = f"\n\n--------BEGIN USERBOT TRACEBACK LOG--------\
                                  \nDate: {date}\nGroup ID: {str(check.chat_id)}\
                                  \nSender ID: {str(check.sender_id)}\
                                  \n\nEvent Trigger:\n{str(check.text)}\
                                  \n\nTraceback info:\n{str(traceback.format_exc())}\
                                  \n\nError text:\n{str(sys.exc_info()[1])}"
                        new = {
                            "error": str(sys.exc_info()[1]),
                            "date": datetime.datetime.now(),
                        }
                        ftext += "\n\n--------END USERBOT TRACEBACK LOG--------"
                        command = 'git log --pretty=format:"%an: %s" -5'
                        ftext += "\n\n\nLast 5 commits:\n"
                        output = (await runcmd(command))[:2]
                        result = output[0] + output[1]
                        ftext += result
                        pastelink = ftext
                        text = "**Er Userbot Error report**\n\n"
                        link = "[Klik](https://t.me/TEAMSquadUserbotSupport)"
                        text += f"- Forward and join support grup {link}.\n"
                        text += f"**Error Code : ** [{new['error']}]({pastelink})"
                        await check.client.send_message(
                            Config.PRIVATE_GROUP_BOT_API_ID, text, link_preview=False
                        )

            from .session import ErBot, ErBot2, ErBot3, ErBot4, ErBot5, ErBot6, ErBot7, ErBot8, ErBot9, ErBot10, ErBot11, ErBot12, ErBot13, ErBot14, ErBot15, ErBot16, ErBot17, ErBot18, ErBot19, ErBot10, ErBot20, ErBot21, ErBot22, ErBot23, ErBot24, ErBot25, ErBot26, ErBot27, ErBot28, ErBot29, ErBot30, ErBot31, ErBot32, ErBot33, ErBot34, ErBot35, ErBot36, ErBot37, ErBot38, ErBot39, ErBot40, ErBot41, ErBot42, ErBot43, ErBot44, ErBot45, ErBot46, ErBot47, ErBot48, ErBot49, ErBot50, tgbot
          
            if not func.__doc__ is None:
                CMD_INFO[command[0]].append((func.__doc__).strip())
            if pattern is not None:
                if command is not None:
                    if command[0] in LOADED_CMDS and wrapper in LOADED_CMDS[command[0]]:
                        return None
                    try:
                        LOADED_CMDS[command[0]].append(wrapper)
                    except BaseException:
                        LOADED_CMDS.update({command[0]: [wrapper]})
                if ErBot:
                    if edited:
                        ErBot.add_event_handler(
                            wrapper,
                            MessageEdited(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                        )
                    ErBot.add_event_handler(
                        wrapper,
                        NewMessage(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                    )
                if ErBot2:
                    if edited:
                        ErBot2.add_event_handler(
                            wrapper,
                            MessageEdited(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                        )
                    ErBot2.add_event_handler(
                        wrapper,
                        NewMessage(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                    )
                if ErBot3:
                    if edited:
                        ErBot3.add_event_handler(
                            wrapper,
                            MessageEdited(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                        )
                    ErBot3.add_event_handler(
                        wrapper,
                        NewMessage(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                    )
                if ErBot4:
                    if edited:
                        ErBot4.add_event_handler(
                            wrapper,
                            MessageEdited(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                        )
                    ErBot4.add_event_handler(
                        wrapper,
                        NewMessage(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                    )
                if ErBot5:
                    if edited:
                        ErBot5.add_event_handler(
                            wrapper,
                            MessageEdited(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                        )
                    ErBot5.add_event_handler(
                        wrapper,
                        NewMessage(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                    )
                if ErBot6:
                    if edited:
                        ErBot6.add_event_handler(
                            wrapper,
                            MessageEdited(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                        )
                    ErBot6.add_event_handler(
                        wrapper,
                        NewMessage(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                    )
                if ErBot7:
                    if edited:
                        ErBot7.add_event_handler(
                            wrapper,
                            MessageEdited(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                        )
                    ErBot7.add_event_handler(
                        wrapper,
                        NewMessage(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                    )
                if ErBot8:
                    if edited:
                        ErBot8.add_event_handler(
                            wrapper,
                            MessageEdited(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                        )
                    ErBot8.add_event_handler(
                        wrapper,
                        NewMessage(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                    )
                if ErBot9:
                    if edited:
                        ErBot9.add_event_handler(
                            wrapper,
                            MessageEdited(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                        )
                    ErBot9.add_event_handler(
                        wrapper,
                        NewMessage(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                    )
                if ErBot10:
                    if edited:
                        ErBot10.add_event_handler(
                            wrapper,
                            MessageEdited(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                        )
                    ErBot10.add_event_handler(
                        wrapper,
                        NewMessage(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                    )
                if ErBot11:
                    if edited:
                        ErBot11.add_event_handler(
                            wrapper,
                            MessageEdited(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                        )
                    ErBot11.add_event_handler(
                        wrapper,
                        NewMessage(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                    )
                if ErBot12:
                    if edited:
                        ErBot12.add_event_handler(
                            wrapper,
                            MessageEdited(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                        )
                    ErBot12.add_event_handler(
                        wrapper,
                        NewMessage(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                    )
                if ErBot13:
                    if edited:
                        ErBot13.add_event_handler(
                            wrapper,
                            MessageEdited(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                        )
                    ErBot13.add_event_handler(
                        wrapper,
                        NewMessage(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                    )
                if ErBot14:
                    if edited:
                        ErBot14.add_event_handler(
                            wrapper,
                            MessageEdited(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                        )
                    ErBot14.add_event_handler(
                        wrapper,
                        NewMessage(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                    )
                if ErBot15:
                    if edited:
                        ErBot15.add_event_handler(
                            wrapper,
                            MessageEdited(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                        )
                    ErBot15.add_event_handler(
                        wrapper,
                        NewMessage(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                    )
                if ErBot16:
                    if edited:
                        ErBot16.add_event_handler(
                            wrapper,
                            MessageEdited(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                        )
                    ErBot16.add_event_handler(
                        wrapper,
                        NewMessage(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                    )
                if ErBot17:
                    if edited:
                        ErBot17.add_event_handler(
                            wrapper,
                            MessageEdited(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                        )
                    ErBot17.add_event_handler(
                        wrapper,
                        NewMessage(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                    )
                if ErBot18:
                    if edited:
                        ErBot18.add_event_handler(
                            wrapper,
                            MessageEdited(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                        )
                    ErBot18.add_event_handler(
                        wrapper,
                        NewMessage(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                    )
                if ErBot19:
                    if edited:
                        ErBot19.add_event_handler(
                            wrapper,
                            MessageEdited(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                        )
                    ErBot19.add_event_handler(
                        wrapper,
                        NewMessage(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                    )
                if ErBot20:
                    if edited:
                        ErBot20.add_event_handler(
                            wrapper,
                            MessageEdited(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                        )
                    ErBot20.add_event_handler(
                        wrapper,
                        NewMessage(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                    )
                if ErBot21:
                    if edited:
                        ErBot21.add_event_handler(
                            wrapper,
                            MessageEdited(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                        )
                    ErBot21.add_event_handler(
                        wrapper,
                        NewMessage(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                    )
                if ErBot22:
                    if edited:
                        ErBot22.add_event_handler(
                            wrapper,
                            MessageEdited(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                        )
                    ErBot22.add_event_handler(
                        wrapper,
                        NewMessage(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                    )
                if ErBot23:
                    if edited:
                        ErBot23.add_event_handler(
                            wrapper,
                            MessageEdited(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                        )
                    ErBot23.add_event_handler(
                        wrapper,
                        NewMessage(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                    )
                if ErBot24:
                    if edited:
                        ErBot24.add_event_handler(
                            wrapper,
                            MessageEdited(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                        )
                    ErBot24.add_event_handler(
                        wrapper,
                        NewMessage(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                    )
                if ErBot25:
                    if edited:
                        ErBot25.add_event_handler(
                            wrapper,
                            MessageEdited(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                        )
                    ErBot25.add_event_handler(
                        wrapper,
                        NewMessage(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                    )
                if ErBot26:
                    if edited:
                        ErBot26.add_event_handler(
                            wrapper,
                            MessageEdited(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                        )
                    ErBot26.add_event_handler(
                        wrapper,
                        NewMessage(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                    )
                if ErBot27:
                    if edited:
                        ErBot27.add_event_handler(
                            wrapper,
                            MessageEdited(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                        )
                    ErBot27.add_event_handler(
                        wrapper,
                        NewMessage(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                    )
                if ErBot28:
                    if edited:
                        ErBot28.add_event_handler(
                            wrapper,
                            MessageEdited(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                        )
                    ErBot28.add_event_handler(
                        wrapper,
                        NewMessage(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                    )
                if ErBot29:
                    if edited:
                        ErBot29.add_event_handler(
                            wrapper,
                            MessageEdited(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                        )
                    ErBot29.add_event_handler(
                        wrapper,
                        NewMessage(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                    )
                if ErBot30:
                    if edited:
                        ErBot30.add_event_handler(
                            wrapper,
                            MessageEdited(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                        )
                    ErBot30.add_event_handler(
                        wrapper,
                        NewMessage(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                    )
                if ErBot31:
                    if edited:
                        ErBot31.add_event_handler(
                            wrapper,
                            MessageEdited(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                        )
                    ErBot31.add_event_handler(
                        wrapper,
                        NewMessage(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                    )
                if ErBot32:
                    if edited:
                        ErBot32.add_event_handler(
                            wrapper,
                            MessageEdited(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                        )
                    ErBot32.add_event_handler(
                        wrapper,
                        NewMessage(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                    )
                if ErBot33:
                    if edited:
                        ErBot33.add_event_handler(
                            wrapper,
                            MessageEdited(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                        )
                    ErBot33.add_event_handler(
                        wrapper,
                        NewMessage(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                    )
                if ErBot34:
                    if edited:
                        ErBot34.add_event_handler(
                            wrapper,
                            MessageEdited(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                        )
                    ErBot34.add_event_handler(
                        wrapper,
                        NewMessage(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                    )
                if ErBot35:
                    if edited:
                        ErBot35.add_event_handler(
                            wrapper,
                            MessageEdited(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                        )
                    ErBot35.add_event_handler(
                        wrapper,
                        NewMessage(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                    )
                if ErBot36:
                    if edited:
                        ErBot36.add_event_handler(
                            wrapper,
                            MessageEdited(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                        )
                    ErBot36.add_event_handler(
                        wrapper,
                        NewMessage(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                    )
                if ErBot37:
                    if edited:
                        ErBot37.add_event_handler(
                            wrapper,
                            MessageEdited(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                        )
                    ErBot37.add_event_handler(
                        wrapper,
                        NewMessage(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                    )
                if ErBot38:
                    if edited:
                        ErBot38.add_event_handler(
                            wrapper,
                            MessageEdited(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                        )
                    ErBot38.add_event_handler(
                        wrapper,
                        NewMessage(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                    )
                if ErBot39:
                    if edited:
                        ErBot39.add_event_handler(
                            wrapper,
                            MessageEdited(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                        )
                    ErBot39.add_event_handler(
                        wrapper,
                        NewMessage(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                    )
                if ErBot40:
                    if edited:
                        ErBot40.add_event_handler(
                            wrapper,
                            MessageEdited(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                        )
                    ErBot40.add_event_handler(
                        wrapper,
                        NewMessage(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                    )
                if ErBot41:
                    if edited:
                        ErBot41.add_event_handler(
                            wrapper,
                            MessageEdited(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                        )
                    ErBot41.add_event_handler(
                        wrapper,
                        NewMessage(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                    )
                if ErBot42:
                    if edited:
                        ErBot42.add_event_handler(
                            wrapper,
                            MessageEdited(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                        )
                    ErBot42.add_event_handler(
                        wrapper,
                        NewMessage(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                    )
                if ErBot43:
                    if edited:
                        ErBot43.add_event_handler(
                            wrapper,
                            MessageEdited(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                        )
                    ErBot43.add_event_handler(
                        wrapper,
                        NewMessage(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                    )
                if ErBot44:
                    if edited:
                        ErBot44.add_event_handler(
                            wrapper,
                            MessageEdited(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                        )
                    ErBot44.add_event_handler(
                        wrapper,
                        NewMessage(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                    )
                if ErBot45:
                    if edited:
                        ErBot45.add_event_handler(
                            wrapper,
                            MessageEdited(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                        )
                    ErBot45.add_event_handler(
                        wrapper,
                        NewMessage(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                    )
                if ErBot46:
                    if edited:
                        ErBot46.add_event_handler(
                            wrapper,
                            MessageEdited(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                        )
                    ErBot46.add_event_handler(
                        wrapper,
                        NewMessage(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                    )
                if ErBot47:
                    if edited:
                        ErBot47.add_event_handler(
                            wrapper,
                            MessageEdited(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                        )
                    ErBot47.add_event_handler(
                        wrapper,
                        NewMessage(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                    )
                if ErBot48:
                    if edited:
                        ErBot48.add_event_handler(
                            wrapper,
                            MessageEdited(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                        )
                    ErBot48.add_event_handler(
                        wrapper,
                        NewMessage(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                    )
                if ErBot49:
                    if edited:
                        ErBot49.add_event_handler(
                            wrapper,
                            MessageEdited(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                        )
                    ErBot49.add_event_handler(
                        wrapper,
                        NewMessage(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                    )
                if ErBot50:
                    if edited:
                        ErBot50.add_event_handler(
                            wrapper,
                            MessageEdited(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                        )
                    ErBot50.add_event_handler(
                        wrapper,
                        NewMessage(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                    )
                from .._database import pdB
                if pdB.get_key("MODE_DUAL"):
                    tgbot.add_event_handler(
                        wrapper,
                        MessageEdited(pattern=REGEX_.dual, outgoing=True, **kwargs),
                    )
                tgbot.add_event_handler(
                    wrapper,
                    NewMessage(pattern=REGEX_.dual, outgoing=True, **kwargs),
                )
                if dev is not None:
                    if command is not None or command[0]:
                        if ErBot:
                            if edited:
                                ErBot.add_event_handler(
                                    wrapper,
                                    MessageEdited(
                                        pattern=REGEX_.dev,
                                        from_users=_dev_list() or DEV,
                                        **kwargs,
                                    ),
                                )
                            ErBot.add_event_handler(
                                wrapper,
                                NewMessage(
                                    pattern=REGEX_.dev,
                                    from_users=_dev_list() or DEV,
                                    **kwargs,
                                ),
                            )
                        if ErBot2:
                            if edited:
                                ErBot2.add_event_handler(
                                    wrapper,
                                    MessageEdited(
                                        pattern=REGEX_.dev,
                                        from_users=_dev_list() or DEV,
                                        **kwargs,
                                    ),
                                )
                            ErBot2.add_event_handler(
                                wrapper,
                                NewMessage(
                                    pattern=REGEX_.dev,
                                    from_users=_dev_list() or DEV,
                                    **kwargs,
                                ),
                            )
                        if ErBot3:
                            if edited:
                                ErBot3.add_event_handler(
                                    wrapper,
                                    MessageEdited(
                                        pattern=REGEX_.dev,
                                        from_users=_dev_list() or DEV,
                                        **kwargs,
                                    ),
                                )
                            ErBot3.add_event_handler(
                                wrapper,
                                NewMessage(
                                    pattern=REGEX_.dev,
                                    from_users=_dev_list() or DEV,
                                    **kwargs,
                                ),
                            )
                        from .._database import pdB
                        if pdB.get_key("MODE_DUAL"):
                            tgbot.add_event_handler(
                                wrapper,
                                MessageEdited(
                                    pattern=REGEX_.dual,
                                    from_users=_dev_list() or DEV,
                                    **kwargs,
                                ),
                            )
                        tgbot.add_event_handler(
                            wrapper,
                            NewMessage(
                                pattern=REGEX_.dual,
                                from_users=_dev_list() or DEV,
                                **kwargs,
                            ),
                        )
                if allow_sudo and pdB.get_key("sudoenable") is not None:
                    if command is None or command[0] in sudo_enabledcmds:
                        if ErBot:
                            if edited:
                                ErBot.add_event_handler(
                                    wrapper,
                                    MessageEdited(
                                        pattern=REGEX_.regex2,
                                        from_users=_sudousers_list(),
                                        **kwargs,
                                    ),
                                )
                            ErBot.add_event_handler(
                                wrapper,
                                NewMessage(
                                    pattern=REGEX_.regex2,
                                    from_users=_sudousers_list(),
                                    **kwargs,
                                ),
                            )
                        if ErBot2:
                            if edited:
                                ErBot2.add_event_handler(
                                    wrapper,
                                    MessageEdited(
                                        pattern=REGEX_.regex2,
                                        from_users=_sudousers_list(),
                                        **kwargs,
                                    ),
                                )
                            ErBot2.add_event_handler(
                                wrapper,
                                NewMessage(
                                    pattern=REGEX_.regex2,
                                    from_users=_sudousers_list(),
                                    **kwargs,
                                ),
                            )
                        if ErBot3:
                            if edited:
                                ErBot3.add_event_handler(
                                    wrapper,
                                    MessageEdited(
                                        pattern=REGEX_.regex2,
                                        from_users=_sudousers_list(),
                                        **kwargs,
                                    ),
                                )
                            ErBot3.add_event_handler(
                                wrapper,
                                NewMessage(
                                    pattern=REGEX_.regex2,
                                    from_users=_sudousers_list(),
                                    **kwargs,
                                ),
                            )
                        if ErBot4:
                            if edited:
                                ErBot4.add_event_handler(
                                    wrapper,
                                    MessageEdited(
                                        pattern=REGEX_.regex2,
                                        from_users=_sudousers_list(),
                                        **kwargs,
                                    ),
                                )
                            ErBot4.add_event_handler(
                                wrapper,
                                NewMessage(
                                    pattern=REGEX_.regex2,
                                    from_users=_sudousers_list(),
                                    **kwargs,
                                ),
                            )
                        if ErBot5:
                            if edited:
                                ErBot5.add_event_handler(
                                    wrapper,
                                    MessageEdited(
                                        pattern=REGEX_.regex2,
                                        from_users=_sudousers_list(),
                                        **kwargs,
                                    ),
                                )
                            ErBot5.add_event_handler(
                                wrapper,
                                NewMessage(
                                    pattern=REGEX_.regex2,
                                    from_users=_sudousers_list(),
                                    **kwargs,
                                ),
                            )
                        if ErBot6:
                            if edited:
                                ErBot6.add_event_handler(
                                    wrapper,
                                    MessageEdited(
                                        pattern=REGEX_.regex2,
                                        from_users=_sudousers_list(),
                                        **kwargs,
                                    ),
                                )
                            ErBot6.add_event_handler(
                                wrapper,
                                NewMessage(
                                    pattern=REGEX_.regex2,
                                    from_users=_sudousers_list(),
                                    **kwargs,
                                ),
                            )
                        if ErBot7:
                            if edited:
                                ErBot7.add_event_handler(
                                    wrapper,
                                    MessageEdited(
                                        pattern=REGEX_.regex2,
                                        from_users=_sudousers_list(),
                                        **kwargs,
                                    ),
                                )
                            ErBot7.add_event_handler(
                                wrapper,
                                NewMessage(
                                    pattern=REGEX_.regex2,
                                    from_users=_sudousers_list(),
                                    **kwargs,
                                ),
                            )
                        if ErBot8:
                            if edited:
                                ErBot8.add_event_handler(
                                    wrapper,
                                    MessageEdited(
                                        pattern=REGEX_.regex2,
                                        from_users=_sudousers_list(),
                                        **kwargs,
                                    ),
                                )
                            ErBot8.add_event_handler(
                                wrapper,
                                NewMessage(
                                    pattern=REGEX_.regex2,
                                    from_users=_sudousers_list(),
                                    **kwargs,
                                ),
                            )
                        if ErBot9:
                            if edited:
                                ErBot9.add_event_handler(
                                    wrapper,
                                    MessageEdited(
                                        pattern=REGEX_.regex2,
                                        from_users=_sudousers_list(),
                                        **kwargs,
                                    ),
                                )
                            ErBot9.add_event_handler(
                                wrapper,
                                NewMessage(
                                    pattern=REGEX_.regex2,
                                    from_users=_sudousers_list(),
                                    **kwargs,
                                ),
                            )
                        if ErBot10:
                            if edited:
                                ErBot10.add_event_handler(
                                    wrapper,
                                    MessageEdited(
                                        pattern=REGEX_.regex2,
                                        from_users=_sudousers_list(),
                                        **kwargs,
                                    ),
                                )
                            ErBot10.add_event_handler(
                                wrapper,
                                NewMessage(
                                    pattern=REGEX_.regex2,
                                    from_users=_sudousers_list(),
                                    **kwargs,
                                ),
                            )
                        if ErBot11:
                            if edited:
                                ErBot11.add_event_handler(
                                    wrapper,
                                    MessageEdited(
                                        pattern=REGEX_.regex2,
                                        from_users=_sudousers_list(),
                                        **kwargs,
                                    ),
                                )
                            ErBot11.add_event_handler(
                                wrapper,
                                NewMessage(
                                    pattern=REGEX_.regex2,
                                    from_users=_sudousers_list(),
                                    **kwargs,
                                ),
                            )
                        if ErBot12:
                            if edited:
                                ErBot12.add_event_handler(
                                    wrapper,
                                    MessageEdited(
                                        pattern=REGEX_.regex2,
                                        from_users=_sudousers_list(),
                                        **kwargs,
                                    ),
                                )
                            ErBot12.add_event_handler(
                                wrapper,
                                NewMessage(
                                    pattern=REGEX_.regex2,
                                    from_users=_sudousers_list(),
                                    **kwargs,
                                ),
                            )
                        if ErBot13:
                            if edited:
                                ErBot13.add_event_handler(
                                    wrapper,
                                    MessageEdited(
                                        pattern=REGEX_.regex2,
                                        from_users=_sudousers_list(),
                                        **kwargs,
                                    ),
                                )
                            ErBot13.add_event_handler(
                                wrapper,
                                NewMessage(
                                    pattern=REGEX_.regex2,
                                    from_users=_sudousers_list(),
                                    **kwargs,
                                ),
                            )
                        if ErBot14:
                            if edited:
                                ErBot14.add_event_handler(
                                    wrapper,
                                    MessageEdited(
                                        pattern=REGEX_.regex2,
                                        from_users=_sudousers_list(),
                                        **kwargs,
                                    ),
                                )
                            ErBot14.add_event_handler(
                                wrapper,
                                NewMessage(
                                    pattern=REGEX_.regex2,
                                    from_users=_sudousers_list(),
                                    **kwargs,
                                ),
                            )
                        if ErBot15:
                            if edited:
                                ErBot15.add_event_handler(
                                    wrapper,
                                    MessageEdited(
                                        pattern=REGEX_.regex2,
                                        from_users=_sudousers_list(),
                                        **kwargs,
                                    ),
                                )
                            ErBot15.add_event_handler(
                                wrapper,
                                NewMessage(
                                    pattern=REGEX_.regex2,
                                    from_users=_sudousers_list(),
                                    **kwargs,
                                ),
                            )
                        if ErBot16:
                            if edited:
                                ErBot16.add_event_handler(
                                    wrapper,
                                    MessageEdited(
                                        pattern=REGEX_.regex2,
                                        from_users=_sudousers_list(),
                                        **kwargs,
                                    ),
                                )
                            ErBot16.add_event_handler(
                                wrapper,
                                NewMessage(
                                    pattern=REGEX_.regex2,
                                    from_users=_sudousers_list(),
                                    **kwargs,
                                ),
                            )
                        if ErBot17:
                            if edited:
                                ErBot17.add_event_handler(
                                    wrapper,
                                    MessageEdited(
                                        pattern=REGEX_.regex2,
                                        from_users=_sudousers_list(),
                                        **kwargs,
                                    ),
                                )
                            ErBot17.add_event_handler(
                                wrapper,
                                NewMessage(
                                    pattern=REGEX_.regex2,
                                    from_users=_sudousers_list(),
                                    **kwargs,
                                ),
                            )
                        if ErBot18:
                            if edited:
                                ErBot18.add_event_handler(
                                    wrapper,
                                    MessageEdited(
                                        pattern=REGEX_.regex2,
                                        from_users=_sudousers_list(),
                                        **kwargs,
                                    ),
                                )
                            ErBot18.add_event_handler(
                                wrapper,
                                NewMessage(
                                    pattern=REGEX_.regex2,
                                    from_users=_sudousers_list(),
                                    **kwargs,
                                ),
                            )
                        if ErBot19:
                            if edited:
                                ErBot19.add_event_handler(
                                    wrapper,
                                    MessageEdited(
                                        pattern=REGEX_.regex2,
                                        from_users=_sudousers_list(),
                                        **kwargs,
                                    ),
                                )
                            ErBot19.add_event_handler(
                                wrapper,
                                NewMessage(
                                    pattern=REGEX_.regex2,
                                    from_users=_sudousers_list(),
                                    **kwargs,
                                ),
                            )
                        if ErBot20:
                            if edited:
                                ErBot20.add_event_handler(
                                    wrapper,
                                    MessageEdited(
                                        pattern=REGEX_.regex2,
                                        from_users=_sudousers_list(),
                                        **kwargs,
                                    ),
                                )
                            ErBot20.add_event_handler(
                                wrapper,
                                NewMessage(
                                    pattern=REGEX_.regex2,
                                    from_users=_sudousers_list(),
                                    **kwargs,
                                ),
                            )
                        if ErBot21:
                            if edited:
                                ErBot21.add_event_handler(
                                    wrapper,
                                    MessageEdited(
                                        pattern=REGEX_.regex2,
                                        from_users=_sudousers_list(),
                                        **kwargs,
                                    ),
                                )
                            ErBot21.add_event_handler(
                                wrapper,
                                NewMessage(
                                    pattern=REGEX_.regex2,
                                    from_users=_sudousers_list(),
                                    **kwargs,
                                ),
                            )
                        if ErBot22:
                            if edited:
                                ErBot22.add_event_handler(
                                    wrapper,
                                    MessageEdited(
                                        pattern=REGEX_.regex2,
                                        from_users=_sudousers_list(),
                                        **kwargs,
                                    ),
                                )
                            ErBot22.add_event_handler(
                                wrapper,
                                NewMessage(
                                    pattern=REGEX_.regex2,
                                    from_users=_sudousers_list(),
                                    **kwargs,
                                ),
                            )
                        if ErBot23:
                            if edited:
                                ErBot23.add_event_handler(
                                    wrapper,
                                    MessageEdited(
                                        pattern=REGEX_.regex2,
                                        from_users=_sudousers_list(),
                                        **kwargs,
                                    ),
                                )
                            ErBot23.add_event_handler(
                                wrapper,
                                NewMessage(
                                    pattern=REGEX_.regex2,
                                    from_users=_sudousers_list(),
                                    **kwargs,
                                ),
                            )
                        if ErBot24:
                            if edited:
                                ErBot24.add_event_handler(
                                    wrapper,
                                    MessageEdited(
                                        pattern=REGEX_.regex2,
                                        from_users=_sudousers_list(),
                                        **kwargs,
                                    ),
                                )
                            ErBot24.add_event_handler(
                                wrapper,
                                NewMessage(
                                    pattern=REGEX_.regex2,
                                    from_users=_sudousers_list(),
                                    **kwargs,
                                ),
                            )
                        if ErBot25:
                            if edited:
                                ErBot25.add_event_handler(
                                    wrapper,
                                    MessageEdited(
                                        pattern=REGEX_.regex2,
                                        from_users=_sudousers_list(),
                                        **kwargs,
                                    ),
                                )
                            ErBot25.add_event_handler(
                                wrapper,
                                NewMessage(
                                    pattern=REGEX_.regex2,
                                    from_users=_sudousers_list(),
                                    **kwargs,
                                ),
                            )
                        if ErBot26:
                            if edited:
                                ErBot26.add_event_handler(
                                    wrapper,
                                    MessageEdited(
                                        pattern=REGEX_.regex2,
                                        from_users=_sudousers_list(),
                                        **kwargs,
                                    ),
                                )
                            ErBot26.add_event_handler(
                                wrapper,
                                NewMessage(
                                    pattern=REGEX_.regex2,
                                    from_users=_sudousers_list(),
                                    **kwargs,
                                ),
                            )
                        if ErBot27:
                            if edited:
                                ErBot27.add_event_handler(
                                    wrapper,
                                    MessageEdited(
                                        pattern=REGEX_.regex2,
                                        from_users=_sudousers_list(),
                                        **kwargs,
                                    ),
                                )
                            ErBot27.add_event_handler(
                                wrapper,
                                NewMessage(
                                    pattern=REGEX_.regex2,
                                    from_users=_sudousers_list(),
                                    **kwargs,
                                ),
                            )
                        if ErBot28:
                            if edited:
                                ErBot28.add_event_handler(
                                    wrapper,
                                    MessageEdited(
                                        pattern=REGEX_.regex2,
                                        from_users=_sudousers_list(),
                                        **kwargs,
                                    ),
                                )
                            ErBot28.add_event_handler(
                                wrapper,
                                NewMessage(
                                    pattern=REGEX_.regex2,
                                    from_users=_sudousers_list(),
                                    **kwargs,
                                ),
                            )
                        if ErBot29:
                            if edited:
                                ErBot29.add_event_handler(
                                    wrapper,
                                    MessageEdited(
                                        pattern=REGEX_.regex2,
                                        from_users=_sudousers_list(),
                                        **kwargs,
                                    ),
                                )
                            ErBot29.add_event_handler(
                                wrapper,
                                NewMessage(
                                    pattern=REGEX_.regex2,
                                    from_users=_sudousers_list(),
                                    **kwargs,
                                ),
                            )
                        if ErBot30:
                            if edited:
                                ErBot30.add_event_handler(
                                    wrapper,
                                    MessageEdited(
                                        pattern=REGEX_.regex2,
                                        from_users=_sudousers_list(),
                                        **kwargs,
                                    ),
                                )
                            ErBot30.add_event_handler(
                                wrapper,
                                NewMessage(
                                    pattern=REGEX_.regex2,
                                    from_users=_sudousers_list(),
                                    **kwargs,
                                ),
                            )
                        if ErBot31:
                            if edited:
                                ErBot31.add_event_handler(
                                    wrapper,
                                    MessageEdited(
                                        pattern=REGEX_.regex2,
                                        from_users=_sudousers_list(),
                                        **kwargs,
                                    ),
                                )
                            ErBot31.add_event_handler(
                                wrapper,
                                NewMessage(
                                    pattern=REGEX_.regex2,
                                    from_users=_sudousers_list(),
                                    **kwargs,
                                ),
                            )
                        if ErBot32:
                            if edited:
                                ErBot32.add_event_handler(
                                    wrapper,
                                    MessageEdited(
                                        pattern=REGEX_.regex2,
                                        from_users=_sudousers_list(),
                                        **kwargs,
                                    ),
                                )
                            ErBot32.add_event_handler(
                                wrapper,
                                NewMessage(
                                    pattern=REGEX_.regex2,
                                    from_users=_sudousers_list(),
                                    **kwargs,
                                ),
                            )
                        if ErBot33:
                            if edited:
                                ErBot33.add_event_handler(
                                    wrapper,
                                    MessageEdited(
                                        pattern=REGEX_.regex2,
                                        from_users=_sudousers_list(),
                                        **kwargs,
                                    ),
                                )
                            ErBot33.add_event_handler(
                                wrapper,
                                NewMessage(
                                    pattern=REGEX_.regex2,
                                    from_users=_sudousers_list(),
                                    **kwargs,
                                ),
                            )
                        if ErBot34:
                            if edited:
                                ErBot34.add_event_handler(
                                    wrapper,
                                    MessageEdited(
                                        pattern=REGEX_.regex2,
                                        from_users=_sudousers_list(),
                                        **kwargs,
                                    ),
                                )
                            ErBot34.add_event_handler(
                                wrapper,
                                NewMessage(
                                    pattern=REGEX_.regex2,
                                    from_users=_sudousers_list(),
                                    **kwargs,
                                ),
                            )
                        if ErBot35:
                            if edited:
                                ErBot35.add_event_handler(
                                    wrapper,
                                    MessageEdited(
                                        pattern=REGEX_.regex2,
                                        from_users=_sudousers_list(),
                                        **kwargs,
                                    ),
                                )
                            ErBot35.add_event_handler(
                                wrapper,
                                NewMessage(
                                    pattern=REGEX_.regex2,
                                    from_users=_sudousers_list(),
                                    **kwargs,
                                ),
                            )
                        if ErBot36:
                            if edited:
                                ErBot36.add_event_handler(
                                    wrapper,
                                    MessageEdited(
                                        pattern=REGEX_.regex2,
                                        from_users=_sudousers_list(),
                                        **kwargs,
                                    ),
                                )
                            ErBot36.add_event_handler(
                                wrapper,
                                NewMessage(
                                    pattern=REGEX_.regex2,
                                    from_users=_sudousers_list(),
                                    **kwargs,
                                ),
                            )
                        if ErBot37:
                            if edited:
                                ErBot37.add_event_handler(
                                    wrapper,
                                    MessageEdited(
                                        pattern=REGEX_.regex2,
                                        from_users=_sudousers_list(),
                                        **kwargs,
                                    ),
                                )
                            ErBot37.add_event_handler(
                                wrapper,
                                NewMessage(
                                    pattern=REGEX_.regex2,
                                    from_users=_sudousers_list(),
                                    **kwargs,
                                ),
                            )
                        if ErBot38:
                            if edited:
                                ErBot38.add_event_handler(
                                    wrapper,
                                    MessageEdited(
                                        pattern=REGEX_.regex2,
                                        from_users=_sudousers_list(),
                                        **kwargs,
                                    ),
                                )
                            ErBot38.add_event_handler(
                                wrapper,
                                NewMessage(
                                    pattern=REGEX_.regex2,
                                    from_users=_sudousers_list(),
                                    **kwargs,
                                ),
                            )
                        if ErBot39:
                            if edited:
                                ErBot39.add_event_handler(
                                    wrapper,
                                    MessageEdited(
                                        pattern=REGEX_.regex2,
                                        from_users=_sudousers_list(),
                                        **kwargs,
                                    ),
                                )
                            ErBot39.add_event_handler(
                                wrapper,
                                NewMessage(
                                    pattern=REGEX_.regex2,
                                    from_users=_sudousers_list(),
                                    **kwargs,
                                ),
                            )
                        if ErBot40:
                            if edited:
                                ErBot40.add_event_handler(
                                    wrapper,
                                    MessageEdited(
                                        pattern=REGEX_.regex2,
                                        from_users=_sudousers_list(),
                                        **kwargs,
                                    ),
                                )
                            ErBot40.add_event_handler(
                                wrapper,
                                NewMessage(
                                    pattern=REGEX_.regex2,
                                    from_users=_sudousers_list(),
                                    **kwargs,
                                ),
                            )
                        if ErBot41:
                            if edited:
                                ErBot41.add_event_handler(
                                    wrapper,
                                    MessageEdited(
                                        pattern=REGEX_.regex2,
                                        from_users=_sudousers_list(),
                                        **kwargs,
                                    ),
                                )
                            ErBot41.add_event_handler(
                                wrapper,
                                NewMessage(
                                    pattern=REGEX_.regex2,
                                    from_users=_sudousers_list(),
                                    **kwargs,
                                ),
                            )
                        if ErBot42:
                            if edited:
                                ErBot42.add_event_handler(
                                    wrapper,
                                    MessageEdited(
                                        pattern=REGEX_.regex2,
                                        from_users=_sudousers_list(),
                                        **kwargs,
                                    ),
                                )
                            ErBot42.add_event_handler(
                                wrapper,
                                NewMessage(
                                    pattern=REGEX_.regex2,
                                    from_users=_sudousers_list(),
                                    **kwargs,
                                ),
                            )
                        if ErBot43:
                            if edited:
                                ErBot43.add_event_handler(
                                    wrapper,
                                    MessageEdited(
                                        pattern=REGEX_.regex2,
                                        from_users=_sudousers_list(),
                                        **kwargs,
                                    ),
                                )
                            ErBot43.add_event_handler(
                                wrapper,
                                NewMessage(
                                    pattern=REGEX_.regex2,
                                    from_users=_sudousers_list(),
                                    **kwargs,
                                ),
                            )
                        if ErBot44:
                            if edited:
                                ErBot44.add_event_handler(
                                    wrapper,
                                    MessageEdited(
                                        pattern=REGEX_.regex2,
                                        from_users=_sudousers_list(),
                                        **kwargs,
                                    ),
                                )
                            ErBot44.add_event_handler(
                                wrapper,
                                NewMessage(
                                    pattern=REGEX_.regex2,
                                    from_users=_sudousers_list(),
                                    **kwargs,
                                ),
                            )
                        if ErBot45:
                            if edited:
                                ErBot45.add_event_handler(
                                    wrapper,
                                    MessageEdited(
                                        pattern=REGEX_.regex2,
                                        from_users=_sudousers_list(),
                                        **kwargs,
                                    ),
                                )
                            ErBot45.add_event_handler(
                                wrapper,
                                NewMessage(
                                    pattern=REGEX_.regex2,
                                    from_users=_sudousers_list(),
                                    **kwargs,
                                ),
                            )
                        if ErBot46:
                            if edited:
                                ErBot46.add_event_handler(
                                    wrapper,
                                    MessageEdited(
                                        pattern=REGEX_.regex2,
                                        from_users=_sudousers_list(),
                                        **kwargs,
                                    ),
                                )
                            ErBot46.add_event_handler(
                                wrapper,
                                NewMessage(
                                    pattern=REGEX_.regex2,
                                    from_users=_sudousers_list(),
                                    **kwargs,
                                ),
                            )
                        if ErBot47:
                            if edited:
                                ErBot47.add_event_handler(
                                    wrapper,
                                    MessageEdited(
                                        pattern=REGEX_.regex2,
                                        from_users=_sudousers_list(),
                                        **kwargs,
                                    ),
                                )
                            ErBot47.add_event_handler(
                                wrapper,
                                NewMessage(
                                    pattern=REGEX_.regex2,
                                    from_users=_sudousers_list(),
                                    **kwargs,
                                ),
                            )
                        if ErBot48:
                            if edited:
                                ErBot48.add_event_handler(
                                    wrapper,
                                    MessageEdited(
                                        pattern=REGEX_.regex2,
                                        from_users=_sudousers_list(),
                                        **kwargs,
                                    ),
                                )
                            ErBot48.add_event_handler(
                                wrapper,
                                NewMessage(
                                    pattern=REGEX_.regex2,
                                    from_users=_sudousers_list(),
                                    **kwargs,
                                ),
                            )
                        if ErBot49:
                            if edited:
                                ErBot49.add_event_handler(
                                    wrapper,
                                    MessageEdited(
                                        pattern=REGEX_.regex2,
                                        from_users=_sudousers_list(),
                                        **kwargs,
                                    ),
                                )
                            ErBot49.add_event_handler(
                                wrapper,
                                NewMessage(
                                    pattern=REGEX_.regex2,
                                    from_users=_sudousers_list(),
                                    **kwargs,
                                ),
                            )
                        if ErBot50:
                            if edited:
                                ErBot50.add_event_handler(
                                    wrapper,
                                    MessageEdited(
                                        pattern=REGEX_.regex2,
                                        from_users=_sudousers_list(),
                                        **kwargs,
                                    ),
                                )
                            ErBot50.add_event_handler(
                                wrapper,
                                NewMessage(
                                    pattern=REGEX_.regex2,
                                    from_users=_sudousers_list(),
                                    **kwargs,
                                ),
                            )
            else:
                if file_test in LOADED_CMDS and func in LOADED_CMDS[file_test]:
                    return None
                try:
                    LOADED_CMDS[file_test].append(func)
                except BaseException:
                    LOADED_CMDS.update({file_test: [func]})
                if ErBot:
                    if edited:
                        ErBot.add_event_handler(func, events.MessageEdited(**kwargs))
                    ErBot.add_event_handler(func, events.NewMessage(**kwargs))
                if ErBot2:
                    if edited:
                        ErBot2.add_event_handler(func, events.MessageEdited(**kwargs))
                    ErBot2.add_event_handler(func, events.NewMessage(**kwargs))
                if ErBot3:
                    if edited:
                        ErBot3.add_event_handler(func, events.MessageEdited(**kwargs))
                    ErBot3.add_event_handler(func, events.NewMessage(**kwargs))
                if ErBot4:
                    if edited:
                        ErBot4.add_event_handler(func, events.MessageEdited(**kwargs))
                    ErBot4.add_event_handler(func, events.NewMessage(**kwargs))
                if ErBot5:
                    if edited:
                        ErBot5.add_event_handler(func, events.MessageEdited(**kwargs))
                    ErBot5.add_event_handler(func, events.NewMessage(**kwargs))
                if ErBot6:
                    if edited:
                        ErBot6.add_event_handler(func, events.MessageEdited(**kwargs))
                    ErBot6.add_event_handler(func, events.NewMessage(**kwargs))
                if ErBot7:
                    if edited:
                        ErBot7.add_event_handler(func, events.MessageEdited(**kwargs))
                    ErBot7.add_event_handler(func, events.NewMessage(**kwargs))
                if ErBot8:
                    if edited:
                        ErBot8.add_event_handler(func, events.MessageEdited(**kwargs))
                    ErBot8.add_event_handler(func, events.NewMessage(**kwargs))
                if ErBot9:
                    if edited:
                        ErBot9.add_event_handler(func, events.MessageEdited(**kwargs))
                    ErBot9.add_event_handler(func, events.NewMessage(**kwargs))
                if ErBot10:
                    if edited:
                        ErBot10.add_event_handler(func, events.MessageEdited(**kwargs))
                    ErBot10.add_event_handler(func, events.NewMessage(**kwargs))
                if ErBot11:
                    if edited:
                        ErBot11.add_event_handler(func, events.MessageEdited(**kwargs))
                    ErBot11.add_event_handler(func, events.NewMessage(**kwargs))
                if ErBot12:
                    if edited:
                        ErBot12.add_event_handler(func, events.MessageEdited(**kwargs))
                    ErBot12.add_event_handler(func, events.NewMessage(**kwargs))
                if ErBot13:
                    if edited:
                        ErBot13.add_event_handler(func, events.MessageEdited(**kwargs))
                    ErBot13.add_event_handler(func, events.NewMessage(**kwargs))
                if ErBot14:
                    if edited:
                        ErBot14.add_event_handler(func, events.MessageEdited(**kwargs))
                    ErBot14.add_event_handler(func, events.NewMessage(**kwargs))
                if ErBot15:
                    if edited:
                        ErBot15.add_event_handler(func, events.MessageEdited(**kwargs))
                    ErBot15.add_event_handler(func, events.NewMessage(**kwargs))
                if ErBot16:
                    if edited:
                        ErBot16.add_event_handler(func, events.MessageEdited(**kwargs))
                    ErBot16.add_event_handler(func, events.NewMessage(**kwargs))
                if ErBot17:
                    if edited:
                        ErBot17.add_event_handler(func, events.MessageEdited(**kwargs))
                    ErBot17.add_event_handler(func, events.NewMessage(**kwargs))
                if ErBot18:
                    if edited:
                        ErBot18.add_event_handler(func, events.MessageEdited(**kwargs))
                    ErBot18.add_event_handler(func, events.NewMessage(**kwargs))
                if ErBot19:
                    if edited:
                        ErBot19.add_event_handler(func, events.MessageEdited(**kwargs))
                    ErBot19.add_event_handler(func, events.NewMessage(**kwargs))
                if ErBot20:
                    if edited:
                        ErBot20.add_event_handler(func, events.MessageEdited(**kwargs))
                    ErBot20.add_event_handler(func, events.NewMessage(**kwargs))
                if ErBot21:
                    if edited:
                        ErBot21.add_event_handler(func, events.MessageEdited(**kwargs))
                    ErBot21.add_event_handler(func, events.NewMessage(**kwargs))
                if ErBot22:
                    if edited:
                        ErBot22.add_event_handler(func, events.MessageEdited(**kwargs))
                    ErBot22.add_event_handler(func, events.NewMessage(**kwargs))
                if ErBot23:
                    if edited:
                        ErBot23.add_event_handler(func, events.MessageEdited(**kwargs))
                    ErBot23.add_event_handler(func, events.NewMessage(**kwargs))
                if ErBot24:
                    if edited:
                        ErBot24.add_event_handler(func, events.MessageEdited(**kwargs))
                    ErBot24.add_event_handler(func, events.NewMessage(**kwargs))
                if ErBot25:
                    if edited:
                        ErBot25.add_event_handler(func, events.MessageEdited(**kwargs))
                    ErBot25.add_event_handler(func, events.NewMessage(**kwargs))
                if ErBot26:
                    if edited:
                        ErBot26.add_event_handler(func, events.MessageEdited(**kwargs))
                    ErBot26.add_event_handler(func, events.NewMessage(**kwargs))
                if ErBot27:
                    if edited:
                        ErBot27.add_event_handler(func, events.MessageEdited(**kwargs))
                    ErBot27.add_event_handler(func, events.NewMessage(**kwargs))
                if ErBot28:
                    if edited:
                        ErBot28.add_event_handler(func, events.MessageEdited(**kwargs))
                    ErBot28.add_event_handler(func, events.NewMessage(**kwargs))
                if ErBot29:
                    if edited:
                        ErBot29.add_event_handler(func, events.MessageEdited(**kwargs))
                    ErBot29.add_event_handler(func, events.NewMessage(**kwargs))
                if ErBot30:
                    if edited:
                        ErBot30.add_event_handler(func, events.MessageEdited(**kwargs))
                    ErBot30.add_event_handler(func, events.NewMessage(**kwargs))
                if ErBot31:
                    if edited:
                        ErBot31.add_event_handler(func, events.MessageEdited(**kwargs))
                    ErBot31.add_event_handler(func, events.NewMessage(**kwargs))
                if ErBot32:
                    if edited:
                        ErBot32.add_event_handler(func, events.MessageEdited(**kwargs))
                    ErBot32.add_event_handler(func, events.NewMessage(**kwargs))
                if ErBot33:
                    if edited:
                        ErBot33.add_event_handler(func, events.MessageEdited(**kwargs))
                    ErBot33.add_event_handler(func, events.NewMessage(**kwargs))
                if ErBot34:
                    if edited:
                        ErBot34.add_event_handler(func, events.MessageEdited(**kwargs))
                    ErBot34.add_event_handler(func, events.NewMessage(**kwargs))
                if ErBot35:
                    if edited:
                        ErBot35.add_event_handler(func, events.MessageEdited(**kwargs))
                    ErBot35.add_event_handler(func, events.NewMessage(**kwargs))
                if ErBot36:
                    if edited:
                        ErBot36.add_event_handler(func, events.MessageEdited(**kwargs))
                    ErBot36.add_event_handler(func, events.NewMessage(**kwargs))
                if ErBot37:
                    if edited:
                        ErBot37.add_event_handler(func, events.MessageEdited(**kwargs))
                    ErBot37.add_event_handler(func, events.NewMessage(**kwargs))
                if ErBot38:
                    if edited:
                        ErBot38.add_event_handler(func, events.MessageEdited(**kwargs))
                    ErBot38.add_event_handler(func, events.NewMessage(**kwargs))
                if ErBot39:
                    if edited:
                        ErBot39.add_event_handler(func, events.MessageEdited(**kwargs))
                    ErBot39.add_event_handler(func, events.NewMessage(**kwargs))
                if ErBot40:
                    if edited:
                        ErBot40.add_event_handler(func, events.MessageEdited(**kwargs))
                    ErBot40.add_event_handler(func, events.NewMessage(**kwargs))
                if ErBot41:
                    if edited:
                        ErBot41.add_event_handler(func, events.MessageEdited(**kwargs))
                    ErBot41.add_event_handler(func, events.NewMessage(**kwargs))
                if ErBot42:
                    if edited:
                        ErBot42.add_event_handler(func, events.MessageEdited(**kwargs))
                    ErBot42.add_event_handler(func, events.NewMessage(**kwargs))
                if ErBot43:
                    if edited:
                        ErBot43.add_event_handler(func, events.MessageEdited(**kwargs))
                    ErBot43.add_event_handler(func, events.NewMessage(**kwargs))
                if ErBot44:
                    if edited:
                        ErBot44.add_event_handler(func, events.MessageEdited(**kwargs))
                    ErBot44.add_event_handler(func, events.NewMessage(**kwargs))
                if ErBot45:
                    if edited:
                        ErBot45.add_event_handler(func, events.MessageEdited(**kwargs))
                    ErBot45.add_event_handler(func, events.NewMessage(**kwargs))
                if ErBot46:
                    if edited:
                        ErBot46.add_event_handler(func, events.MessageEdited(**kwargs))
                    ErBot46.add_event_handler(func, events.NewMessage(**kwargs))
                if ErBot47:
                    if edited:
                        ErBot47.add_event_handler(func, events.MessageEdited(**kwargs))
                    ErBot47.add_event_handler(func, events.NewMessage(**kwargs))
                if ErBot48:
                    if edited:
                        ErBot48.add_event_handler(func, events.MessageEdited(**kwargs))
                    ErBot48.add_event_handler(func, events.NewMessage(**kwargs))
                if ErBot49:
                    if edited:
                        ErBot49.add_event_handler(func, events.MessageEdited(**kwargs))
                    ErBot49.add_event_handler(func, events.NewMessage(**kwargs))
                if ErBot50:
                    if edited:
                        ErBot50.add_event_handler(func, events.MessageEdited(**kwargs))
                    ErBot50.add_event_handler(func, events.NewMessage(**kwargs))
            return wrapper

        return decorator

    async def get_traceback(self, exc: Exception) -> str:
        return "".join(
            traceback.format_exception(etype=type(exc), value=exc, tb=exc.__traceback__)
        )

    def _kill_running_processes(self) -> None:
        """Kill all the running asyncio subprocessess"""
        for _, process in self.running_processes.items():
            try:
                process.kill()
                LOGS.debug("Killed %d which was still running.", process.pid)
            except Exception as e:
                LOGS.debug(e)
        self.running_processes.clear()

ErUbotSession.fast_download_file = download_file
ErUbotSession.fast_upload_file = upload_file
ErUbotSession.reload = restart_script
ErUbotSession.check_testcases = checking
