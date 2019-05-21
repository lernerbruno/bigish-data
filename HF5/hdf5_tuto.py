import pandas as pd

df = pd.read_csv('stocks.csv', parse_dates=['Date'])
store = pd.HDFStore('stocks.h5')
# Here you create indices Symbol and Date
store.append('stocks', df, data_columns=['Symbol', 'Date'])
# print(store.keys())
store.select('stocks', where='index < 10', columns=['Symbol', 'Open', 'Close'])
store.query("Symbol == 'AAPL' & Date > '' ")
store.close()

