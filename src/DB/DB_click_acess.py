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
DB_COLLECTION = 'click'

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

def create_clicks(doc):
    with _connect_to_mongo() as collection:
        try:
            result = collection.insert_one(doc).inserted_id
            print(f"Inserted document with ID: {result}")
        except Exception as e:
            print(f"Error in create_clicks: {e}")
            raise

def _update_clicks(filter, attributes):
        with _connect_to_mongo() as collection:
            try:
                collection.update_one(filter, attributes)
            except Exception as e:
                print(f"Error in update_clicks: {e}")
                raise
    
def get_clicks():
    with _connect_to_mongo() as collection:
        return collection.find_one()
    
def update_clicks(date):
    doc = get_clicks()
    _update_clicks({'_id': doc['_id']}, {'$set': {'total_clicks': doc['total_clicks'] + 1, 'last_update': date}})
