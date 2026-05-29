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
except:
    pass


# ---------------- CREATE PAGE ---------------- #

def create_page(title, content):
    try:
        response = tg.create_page(
            title=title,
            html_content=content
        )
        return response["url"]
    except:
        return None

# ------------------------- #
# Don't Remove Credit 
# Ask Doubt @AU_Bot_Discussion 
# Owner @Mr_Mohammed_29 
# ------------------------- #


# ---------------- BATCH COMMAND (UPGRADED) ---------------- #

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
        return await message.reply_text(
            "❌ Invalid format\nUse:\n/batch Title | text1,text2"
        )

    texts = [t.strip() for t in texts.split(",") if t.strip()]

    if not texts:
        return await message.reply_text("❌ No valid batch content found")

# ------------------------- #
# Don't Remove Credit 
# Ask Doubt @AU_Bot_Discussion 
# Owner @Mr_Mohammed_29 
# ------------------------- #
    
    # ---------------- BUILD HTML ---------------- #

    content = f"<h2>{title}</h2><hr>"

    for i, text in enumerate(texts, start=1):
        content += f"""
        <h3>Page {i}</h3>
        <p>{text}</p>
        <hr>
        """
# ------------------------- #
# Don't Remove Credit 
# Ask Doubt @AU_Bot_Discussion 
# Owner @Mr_Mohammed_29 
# ------------------------- #
    
    # ---------------- FOOTER ---------------- #

    content += """
    <br>
    <hr>
    <p><b>Channel:</b> @Anime_UpdatesAU</p>
    <p><b>Owner:</b> @Mr_Mohammed_29</p>
    """

# ------------------------- #
# Don't Remove Credit 
# Ask Doubt @AU_Bot_Discussion 
# Owner @Mr_Mohammed_29 
# ------------------------- #

    # ---------------- CREATE PAGE ---------------- #

    url = create_page(title, content)

    if not url:
        return await message.reply_text("❌ Failed to create batch page")

    save_batch(message.from_user.id, [url])

    await message.reply_text(
        f"✅ Batch Page Created\n\n{url}"
    )

# ------------------------- #
# Don't Remove Credit 
# Ask Doubt @AU_Bot_Discussion 
# Owner @Mr_Mohammed_29 
# ------------------------- #
