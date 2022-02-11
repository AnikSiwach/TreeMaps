import yfinance as yf
from datetime import datetime, timedelta
import os


tickerNames = ['AAPL', 'MSFT', '2222.SR', 'GOOG', 'AMZN', 'BRK-A','TSM', 'NVDA', 'FB' ]
stockReturns = {}
marketCap = {}
frequency = 'weekly' #'daily' or 'weekly' or 'monthly'
today = datetime.now()

#Formatting Date
year = today.strftime("%Y")
month = today.strftime("%m")
day = today.strftime("%d")

if frequency == 'weekly':
    fromDate = (today - timedelta(days = 7))
    toDate = today
elif frequency == 'monthly':
    fromDate = (today - timedelta(month = 1))
    toDate = today
else:
    fromDate = today
    toDate = today

fromYear = fromDate.strftime("%Y")
toYear = fromDate.strftime("%Y")
fromMonth = fromDate.strftime("%m")
toMonth = fromDate.strftime("%m")
fromDay = fromDate.strftime("%d")
toDay = fromDate.strftime("%d")

fromDate = "{}-{}-{}".format(fromYear, fromMonth, fromDay)
toDate = "{}-{}-{}".format(toYear, toMonth, toDay)


