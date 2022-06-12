from selenium import webdriver
import time
import csv
import re


driver = webdriver.Chrome(r'C:\Users\HASEE\AppData\Local\Temp\Rar$EXa19552.47034\chromedriver.exe')
driver.maximize_window()
# stock_list_url = 'http:/ / quote.eastmoney.com/stocklist.html'
# http:7// quotes.money.163.com/old/#query=EQA&DataType-HS_RANK&sort=PERCENT&o1
stock_list_url = r'http://quotes.money.163.com/old/#query=EQA&DataType=HS_RANK&sort=PERCENT&order=desc&count=5000&page=0'
driver.get(stock_list_url)
time.sleep(20) # 加载5000个股票需要时间
data = driver.page_source
with open('tmp.txt', encoding='utf-8', mode='w') as fp:
    fp.write(data)
stock_p = '<a href="http://quotes.money.163.com/(\d{7}).html" target="_blank" class="symbol">(.*?)</a>'
stocks = re.findall(stock_p, data)
print("一共获得股票数量:{}".format(len(stocks)))
# 7位的代码，变成6位
# 这个操作无所谓，到时读取的时候，取后6个数字即可。#因为6位代码，写入csv的时候，前面的0不见了
##stocks6 = list (
##for i in range(len (stocks) ) :
##stocks6. append(list(stocks[i]))##

head = ('code', 'name')
with open('stock.csv', 'a', newline='') as f:
    writer = csv.writer(f)
    for stock in stocks:
        writer.writerow(stock)

cnt = 0
with open('stocks_filter.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(head)

with open('stocks_filter.csv', 'a', newline='') as f:
    writer = csv.writer(f)
    for stock in stocks:
        if "退" in stock[1] or "ST" in stock[1]:
            continue

        writer.writerow(stock)
        cnt = cnt + 1
print("过滤后，共获得股票{}只".format(cnt))