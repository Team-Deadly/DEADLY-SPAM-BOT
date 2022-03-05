# DEADLY X Spam - Spam Userbots
# © 2021 - 2022 - TheDEADLY

import os
import sys
from OfficialSameer import SAM, SAM2, SAM3, SAM4, SAM5 , SAM6, SAM7, SAM8, SAM9, SAM10, SAM11, SAM12, SAM13, SAM14, SAM15, SAM16, SAM17, SAM18, SAM19, SAM20, SAM21, SAM22, SAM23, SAM24, SAM25, SAM26, SAM27, SAM28, SAM29, SAM30, SAM31, SAM32, SAM33, SAM34, SAM35, SAM36, SAM37, SAM38, SAM39, SAM40, SUDO_USERS
from OfficialSameer import ALIVE_PIC, deadlyversion
from .. import CMD_HNDLR as hl
from telethon import events, version
from time import time
from datetime import datetime

def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time

@SAM.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@SAM2.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@SAM3.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@SAM4.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@SAM5.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@SAM6.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@SAM7.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@SAM8.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@SAM9.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@SAM10.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@SAM11.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@SAM12.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@SAM13.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@SAM14.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@SAM15.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@SAM16.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@SAM17.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@SAM18.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@SAM19.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@SAM20.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@SAM21.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@SAM22.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@SAM23.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@SAM24.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@SAM25.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@SAM26.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@SAM27.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@SAM28.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@SAM29.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@SAM30.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@SAM31.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@SAM32.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@SAM33.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@SAM34.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@SAM35.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@SAM36.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@SAM37.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@SAM38.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@SAM39.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@SAM40.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
async def ping(e):
    if e.sender_id in SUDO_USERS:
        if e.reply_to_msg_id:
            fuk = await e.respond("Pᴏɴɢ!!.....", reply_to=e.reply_to_msg_id)
        else:
            fuk = await e.reply("Pᴏɴɢ!!.....")
        start = datetime.now()
        end = datetime.now()
        ms = (end-start).microseconds / 1000
        pingop =             f"😁 🇵 🇴 🇳 🇬 !\n\n♡︎ `{ms}` 𝗺𝘀 ♡︎"                   
        await fuk.edit(pingop)


# ALIVE

SAM_PIC = ALIVE_PIC if ALIVE_PIC else "https://te.legra.ph/file/1b99b29043777af4e3898.jpg"


DEADLY = "🔥 ᴅᴇᴀᴅʟʏ sᴘᴀᴍ ʙᴏᴛ 🔥 \n\n"

DEADLY += f"┏━━━━━━━━━━━━━━━━━━━\n"

DEADLY += f"┣➣ **ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ** : `3.9.6`\n"
                           
DEADLY += f"┣➣ **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ** : `{version.__version__}`\n"

DEADLY += f"┣➣ **ᴅᴇᴀᴅʟʏ ᴠᴇʀsɪᴏɴ**  : `{8xversion}`\n"
    
DEADLY += f"┣➣ **sᴜᴘᴘᴏʀᴛ** : [JOIN](https://t.me/clan8xofficial)\n"

DEADLY += f"┣➣ **ᴄʜᴀɴɴᴇʟ** : [JOIN](https://t.me/allf_ban)\n"

DEADLY += f"┗━━━━━━━━━━━━━━━━━━━\n\n"

DEADLY += f"🖤 [𝐑𝐄𝐏𝐎](https://github.com/SUSHILxPLAYER) 🖤"            
                                    
@SAM.on(events.NewMessage(incoming=True, pattern=r"\%salive" % hl))
async def alive(event):
    if event.sender_id in SUDO_USERS:
     await SAM.send_file(event.chat_id,
                                  SAM_PIC,
                                  caption=DEADLY)
   
   
# help

HELP_PIC = "https://te.legra.ph/file/1b99b29043777af4e3898.jpg"

DEADLY = "🔥 CobRA SPAM BOT 🔥\n\n"
 
DEADLY += f"__ᴄᴍᴅs ᴀᴠᴀɪʟᴀʙʟᴇ ɪɴ ᴅᴇᴀᴅʟʏ sᴘᴀᴍ ʙᴏᴛ__\n\n"

DEADLY += f" ↧ 𝚄𝚂𝙴𝚁𝙱𝙾𝚃 𝙲𝙼𝙳𝚂 ↧\n\n"

DEADLY += f" `.ping` - `.alive` - `.setname` - `.setbio` - `.inviteall` - .`restart` - `.update` - `.stats` - `.addsudo` \n\n"
 
DEADLY += f" ↧ 𝙹𝙾𝙸𝙽/𝙻𝙴𝙰𝚅𝙴 𝙲𝙼𝙳𝚂 ↧\n\n"

DEADLY += f" `.join` - `.pjoin` - `.leave`\n\n"
 
