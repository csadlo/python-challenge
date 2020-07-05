import os
import csv

csv_file_path = os.path.join("Resources","election_data.csv")
analysis_file_path = os.path.join("Analysis","PyPoll_output")

with open(csv_file_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    num_of_votes = 0
    frontrunner = ""
    candidates_dict = {}
    #candidates_name_list = []
    #candidates_vote_count = []

    # Skip the Header
    next(csvreader)

    # Loop through looking for the video
    for row in csvreader:

        # Parse the data and store it
        voter_id = int(row[0])
        county = row[1]
        name = row[2]
        
        # The total number of votes included in the dataset
        num_of_votes += 1

        # If the candidates name is already in the dictionary
        if name in candidates_dict.keys():
            # Increment the vote count for the selected candidate
            candidates_dict[name] += 1
        else:
            # Append the candidate name to the dictionary of candidates
            #print("DEBUG: Adding candidate name to dictionary " + name)
            candidates_dict[name] = 1

    # Error-Checking
    vote_count_check = 0
    for dname in candidates_dict.keys():
        vote_count_check += candidates_dict[dname]
    
    output = ""

    if vote_count_check != num_of_votes:
        output += "Error: Vote counts do not agree with each other!"

    # Example printout:

    # Election Results
    # -------------------------
    # Total Votes: 3521001
    # -------------------------
    # Khan: 63.000% (2218231)
    # Correy: 20.000% (704200)
    # Li: 14.000% (492940)
    # O'Tooley: 3.000% (105630)
    # -------------------------
    # Winner: Khan
    # -------------------------

    output += "\n Election Results\n -------------------------"
    output += "\n Total Votes: " + str(num_of_votes) + "\n -------------------------"
    for dname in candidates_dict.keys():
        # Calculate percentage of the vote
        percent = round( ((candidates_dict[dname] / num_of_votes) * 100) , 3)
        output += "\n " + dname + ": " + str(percent) + " (" + str(candidates_dict[dname]) + ")"

    output += "\n -------------------------"

    # Determine the winner of the election
    frontrunner_vote_count = 0
    for dname in candidates_dict.keys():

        if candidates_dict[dname] > frontrunner_vote_count:
            frontrunner_vote_count = candidates_dict[dname]
            frontrunner = dname 

    # Output the winner of the election
    output += "\n Winner: " + frontrunner
    output += "\n -------------------------\n"

    print(output)


with open(analysis_file_path, 'w') as writer:
    
    writer.write(output)


