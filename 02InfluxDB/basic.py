from influxdb import InfluxDBClient
json_body = [
    {
        "measurement": "quotes",
        "tags": {
            "symbol": "GOLD"
        },
        "fields": {
            "bid": 1250,
            "ask": 1251
        }
    }
]
client = InfluxDBClient('localhost', 8086, 'root', 'root', 'example')
client.create_database('example')
client.write_points(json_body)
client.write_points(json_body)
client.write_points(json_body)
result = client.query('select bid from quotes;')
print("Result: {0}".format(result))