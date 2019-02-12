import pandas as pd
#read csv file using read_csv method
df = pd.read_csv("Resources/budget_data.csv")
#head() will check for the top 5 values
print(df.head())
