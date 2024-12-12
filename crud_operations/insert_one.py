from pymongo import MongoClient
import datetime
import os
from dotenv import load_dotenv

# Load env variables
load_dotenv()

# Connect to MongoDB using MongoClient
mongodb_uri = os.environ['MONGODB_CONN_STRING']
client = MongoClient(mongodb_uri)

# Get reference to 'bank' database
db = client.bank

# Get access to 'accounts' collection
accounts_collection = db.accounts

new_account = {
    "account_holder": "Linus Torvalds",
    "account_id": "MDB1290129",
    "account_type": "checking",
    "balance": 91821,
    "last_updated": datetime.datetime.utcnow()
}

# insert the new_account into the accounts collection
result = accounts_collection.insert_one(new_account)
inserted_id = result.inserted_id

print(f'Inserted id: {inserted_id}')

client.close()