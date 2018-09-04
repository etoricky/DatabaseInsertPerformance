from timer import *
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="Tin.netS1",
  auth_plugin='mysql_native_password'
)
print(mydb)
with Timer() as t:
    with open('input.ssv', 'r') as infile:
        lines = infile.read().splitlines()
        t.setSize(len(lines))
        documents = []
        for line in lines:
            documents.append({
                    "time": time.time(),
                    "symbol": line[0:6],
                    "bid": float(line[7:14]),
                    "ask": float(line[15:])
                })
            if len(documents)>128:
                collect.insert_many(documents)
                documents = []
        collect.insert_many(documents)
        documents = []