import os, csv

budget_csv = os.path.join("Resources/budget_data.csv")

months = 0
netprofit = 0
totalchange = 0
greatestinc_amt = 0
greatestdec_amt = 0

with open(budget_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader, None)
    for row in csvreader:
        months += 1
        netprofit += int(row[1])
        previous = int(row[1])
        break
    for row in csvreader:
        months += 1
        netprofit += int(row[1])
        change = int(row[1]) - previous
        totalchange += change
        if(change > greatestinc_amt):
            greatestinc_mo = row[0]
            greatestinc_amt = change
        if(change < greatestdec_amt):
            greatestdec_mo = row[0]
            greatestdec_amt = change
        previous = int(row[1])

averagechange = round(totalchange/(months - 1), 2)
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {months}")
print(f"Total: ${netprofit}")
print(f"Average Change: ${averagechange}")
print(f"Greatest Increase in Profits: {greatestinc_mo} (${greatestinc_amt})")
print(f"Greatest Decrease in Profits: {greatestdec_mo} (${greatestdec_amt})")

outputfile = open("FinancialAnalysis.txt", "w")
outputfile.write("Financial Analysis\n")
outputfile.write("----------------------------\n")
outputfile.write(f"Total Months: {months}\n")
outputfile.write(f"Total: ${netprofit}\n")
outputfile.write(f"Average Change: ${averagechange}\n")
outputfile.write(f"Greatest Increase in Profits: {greatestinc_mo} (${greatestinc_amt})\n")
outputfile.write(f"Greatest Decrease in Profits: {greatestdec_mo} (${greatestdec_amt})")
outputfile.close()