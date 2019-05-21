import pandas as pd
from pathlib import Path
import bz2

csv_file = 'yellow_tripdata_2018-05.csv.bz2'
time_cols = ['tpep_pickup_datetime', 'tpep_dropoff_datetime']

size = Path(csv_file).stat().st_size
print(f'size = {size / (2 ** 20)} MB')
# with bz2.open(csv_file, 'rt') as fp:
#     for _ in range(5):
#         print(fp.readline().strip())

# Load only first 1000 rows for quick look at data
# df = pd.read_csv(csv_file, parse_dates=time_cols, nrows=1000)
dfs = pd.read_csv(csv_file, parse_dates=time_cols, chunksize=10_000)

# Calculate the mean ride duration using the above iterator (mean of means)
total_mean = pd.Timedelta(0)
total_items = 0
for df in dfs:
    pickup_times = df['tpep_pickup_datetime']
    dropoff_times = df['tpep_dropoff_datetime']
    ride_time_mean = (dropoff_times - pickup_times).mean()
    total_mean += ride_time_mean
    total_items += 1

print(f'The average ride time is {total_mean/total_items}')

