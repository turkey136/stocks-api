import numpy as np
from stock.models import DailyStock

date_format = "%Y-%m-%d"

class DailyStockModule():
  def save_daily_stock(self, daily_data, stock):
    if daily_data.sum()['Open'][stock.code] == 0:
      # 過去x日にデータが無いので廃止銘柄 or 取得不可
      print('not found stock data')
    else:
      for i in range(len(daily_data.index)):
        date = daily_data.index[i].strftime(date_format)
        daily_stock = self.build_daily_stock(stock, date)
        daily_stock.high=daily_data['High'][stock.code][date]
        daily_stock.low=daily_data['Low'][stock.code][date]
        daily_stock.open=daily_data['Open'][stock.code][date]
        daily_stock.close=daily_data['Close'][stock.code][date]
        daily_stock = self.calculation_daily_stock(daily_stock, stock, date)
        daily_stock.save()
        print('save daily stock. stock: %s, date: %s' %(stock.code, date))

  def calculation_daily_stock(self, daily_stock, stock, date):
    day_before_yesterday_daily_stock = DailyStock.objects.filter(stock=stock,date__lt=date).order_by('-date')[:1]
    if day_before_yesterday_daily_stock.exists():
      daily_stock.amount_of_change=daily_stock.close - day_before_yesterday_daily_stock[0].close

    # calculation
    daily_stock.rsi = self.calculation_rsi(stock, date)

    return daily_stock

  def build_daily_stock(self, stock, date):
    daily_stock = DailyStock.objects.filter(stock=stock,date=date)
    if not daily_stock.exists():
      daily_stock = DailyStock(stock=stock,date=date)
    else:
      daily_stock = daily_stock[0]
    return daily_stock

  def calculation_rsi(self, stock, date):
    old_stocks = DailyStock.objects.filter(stock=stock, amount_of_change__isnull=False, date__lt=date).order_by('-date')[:14]
    if old_stocks.count() == 14:
      over_zeros = np.sum([i['amount_of_change'] for i in old_stocks.values() if i['amount_of_change'] > 0])
      under_zeros = np.sum([i['amount_of_change'] for i in old_stocks.values() if i['amount_of_change'] < 0]) * -1
      return over_zeros / (under_zeros + over_zeros) * 100
    else:
      return None
