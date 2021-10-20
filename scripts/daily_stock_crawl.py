import pandas_datareader.data as web
import time
from datetime import datetime, timedelta
from stock.models import Stock
from multiprocessing import Pool
from scripts.modules import DailyStockModule

# dc run --rm api python3 manage.py runscript daily_stock_crawl

date_format = "%Y-%m-%d"
five_day_ago = (datetime.today() - timedelta(days=30)).strftime(date_format)

# 1銘柄単位でやると時間がかかる ＆ 外部システムから接続切られるので100銘柄単位で取得する
def run():
  stocks = each_slice(Stock.objects.filter().order_by('code'), 100)
  with Pool(processes=2) as p:
    p.map(func=create_daily_stock, iterable=stocks)

def create_daily_stock(stocks):
  try:  
    daily_data = fetch_daily_data(stocks)
    for stock in stocks:
      DailyStockModule().save_daily_stock(daily_data, stock)
      print('created daily data. code: %s' %(stock.code))
  except Exception as e:
    for stock in stocks:
      print('error daily data. code: %s, error: %s' %(stock.code, e))
  finally:
    time.sleep(1)

def fetch_daily_data(stocks):
  symbols =  [stock.code for stock in stocks]
  return web.DataReader(symbols, 'yahoo', five_day_ago)

def each_slice(arr, n):
  return [arr[i:i + n] for i in range(0, len(arr), n)]
