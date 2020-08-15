import csv
import os

csvpath = os.path.join("Resources","election_data.csv")

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvreader,None)

    votes = []
    candidates = []
    for row in csvreader:
        votes.append(row[0])
        candidates.append(row[2])
    total_votes = len(votes)

    unique_candidates = []
    for name in candidates:
        if name not in unique_candidates:
            unique_candidates.append(name)
    
    candidate1 = unique_candidates[0]
    candidate2 = unique_candidates[1]
    candidate3 = unique_candidates[2]
    candidate4 = unique_candidates[3]
    
