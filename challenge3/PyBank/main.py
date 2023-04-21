import os
import csv

budgetdata_csv = os.path.join("Resources", "budget_data.csv")

totalmonths = 0
totalprofitloss = 0
value = 0
change = 0
dates = []
profits = []

with open(budgetdata_csv, newline="") as budget_file:
    csvreader = csv.reader(budget_file, delimiter= ",")
    csv_header = next(csvreader)
    first_row = next(csvreader)

    totalmonths += 1
    totalprofitloss += int(first_row[1])
    value = int(first_row[1])

    for row in csvreader:
        dates.append(row[0])
        change = int(row[1])-value
        profits.append(change)
        value = int(row[1])
        totalmonths += 1
        totalprofitloss = totalprofitloss + int(row[1])
        avg_change =sum(profits)/len(profits)
    
    greatestincrease = max(profits)
    greatestincreaseindex = profits.index(greatestincrease)
    greatestincreasedate = dates[greatestincreaseindex]
    
    greatestdecrease = min(profits)
    greatestdecreaseindex = profits.index(greatestdecrease)
    greatestdecreasedate = dates[greatestdecreaseindex]

    print(f"Financial Analysis\n")
    print(f"-----------------------------------\n")
    print(f"Total Months: {str(totalmonths)}\n")
    print(f"Total: ${str(totalprofitloss)}\n")
    print(f"Average Change: ${str(round(avg_change,2))}\n")
    print(f"Greatest Increase in Profits: {greatestincreasedate} (${str(greatestincrease)})\n")
    print(f"Greatest Decrease in Profits: {greatestdecreasedate} (${str(greatestdecrease)})\n")

    output_file = os.path.join('Analysis', 'PyBank_output.txt')

    PyBankoutput = open(output_file, "w")

    line1 = "Financial Analysis"
    line2 = "----------------------------------"
    line3 = str(f"Total Months: {str(totalmonths)}")
    line4 = str(f"Total: ${str(totalprofitloss)}")
    line5 = str(f"Average Change: ${str(round(avg_change,2))}")
    line6 = str(f"Greatest Increase in Profits: {greatestincreasedate} (${str(greatestincrease)}")
    line7 = str(f"Greatest Decrease in Profits: {greatestdecreasedate} (${str(greatestdecrease)}")

    PyBankoutput.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(line1, line2, line3, line4, line5, line6, line7))

