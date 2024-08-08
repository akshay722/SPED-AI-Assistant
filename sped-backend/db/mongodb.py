from pymongo import MongoClient
from pymongo.uri_parser import parse_uri
from dotenv import load_dotenv
import os
import certifi

load_dotenv()

MONGODB_URL = os.environ.get("MONGODB_URI")
DB_NAME = os.environ.get("DB_NAME")

client = MongoClient(MONGODB_URL, tlsCAFile=certifi.where())
# customer_db_name = parse_uri(MONGODB_URL)["database"]
# print("customer_db_name", customer_db_name)
db = client[DB_NAME]
print("Connected to MongoDB...")
Users = db.users
Sessions = db.session
