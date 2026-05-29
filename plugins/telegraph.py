# ------------------------- #
# Don't Remove Credit 
# Ask Doubt @AU_Bot_Discussion 
# Owner @Mr_Mohammed_29 
# ------------------------- #

import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from telegraph import Telegraph
from database import save_post

# ---------------- TELEGRAPH INIT ---------------- #

tg = Telegraph()

try:
    tg.create_account(short_name="ultra-bot")
except:
    pass

# ------------------------- #
# Don't Remove Credit 
# Ask Doubt @AU_Bot_Discussion 
# Owner @Mr_Mohammed_29 
# ------------------------- #

# ---------------- HTML FORMAT ---------------- #

def html_format(text):
    if not text:
        return ""
    return (
        text.replace("&", "&amp;")
             .replace("<", "&lt;")
             .replace(">", "&gt;")
             .replace("\n", "<br>")
    )

# ------------------------- #
# Don't Remove Credit 
# Ask Doubt @AU_Bot_Discussion 
# Owner @Mr_Mohammed_29 
# ------------------------- #

# ---------------- CREATE PAGE ---------------- #

def create_page(title, content):
    response = tg.create_page(
        title=title,
        html_content=content
    )
    return response["url"]

# ------------------------- #
# Don't Remove Credit 
# Ask Doubt @AU_Bot_Discussion 
# Owner @Mr_Mohammed_29 
# ------------------------- #

# ---------------- CREATE /TGM ---------------- #

@Client.on_message(filters.command("tgm"))
async def telegraph(_, message):

    title = "Telegraph Post"
    text = None
    media_html = ""

    # /tgm title | text
    if "|" in message.text:
        try:
            title, text = message.text.split("|", 1)
            title = title.split(None, 1)[1].strip()
            text = text.strip()
        except:
            pass

    # REPLY SUPPORT
    elif message.reply_to_message:
        reply = message.reply_to_message

        # PHOTO
        if reply.photo:
            file_path = await reply.download()
            try:
                response = tg.upload_file(file_path)
                url = "https://telegra.ph" + response[0]
                media_html += f'<img src="{url}"><br>'
            finally:
                if os.path.exists(file_path):
                    os.remove(file_path)

        # GIF / ANIMATION
        elif reply.animation:
            file_path = await reply.download()
            try:
                response = tg.upload_file(file_path)
                url = "https://telegra.ph" + response[0]
                media_html += f'<img src="{url}"><br>'
            finally:
                if os.path.exists(file_path):
                    os.remove(file_path)

        # TEXT / CAPTION
        else:
            text = reply.text or reply.caption

    # DIRECT TEXT
    elif len(message.command) > 1:
        text = message.text.split(None, 1)[1]

    # VALIDATION
    if not text and not media_html:
        return await message.reply_text(
            "❌ Send text or reply to photo/gif/text"
        )

# ------------------------- #
# Don't Remove Credit 
# Ask Doubt @AU_Bot_Discussion 
# Owner @Mr_Mohammed_29 
# ------------------------- #

    # ---------------- BUILD CONTENT ---------------- #

    content = ""

    if text:
        content += f"<p>{html_format(text)}</p>"

    if media_html:
        content += media_html

# ------------------------- #
# Don't Remove Credit 
# Ask Doubt @AU_Bot_Discussion 
# Owner @Mr_Mohammed_29 
# ------------------------- #

    # ---------------- FOOTER ---------------- #

    content += """
    <hr>
    <p><b>ᴄʜᴀɴɴᴇʟ :</b> <a href="https://t.me/Anime_UpdatesAU">ᴀɴɪᴍᴇ ᴜᴘᴅᴀᴛᴇs ᴀᴜ</a></p>
    <p><b>ᴅᴇᴠᴇʟᴏᴘᴇʀ:</b> <a href="https://t.me/Mr_Mohammed_29">ᴍᴏʜᴀᴍᴍᴇᴅ</a></p>
    """
# ------------------------- #
# Don't Remove Credit 
# Ask Doubt @AU_Bot_Discussion 
# Owner @Mr_Mohammed_29 
# ------------------------- #
    # ---------------- CREATE PAGE ---------------- #

    url = create_page(title, content)

    save_post(message.from_user.id, url, title)

    await message.reply_text(
        f"✅ Telegraph Created\n\n{url}",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🌐 Open", url=url)]]
        )
    )

# ------------------------- #
# Don't Remove Credit 
# Ask Doubt @AU_Bot_Discussion 
# Owner @Mr_Mohammed_29 
# ------------------------- #

# ---------------- IMAGE UPLOAD ---------------- #

@Client.on_message(filters.photo)
async def upload_photo(_, message):

    file_path = await message.download()

    try:
        response = tg.upload_file(file_path)

        telegraph_url = "https://telegra.ph" + response[0]

        await message.reply_text(
            f"🖼 Uploaded To Telegraph\n\n{telegraph_url}"
        )

    except Exception as e:
        await message.reply_text(str(e))

    finally:
        if os.path.exists(file_path):
            os.remove(file_path)


# ------------------------- #
# Don't Remove Credit 
# Ask Doubt @AU_Bot_Discussion 
# Owner @Mr_Mohammed_29 
# ------------------------- #
