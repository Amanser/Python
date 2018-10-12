
import os
import csv

input_csv = os.path.join("","","election_data.csv")

#Set initial variables
TotalVotes = 0
Khan = 0
Correy = 0
Li = 0
OTooley = 0


with open(input_csv, "r") as csvfile:


    csvreader = csv.reader(csvfile, delimiter = ',')
    
    csv_header = (next(csvreader))

    for row in csvreader:

        # Add 1 to the TotalVotes variable per each row
        TotalVotes += 1

        # Find total votes for each candidates
        if row[2] == "Khan":
            Khan += 1

        if row[2] == "Correy":
            Correy += 1
        
        if row[2] == "Li":
            Li += 1

        if row[2] == "O'Tooley":
            OTooley += 1


#Find percentage of votes for each candidate
KhanPercent = "{:.3f}".format((Khan / TotalVotes) * 100)
CorreyPercent = "{:.3f}".format((Correy / TotalVotes) * 100)
LiPercent = "{:.3f}".format((Li / TotalVotes) * 100)
OTooleyPercent = "{:.3f}".format((OTooley / TotalVotes) * 100)


#Print results to the console
print("Election Results")
print("-------------------------")
print(f"Total Votes: {TotalVotes}")
print("-------------------------")
print(f"Khan: {KhanPercent}% ({Khan})")
print(f"Correy: {CorreyPercent}% ({Correy})")
print(f"Li : {LiPercent}% ({Li})")
print(f"O'Tooley: {OTooleyPercent}% ({OTooley})")
print("-------------------------")

#If statements to print the winner
if Khan > Correy or Li or OTooley:
    print("Winner: Khan")
elif Correy > Li or OTooley:
    print("Winner: Correy")
elif Li > OTooley:
    print("Winner: Li")
else:
    print("Winner: O'Tooley")



# Create an output text file
output_txt = os.path.join('','','updated_poll_data.txt')

with open(output_txt, "w",) as datafile:
    
    print("Election Results", file = datafile)
    
    print("-------------------------", file = datafile)

    print(f"Total Votes: {TotalVotes}", file = datafile)

    print("-------------------------", file = datafile)

    print(f"Khan: {KhanPercent}% ({Khan})", file = datafile)

    print(f"Correy: {CorreyPercent}% ({Correy})", file = datafile)
    
    print(f"Li : {LiPercent}% ({Li})", file = datafile)

    print(f"O'Tooley: {OTooleyPercent}% ({OTooley})", file = datafile)

    print("-------------------------", file = datafile)

    #If statements to print the winner to the text file
    if Khan > Correy or Li or OTooley:
        print("Winner: Khan", file = datafile)
    elif Correy > Li or OTooley:
        print("Winner: Correy", file = datafile)
    elif Li > OTooley:
        print("Winner: Li", file = datafile)
    else:
        print("Winner: O'Tooley", file = datafile)