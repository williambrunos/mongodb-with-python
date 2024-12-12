from bson.objectid import ObjectId
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()
mongodb_uri = os.environ['MONGODB_CONN_STRING']

client = MongoClient(mongodb_uri)
db = client.bank
accounts_collection = db.accounts

filter_document = {"_id": ObjectId("990sdaIOA21312")}
add_to_balance = {"$inc": {"balance": 100}}

print(accounts_collection.find_one(filter_document))

result = accounts_collection.update_one(filter_document, add_to_balance)
print(f'Modified documents: {result.modified_count}')

print(accounts_collection.find_one(filter_document))

client.close()
