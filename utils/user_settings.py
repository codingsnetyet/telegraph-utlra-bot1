# ------------------------- #
# Don't Remove Credit 
# Ask Doubt @AU_Bot_Discussion 
# Owner @Mr_Mohammed_29 
# ------------------------- #

from database import users

def get_user_settings(user_id, telegram_first_name=None):
    data = users.find_one({"user_id": user_id})

    account_name = data.get("account_name") if data and data.get("account_name") else telegram_first_name
    author_name = data.get("author_name") if data and data.get("author_name") else "Unknown"

    return {
        "account_name": account_name or "User",
        "author_name": author_name
    }
# ------------------------- #
# Don't Remove Credit 
# Ask Doubt @AU_Bot_Discussion 
# Owner @Mr_Mohammed_29 
# ------------------------- #
