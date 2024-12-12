from bson.objectid import ObjectId
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()
mongodb_uri = os.environ['MONGODB_CONN_STRING']

client = MongoClient(mongodb_uri)
db = client.bank
accounts_collection = db.accounts

filter_document = {"account_type": "savings"}
update_document = {"$set": {"minimun_balance": 100}}

result = accounts_collection.update_many(filter_document, update_document)
print(f'Matched documents: {result.matched_count}')
print(f'Modified documents: {result.modified_count}')
print(accounts_collection.find(filter_document))

client.close()
