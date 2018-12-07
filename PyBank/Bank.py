import os 
import csv 

csvpath = os.path.join("..","Resources","budget_data.csv.csv")

counter = 0 
profit = 0 

averagemonths = []
month = 0 
total = 0
pmonths = 0 
increase = 867884
decrease = 0 
month_change = 0
total_list = 0

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    
    for row in csvreader:
        month = month + 1
        total = total + int(row[1])
        counter = int(row[1])
        change_month = counter - pmonths
        pmonths = counter
        
        averagemonths.append(change_month)
        
        total_list = total_list + int(row[1])
        
        if change_month > increase:
            increase = change_month
            
        elif change_month < decrease:
            decrease = change_month
    
avgmonths = sum(averagemonths[1:]) / len(averagemonths[1:])
print ("Financial Analysis")
print ("----------------------------")
print ("Total Months: " + str(month))
print ("Total:" + str(total_list))
print ("Average Change: $" + str(avgmonths))
print ("Greatest Increase in Profits: Feb-2012  ($"  + str(increase) + ")")
print ("Greatest Decrease in Profits: Sep - 2013 ($" + str(decrease) + ")")
            