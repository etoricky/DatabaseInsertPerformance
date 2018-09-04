from timer import *

import queue, threading

def Worker(q):
    import sqlite3
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute('''DROP TABLE IF EXISTS stocks''')
    c.execute('''CREATE TABLE IF NOT EXISTS stocks
                 (sym text, bid real, ask real)''')
    c.execute('''PRAGMA synchronous = EXTRA''')
    c.execute('''PRAGMA journal_mode = WAL''')
    while True:
        line = q.get()
        if not line:
            break
        c.executemany("INSERT INTO stocks VALUES (?,?,?)", [(line[0:6], line[7:14], line[15:])])
    conn.commit()
    conn.close()
        
if __name__=='__main__':
    q = queue.Queue()
    t = threading.Thread(target=Worker, args=(q,))
    t.start()
    with Timer() as timer:
        with open('input.ssv', 'r') as infile:
            lines = infile.read().splitlines()
            timer.setSize(len(lines))
            for line in lines:
                q.put(line)
            q.put(None)
        t.join()