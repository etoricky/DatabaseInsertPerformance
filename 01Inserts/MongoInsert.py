from timer import *
from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017/" )
client.drop_database('test-collection')
db = client['test-database']
collect = db['test-collection']
with Timer() as t:
    with open('input.ssv', 'r') as infile:
        lines = infile.read().splitlines()
        t.setSize(len(lines))
        for line in lines:
            document = {
                    "time": time.time(),
                    "symbol": line[0:6],
                    "bid": float(line[7:14]),
                    "ask": float(line[15:])
                }
            collect.insert_one(document)