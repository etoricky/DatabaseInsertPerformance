from timer import *
from influxdb import InfluxDBClient
client = InfluxDBClient('localhost', 8086, 'root', 'root', 'database01')
client.create_database('database01')
with Timer() as t:
    with open('input.ssv', 'r') as infile:
        lines = infile.read().splitlines()
        t.setSize(len(lines))
        json_body = []
        for line in lines:
            json_body.append({
                    "measurement": "quotes",
                    "tags": {
                        "symbol": line[0:6]
                    },
                    "fields": {
                        "bid": float(line[7:14]),
                        "ask": float(line[15:])
                    }
                })
            if len(json_body)>1024:
                client.write_points(json_body)
                json_body = []
        client.write_points(json_body)
