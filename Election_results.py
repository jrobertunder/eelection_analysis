#Election_result

#The data we need to import

from ast import If
import os
import csv

# Assign a variable for the file to load and the path.
file_to_load = os.path.join('.', "Resources", "election_results.csv")
#print(file_to_load)
file_to_save = os.path.join('.', "analysis", "election_analysis.txt")

total_votes = 0
candidate_names = []
candidate_votes = {}
counties_votes = {}
percent_votes = {}
winning_candidate = []

with open(file_to_load) as election_data:
#to do read and analyse data here

    file_reader = csv.reader(election_data)
    print(file_reader)
#print each row in the csv file
    header = next(file_reader)
    print(header)

    for row in file_reader:
     #   print(row)
#2. A complete list of candidates who received votes     
        # create a list of candidates
        if row[2] not in candidate_names:
            candidate_names.append(row[2])
        # Add to the total vote count
        total_votes = total_votes + 1
        try: 
            candidate_votes[row[2]] = candidate_votes[row[2]] + 1
        except:
            candidate_votes[row[2]] = 1
        try:
            counties_votes[row[1]] = counties_votes[row[1]] + 1
        except:
            counties_votes[row[1]] = 1

#3. The percentage of votes each candidate won
for name in candidate_names:
    percent_votes[name] = round((candidate_votes[name] / total_votes) * 100, 2)


print(f"\n{percent_votes}\n")

#4. The total number of votes each candidate won

print(f"{candidate_votes}\n")

#5. The winner of theelection based on popular vote.
if percent_votes[candidate_names[0]] >= 50.1 :
    print(f"{candidate_names[0]} {percent_votes[candidate_names[0]]}% You are the winner\n")
else:
    print(f"{candidate_names[0]} {percent_votes[candidate_names[0]]}% You did not win\n")

if percent_votes[candidate_names[1]]  >= 50.1 :
    print(f"{candidate_names[1]} {percent_votes[candidate_names[1]]}% You are the winner\n")
else:
    print(f"{candidate_names[1]} {percent_votes[candidate_names[1]]}% You did not win\n")

if percent_votes[candidate_names[2]]  >= 50.1 :
        print(f"{candidate_names[2]} {percent_votes[candidate_names[2]]}% You are the winner\n")
else:
    print(f"{candidate_names[2]} {percent_votes[candidate_names[2]]}% You did not win\n")

with open(file_to_save, "w") as txt_file:

    # Print the final vote count (to terminal)
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        
        f"{candidate_names}\n"

        f"\n{counties_votes}\n")

    print(election_results, end="")

    txt_file.write(election_results)

#close the file
election_data.close()

