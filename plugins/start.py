# ------------------------- #
# Don't Remove Credit 
# Ask Doubt @AU_Bot_Discussion 
# Owner @Mr_Mohammed_29 
# ------------------------- #

import asyncio
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from database import add_user


START_GIF = "https://media.giphy.com/media/3o7aD2saalBwwftBIY/giphy.gif"

START_TEXT = """
Welcome To AU Ultra Telegraph Bot
"""

ABOUT_TEXT = """
🤖 About This Bot

Language : Python 3
Library : Pyrogram 
Database : MongoDB
Channel : @Anime_UpdatesAU 
Support : @AU_Bot_Discussion 
Owner : @Mr_Mohammed_29 
"""

HELP_TEXT = """
❓ HELP MENU

📌 /tgm
→ Create Telegraph page from text/media

📌 /batch
→ Generate batch links for multiple files

💡 Just send files or text and follow instructions.
"""

# ---------------- BUTTONS ---------------- #

def start_buttons():
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton("📢 Updates", url="https://t.me/Anime_UpdatesAU")
        ],
        [
            InlineKeyboardButton("ℹ️ About", callback_data="about"),
            InlineKeyboardButton("❓ Help", callback_data="help")
        ],
        [
            InlineKeyboardButton("👑 Owner", url="https://t.me/Mr_Mohammed_29")
        ]
    ])


def back_button():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🏠 Home", callback_data="start_home")]
    ])


# ---------------- START COMMAND ---------------- #

@Client.on_message(filters.command("start"))
async def start(client, message):

    add_user(message.from_user.id)

    m = await message.reply_text("🚀 Sʜᴀᴅᴏᴡ Oғ Mᴏɴᴀʀᴄʜ . . .")
    await asyncio.sleep(0.5)

    await m.edit_text("🎊")
    await asyncio.sleep(0.5)

    await m.edit_text("⚡")
    await asyncio.sleep(0.5)

    await m.edit_text("🤖 Wᴇʟᴄᴏᴍɪɴɢ Yᴏᴜ . . .")
    await asyncio.sleep(0.7)

    await m.delete()

    await message.reply_animation(
        animation=START_GIF,
        caption=START_TEXT,
        reply_markup=start_buttons()
    )


# ---------------- CALLBACK ---------------- #

@Client.on_callback_query()
async def callback_handler(client: Client, query: CallbackQuery):

    data = query.data

    if data == "about":
        await query.message.edit_caption(
            ABOUT_TEXT,
            reply_markup=back_button()
        )

    elif data == "help":
        await query.message.edit_caption(
            HELP_TEXT,
            reply_markup=back_button()
        )

    elif data == "start_home":
        await query.message.edit_caption(
            START_TEXT,
            reply_markup=start_buttons()
        )

    elif data == "close_panel":
        await query.message.delete()

    elif data == "stats_panel":
        await query.message.edit_text("Use /stats")

    elif data == "broadcast_panel":
        await query.message.edit_text("Reply and use /broadcast")

    elif data == "batch_panel":
        await query.message.edit_text("Use /batch command")

    elif data == "reset_settings":
        await query.message.edit_text(
            "⚠️ Settings reset completed.",
            reply_markup=start_buttons()
        )

    elif data == "noop":
        await query.answer()

# ------------------------- #
# Don't Remove Credit 
# Ask Doubt @AU_Bot_Discussion 
# Owner @Mr_Mohammed_29 
# ------------------------- #
