import csv
import os

csvpath = os.path.join("Resources","budget_data.csv")

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvreader,None)
    #print(f"{csv_header}")

    monthcount = []
    pnl_list = []
    for row in csvreader:
        monthcount.append(row[0])
        pnl_list.append(int(row[1]))
    
    total_months = len(monthcount)
    pnl_total = sum(pnl_list)
    
    pnl_change = []
    for i in range(len(pnl_list)):
        change = int(pnl_list[i] - pnl_list[i-1])
        pnl_change.append(change)
     
    greatest_increase = max(pnl_change)
    greatest_decrease = min(pnl_change)
    

    #pnl_average = change_total

    print("Financial Analysis")
    print("---------------------")
    print(f"Total Months: {total_months}")
    print(f"Total Profits/Losses: ${pnl_total}")
    #print(f"Average Change: ${pnl_average}")
    print(f"Greatest Increase in Profits: ${greatest_increase}")
    print(f"Greatest Decrease in Profits: ${greatest_decrease}")

