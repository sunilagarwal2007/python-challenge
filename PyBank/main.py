#Import the libraries
import csv
import os

#print("****************************")
#print("current path: " + os.getcwd())

# Set path for file
budget_csv = os.path.join(".", "Resources", "budget_data.csv")

#open and read cvs
with open(budget_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # This is to skip the header in the csv file
    header = next(csvreader)

    #Creating empty list
    date = []
    revenue = []
    revenue_change = []

    # Loop through looking for the video
    for row in csvreader:
        date.append(row[0])
        revenue.append(int(row[1]))

    print("Financial Analysis")
    print("----------------------------")
    print("Total Months:", len(date))
    print("Total: $",sum(revenue) )

    for i in range(1, len(revenue)):
        revenue_change.append(revenue[i] - revenue[i-1])
        #The average of the changes in "Profit/Losses" over the entire period
        avg_revenue_change = sum(revenue_change)/len(revenue_change)

        max_revenue_change =  max(revenue_change)
        min_revenue_change = min(revenue_change)
        #The greatest increase in profits (date and amount) over the entire period
        date_for_max_revenue_change = str(date[revenue_change.index(max_revenue_change)+1])
        #The greatest decrease in losses (date and amount) over the entire period
        date_for_min_revenue_change = str(date[revenue_change.index(min_revenue_change)+1])

    print("Average Change: $",float(round(avg_revenue_change,2)))
    print("Greatest Increase in Profits:",date_for_max_revenue_change,"($",int(max_revenue_change),")")
    print("Greatest Decrease in Profits:",date_for_min_revenue_change,"($",int(min_revenue_change),")")

    outputfile = open("budget_analysis.txt", "w")
    outputfile.write("Financial Analysis \n")
    outputfile.write("---------------------------- \n")

    outputfile.write(f"Total Months: {len(date)}  \n")
    outputfile.write(f"Total: ${sum(revenue)} \n")
    outputfile.write(f"Average Change: ${float(round(avg_revenue_change,2))} \n")
    outputfile.write(f"Greatest Increase in Profits: {date_for_max_revenue_change} (${int(max_revenue_change)})\n")
    outputfile.write(f"Greatest Decrease in Profits: {date_for_min_revenue_change} (${int(min_revenue_change)})\n")







