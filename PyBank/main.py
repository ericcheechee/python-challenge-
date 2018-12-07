import os 
import csv 

csvpath = os.path.join("../","Resources","budget_data.cvs")

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # CSV reader specifies delimiter and variable that holds contents    
    print(csvreader)




    # Read the header row first (skip this step if there is now header)
    #csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    #for row in csvreader:
    #   print(row)

