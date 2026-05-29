# ------------------------- #
# Don't Remove Credit 
# Ask Doubt @AU_Bot_Discussion 
# Owner @Mr_Mohammed_29 
# ------------------------- #

from database import users  # your Mongo collection

def get_user_settings(user_id):
    data = users.find_one({"user_id": user_id})

    if not data:
        return {
            "account_name": "Default User",
            "author_name": "Unknown"
        }

    return {
        "account_name": data.get("account_name", "Default User"),
        "author_name": data.get("author_name", "Unknown")
    }

# ------------------------- #
# Don't Remove Credit 
# Ask Doubt @AU_Bot_Discussion 
# Owner @Mr_Mohammed_29 
# ------------------------- #
