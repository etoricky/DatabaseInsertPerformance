from timer import *

import sqlite3
conn = sqlite3.connect('example.db')
c = conn.cursor()
             
with Timer() as timer:
    c.execute("SELECT * FROM stocks")
    rows = c.fetchall()
    timer.setSize(len(rows))
    print(len(rows))