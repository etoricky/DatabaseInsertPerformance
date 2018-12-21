import pandas as pd
import mysql.connector
def GetData(symbol, cmd, db):
    conn = mysql.connector.connect(user='reportserveruser', password='@cet0p@dmin@db',host='127.0.0.1',database='mt4_share')
    cursor = conn.cursor()
    sql = '''
    SELECT 
      OPEN_TIME, CLOSE_TIME, Volume, OPEN_PRICE
    FROM
      {}.mt4_trades AS t
    WHERE (t.SYMBOL = '{}') AND (t.CMD = {});
    '''.format(db, symbol, cmd)
    cursor.execute(sql);
    row = cursor.fetchone()
    while row is not None:
        line = ','.join(row)
        print(line)
        row = cursor.fetchone()
    cursor.close()
    conn.close()
GetData('GOLD', 0, 'mt4_live03')