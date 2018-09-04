from timer import *

import sqlite3
conn = sqlite3.connect('example.db')
c = conn.cursor()
c.execute('''DROP TABLE IF EXISTS stocks''')
c.execute('''CREATE TABLE IF NOT EXISTS stocks
             (sym text, bid real, ask real)''')
c.execute('''PRAGMA synchronous = EXTRA''')
c.execute('''PRAGMA journal_mode = WAL''')
             
with Timer() as timer:
    with open('input.ssv', 'r') as infile:
        lines = infile.read().splitlines()
        timer.setSize(len(lines))
        for line in lines:
            c.executemany("INSERT INTO stocks VALUES (?,?,?)", [(line[0:6], line[7:14], line[15:])])
        conn.commit()
        conn.close()
