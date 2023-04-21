
import os
import csv
import datetime

#define terms
total_months = []
total_proceeds = []
total_changes = []
greatestincrease = 0
greatestdecrease = 0

#csv_file.seek(0)  # move the file pointer back to the beginning

source_csv = os.path.join("/Users/oliviaramsey/Desktop/Data Bootcamp/Module 3 Python/python-challenge/Module 3 Challenge Files/PyBank/Resources/budget_data.csv")

with open(source_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header =next(csvreader)
    #gets our initial value
    firstrow =next(csvreader)
    previous =int(firstrow[1])
    #go through each row
    for row in csvreader:
    
#call up data 
        m=int(row[1])
        d=str(row[0])
        print(f"{d} {m}")
        total_months.append(d)
        total_proceeds.append(m)
        diff=m-previous
        #replace current value with previous value
        previous=m
        total_changes.append(diff)
        if diff>greatestincrease:
            greatestincrease = diff
            gim = d
        if diff<greatestdecrease:
            greatestdecrease = diff
            gdm = d
    print(len(total_months)+1)
    print(sum(total_proceeds)+int(firstrow[1]))
    #cannot compare Jan10 with Jan10 so divided by 85 instead of 86
    print(sum(total_changes)/(len(total_months)))
#define variables
    print(gdm,greatestdecrease)
    print(gim,greatestincrease)




                






