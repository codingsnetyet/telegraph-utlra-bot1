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

This bot helps you create Telegraph pages, batch uploads, and manage files easily.
Language : Python 3
Library : Pyrogram 
Database : MongoDB
Channel : @Anime_UpdatesAU 
Support : @AU_Bot_Discussion 
Owner : @Mr_Mohammed_29 
"""
# ------------------------- #
# Don't Remove Credit 
# Ask Doubt @AU_Bot_Discussion 
# Owner @Mr_Mohammed_29 
# ------------------------- #


# ---------------- BUTTONS ---------------- #

def start_buttons():
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton("🚀 Start", callback_data="start_home"),
            InlineKeyboardButton("📢 Updates", url="https://t.me/Anime_UpdatesAU")
        ],
        [
            InlineKeyboardButton("ℹ️ About", callback_data="about"),
            InlineKeyboardButton("👑 Owner", url="https://t.me/Mr_Mohammed_29")
        ]
    ])


def back_button():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🏠 Home", callback_data="start_home")]
    ])

# ------------------------- #
# Don't Remove Credit 
# Ask Doubt @AU_Bot_Discussion 
# Owner @Mr_Mohammed_29 
# ------------------------- #


# ---------------- START COMMAND ---------------- #

@Client.on_message(filters.command("start"))
async def start(client, message):

    add_user(message.from_user.id)

    # 🔥 Animation sequence
    m = await message.reply_text("🚀 Sʜᴀᴅᴏᴡ Oғ Mᴏɴᴀʀᴄʜ . . .")
    await asyncio.sleep(0.5)

    await m.edit_text("🎊")
    await asyncio.sleep(0.5)

    await m.edit_text("⚡")
    await asyncio.sleep(0.5)

    await m.edit_text("🤖 Wᴇʟᴄᴏᴍɪɴɢ Yᴏᴜ . . .")
    await asyncio.sleep(0.7)

    await m.delete()

    # 🎬 Final GIF + Menu
    await message.reply_animation(
        animation=START_GIF,
        caption=START_TEXT,
        reply_markup=start_buttons()
    )

# ------------------------- #
# Don't Remove Credit 
# Ask Doubt @AU_Bot_Discussion 
# Owner @Mr_Mohammed_29 
# ------------------------- #

# ---------------- CALLBACK ---------------- #

@Client.on_callback_query()
async def callback_handler(client: Client, query: CallbackQuery):

    data = query.data

    if data == "start_home":
        await query.message.edit_caption(
            START_TEXT,
            reply_markup=start_buttons()
        )

    elif data == "about":
        await query.message.edit_caption(
            ABOUT_TEXT,
            reply_markup=back_button()
        )

# ------------------------- #
# Don't Remove Credit 
# Ask Doubt @AU_Bot_Discussion 
# Owner @Mr_Mohammed_29 
# ------------------------- #
