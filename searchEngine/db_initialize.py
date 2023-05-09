'''
connects to the MongoDB database
'''

import os
import certifi
from pymongo import MongoClient
from dotenv import load_dotenv, find_dotenv
from searchEngine.constants import DATABASE

global database

load_dotenv(find_dotenv())
password = os.environ.get("MONGODB_PWD")
connection_string = f"mongodb+srv://sajad-1:{password}@searchengine.jdnugf9.mongodb.net/?retryWrites=true&" \
                    f"w=majority&authSource=admin"
client = MongoClient(connection_string, tlsCAFile=certifi.where())
client.drop_database(DATABASE)
database = client[DATABASE]
