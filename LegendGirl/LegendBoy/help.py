from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, Message

from Data import Data
from LegendGirl.Config import *

if HELP_MSG:
    HELP_MSG = HELP_MSG
else:
    HELP_MSG = "[Spam Bot](https://t.me/YARANA_TG) Help Menu"


@Client.on_message(filters.command(["dxhelp"], prefixes=HANDLER))
async def _help(Legend: Client, message: Message):
    HELP_MSG = "╔═════❰🇼𝐄𝐋𝐋𝐂𝐎𝐌𝐄❱═❍
║╔═════🦋۩۞۩🦋════╗
║     𝐃𝐌 𝐏𝐌 𝐍𝐎𝐓 𝐀𝐥𝐥𝐨𝐰 
║╚═════🦋۩۞۩🦋════╝
║ ┏━━━━━━➣
║ ┣⪼ ᴏᴡɴᴇʀ (@ll_LEGEND_ll)
║ ┗━━━━━━➣
╚════════════════❍
┏━━━━━━➣
┣⪼  [ @DX_INFO ]
┗━━━━━━➣
┏━━━━━━➣
┣⪼  { @DXallBot }
┗━━━━━━➣"
    if ".jpg" in HELP_PIC or ".png" in HELP_PIC:
        await Legend.send_photo(
            message.chat.id,
            HELP_PIC,
            caption=HELP_MSG,
            reply_markup=InlineKeyboardMarkup(Data.HELP_MENU1),
        )
    elif ".mp4" in HELP_PIC.lower():
        await Legend.send_video(
            message.chat.id,
            HELP_PIC,
            caption=HELP_MSG,
            reply_markup=InlineKeyboardMarkup(Data.HELP_MENU1),
        )
    else:
        await Legend.send_message(
            message.chat.id,
            HELP_MSG,
            reply_markup=InlineKeyboardMarkup(Data.HELP_MENU1),
        )
