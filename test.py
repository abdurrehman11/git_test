import pandas as pd

df = pd.read_csv('sales_info.csv')

print(df.head(100))

print(df.Company.value_counts())