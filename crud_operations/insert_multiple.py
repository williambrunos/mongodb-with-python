from pymongo import MongoClient
from dotenv import load_dotenv
import datetime
import os 

# Loading env variables
load_dotenv()
mongo_uri = os.environ['MONGODB_CONN_STRING']

# Create mongo client
client = MongoClient(mongo_uri)

# Reference the database
db = client.bank

# Referennce the collection
collection = db.accounts

new_accounts = [
    {
        "account_holder": "Linus Torvalds",
        "account_id": "MDB1290129",
        "account_type": "checking",
        "balance": 91821,
        "last_updated": datetime.datetime.utcnow()
    },
    {
        "account_holder": "Linus Torvalds",
        "account_id": "MDB1290129",
        "account_type": "checking",
        "balance": 91821,
        "last_updated": datetime.datetime.utcnow()
    }   
]

# Inser many operation
result = collection.insert_many(new_accounts)
inserted_ids = result.inserted_ids

print(f'Inserted ids: {inserted_ids}')

client.close()
