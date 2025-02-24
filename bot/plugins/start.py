from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from ..screenshotbot import ScreenShotBot


@ScreenShotBot.on_message(filters.private & filters.command("start"))
async def start(c, m):

    await m.reply_text(
        text=f"Hi there {m.from_user.mention}.\n\nI'm Screenshot Generator Bot. I can provide screenshots from "
        "your video files without downloading the entire file (almost instantly). For more details check /help.",
        quote=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🌀SUPPORT GROUP🌀", url="https://github.com/odysseusmax/animated-lamp"
                    ),
                    InlineKeyboardButton("🔱BOTS Channel🔱", url="https://t.me/KOT_BOTS"),
                ],
                [InlineKeyboardButton("🌐My Father🌐", url="https://t.me/KOT_FREE_DE_LA_HOYA_OFF")],
            ]
        ),
    )
