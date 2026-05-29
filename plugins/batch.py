# ------------------------- #
# Don't Remove Credit 
# Ask Doubt @AU_Bot_Discussion 
# Owner @Mr_Mohammed_29 
# ------------------------- #

from pyrogram import Client, filters
from telegraph import Telegraph
from database import save_batch, user_images

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

    content = ""

    # ✅ MULTIPLE IMAGES FROM DB
    img_data = user_images.find_one({"user_id": message.from_user.id})

    if img_data and "images" in img_data and img_data["images"]:
        for img in img_data["images"]:
            content += f'<img src="{img}"><br>'
        content += "<br>"

    # TITLE
    content += f"<b>{title}</b>\n\n"

    # EPISODES
    for i, t in enumerate(texts, 1):
        content += (
            f"<p><b>{title} {i}.</b> {t}</p>\n"
            "<hr>\n"
        )

    # ---------------- FOOTER ---------------- #

    content += """
    <br><br>
    <p><b>ᴄʜᴀɴɴᴇʟ :</b> <a href="https://t.me/Anime_UpdatesAU">ᴀɴɪᴍᴇ ᴜᴘᴅᴀᴛᴇs ᴀᴜ</a></p>
    <p><b>ᴅᴇᴠᴇʟᴏᴘᴇʀ :</b> <a href="https://t.me/Mr_Mohammed_29">ᴍᴏʜᴀᴍᴍᴇᴅ</a></p>
    """

    # ---------------- CREATE PAGE ---------------- #

    url = create_page(title, content)

    if not url:
        return await message.reply_text("❌ Telegraph failed")

    save_batch(message.from_user.id, [url])

    await message.reply_text(f"✅ Batch Created\n\n{url}")


# ---------------- IMAGE SAVE (MULTI IMAGE) ---------------- #

@Client.on_message(filters.photo)
async def upload_photo(_, message):

    user_id = message.from_user.id
    file_path = await message.download()

    try:
        response = tg.upload_file(file_path)
        telegraph_url = "https://telegra.ph" + response[0]

        # ✅ STORE MULTIPLE IMAGES
        user_images.update_one(
            {"user_id": user_id},
            {"$push": {"images": telegraph_url}},
            upsert=True
        )

        await message.reply_text(
            "🖼 Image added!\nSend more images or use /batch"
        )

    finally:
        if os.path.exists(file_path):
            os.remove(file_path)

# ------------------------- #
# Don't Remove Credit 
# Ask Doubt @AU_Bot_Discussion 
# Owner @Mr_Mohammed_29 
# ------------------------- #
