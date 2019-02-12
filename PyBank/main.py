import pandas as pd
#read csv file using read_csv method
df = pd.read_csv("Resources/budget_data.csv")
#head() will check for the top 5 values
print(df.head())
print(df.shape)
size = df.shape
print(size[0])

total_months = size[0]

second_col = df["Profit/Losses"]

print(second_col)

print(second_col.sum())

print(df["Profit/Losses"].diff())

print(df["Profit/Losses"].diff().mean())

amount = df["Profit/Losses"].diff().max()


print(amount)

index = df["Profit/Losses"].diff().idxmax()

month = df["Date"][index]

decrease_amount = df["Profit/Losses"].diff().min()

index_decrease = df["Profit/Losses"].diff().idxmin()

decrease_month =  df["Date"][index_decrease]




