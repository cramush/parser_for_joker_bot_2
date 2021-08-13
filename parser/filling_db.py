from datetime import datetime
import pymongo
from config import db_login, db_password, db_host, db_name

client = pymongo.MongoClient(f"mongodb://{db_login}:{db_password}@{db_host}/{db_name}?authSource=admin")
db = client["joker_database"]
collection = db["jokes_b_category"]
if collection.estimated_document_count() == 0:
    collection.drop()
    collection.create_index([("tag", pymongo.ASCENDING), ("date", pymongo.ASCENDING)])


def filling_data(tag, new_joke):
    date = datetime.now()
    data = ""
    joke = {
        "tag": tag,
        "data": data,
        "content": new_joke,
        "date": date
    }
    collection.insert_one(joke)
