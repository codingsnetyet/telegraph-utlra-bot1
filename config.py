# ------------------------- #
# Don't Remove Credit 
# Ask Doubt @AU_Bot_Discussion 
# Owner @Mr_Mohammed_29 
# ------------------------- #

import os

API_ID = os.environ.get("API_ID")
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")
OWNER_ID = os.environ.get("OWNER_ID")
MONGO_URL = os.environ.get("MONGO_URL")

if not API_ID or not API_HASH or not BOT_TOKEN or not OWNER_ID or not MONGO_URL:
    raise Exception("One or more environment variables are missing")

API_ID = int(API_ID)
OWNER_ID = int(OWNER_ID)

DB_NAME = "telegraph_ultra"

# ------------------------- #
# Don't Remove Credit 
# Ask Doubt @AU_Bot_Discussion 
# Owner @Mr_Mohammed_29 
# ------------------------- #
