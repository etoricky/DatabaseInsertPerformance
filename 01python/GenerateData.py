import time
start_time = time.time()
with open('input.ssv', 'w') as out:
    symbols = ['AUDUSD','EURUSD','GBPUSD','NZDUSD','USDCAD','USDCHF','USDJPY','USDCNY','USDHKD']
    lines = []
    for i in range(0,1*1000*1000):
        q1, r1, q2, r2 = i//100000, i%100000, (i+1)//100000, (i+1)%100000
        line = '{} {}.{:05d} {}.{:05d}'.format(symbols[i%len(symbols)], q1, r1, q2, r2)
        lines.append(line)
    out.write('\n'.join(lines))
print(time.time()-start_time, i)