import datetime
import pymongo
from pymongo import MongoClient

client=MongoClient("mongodb+srv://stark:liyaxlambert@cluster0.pdabrye.mongodb.net/?retryWrites=true&w=majority")

db=client["stark-db"]

collection=db.test

collection=db["test-collection"]

post = {"author": "Mike",
        "text": "My first blog post!",
        "tags": ["mongodb", "python", "pymongo"],
        "date": datetime.datetime.utcnow()}
        
post_id=collection.insert_one(post).inserted_id
