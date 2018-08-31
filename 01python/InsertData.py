import time

class Timer:    
    def __enter__(self):
        self.start = time.time()
        return self
    def __exit__(self, *args):
        elapsed = time.time()-self.start
        print('Imported in {:.2f} seconds or {:.0f} per second'.format(elapsed, 1*1000*1000/elapsed))

import sqlite3
conn = sqlite3.connect('example.db')
c = conn.cursor()
c.execute('''DROP TABLE IF EXISTS stocks''')
c.execute('''CREATE TABLE IF NOT EXISTS stocks
             (sym text, bid real, ask real)''')
c.execute('''PRAGMA synchronous = EXTRA''')
c.execute('''PRAGMA journal_mode = DELETE''')
             
with Timer() as t:
    with open('input.ssv', 'r') as infile:
        lines = infile.read().splitlines()
        for line in lines:
            c.executemany("INSERT INTO stocks VALUES (?,?,?)", [(line[0:6], line[7:14], line[15:])])
        conn.commit()
        conn.close()
