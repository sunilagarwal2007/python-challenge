#Import the libraries
import csv
import os

# Function to perform election_data_analysis
def election_data_analysis(candidate_name,candidate_list,total_votes,outputfile):
    candidates_votes = 0
    for candidate in candidate_list:
        if candidate_name == candidate:
            candidates_votes = candidates_votes + 1
    win_percent = round((candidates_votes / total_votes) * 100,2)
    print(f"{candidate_name}: {win_percent}% ({candidates_votes})")
    outputfile.write(f"{candidate_name}: {win_percent}% ({candidates_votes})\n")
    return candidates_votes

# Set path for file
election_data_csv = os.path.join(".", "Resources", "election_data.csv")

#open and read cvs
with open(election_data_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # This is to skip the header in the csv file
    header = next(csvreader)
    #Creating empty list
    voters = []
    countries = []
    candidate_list = []

    # Loop through looking for the video
    for row in csvreader:
        voters.append(row[0])
        countries.append(row[1])
        candidate_list.append(row[2])

    total_votes = len(voters)
    print("Election Results")
    print("----------------------------")
    print("Total Votes:", total_votes )
    print("----------------------------")

    # Open the file using "write" mode. Specify the variable to hold the contents
    outputfile = open("poll_analysis.txt", "w")
    outputfile.write("Election Results \n")
    outputfile.write("---------------------------- \n")
    outputfile.write(f"Total Votes: {total_votes}  \n")
    outputfile.write("---------------------------- \n")

    #This is to find unique list of candidates
    candidates = set(candidate_list)
    #print("Candidates List: $", candidates)
    max_voting_count=0
    winner = ""
    for candidate_name in candidates:
        candidates_votes = election_data_analysis(candidate_name, candidate_list, total_votes,outputfile)
        #Calculate the Candidate which got more votes to find winner
        if candidates_votes > max_voting_count:
            max_voting_count = candidates_votes
            winner = candidate_name
    print("----------------------------")
    print("Winner: ", winner)
    print("----------------------------")

    outputfile.write("----------------------------\n")
    outputfile.write(f"Winner: {winner}\n")
    outputfile.write("----------------------------")