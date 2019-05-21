import pandas as pd

csv_file = 'data/yellow_tripdata_2018-05.csv.bz2'
time_cols = ['tpep_pickup_datetime', 'tpep_dropoff_datetime']
columns_to_index = ['VendorID', 'passenger_count']

df = pd.read_csv(csv_file, parse_dates=time_cols, nrows=1_000_000)
store = pd.HDFStore('HF5/yellow.h5')
store.append('HF5/yellow', df, data_columns=columns_to_index)
result = store.select('HF5/yellow', where='VendorID == 1 & passenger_count > 1', columns=time_cols+['trip_distance'])
print(len(result))
store.close()



