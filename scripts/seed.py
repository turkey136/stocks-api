import csv
import os
from stock.models import Market, Sector, Stock
# dc run --rm api python3 manage.py runscript seed

def run():
  # nasdaq, nyse csv: https://www.nasdaq.com/market-activity/stocks/screener
  # en etf csv: https://www.nasdaq.com/market-activity/etf/screener
  nasdaq_file_path = './scripts/seeds/nasdaq.csv'
  nyse_file_path = './scripts/seeds/nyse.csv'
  en_etf_file_path = './scripts/seeds/en_etf.csv'
  nyse = 'NYSE'
  nasdaq = 'NASDAQ'
  en_etf = 'EN ETF'
  market_names = [nyse, nasdaq, en_etf]

  for row in market_names:
    Market.objects.get_or_create(name=row)

  if os.path.exists(nasdaq_file_path):
    csv_file = read_csv(nasdaq_file_path)
    next(csv_file)
    market = Market.objects.get(name=nasdaq)
    for row in csv_file:
      create_stock(row, market)
      print('created code: %s' %(row[0]))

  if os.path.exists(nyse_file_path):
    csv_file = read_csv(nyse_file_path)
    next(csv_file)
    market = Market.objects.get(name=nyse)
    for row in csv_file:
      create_stock(row, market)
      print('created code: %s' %(row[0]))
    
  if os.path.exists(en_etf_file_path):
    csv_file = read_csv(en_etf_file_path)
    next(csv_file)
    market = Market.objects.get(name=en_etf)
    sector, _ = Sector.objects.get_or_create(name='ETF')
    for row in csv_file:
      create_etf_stock(row, market, sector)
      print('created code: %s' %(row[0]))

  print('insert seed done!')

def create_stock(row, market):
  sector, _ = Sector.objects.get_or_create(name=row[9])
  stock, _ = Stock.objects.get_or_create(code=row[0],market=market, sector=sector)
  stock.name=row[1]
  stock.industry=row[10]
  stock.save()

def create_etf_stock(row, market, sector):
  stock, _ = Stock.objects.get_or_create(code=row[0],market=market, sector=sector)
  stock.name=row[1]
  stock.save()

def read_csv(path):
  return csv.reader(
    open(path, "r"),
    delimiter=",",
    doublequote=True,
    lineterminator="\r\n",
    quotechar='"',
    skipinitialspace=True
  )
