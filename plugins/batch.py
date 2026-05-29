# ------------------------- #
# Don't Remove Credit 
# Ask Doubt @AU_Bot_Discussion 
# Owner @Mr_Mohammed_29 
# ------------------------- #

from pyrogram import Client, filters
from telegraph import Telegraph
from database import save_batch

tg = Telegraph()

try:
    tg.create_account(short_name="batch-bot")
except Exception as e:
    print("Telegraph account error:", e)


# ---------------- CREATE PAGE ---------------- #

def create_page(title, content):
    try:
        response = tg.create_page(
            title=title[:100],
            html_content=content
        )
        return response["url"]

    except Exception as e:
        print("Telegraph error:", e)
        return None


# ---------------- BATCH COMMAND ---------------- #

@Client.on_message(filters.command("batch"))
async def batch(_, message):

    if "|" not in message.text:
        return await message.reply_text(
            "❌ Usage:\n/batch Title | text1,text2,text3"
        )

    try:
        title, texts = message.text.split("|", 1)
        title = title.split(None, 1)[1].strip()
    except:
        return await message.reply_text("❌ Invalid format")

    texts = [t.strip() for t in texts.split(",") if t.strip()]

    if not texts:
        return await message.reply_text("❌ No text found")


    # ---------------- HTML BUILD ---------------- #

    content = f"<b>{title}</b>\n\n"

    # ✅ Each episode in clean block
    for i, t in enumerate(texts, 1):
        content += (
            f"<p><b>{title} {i}.</b> {t}</p>\n"
            "<hr>\n"
        )

    # ---------------- FOOTER (ONLY ONCE) ---------------- #

    content += """
    <br><br>
    <p><b>ᴄʜᴀɴɴᴇʟ :</b> <a href="https://t.me/Anime_UpdatesAU">ᴀɴɪᴍᴇ ᴜᴘᴅᴀᴛᴇs ᴀᴜ</a></p>
    <p><b>ᴅᴇᴠᴇʟᴏᴘᴇʀ :</b> <a href="https://t.me/Mr_Mohammed_29">ᴍᴏʜᴀᴍᴍᴇᴅ</a></p>
    """

    # ---------------- CREATE PAGE ---------------- #

    url = create_page(title, content)

    if not url:
        return await message.reply_text(
            "❌ Telegraph failed (check logs)"
        )

    save_batch(message.from_user.id, [url])

    await message.reply_text(
        f"✅ Batch Created\n\n{url}"
    )

# ------------------------- #
# Don't Remove Credit 
# Ask Doubt @AU_Bot_Discussion 
# Owner @Mr_Mohammed_29 
# ------------------------- #
