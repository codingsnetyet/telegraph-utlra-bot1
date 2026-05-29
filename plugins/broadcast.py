# ------------------------- #
# Don't Remove Credit 
# Ask Doubt @AU_Bot_Discussion 
# Owner @Mr_Mohammed_29 
# ------------------------- #

import asyncio
from pyrogram import Client, filters
from pyrogram.errors import FloodWait, UserIsBlocked, InputUserDeactivated
from database import users
import config

# ------------------------- #
# Don't Remove Credit 
# Ask Doubt @AU_Bot_Discussion 
# Owner @Mr_Mohammed_29 
# ------------------------- #

@Client.on_message(filters.command("broadcast"))
async def broadcast(client, message):

    if message.from_user.id != config.OWNER_ID:
        return await message.reply_text("❌ Not allowed")

    if not message.reply_to_message:
        return await message.reply_text("❌ Reply to a message to broadcast")

    text = (
        message.reply_to_message.text
        or message.reply_to_message.caption
    )

    if not text:
        return await message.reply_text("❌ No content found")

    sent = 0
    failed = 0
    
# ------------------------- #
# Don't Remove Credit 
# Ask Doubt @AU_Bot_Discussion 
# Owner @Mr_Mohammed_29 
# ------------------------- #
    
    msg = await message.reply_text("📢 Broadcasting started...")

    for user in users.find():

        try:
            await client.send_message(
                user["user_id"],
                text
            )
            sent += 1

            await asyncio.sleep(0.05)  # prevents flood

        except FloodWait as e:
            await asyncio.sleep(e.value)

        except (UserIsBlocked, InputUserDeactivated):
            failed += 1

        except Exception:
            failed += 1

    await msg.edit_text(
        f"""
📢 Broadcast Completed

✅ Sent: {sent}
❌ Failed: {failed}
"""
    )

# ------------------------- #
# Don't Remove Credit 
# Ask Doubt @AU_Bot_Discussion 
# Owner @Mr_Mohammed_29 
# ------------------------- #
