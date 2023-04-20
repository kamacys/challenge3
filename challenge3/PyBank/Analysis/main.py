import os
import csv

budgetdata_csv = os.path.join("Resources", "budget_data.csv")

totalMonth = 0
totalProfit_Losses = 0
previousProfit_Losses = 0
Profit_Losses_change = 0
ProfitLoss_change_list = []
month_change = []
greatestIncrease = 0
greatestDecrease = 9999999

with open(budgetdata_csv) as profit_lossData:
    reader = csv.DictReader(profit_lossData)

    for row in reader:
        totalMonth = totalMonth + 1

totalProfit_Losses = totalProfit_Losses + int(row["Profit/Losses"])
Profit_Losses_change = int(row["Profit/Losses"]) - previousProfit_Losses
previousProfit_Losses = int(row["Profit/Losses"])
month_change = month_change + [row["Date"]]

print("Financial Analysis")
print("----------------------")
print(f"Total Months: {totalMonth}\n")
print(f"Total Profit/Losess: ${totalProfit_Losses}\n")

#print(f"Average Change: ${round(sum(ProfitLoss_change_list)/len(ProfitLoss_change_list),2)}") 
#print(f"Greatest Increase in Profits: {month_change[greatestIncrease]} (${(str(greatestIncrease))})")
#print(f"Greatest decrease in Profits: {totalMonth[greatestDecrease_month]} (${(str(greatestDecrease))})")