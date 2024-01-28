import os
from dotenv import load_dotenv
from pymongo import MongoClient  

load_dotenv()

client = MongoClient(os.getenv('DB_host'), int(os.getenv('DB_port')))
db = client['short_url']
collection = db['fast']

def create_fast_url(doc):
    try:
        result = collection.insert_one(doc).inserted_id
        return str(result)
    finally:
        client.close()

def get_fast_url(name):
    return collection.find_one({"name":name})

def exists_fast_url(name):
    if collection.count_documents({"name":name}, limit = 1) != 0:
        return True
    return False