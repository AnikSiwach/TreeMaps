import yfinance as yf
from datetime import datetime

tickerNames = ['AAPL', 'MSFT', '2222.SR', 'GOOG', 'AMZN', 'BRK-A','TSM', 'NVDA', 'FB' ]
frequency = '1D'
dataDict = {}
todayDateTime = datetime.now()

for ticker in tickerNames:
    data = yf.download(ticker,start=todayDateTime, end=todayDateTime )
    closePrice = data['Close']
    openPrice = data['Open']
    change = float((closePrice - openPrice) / closePrice)
    dataDict[ticker] = change


