import csv
import os
import pandas as pd

files = os.listdir(r'.\\Stocks')
cnt = 0
cnt_stk = 0
total_num = len(files)
fp_out_d7O = open(r'out_d70.txt', 'w')

for file in files:
    data = pd.read_csv(r'.\\Stocks\\{}'.format(file), encoding='gbk')
    price = data['收盘价'].values
    print("length of price", len(price))
    # price = price[:500]
    cnt += 1
    print('检查股票:{},总体进度{}/{}'.format(file[:-4], cnt, total_num))
    max_value, min_value = max(price), min(price)

    current_value = price[-1]
    if current_value < max_value*0.3:
        print("当前值{0},最大值{1}".format(current_value,max_value))
        cnt_stk = cnt_stk + 1
        print("当前价格已从最高的下跌超过70%,代码:{}".format(file[:-4]),file=print("符合条件的股票数量有:{0}".format(cnt_stk)))
print("符合条件的股票数量有:{0}".format(cnt_stk))
fp_out_d7O.close()
