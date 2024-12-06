from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

mongodb_conn_string = os.environ["MONGODB_CONN_STRING"]
client = MongoClient(mongodb_conn_string)

for db in client.list_database_names():
    print(db)
