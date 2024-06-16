from contextlib import contextmanager
import os
from dotenv import load_dotenv
from pymongo import MongoClient
from pymongo.server_api import ServerApi

load_dotenv()

DB_URI = os.getenv('DB_URI')
DB_HOST = os.getenv('DB_host')
DB_PORT = int(os.getenv('DB_port'))

DB_NAME = 'short_url'
DB_COLLECTION = 'fast'

@contextmanager
def _connect_to_mongo():
    client = MongoClient(DB_URI)
    db = client[DB_NAME]
    collection = db[DB_COLLECTION]
    
    try:
        print(f"Connected to MongoDB - {DB_COLLECTION}")
        yield collection
    except Exception as e:
        print(f"Error in MongoDB - {DB_COLLECTION} operation: {e}")
        raise Exception(e)
    finally:
        print(f"Closing MongoDB - {DB_COLLECTION} connection")
        client.close()

def create_fast_url(doc):
    with _connect_to_mongo() as collection:
        try:
            result = collection.insert_one(doc).inserted_id
            print(f"Inserted document with ID: {result}")
            return str(doc['hash'])
        except Exception as e:
            print(f"Error in create_fast_url: {e}")
            raise

def update_fast_url(filter, attributes):
    with _connect_to_mongo() as collection:
        try:
            collection.update_one(filter, attributes)
        except Exception as e:
            print(f"Error in update_fast_url: {e}")
            raise

def get_fast_url_by_hash(hash):
    with _connect_to_mongo() as collection:
        doc = collection.find_one({"hash": hash})
        update_fast_url({'_id': doc['_id']}, {'$set': {'clicks': doc['clicks'] + 1}})

        return doc

def get_fast_url_by_link(link):
    with _connect_to_mongo() as collection:
        return collection.find_one({"link": link})

def exists_url_by_hash(hash):
    with _connect_to_mongo() as collection:
        return collection.count_documents({"hash": hash}, limit=1) != 0
    
def exists_url_by_link(link):
    with _connect_to_mongo() as collection:
        return collection.count_documents({"link": link}, limit=1) != 0
    
def count_total_clicks_fast_url(result={'total': 0}):
    with _connect_to_mongo() as collection:
        for doc in list(collection.find()):
            result['total'] += doc['clicks']
        
        return result['total']