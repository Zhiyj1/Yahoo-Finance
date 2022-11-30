import yfinance as yf

# Method 1
def getYahooFinanceCandleStick(ticker, start=None, end=None, period=None, interval="1d", actions=True):
    # get historical data for the specified ticker
    print("Ticker:", ticker)
    ticker_info = yf.Ticker(ticker)
    data = ticker_info.history(start=start, end=end, period=period, interval=interval, actions=actions)
    # drop the timezones in datetimes, since Excel does not support datetimes with timezones
    data.index = data.index.date
    data.index.name = "Date"
    return data


def export_to_excel(data, ticker, start=None, end=None, period=None, interval="1d"):
    # export to Excel
    if start is None: start = ""
    if end is None: end = ""
    if period is None: period = ""
    fimename = ticker+start+end+period+interval
    data.to_excel("{}.xlsx".format(fimename))


 # set 1 year time up to today, interval as daily,actions as False since no need for dividends and stock splites info
spy_data = getYahooFinanceCandleStick(ticker="SPY", start=None, end=None, period="1y", interval="1d", actions=False)
export_to_excel(data=spy_data, ticker="SPY", start=None,end=None, period="1y", interval="1d")


# Method 2
#def getYahooFinanceCandleStick2(tickers, start=None, end=None, period=None, interval="1d", ignore_tz=False):
#    print("Tickers:", tickers)
#    data = yf.download(tickers=tickers, start=start, end=end,period=period, interval=interval, ignore_tz=ignore_tz)
#    # get the candle stick data (date, open, high, low, close, volume)
#    data = data.drop(columns="Close")
#    data.rename(columns={'Adj Close': 'Close'}, inplace=True)
#    # change the datetime to data
#    data.index = data.index.date
#    data.index.name = "Date"
#    return data
#
#
#def export_to_excel(data, ticker, start=None, end=None, period=None, interval="1d"):
#    # export to Excel
#    if start is None:start = ""
#    if end is None: end = ""
#    if period is None: period = ""
#    fimename = ticker+start+end+period+interval
#    data.to_excel("{}.xlsx".format(fimename))
#
#
## set 1 year time up to today, interval as daily,ignore_tz as True since Excel does not support datetimes with timezones
#spy_data = getYahooFinanceCandleStick2(tickers="SPY", start=None, end=None, period="1y", interval="1d", ignore_tz=True)
#export_to_excel(data=spy_data, ticker="SPY", start=None, end=None, period="1y", interval="1d")
