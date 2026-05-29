
# ------------------------- #
# Don't Remove Credit 
# Ask Doubt @AU_Bot_Discussion 
# Owner @Mr_Mohammed_29 
# ------------------------- #

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from database import posts


# ---------------- BUTTONS ---------------- #

def settings_buttons(user_id, post_count):

    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton(f"USER ID : {user_id}", callback_data="noop")
        ],
        [
            InlineKeyboardButton("DOMAIN : Telegraph", callback_data="noop")
        ],
        [
            InlineKeyboardButton("DEFAULT PAGE : @AU_Telegraph_Post_Bot", callback_data="noop")
        ],
        [
            InlineKeyboardButton("ACCOUNT NAME : Mohammed", callback_data="noop")
        ],
        [
            InlineKeyboardButton("AUTHOR : Mr_Mohammed_29", callback_data="noop")
        ],
        [
            InlineKeyboardButton("PROFILE LINK", url="https://t.me/Mr_Mohammed_29")
        ],
        [
            InlineKeyboardButton(f"NO. OF POSTS : {post_count}", callback_data="noop")
        ],
        [
            InlineKeyboardButton("🔄 Reset All", callback_data="reset_settings"),
            InlineKeyboardButton("🔙 Go Back", callback_data="start_home")
        ]
    ])

# ------------------------- #
# Don't Remove Credit 
# Ask Doubt @AU_Bot_Discussion 
# Owner @Mr_Mohammed_29 
# ------------------------- #

# ---------------- SETTINGS COMMAND ---------------- #

@Client.on_message(filters.command("settings"))
async def settings(_, message):

    user_id = message.from_user.id

    post_count = posts.count_documents({"user_id": user_id})

    text = f"""
⚙️ ACCOUNT SETTINGS

User ID: {user_id}
Domain: Telegraph
Default Page Title: @AU_Telegraph_Post_Bot

Account Name: Mohammed
Author Name: Mr_Mohammed_29
Profile Link: https://t.me/Mr_Mohammed_29
No. of Posts: {post_count}
"""

    await message.reply_text(
        text,
        reply_markup=settings_buttons(user_id, post_count)
    )

# ------------------------- #
# Don't Remove Credit 
# Ask Doubt @AU_Bot_Discussion 
# Owner @Mr_Mohammed_29 
# ------------------------- #
