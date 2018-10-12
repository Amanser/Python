import os
import csv


csvpath = os.path.join('','','budget_data.csv')

# Set initial variables
totalRev = 0
Months = 0
Average = []
GreatestIncrease = 0
GreatestDecrease = 0
Past = 0



with open(csvpath,'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter = ',')
    
    csv_header = (next(csvreader))

    
#  Loop through the rows to collect data 

    for row in csvreader:

        # Find number of months
        Months += 1
        
        # Find total revenue
        totalRev += int(row[1])

        # Find the change in revenue between each month into a list
        Current = int(row[1])
        Avg = Current - Past
        Increase = Current - Past
        Average.append(Avg)
        Past = int(row[1])

        # Find greatest increase and month where it occured
        if Increase > GreatestIncrease:
            GreatestIncrease = Increase
            BestMonth = row[0]

        # Find greatest decease and month where it occured
        if Increase < GreatestDecrease:
            GreatestDecrease = Increase
            WorstMonth = row[0]
               
        

# Find the average change between months in the "Average" list
# Format the Average_Change variable to two decimal places
Average_Change = "{:.2f}".format(sum(Average[1:]) / float(len(Average[1:]) ))


print ("Financial Analysis")

print ("----------------------------")

print(f"Total Months: {Months}")

print(f"Total: ${totalRev}")

print(f"Average Change: ${Average_Change}")

print(f"Greatest Increase in Profits: {BestMonth} (${GreatestIncrease})")

print(f"Greatest Increase in Profits: {WorstMonth} (${GreatestDecrease})")


# Create an output text file
output_txt = os.path.join('','','updated_budget_data.txt')

with open(output_txt, "w",) as datafile:
    
    print("Financial Analysis", file = datafile)
    
    print("----------------------------", file = datafile)

    print(f"Total Months: {Months}", file = datafile)

    print(f"Total: ${totalRev}", file = datafile)

    print(f"Average Change: ${Average_Change}", file = datafile)

    print(f"Greatest Increase in Profits: {BestMonth} (${GreatestIncrease})", file = datafile)

    print(f"Greatest Increase in Profits: {WorstMonth} (${GreatestDecrease})", file = datafile)
