import datetime
import pymongo
from pymongo import MongoClient

post = {"author": "Mike",
        "text": "My first blog post!",
        "tags": ["mongodb", "python", "pymongo"],
        "date": datetime.datetime.utcnow()}

client=MongoClient("mongodb+srv://Stark:liyaxlambert@cluster0.qekel3r.mongodb.net/?retryWrites=true&w=majority")

db=client["stark-db"]

#collection=db["test-collection"]

karma_statusdb = db.karma_status


def is_karma(chat_id):
    karma = karma_statusdb.find_one({"chat_id": -100})
    


def set_karma(chat_id):
    karma = is_karma(chat_id)
    if not karma:
        collection.insert_one(post)
