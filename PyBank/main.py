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
    
    #print(f"Change {change}")

    change_total = 0
    for i in range(len(pnl_change)):
        change_total =+ int(pnl_change[i])
    #print(change_total)
    greatest_increase = max(pnl_change)
    greatest_decrease = min(pnl_change)
    
    max_month_index = pnl_change.index(max(pnl_change))
    max_month = monthcount[max_month_index]

    min_month_index = pnl_change.index(min(pnl_change))
    min_month = monthcount[min_month_index]

    #pnl_average = change_total

    print("Financial Analysis")
    print("---------------------")
    print(f"Total Months: {total_months}")
    print(f"Total Profits/Losses: ${pnl_total}")
    # print(f"Average Change: ${pnl_average}")
    print(f"Greatest Increase in Profits: {max_month} (${greatest_increase})")
    print(f"Greatest Decrease in Profits: {min_month} (${greatest_decrease})")

