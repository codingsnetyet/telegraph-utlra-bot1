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
    
# ------------------------- #
# Don't Remove Credit 
# Ask Doubt @AU_Bot_Discussion 
# Owner @Mr_Mohammed_29 
# ------------------------- #

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

# ------------------------- #
# Don't Remove Credit 
# Ask Doubt @AU_Bot_Discussion 
# Owner @Mr_Mohammed_29 
# ------------------------- #
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
# ------------------------- #
# Don't Remove Credit 
# Ask Doubt @AU_Bot_Discussion 
# Owner @Mr_Mohammed_29 
# ------------------------- #
    # ---------------- HTML BUILD (FIXED) ---------------- #
    content = f"<b>{title}</b>\n\n"

    for i, t in enumerate(texts, 1):
        content += f"<b>{i}.</b> {t}\n\n"

    content += """
    <b>Channel:</b> @Anime_UpdatesAU<br>
    <b>Owner:</b> @Mr_Mohammed_29
    """

    # ------------------------- #
# Don't Remove Credit 
# Ask Doubt @AU_Bot_Discussion 
# Owner @Mr_Mohammed_29 
# ------------------------- #

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
