#Election_results
#The data we need to import
import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
file_to_save = os.path.join("analysis", "election_analysis.txt")
with open(file_to_load) as election_data:
#to do read and analyse data here
    file_reader = csv.reader(election_data)
#print each row in the csv file
    for row in file_reader:
        print(row)
#1. The total number of votes cast
#2. A complete list of candidates who received votes
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of theelection based on popular vote.
#close the file
election_data.close()
