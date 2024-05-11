import redis
import json
from dotenv import load_dotenv
import os
from util import fix_keys
from pymongo import MongoClient

load_dotenv(".env.local")
load_dotenv(".env")

db = MongoClient(os.environ.get("MONGODB_CONNECT_URL")).get_database()
r = redis.Redis.from_url(os.environ.get('REDIS_CONNECT_URL'), decode_responses=True)

list_key = os.environ.get('REDIS_LIST')

while True:
    log = r.blpop(list_key, timeout=0)
    event = json.loads(log[1])
    if event['event_type'] != 'alert':
        continue;

    result = db['alerts'].insert_one(fix_keys(event))

    print("Event added to database: {}".format(result.inserted_id))