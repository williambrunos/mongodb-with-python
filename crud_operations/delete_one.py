from bson.objectid import ObjectId
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()
mongodb_uri = os.environ['MONGODB_CONN_STRING']

client = MongoClient(mongodb_uri)
db = client.bank
accounts_collection = db.accounts

document_to_delete = {"_id": ObjectId("990sdaIOA21312")}
print(f'Searching for document: {document_to_delete}')
print(accounts_collection.find_one(document_to_delete))

result = accounts_collection.delete_one(document_to_delete)
print(f'Deleted documents: {result.deleted_count}')

print(f'Searching for document after deletion: {document_to_delete}')
print(accounts_collection.find_one(document_to_delete))

client.close()