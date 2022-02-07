# election_analysis
Analyzing Election data for statistics and certification
1.	Overview of Election Audit: 

o	The purpose of this audit was to determine if there had been any irregularities in the collection and counting of the votes submitted during the election.

2.	Election-Audit Results: 

o	How many votes were cast in this congressional election? 

1.	The total number of votes was 369,711

o	Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.

1.	Jefferson: 10.51% (38,855)
2.	Denver: 82.78% (306,055)
3.	Arapahoe: 6.71% (24,801)

o	Which county had the largest number of votes?

1.	Denver

o	Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.

1.	Charles Casper Stockham: 23.05% (85,213)

2.	Diana DeGette: 73.81% (272,892)

3.	Raymon Anthony Doane: 3.14% (11,606)

o	Which candidate won the election, what was their vote count, and what was their percentage of the total votes?

1.	Winner: Diana DeGette
2.	Winning Vote Count: 272,892
3.	Winning Percentage: 73.81%

Election-Audit Summary
While limited in its current scope this program can be expanded to cover a greater number of precincts and candidates.  With the addition of two small files and the modification of some coding. First a file containing the number of registered voters in each participating district, then a file containing the names of the candidates running for office. 

The following lines of code would need to be added.

distrct_to_load = os.path.join('.', "Resources", "district_names.csv")
cnddt_to_load = os.path.join('.', "Resources", "candidate_names.csv")

with open(distrct_to_load) as district_data:
with open(cnddt_to_load) as candidate_data:

file_reader = csv.reader(district_data)
file_reader = csv.reader(candidate_data)

It would then be possible to parse the district and candidates more directly rather than creating loops to identify the districts, and candidates from the raw data.
