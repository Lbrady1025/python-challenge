import csv
import os

csvpath = os.path.join("Resources","election_data.csv")

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvreader,None)

    votes = []
    candidates = []
    unique_candidates = []
    candidate1_votes = []
    candidate2_votes = []
    candidate3_votes = []
    candidate4_votes = []
    for row in csvreader:
        votes.append(row[0])
        #candidates.append(row[2])
        if row[2] not in unique_candidates:
            unique_candidates.append(row[2])
        if row[2] == unique_candidates[0]:
            candidate1_votes.append(row[2])
        elif row[2] == unique_candidates[1]:
            candidate2_votes.append(row[2])
        elif row[2] == unique_candidates[2]:
            candidate3_votes.append(row[2])
        elif row[2] == unique_candidates[3]:
            candidate4_votes.append(row[2])
    
    total_votes = len(votes)
    print(len(candidate1_votes))
    print(len(candidate2_votes))

    #for name in candidates:
        #if name not in unique_candidates:
            #unique_candidates.append(name)
    
    #candidate1 = unique_candidates[0]
    #candidate2 = unique_candidates[1]
    ##candidate3 = unique_candidates[2]
    #candidate4 = unique_candidates[3]

    #for candidate in candidates:
        
    
    #print(candidate1_votes)
    