DEADLY += f" ↧ 𝚂𝙿𝙰𝙼 / 𝚁𝙰𝙸𝙳 𝙲𝙼𝙳𝚂 ↧\n\n"

DEADLY += f" `.raid` - `.replyraid` - `.dreplyraid` - `.delayraid` \n\n `.spam` - `.bigspam` - `.delayspam` - `.abuse` \n\n"

DEADLY += f" 𝙳𝙼 / 𝙴𝚌𝚑𝚘 𝙲𝚖𝚍𝚜 \n\n"

DEADLY += f" `.dm` - `.dmraid` - `.dmspam` \n\n `.addecho` - `.rmecho` \n\n"

DEADLY += f"All Cmds Uploaded : [•HERE•](https://t.me/allf_ban/) \n\n"
                                                         
DEADLY += f"© @tag_ban | @allf_ban\n"


@SAM.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
async def help(event):
    if event.sender_id in SUDO_USERS:
     await SAM.send_file(event.chat_id,
                                  HELP_PIC,
                                  caption=DEADLY)                                                         


@SAM.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@SAM2.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@SAM3.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@SAM4.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@SAM5.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@SAM6.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@SAM7.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@SAM8.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@SAM9.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@SAM10.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@SAM11.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@SAM12.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@SAM13.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@SAM14.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@SAM15.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@SAM16.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@SAM17.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@SAM18.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@SAM19.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@SAM20.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@SAM21.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@SAM22.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@SAM23.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@SAM24.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@SAM25.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@SAM26.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@SAM27.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@SAM28.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@SAM29.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@SAM30.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@SAM31.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@SAM32.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@SAM33.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@SAM34.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@SAM35.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@SAM36.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@SAM37.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@SAM38.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@SAM39.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@SAM40.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
async def restart(e):
    if e.sender_id in SUDO_USERS:
        text = "𝙍𝙀𝙎𝙏𝘼𝙍𝙏𝙄𝙉𝙂\n\n ....Please Wait Until It Starts Again"
        await e.reply(text, parse_mode=None, link_preview=None)
        try:
            await SAM.disconnect()
        except Exception:
            pass
        try:
            await SAM2.disconnect()
        except Exception:
            pass
        try:
            await SAM3.disconnect()
        except Exception:
            pass
        try:
            await SAM4.disconnect()
        except Exception:
            pass
        try:
            await SAM5.disconnect()
        except Exception:
            pass
        try:
            await SAM6.disconnect()
        except Exception:
            pass
        try:
            await SAM7.disconnect()
        except Exception:
            pass
        try:
            await SAM8.disconnect()
        except Exception:
            pass
        try:
            await SAM9.disconnect()
        except Exception:
            pass
        try:
            await SAM10.disconnect()
        except Exception:
            pass
        try:
            await SAM11.disconnect()
        except Exception:
            pass
        try:
            await SAM12.disconnect()
        except Exception:
            pass
        try:
            await SAM13.disconnect()
        except Exception:
            pass
        try:
            await SAM14.disconnect()
        except Exception:
            pass
        try:
            await SAM15.disconnect()
        except Exception:
            pass
        try:
            await SAM16.disconnect()
        except Exception:
            pass
        try:
            await SAM17.disconnect()
        except Exception:
            pass
        try:
            await SAM18.disconnect()
        except Exception:
            pass
        try:
            await SAM19.disconnect()
        except Exception:
            pass
        try:
            await SAM20.disconnect()
        except Exception:
            pass
        try:
            await SAM21.disconnect()
        except Exception:
            pass
        try:
            await SAM22.disconnect()
        except Exception:
            pass
        try:
            await SAM23.disconnect()
        except Exception:
            pass
        try:
            await SAM24.disconnect()
        except Exception:
            pass
        try:
            await SAM25.disconnect()
        except Exception:
            pass
        try:
            await SAM26.disconnect()
        except Exception:
            pass
        try:
            await SAM27.disconnect()
        except Exception:
            pass
        try:
            await SAM28.disconnect()
        except Exception:
            pass
        try:
            await SAM29.disconnect()
        except Exception:
            pass
        try:
            await SAM30.disconnect()
        except Exception:
            pass
        try:
            await SAM31.disconnect()
        except Exception:
            pass
        try:
            await SAM32.disconnect()
        except Exception:
            pass
        try:
            await SAM33.disconnect()
        except Exception:
            pass
        try:
            await SAM34.disconnect()
        except Exception:
            pass
        try:
            await SAM35.disconnect()
        except Exception:
            pass
        try:
            await SAM36.disconnect()
        except Exception:
            pass
        try:
            await SAM37.disconnect()
        except Exception:
            pass
        try:
            await SAM38.disconnect()
        except Exception:
            pass
        try:
            await SAM39.disconnect()
        except Exception:
            pass
        try:
            await SAM40.disconnect()
        except Exception:
            pass

        os.execl(sys.executable, sys.executable, *sys.argv)
        quit()
