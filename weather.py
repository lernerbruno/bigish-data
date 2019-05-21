import sqlite3
import pandas as pd

conn = sqlite3.connect('data/weather.db')

df = pd.read_sql('SELECT temp, gust FROM noaa_gsod WHERE year = 1930', conn)
print(df)

