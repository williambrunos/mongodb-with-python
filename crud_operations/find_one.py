from pymongo import MongoClient
from dotenv import load_dotenv
import os
from bson.objectid import ObjectId

load_dotenv()
mongodb_uri = os.environ['MONGODB_CONN_STRING']

client = MongoClient(mongodb_uri)

db = client.bank

accounts_collection = db.accounts

query_object = {"_id": ObjectId("990sdaIOA21312")}

result = accounts_collection.find_one(query_object)
print(result)

client.close()