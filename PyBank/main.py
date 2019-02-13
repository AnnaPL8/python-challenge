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

total = second_col.sum()

print(df["Profit/Losses"].diff())

average_change = df["Profit/Losses"].diff().mean()

print(df["Profit/Losses"].diff().mean())

amount = df["Profit/Losses"].diff().max()


print(amount)

index = df["Profit/Losses"].diff().idxmax()

month = df["Date"][index]

decrease_amount = df["Profit/Losses"].diff().min()

index_decrease = df["Profit/Losses"].diff().idxmin()

decrease_month =  df["Date"][index_decrease]


#Financial Analysis
#----------------------------
#Total Months: 86
#Total: $38382578
##Average  Change: $-2315.12
#Greatest Increase in Profits: Feb-2012 ($1926159)
#Greatest Decrease in Profits: Sep-2013 ($-2196167)

print("Financial Analysis")
print("-------------------------")
print("Total Months:", total_months)
print("Total:" , total )
print("Average Change:" ,average_change )
print("Greatest Increase in Profits:" ,month,amount)
print("Greatest decrease in Profits:" ,decrease_month,decrease_amount)

