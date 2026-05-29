# ------------------------- #
# Don't Remove Credit 
# Ask Doubt @AU_Bot_Discussion 
# Owner @Mr_Mohammed_29 
# ------------------------- #

from pyrogram import Client, filters
from database import total_users, total_posts
import config

# ------------------------- #
# Don't Remove Credit 
# Ask Doubt @AU_Bot_Discussion 
# Owner @Mr_Mohammed_29 
# ------------------------- #

@Client.on_message(filters.command("stats"))
async def stats(_, message):

    # OWNER CHECK
    if message.from_user.id != config.OWNER_ID:
        return await message.reply_text("❌ You are not allowed to use this command.")

    try:
        users = total_users()
        posts = total_posts()

    except Exception:
        return await message.reply_text("⚠️ Database error. Try again later.")

    text = f"""
📊 BOT STATISTICS

👥 Total Users: {users}
📝 Total Posts: {posts}

⚡ Status: Live
"""

    await message.reply_text(text)

# ------------------------- #
# Don't Remove Credit 
# Ask Doubt @AU_Bot_Discussion 
# Owner @Mr_Mohammed_29 
# ------------------------- #
