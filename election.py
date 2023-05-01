

#bring in csv
import os
import csv

#define terms
total_votes = []
total_candidates = []
candidate_votes = {}
vote_total = 0



#bring in csv file

source_csv = os.path.join("/Users/oliviaramsey/Desktop/Data Bootcamp/Module 3 Python/python-challenge/Module 3 Challenge Files/PyPoll/Resources/election_data.csv")
with open(source_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header =next(csvreader)

    for row in csvreader:
        ballot=int(row[0])
        county=(row[1])
        candidate=(row[2])
        #print(f"{row[0]},{row[1]},{row[2]}")
        total_votes.append(ballot)
        if candidate not in total_candidates:
            total_candidates.append(candidate)
            candidate_votes[candidate]=0
        candidate_votes[candidate]+=1
        vote_total += 1
    
    for candidate in candidate_votes:

    # Retrieve vote count and percentage
        votes = candidate_votes.get(candidate)
        vote_percentage = float(votes) / float(vote_total) * 100
        print(f'candidate name: {candidate} vote percentage: {vote_percentage}')
        print(f'candidate name: {candidate} total votes: {candidate_votes}')

    #finding the winner based on popular vote
    winner = max(candidate_votes, key=candidate_votes.get)
    print(f'winner: {winner} candidate: {candidate_votes[winner]}')

    #total votes cast
    print(len(total_votes))
  

    

    


   