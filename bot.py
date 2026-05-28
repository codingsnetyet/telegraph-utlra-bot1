# ------------------------- #
# Don't Remove Credit 
# Ask Doubt @AU_Bot_Discussion 
# Owner @Mr_Mohammed_29 
# ------------------------- #

from threading import Thread
from flask import Flask
from pyrogram import Client
import config

app = Flask(__name__)

# ------------------------- #
# Don't Remove Credit 
# Ask Doubt @AU_Bot_Discussion 
# Owner @Mr_Mohammed_29 
# ------------------------- #

@app.route("/")
def home():
    return "Telegraph Bot Running"


def run_web():
    app.run(
        host="0.0.0.0",
        port=8080
    )

# ------------------------- #
# Don't Remove Credit 
# Ask Doubt @AU_Bot_Discussion 
# Owner @Mr_Mohammed_29 
# ------------------------- #

bot = Client(
    "TelegraphUltraBot",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    bot_token=config.BOT_TOKEN,
    plugins=dict(root="plugins")
)

Thread(target=run_web).start()

print("""
╔══════════════════════╗
║   ᴍᴅ-ᴅᴇᴠᴇʟᴏᴘᴇʀ-ʏᴛ         ║
║   ᴛᴇʟᴇɢʀᴀᴘʜ ꜱᴛᴀʀᴛᴇᴅ.       ║
╚══════════════════════╝
""")

bot.run()

# ------------------------- #
# Don't Remove Credit 
# Ask Doubt @AU_Bot_Discussion 
# Owner @Mr_Mohammed_29 
# ------------------------- #
