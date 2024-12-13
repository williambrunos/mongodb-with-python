from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()
mongodb_uri = os.environ['MONGODB_CONN_STRING']

client = MongoClient(mongodb_uri)
db = client.sample_training
companies_collection = db.companies

documents_to_update = {"name": "Zvents"}
update_employees = {"$set": {"number_of_employees": 70}}

result = companies_collection.update_one(documents_to_update, update_employees)
print(f'Matched documents: {result.matched_count}')
print(f'Modified documents: {result.modified_count}')

print(companies_collection.find_one(documents_to_update, {"_id": 0, "number_of_employees": 1}))