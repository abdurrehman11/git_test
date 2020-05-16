import pandas as pd

df = pd.read_csv('sales_info.csv')

print(df.head(20))

print(df.Company.value_counts())