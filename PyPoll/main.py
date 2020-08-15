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
 
    candidate1 = unique_candidates[0]
    candidate2 = unique_candidates[1]
    candidate3 = unique_candidates[2]
    candidate4 = unique_candidates[3]

    candidate1_calc = len(candidate1_votes)/total_votes
    candidate1_pct = "{:.3%}".format(candidate1_calc)

    candidate2_calc = len(candidate2_votes)/total_votes
    candidate2_pct = "{:.3%}".format(candidate2_calc)

    candidate3_calc = len(candidate3_votes)/total_votes
    candidate3_pct = "{:.3%}".format(candidate3_calc)

    candidate4_calc = len(candidate4_votes)/total_votes
    candidate4_pct = "{:.3%}".format(candidate4_calc)

    results = {
        candidate1_pct:candidate1,
        candidate2_pct:candidate2,
        candidate3_pct:candidate3,
        candidate4_pct:candidate4}

    winner = max(results)
    print(winner)

    print(f"Election Results")
    print("-------------------")
    print(f"Total Votes: {total_votes}")
    print("-------------------")
    print(f"{candidate1}: {candidate1_pct} {len(candidate1_votes)}")
    print(f"{candidate2}: {candidate2_pct} {len(candidate2_votes)}")
    print(f"{candidate3}: {candidate3_pct} {len(candidate3_votes)}")
    print(f"{candidate4}: {candidate4_pct} {len(candidate4_votes)}")
    
