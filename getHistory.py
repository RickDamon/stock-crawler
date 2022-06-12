import requests
from lxml import etree
import pandas as pd
import os
import time

class Download_HistoryStock(object):
    def __init__(self,code):
        self.code = code
        self.start_url = "http://quotes.money.163.com/trade/lsjysj_" + self.code + ".html"
        print(self.start_url)
        self.headers = {
            "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1"
        }

    def parse_url(self):
        response = requests.get(self.start_url)
        print(response.status_code)
        if response.status_code == 200:
            return etree.HTML(response.content)
        return False

    def get_date(self,response):
        start_date = ''.join(response.xpath('//input[@name="date_start_type"]/@value')[0].split('-'))
        end_date = ''.join(response.xpath('//input[@name="date_end_type"]/@value')[0].split('-'))
        print('start date = ',start_date)
        print('end date = ',end_date)
        return start_date,end_date

    def download(self, start_date, end_date):

    # 上证股票code=0,深圳的股票code=1，创业板 code=1，#北京交易所的688， code=0
        if self.code[0] == '6':
            dl_code ='O'+self.code
    # if self.code[o] == '0’or self.code[0] == '3’:
        else:
            dl_code = '1' + self.code
        download_url = "http://quotes.money.163.com/service/chddata.html?code="+dl_code+"&start="+start_date+"&end="+end_date+"&fields=TCLOSE;HIGH;LOW;TOPEN;LCLOSE;CHG;PCHG;TURNOVER;VOTURNOVER;VATURNOVER;TCAP;MCAP"
        print ('download address = ', download_url)
        data = requests.get(download_url)
        f = open('stocks\\' + self.code + '.csv', 'wb')
        for chunk in data.iter_content(chunk_size=10000):
            if chunk:
                f.write(chunk)
        print('股票---', self.code, '历史数据正在下载')

    def run(self):
        try:
            html = self.parse_url()
            start_date,end_date = self.get_date(html)
            self.download(start_date,end_date)
        except Exception as e:
            print(e)


if not os.path.isdir('stocks'):
    os.mkdir('stocks')
stk_file = "stocks.csv"
stk_list = pd.read_csv(stk_file, encoding='gbk')
code = list(stk_list['code'])
code_str = [str(x) for x in code]
code_list = [x[-6:] for x in code_str]

for temp_code in code_list[:5]:
    time.sleep(1)
    download = Download_HistoryStock(temp_code)
    download.run()

