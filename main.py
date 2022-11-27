import datetime
import pymongo
from pymongo import MongoClient

client=MongoClient("mongodb+srv://Stark:liyaxlambert@cluster0.qekel3r.mongodb.net/?retryWrites=true&w=majority")

db=client["stark-db"]

collection=db["test-collection"]

post = {"author": "stark",
        "text": "My first db",
        "tags": ["mongodb", "python", "pymongo"],
        "date": datetime.datetime.utcnow()}
        
post_id=collection.insert_one(post).inserted_id
