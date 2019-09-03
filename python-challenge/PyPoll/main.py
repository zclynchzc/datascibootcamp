import os, csv

election_csv = os.path.join("Resources/election_data.csv")

votefreq = {}

with open(election_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader, None)
    for row in csvreader:
        if(row[2] in votefreq):
            votefreq[row[2]] += 1
        else:
            votefreq[row[2]] = 1

outputfile = open("ElectionResults.txt", "w")

print("Election Results")
print("-------------------------")
outputfile.write("Election Results\n")
outputfile.write("-------------------------\n")
totalvotes = 0
for key, value in votefreq.items(): 
        totalvotes += value
print("Total Votes:", totalvotes)
print("-------------------------")
outputfile.write(f"Total Votes: {totalvotes}\n")
outputfile.write("-------------------------\n")
winner_votes = 0
for key, value in votefreq.items():
    candivotes = round(((value/totalvotes)*100), 3)
    print(f"{key}: {candivotes}% ({value})")
    outputfile.write(f"{key}: {candivotes}% ({value})\n")
    if(value > winner_votes):
        winner_name = key
        winner_votes = value
print("-------------------------")
outputfile.write("-------------------------\n")
print("Winner:", winner_name)
print("-------------------------")
outputfile.write(f"Winner: {winner_name}\n")
outputfile.write("-------------------------")

outputfile.close()