from timer import *
import redis
r = redis.StrictRedis(host='localhost', port=6379, db=0)
with Timer() as t:
    with open('input.ssv', 'r') as infile:
        lines = infile.read().splitlines()
        t.setSize(len(lines))
        for line in lines:
            r.set(line[0:6]+'.bid', line[7:14])
            r.set(line[0:6]+'.ask', line[15:])