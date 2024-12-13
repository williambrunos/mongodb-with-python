from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()
mongodb_uri = os.environ['MONGODB_CONN_STRING']

client = MongoClient(mongodb_uri)
db = client.bank
accounts_collection = db.accounts

document_to_delete = {"balance": {"$lt": 2000}}

print(f'Searching for documents: {document_to_delete}')
print(accounts_collection.find(document_to_delete))

print(f'Deleting documents: {document_to_delete}')
result = accounts_collection.delete_many(document_to_delete)
print(f'Deleted documents: {result.deleted_count}')

print(f'Searching for documents after deletion: {document_to_delete}')
print(accounts_collection.find(document_to_delete))

client.close()
