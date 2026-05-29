# ------------------------- #
# Don't Remove Credit 
# Ask Doubt @AU_Bot_Discussion 
# Owner @Mr_Mohammed_29 
# ------------------------- #

from pymongo import MongoClient
import config
import time

# ---------------- CONNECTION ---------------- #

client = MongoClient(config.MONGO_URL, serverSelectionTimeoutMS=5000)

db = client[config.DB_NAME]

users = db.users
posts = db.posts
batches = db.batches

# ------------------------- #
# Don't Remove Credit 
# Ask Doubt @AU_Bot_Discussion 
# Owner @Mr_Mohammed_29 
# ------------------------- #

# ---------------- INDEXES (IMPORTANT) ---------------- #

users.create_index("user_id", unique=True)
posts.create_index("user_id")
batches.create_index("user_id")

# ------------------------- #
# Don't Remove Credit 
# Ask Doubt @AU_Bot_Discussion 
# Owner @Mr_Mohammed_29 
# ------------------------- #


# ---------------- USER ---------------- #

def add_user(user_id):
    if not user_id:
        return

    users.update_one(
        {"user_id": user_id},
        {"$set": {
            "user_id": user_id,
            "time": int(time.time())
        }},
        upsert=True
    )

# ------------------------- #
# Don't Remove Credit 
# Ask Doubt @AU_Bot_Discussion 
# Owner @Mr_Mohammed_29 
# ------------------------- #


# ---------------- POSTS ---------------- #

def save_post(user_id, url, title):
    posts.insert_one({
        "user_id": user_id,
        "url": url,
        "title": title,
        "time": int(time.time())
    })
    
# ------------------------- #
# Don't Remove Credit 
# Ask Doubt @AU_Bot_Discussion 
# Owner @Mr_Mohammed_29 
# ------------------------- #

# ---------------- BATCH ---------------- #

def save_batch(user_id, urls):
    batches.insert_one({
        "user_id": user_id,
        "urls": urls,
        "time": int(time.time())
    })

# ------------------------- #
# Don't Remove Credit 
# Ask Doubt @AU_Bot_Discussion 
# Owner @Mr_Mohammed_29 
# ------------------------- #

# ---------------- STATS ---------------- #

def total_users():
    return users.count_documents({})


def total_posts():
    return posts.count_documents({})


def total_batches():
    return batches.count_documents({})

# ------------------------- #
# Don't Remove Credit 
# Ask Doubt @AU_Bot_Discussion 
# Owner @Mr_Mohammed_29 
# ------------------------- #
