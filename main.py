import datetime
import pymongo
from pymongo import MongoClient

client=MongoClient("mongodb+srv://Stark:liyaxlambert@cluster0.qekel3r.mongodb.net/?retryWrites=true&w=majority")

db=client["stark-db"]

#collection=db["test-collection"]

karma_statusdb = db.karma_status

def set_karma(chat_id):
    karma = is_karma(chat_id)
    if not karma:
        karma_statusdb.insert_one({"chat_id":"-100"})
