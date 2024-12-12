from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()
mongodb_uri = os.environ['MONGODB_CONN_STRING']

client = MongoClient(mongodb_uri)

db = client.bank

accounts_collection = db.accounts

query_object = {"balance": {"$gt": 4700}}

cursor = accounts_collection.find(query_object)

num_docs = 0
for document in cursor:
    num_docs += 1
    print(document + "\n\n")

print(f'\n\nFound {num_docs} documents')
client.close()