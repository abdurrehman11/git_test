import pandas as pd

df = pd.read_csv('sales_info.csv')

print(df.Company.value_counts())