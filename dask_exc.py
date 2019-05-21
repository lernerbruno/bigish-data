import dask.dataframe as dd

df = dd.read_csv('data/taxi/*.csv')
# it doesn't work because median is not trivial for parallel work
# vc = df['VendorID'].median()
vc = df.groupby('passenger_count')['trip_distance'].max()
out = vc.compute()
print(out)
