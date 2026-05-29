# ------------------------- #
# Don't Remove Credit 
# Ask Doubt @AU_Bot_Discussion 
# Owner @Mr_Mohammed_29 
# ------------------------- #

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import config

# ------------------------- #
# Don't Remove Credit 
# Ask Doubt @AU_Bot_Discussion 
# Owner @Mr_Mohammed_29 
# ------------------------- #

@Client.on_message(filters.command("panel"))
async def panel(_, message):

    if message.from_user.id != config.OWNER_ID:
        return await message.reply_text("❌ You are not allowed to use this command.")

    text = """
🧠 ADMIN CONTROL PANEL

Manage your bot from here:
"""
# ------------------------- #
# Don't Remove Credit 
# Ask Doubt @AU_Bot_Discussion 
# Owner @Mr_Mohammed_29 
# ------------------------- #
    buttons = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("📊 Stats", callback_data="stats_panel"),
            InlineKeyboardButton("📢 Broadcast", callback_data="broadcast_panel")
        ],
        [
            InlineKeyboardButton("📦 Batch", callback_data="batch_panel")
        ],
        [
            InlineKeyboardButton("❌ Close", callback_data="close_panel")
        ]
    ])

    await message.reply_text(text, reply_markup=buttons)

# ------------------------- #
# Don't Remove Credit 
# Ask Doubt @AU_Bot_Discussion 
# Owner @Mr_Mohammed_29 
# ------------------------- #
